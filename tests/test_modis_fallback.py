"""Checks that example vegetation data is never labelled as a real observation."""
import unittest

from modis_ornl import generate_illustrative_baseline_payload


class ModisFallbackLabelTests(unittest.TestCase):
    def test_fallback_is_marked_as_modeled_not_observed(self):
        result = generate_illustrative_baseline_payload(9.93, 76.27, 2018, 2020)

        self.assertTrue(result["available"])
        self.assertTrue(result["is_fallback"])
        self.assertEqual(result["meta"]["kind"], "modeled")
        self.assertIn("not an observed satellite reading", result["fallback_notice"])
        self.assertIn("not MODIS satellite observations", result["meta"]["name"])

    def test_fallback_values_are_in_range_and_dates_match(self):
        result = generate_illustrative_baseline_payload(13.08, 80.27, 2020, 2021)

        self.assertEqual(len(result["dates"]), len(result["ndvi"]))
        self.assertEqual(len(result["dates"]), len(result["reliability"]))
        valid = [value for value in result["ndvi"] if value is not None]
        self.assertTrue(valid)
        self.assertTrue(all(-0.2 <= value <= 1.0 for value in valid))


if __name__ == "__main__":
    unittest.main()
