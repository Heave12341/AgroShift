import unittest
import rotation

class GlobalCatalogueMergeTests(unittest.TestCase):
    def test_global_catalogue_has_more_than_1200_crops(self):
        self.assertGreaterEqual(len(rotation.CROPS), 1200)

    def test_original_indian_crop_records_are_preserved(self):
        for crop_id in ("rice", "wheat", "pearl_millet", "chickpea", "finger_millet"):
            self.assertIn(crop_id, rotation.CROPS)
            self.assertTrue(rotation.CROPS[crop_id].get("regional_suitability"))

    def test_global_candidates_reference_known_crops(self):
        regions = ("us_corn_belt", "latin_america_cerrado", "europe_temperate", "sub_saharan_africa", "east_asia", "australia_grain_belt")
        for region in regions:
            candidates = rotation._global_candidate_rotations(region)
            self.assertTrue(candidates, region)
            for item in candidates:
                for crop_id in item["crop_ids"]:
                    self.assertIn(crop_id, rotation.CROPS)

if __name__ == "__main__":
    unittest.main()
