"""Regression checks for profile-aware crop-rotation recommendations."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "backend"))
import rotation


class TestProfileAdaptation(unittest.TestCase):
    def test_west_coast_coordinates_get_a_more_specific_zone(self):
        key, name = rotation.detect_indian_agroclimatic_zone(9.6, 76.5)
        self.assertEqual(key, "western_ghats")
        self.assertIn("Kerala", name)

    def test_missing_coordinates_are_not_silently_assigned_to_bihar(self):
        key, _ = rotation.detect_indian_agroclimatic_zone(None, None)
        self.assertEqual(key, "pan_india")

    def test_location_changes_the_candidate_ranking(self):
        common = {"priority": "balanced", "irrigation": "assured_canal", "soil_type": "alluvial"}
        bihar = rotation.evaluate_rotations({**common, "lat": 25.5, "lon": 85.1})
        rajasthan = rotation.evaluate_rotations({**common, "lat": 26.0, "lon": 71.0})
        self.assertNotEqual(bihar["rotations"][0]["id"], rajasthan["rotations"][0]["id"])

    def test_soil_texture_changes_the_top_recommendation(self):
        common = {"priority": "balanced", "irrigation": "assured_tubewell", "lat": 9.6, "lon": 76.5}
        alluvial = rotation.evaluate_rotations({**common, "soil_type": "alluvial"})
        laterite = rotation.evaluate_rotations({**common, "soil_type": "red_laterite"})
        self.assertNotEqual(alluvial["rotations"][0]["id"], laterite["rotations"][0]["id"])

    def test_priority_weights_and_rankings_are_distinct(self):
        results = {
            p: rotation.evaluate_rotations({
                "priority": p,
                "lat": 9.6,
                "lon": 76.5,
                "irrigation": "assured_tubewell",
                "soil_type": "red_laterite",
                "soil_ph": 4.8,
                "organic_carbon_pct": 0.4,
            })
            for p in ("water_conservation", "soil_improvement", "income_stability", "balanced")
        }
        weight_sets = {tuple(sorted(r["weights"].items())) for r in results.values()}
        self.assertEqual(len(weight_sets), 4)
        top_ids = {r["rotations"][0]["id"] for r in results.values()}
        self.assertGreaterEqual(len(top_ids), 3)

    def test_irrigation_changes_the_top_rotation_when_water_access_is_material(self):
        common = {"lat": 25.59, "lon": 85.13, "priority": "water_conservation", "soil_type": "clay_loam"}
        rainfed = rotation.evaluate_rotations({**common, "irrigation": "rainfed"})
        canal = rotation.evaluate_rotations({**common, "irrigation": "assured_canal"})
        self.assertNotEqual(rainfed["rotations"][0]["id"], canal["rotations"][0]["id"])

    def test_each_strategy_exposes_weighted_criterion_contributions(self):
        result = rotation.evaluate_rotations({
            "lat": 9.6, "lon": 76.5, "priority": "water_conservation",
            "soil_type": "red_laterite", "irrigation": "rainfed",
        })
        strategy = result["rotations"][0]
        self.assertEqual(set(strategy["weighted_contributions"]), set(strategy["criteria_scores"]))
        self.assertAlmostEqual(sum(strategy["weights_used"].values()), 1.0, places=5)
        self.assertAlmostEqual(
            sum(strategy["weighted_contributions"].values()),
            strategy["five_criteria_score"],
            places=1,
        )

    def test_west_coast_uses_direct_local_crop_evidence(self):
        profile = {"lat": 9.6, "lon": 76.5, "priority": "balanced", "soil_type": "alluvial"}
        result = rotation.evaluate_rotations(profile)
        rotations = {r["id"]: r for r in result["rotations"]}
        self.assertGreater(
            rotations["rice_okra"]["regional_fit_score"],
            rotations["pearl_millet_chickpea"]["regional_fit_score"],
        )

    def test_eastern_rajasthan_is_not_misclassified_as_indo_gangetic(self):
        key, _ = rotation.detect_indian_agroclimatic_zone(26.9, 75.8)
        self.assertEqual(key, "arid_west")

    def test_acidic_ph_changes_crop_relative_suitability(self):
        pearl = [rotation.CROPS["pearl_millet"], rotation.CROPS["chickpea"]]
        finger = [rotation.CROPS["finger_millet"], rotation.CROPS["pigeonpea"]]
        pearl_neutral, _ = rotation._score_soil_health(pearl, "red_laterite", soil_ph=6.5)
        pearl_acid, _ = rotation._score_soil_health(pearl, "red_laterite", soil_ph=4.8)
        finger_neutral, _ = rotation._score_soil_health(finger, "red_laterite", soil_ph=6.5)
        finger_acid, _ = rotation._score_soil_health(finger, "red_laterite", soil_ph=4.8)
        self.assertLess(pearl_acid, pearl_neutral)
        self.assertGreater(finger_acid, finger_neutral)

    def test_low_organic_carbon_changes_soil_score(self):
        sequence = [rotation.CROPS["finger_millet"], rotation.CROPS["groundnut"]]
        normal, _ = rotation._score_soil_health(sequence, "red_laterite", organic_carbon_pct=0.9)
        low_carbon, _ = rotation._score_soil_health(sequence, "red_laterite", organic_carbon_pct=0.2)
        self.assertGreater(low_carbon, normal)

    def test_observed_wet_climate_penalises_waterlogging_sensitive_sequence(self):
        wet = {
            "available": True,
            "baseline": {"rainfall_mean_mm": 2600},
            "seasonal_period_means": [{"season": "kharif", "mean_rainfall_mm": 1800}],
        }
        sensitive = [rotation.CROPS["pearl_millet"], rotation.CROPS["chickpea"]]
        score_without_site_data, _ = rotation._score_climate_resilience(sensitive)
        score_with_wet_climate, warnings = rotation._score_climate_resilience(sensitive, wet, "western_ghats")
        self.assertLess(score_with_wet_climate, score_without_site_data)
        self.assertTrue(any("waterlogging" in w.lower() for w in warnings))

    def test_irrigation_source_changes_high_water_sequence_score(self):
        crops = [rotation.CROPS[c] for c in ("rice", "potato", "green_gram")]
        well, _, _ = rotation._score_water(crops, "assured_tubewell")
        canal, _, _ = rotation._score_water(crops, "assured_canal")
        rainfed, _, _ = rotation._score_water(crops, "rainfed")
        self.assertGreater(canal, well)
        self.assertGreater(well, rainfed)


if __name__ == "__main__":
    unittest.main()
