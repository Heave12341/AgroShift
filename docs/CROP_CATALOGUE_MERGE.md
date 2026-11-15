# Global Crop Catalogue Merge

The teammate-provided global dataset (`backend/data/crops_global.json`) contains 1,232 crop records. It is loaded by `backend/crops_registry.py` and merged into `backend/rotation.py`. The original 53 locally calibrated Indian crop records are preserved and take precedence for matching IDs.

The crop explorer and custom rotation builder use the expanded catalogue. Existing five-criterion scoring, soil pH / organic carbon handling, Indian region adjustments, MODIS handling and farmer-facing interface logic remain from the current project.

For locations outside the Indian coordinate envelope, curated region-specific crop pathways from the teammate's engine are used with the current project's scoring functions. A crop's presence in the catalogue is not proof of local suitability; use the regional suitability fields and local extension advice.

Catalogue source/provider metadata remains on each crop record. The catalogue is not a substitute for locally validated package-of-practice recommendations.
