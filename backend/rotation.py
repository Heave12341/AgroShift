"""Global Crop Catalogue (1,232 records) & Multi-Criteria Rotation Engine.
Scientifically calibrated for the Agro-Climatic Zones of Bihar and the Indo-Gangetic Plains.
"""
from typing import Any
from crops_registry import CROPS as GLOBAL_CROPS

CROPS: dict[str, dict[str, Any]] = {
    "rice": {
        "id": "rice",
        "name": "Rice (Paddy / Dhan)",
        "scientific_name": "Oryza sativa",
        "categories": [
            "cereal",
            "staple"
        ],
        "crop_family": "Poaceae",
        "season": "kharif",
        "duration_range_days": [
            115,
            140
        ],
        "typical_duration": 125,
        "water_need_range_mm": [
            1100,
            1400
        ],
        "typical_water_mm": 1200,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "shallow_fibrous",
        "root_depth_range_cm": [
            20,
            40
        ],
        "soil_cover_rating": 4,
        "drought_tolerance": 2,
        "waterlogging_tolerance": 5,
        "market_stability": "high",
        "n_feeder": "high",
        "suitable_soils": [
            "alluvial",
            "clay_loam",
            "silt_loam",
            "black_cotton"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "eastern_coastal": "high",
            "central": "moderate",
            "arid_west": "low"
        },
        "data_source": "ICAR-NRRI & BAU Sabour Agronomy Compendium",
        "source_year": "2022",
        "data_confidence": "high",
        "limitations": [
            "Heavy groundwater extraction in dry season",
            "Puddled soil forms dense plow pan",
            "High methane emissions under continuous flooding"
        ],
        "primary_category": "cereals_millets",
        "water_need_mm": [
            1100,
            1400
        ],
        "duration_days": [
            115,
            140
        ],
        "root_depth_cm": [
            20,
            40
        ]
    },
    "wheat": {
        "id": "wheat",
        "name": "Wheat (Gehun)",
        "scientific_name": "Triticum aestivum",
        "categories": [
            "cereal",
            "staple"
        ],
        "crop_family": "Poaceae",
        "season": "rabi",
        "duration_range_days": [
            110,
            125
        ],
        "typical_duration": 115,
        "water_need_range_mm": [
            350,
            450
        ],
        "typical_water_mm": 400,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "shallow_fibrous",
        "root_depth_range_cm": [
            30,
            60
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 3,
        "waterlogging_tolerance": 2,
        "market_stability": "high",
        "n_feeder": "high",
        "suitable_soils": [
            "alluvial",
            "clay_loam",
            "silt_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "central": "high",
            "arid_west": "moderate",
            "southern_peninsula": "low"
        },
        "data_source": "ICAR-IIWBR Karnal Research Bulletin",
        "source_year": "2023",
        "data_confidence": "high",
        "limitations": [
            "Highly sensitive to terminal heat stress during grain filling in March",
            "Requires 4-5 timely irrigations",
            "Zero N fixation"
        ],
        "primary_category": "cereals_millets",
        "water_need_mm": [
            350,
            450
        ],
        "duration_days": [
            110,
            125
        ],
        "root_depth_cm": [
            30,
            60
        ]
    },
    "maize": {
        "id": "maize",
        "name": "Maize (Corn / Makka)",
        "scientific_name": "Zea mays",
        "categories": [
            "cereal",
            "feed",
            "industrial"
        ],
        "crop_family": "Poaceae",
        "season": "kharif_or_rabi",
        "duration_range_days": [
            100,
            125
        ],
        "typical_duration": 115,
        "water_need_range_mm": [
            450,
            600
        ],
        "typical_water_mm": 500,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "deep_fibrous",
        "root_depth_range_cm": [
            50,
            90
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 3,
        "waterlogging_tolerance": 2,
        "market_stability": "medium",
        "n_feeder": "high",
        "suitable_soils": [
            "alluvial",
            "sandy_loam",
            "clay_loam",
            "red_laterite"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "central": "high",
            "southern_peninsula": "high",
            "arid_west": "moderate"
        },
        "data_source": "ICAR-IIMR Ludhiana Maize Agronomy Manual",
        "source_year": "2022",
        "data_confidence": "high",
        "limitations": [
            "Heavy nutrient extractor; requires balanced NPK",
            "Susceptible to Fall Armyworm (Spodoptera frugiperda)",
            "Waterlogging sensitive in early stage"
        ],
        "primary_category": "cereals_millets",
        "water_need_mm": [
            450,
            600
        ],
        "duration_days": [
            100,
            125
        ],
        "root_depth_cm": [
            50,
            90
        ]
    },
    "pearl_millet": {
        "id": "pearl_millet",
        "name": "Pearl Millet (Bajra)",
        "scientific_name": "Pennisetum glaucum",
        "categories": [
            "cereal",
            "millet",
            "climate_resilient"
        ],
        "crop_family": "Poaceae",
        "season": "kharif",
        "duration_range_days": [
            75,
            90
        ],
        "typical_duration": 85,
        "water_need_range_mm": [
            250,
            350
        ],
        "typical_water_mm": 300,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "deep_fibrous",
        "root_depth_range_cm": [
            60,
            120
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 5,
        "waterlogging_tolerance": 1,
        "market_stability": "medium",
        "n_feeder": "medium",
        "suitable_soils": [
            "sandy_loam",
            "alluvial",
            "red_laterite"
        ],
        "regional_suitability": {
            "bihar": "moderate",
            "arid_west": "high",
            "central": "high",
            "indo_gangetic": "moderate",
            "southern_peninsula": "high"
        },
        "data_source": "ICAR-AICRP on Pearl Millet & ICRISAT",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Lower grain price realization compared to MSP cereals in eastern states",
            "Cannot tolerate waterlogging",
            "Susceptible to downy mildew"
        ],
        "primary_category": "cereals_millets",
        "water_need_mm": [
            250,
            350
        ],
        "duration_days": [
            75,
            90
        ],
        "root_depth_cm": [
            60,
            120
        ]
    },
    "sorghum": {
        "id": "sorghum",
        "name": "Sorghum (Jowar)",
        "scientific_name": "Sorghum bicolor",
        "categories": [
            "cereal",
            "millet",
            "fodder"
        ],
        "crop_family": "Poaceae",
        "season": "kharif_or_rabi",
        "duration_range_days": [
            95,
            115
        ],
        "typical_duration": 105,
        "water_need_range_mm": [
            350,
            450
        ],
        "typical_water_mm": 400,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "deep_fibrous",
        "root_depth_range_cm": [
            70,
            130
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 5,
        "waterlogging_tolerance": 2,
        "market_stability": "medium",
        "n_feeder": "medium",
        "suitable_soils": [
            "black_cotton",
            "clay_loam",
            "alluvial"
        ],
        "regional_suitability": {
            "bihar": "moderate",
            "central": "high",
            "deccan": "high",
            "indo_gangetic": "moderate",
            "southern_peninsula": "high"
        },
        "data_source": "ICAR-IIMR Hyderabad Sorghum Research Package",
        "source_year": "2022",
        "data_confidence": "high",
        "limitations": [
            "Susceptible to shoot fly and stem borer",
            "Allelopathic root exudates can slightly suppress succeeding pulse emergence if not tilled"
        ],
        "primary_category": "cereals_millets",
        "water_need_mm": [
            350,
            450
        ],
        "duration_days": [
            95,
            115
        ],
        "root_depth_cm": [
            70,
            130
        ]
    },
    "finger_millet": {
        "id": "finger_millet",
        "name": "Finger Millet (Ragi / Mandua)",
        "scientific_name": "Eleusine coracana",
        "categories": [
            "cereal",
            "millet",
            "nutri_cereal"
        ],
        "crop_family": "Poaceae",
        "season": "kharif",
        "duration_range_days": [
            100,
            120
        ],
        "typical_duration": 110,
        "water_need_range_mm": [
            300,
            400
        ],
        "typical_water_mm": 350,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "shallow_fibrous",
        "root_depth_range_cm": [
            30,
            60
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 4,
        "waterlogging_tolerance": 2,
        "market_stability": "medium",
        "n_feeder": "low",
        "suitable_soils": [
            "red_laterite",
            "alluvial",
            "sandy_loam"
        ],
        "regional_suitability": {
            "bihar": "moderate",
            "southern_peninsula": "high",
            "central": "high",
            "hilly_north": "high",
            "indo_gangetic": "moderate"
        },
        "data_source": "ICAR-AICRP on Small Millets Bengaluru",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Slow early vegetative growth requiring careful weed control",
            "Threshing and processing machinery less widespread in north India"
        ],
        "primary_category": "cereals_millets",
        "water_need_mm": [
            300,
            400
        ],
        "duration_days": [
            100,
            120
        ],
        "root_depth_cm": [
            30,
            60
        ]
    },
    "foxtail_millet": {
        "id": "foxtail_millet",
        "name": "Foxtail Millet (Kangni / Kakum)",
        "scientific_name": "Setaria italica",
        "categories": [
            "cereal",
            "millet",
            "short_duration"
        ],
        "crop_family": "Poaceae",
        "season": "kharif_or_zaid",
        "duration_range_days": [
            65,
            80
        ],
        "typical_duration": 70,
        "water_need_range_mm": [
            200,
            300
        ],
        "typical_water_mm": 250,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "shallow_fibrous",
        "root_depth_range_cm": [
            30,
            50
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 5,
        "waterlogging_tolerance": 1,
        "market_stability": "medium",
        "n_feeder": "low",
        "suitable_soils": [
            "sandy_loam",
            "red_laterite",
            "alluvial"
        ],
        "regional_suitability": {
            "bihar": "moderate",
            "southern_peninsula": "high",
            "central": "high",
            "arid_west": "moderate"
        },
        "data_source": "ICAR-AICRP on Small Millets & TNAU Portal",
        "source_year": "2020",
        "data_confidence": "medium",
        "limitations": [
            "Lower grain volume per hectare than major cereals",
            "Niche local market demand"
        ],
        "primary_category": "cereals_millets",
        "water_need_mm": [
            200,
            300
        ],
        "duration_days": [
            65,
            80
        ],
        "root_depth_cm": [
            30,
            50
        ]
    },
    "barley": {
        "id": "barley",
        "name": "Barley (Jau)",
        "scientific_name": "Hordeum vulgare",
        "categories": [
            "cereal",
            "malt",
            "feed"
        ],
        "crop_family": "Poaceae",
        "season": "rabi",
        "duration_range_days": [
            100,
            120
        ],
        "typical_duration": 110,
        "water_need_range_mm": [
            250,
            350
        ],
        "typical_water_mm": 300,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "shallow_fibrous",
        "root_depth_range_cm": [
            40,
            70
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 4,
        "waterlogging_tolerance": 2,
        "market_stability": "medium",
        "n_feeder": "medium",
        "suitable_soils": [
            "alluvial",
            "sandy_loam",
            "clay_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "arid_west": "high",
            "central": "moderate"
        },
        "data_source": "ICAR-IIWBR Barley Improvement Program",
        "source_year": "2022",
        "data_confidence": "high",
        "limitations": [
            "Lower procurement support than wheat",
            "Requires premium malting grade varieties for industrial brewery contracts"
        ],
        "primary_category": "cereals_millets",
        "water_need_mm": [
            250,
            350
        ],
        "duration_days": [
            100,
            120
        ],
        "root_depth_cm": [
            40,
            70
        ]
    },
    "chickpea": {
        "id": "chickpea",
        "name": "Chickpea (Gram / Chana)",
        "scientific_name": "Cicer arietinum",
        "categories": [
            "pulse",
            "legume",
            "n_fixing"
        ],
        "crop_family": "Fabaceae",
        "season": "rabi",
        "duration_range_days": [
            105,
            120
        ],
        "typical_duration": 110,
        "water_need_range_mm": [
            200,
            260
        ],
        "typical_water_mm": 230,
        "nitrogen_fixation_range_kg_ha": [
            25,
            45
        ],
        "nitrogen_fixation_kg_ha": 35,
        "root_type": "deep_taproot",
        "root_depth_range_cm": [
            60,
            100
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 4,
        "waterlogging_tolerance": 1,
        "market_stability": "medium",
        "n_feeder": "low",
        "suitable_soils": [
            "alluvial",
            "silt_loam",
            "black_cotton"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "central": "high",
            "deccan": "high",
            "arid_west": "moderate"
        },
        "data_source": "ICAR-IIPR Kanpur Pulse Production Guide",
        "source_year": "2022",
        "data_confidence": "high",
        "limitations": [
            "Highly sensitive to waterlogging and collar rot",
            "Susceptible to pod borer (Helicoverpa armigera)"
        ],
        "primary_category": "pulses",
        "water_need_mm": [
            200,
            260
        ],
        "duration_days": [
            105,
            120
        ],
        "root_depth_cm": [
            60,
            100
        ]
    },
    "pigeonpea": {
        "id": "pigeonpea",
        "name": "Pigeonpea (Arhar / Tur)",
        "scientific_name": "Cajanus cajan",
        "categories": [
            "pulse",
            "legume",
            "n_fixing"
        ],
        "crop_family": "Fabaceae",
        "season": "kharif",
        "duration_range_days": [
            150,
            200
        ],
        "typical_duration": 175,
        "water_need_range_mm": [
            400,
            550
        ],
        "typical_water_mm": 450,
        "nitrogen_fixation_range_kg_ha": [
            35,
            60
        ],
        "nitrogen_fixation_kg_ha": 45,
        "root_type": "deep_taproot",
        "root_depth_range_cm": [
            100,
            180
        ],
        "soil_cover_rating": 4,
        "drought_tolerance": 5,
        "waterlogging_tolerance": 1,
        "market_stability": "high",
        "n_feeder": "low",
        "suitable_soils": [
            "alluvial",
            "black_cotton",
            "red_laterite"
        ],
        "regional_suitability": {
            "bihar": "high",
            "central": "high",
            "deccan": "high",
            "indo_gangetic": "high",
            "southern_peninsula": "high"
        },
        "data_source": "ICAR-IIPR Kanpur & ICRISAT Factsheet",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Long duration ties up land into late Rabi unless early varieties (UPAS-120) are used",
            "Sterility mosaic disease risk"
        ],
        "primary_category": "pulses",
        "water_need_mm": [
            400,
            550
        ],
        "duration_days": [
            150,
            200
        ],
        "root_depth_cm": [
            100,
            180
        ]
    },
    "lentil": {
        "id": "lentil",
        "name": "Lentil (Masoor)",
        "scientific_name": "Lens culinaris",
        "categories": [
            "pulse",
            "legume",
            "n_fixing"
        ],
        "crop_family": "Fabaceae",
        "season": "rabi",
        "duration_range_days": [
            95,
            115
        ],
        "typical_duration": 105,
        "water_need_range_mm": [
            180,
            230
        ],
        "typical_water_mm": 200,
        "nitrogen_fixation_range_kg_ha": [
            20,
            40
        ],
        "nitrogen_fixation_kg_ha": 30,
        "root_type": "moderate_taproot",
        "root_depth_range_cm": [
            40,
            70
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 4,
        "waterlogging_tolerance": 1,
        "market_stability": "medium",
        "n_feeder": "low",
        "suitable_soils": [
            "alluvial",
            "clay_loam",
            "silt_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "central": "high",
            "eastern_coastal": "moderate"
        },
        "data_source": "ICAR-IIPR & BAU Sabour Pulses Program",
        "source_year": "2022",
        "data_confidence": "high",
        "limitations": [
            "Susceptible to Stemphylium blight and vascular wilt during warm winter transitions"
        ],
        "primary_category": "pulses",
        "water_need_mm": [
            180,
            230
        ],
        "duration_days": [
            95,
            115
        ],
        "root_depth_cm": [
            40,
            70
        ]
    },
    "green_gram": {
        "id": "green_gram",
        "name": "Green Gram (Moong)",
        "scientific_name": "Vigna radiata",
        "categories": [
            "pulse",
            "legume",
            "n_fixing",
            "catch_crop"
        ],
        "crop_family": "Fabaceae",
        "season": "zaid",
        "duration_range_days": [
            60,
            70
        ],
        "typical_duration": 65,
        "water_need_range_mm": [
            180,
            220
        ],
        "typical_water_mm": 200,
        "nitrogen_fixation_range_kg_ha": [
            20,
            38
        ],
        "nitrogen_fixation_kg_ha": 30,
        "root_type": "moderate_taproot",
        "root_depth_range_cm": [
            30,
            50
        ],
        "soil_cover_rating": 4,
        "drought_tolerance": 3,
        "waterlogging_tolerance": 2,
        "market_stability": "medium",
        "n_feeder": "low",
        "suitable_soils": [
            "alluvial",
            "sandy_loam",
            "clay_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "central": "high",
            "southern_peninsula": "high",
            "arid_west": "moderate"
        },
        "data_source": "ICAR-IIPR Summer Moong Initiative",
        "source_year": "2023",
        "data_confidence": "high",
        "limitations": [
            "Yellow Mosaic Virus (MYMV) transmitted by whitefly in summer",
            "Pod shattering if harvesting is delayed"
        ],
        "primary_category": "pulses",
        "water_need_mm": [
            180,
            220
        ],
        "duration_days": [
            60,
            70
        ],
        "root_depth_cm": [
            30,
            50
        ]
    },
    "black_gram": {
        "id": "black_gram",
        "name": "Black Gram (Urad)",
        "scientific_name": "Vigna mungo",
        "categories": [
            "pulse",
            "legume",
            "n_fixing"
        ],
        "crop_family": "Fabaceae",
        "season": "kharif_or_zaid",
        "duration_range_days": [
            70,
            85
        ],
        "typical_duration": 75,
        "water_need_range_mm": [
            250,
            350
        ],
        "typical_water_mm": 300,
        "nitrogen_fixation_range_kg_ha": [
            22,
            40
        ],
        "nitrogen_fixation_kg_ha": 32,
        "root_type": "moderate_taproot",
        "root_depth_range_cm": [
            35,
            60
        ],
        "soil_cover_rating": 4,
        "drought_tolerance": 3,
        "waterlogging_tolerance": 2,
        "market_stability": "medium",
        "n_feeder": "low",
        "suitable_soils": [
            "alluvial",
            "black_cotton",
            "clay_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "central": "high",
            "deccan": "high",
            "southern_peninsula": "high"
        },
        "data_source": "ICAR-IIPR Pulse Compendium",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Susceptible to powdery mildew and Cercospora leaf spot in humid conditions"
        ],
        "primary_category": "pulses",
        "water_need_mm": [
            250,
            350
        ],
        "duration_days": [
            70,
            85
        ],
        "root_depth_cm": [
            35,
            60
        ]
    },
    "field_pea": {
        "id": "field_pea",
        "name": "Field Pea (Matar)",
        "scientific_name": "Pisum sativum",
        "categories": [
            "pulse",
            "legume",
            "n_fixing"
        ],
        "crop_family": "Fabaceae",
        "season": "rabi",
        "duration_range_days": [
            90,
            110
        ],
        "typical_duration": 100,
        "water_need_range_mm": [
            200,
            280
        ],
        "typical_water_mm": 240,
        "nitrogen_fixation_range_kg_ha": [
            25,
            45
        ],
        "nitrogen_fixation_kg_ha": 35,
        "root_type": "moderate_taproot",
        "root_depth_range_cm": [
            40,
            75
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 3,
        "waterlogging_tolerance": 2,
        "market_stability": "medium",
        "n_feeder": "low",
        "suitable_soils": [
            "alluvial",
            "silt_loam",
            "clay_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "central": "high"
        },
        "data_source": "ICAR-IIPR Research Bulletin",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Powdery mildew (Erysiphe pisi) during warm February days",
            "Frost vulnerability during flowering"
        ],
        "primary_category": "pulses",
        "water_need_mm": [
            200,
            280
        ],
        "duration_days": [
            90,
            110
        ],
        "root_depth_cm": [
            40,
            75
        ]
    },
    "cowpea": {
        "id": "cowpea",
        "name": "Cowpea (Lobia)",
        "scientific_name": "Vigna unguiculata",
        "categories": [
            "pulse",
            "legume",
            "n_fixing",
            "green_manure"
        ],
        "crop_family": "Fabaceae",
        "season": "kharif_or_zaid",
        "duration_range_days": [
            65,
            80
        ],
        "typical_duration": 70,
        "water_need_range_mm": [
            250,
            350
        ],
        "typical_water_mm": 280,
        "nitrogen_fixation_range_kg_ha": [
            30,
            50
        ],
        "nitrogen_fixation_kg_ha": 40,
        "root_type": "deep_taproot",
        "root_depth_range_cm": [
            50,
            90
        ],
        "soil_cover_rating": 4,
        "drought_tolerance": 4,
        "waterlogging_tolerance": 2,
        "market_stability": "medium",
        "n_feeder": "low",
        "suitable_soils": [
            "sandy_loam",
            "alluvial",
            "red_laterite"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "southern_peninsula": "high",
            "central": "high"
        },
        "data_source": "TNAU Agritech Portal & ICAR Pulse Guide",
        "source_year": "2020",
        "data_confidence": "high",
        "limitations": [
            "Aphid infestation vectors mosaic virus",
            "Excessive vegetative growth if over-irrigated"
        ],
        "primary_category": "pulses",
        "water_need_mm": [
            250,
            350
        ],
        "duration_days": [
            65,
            80
        ],
        "root_depth_cm": [
            50,
            90
        ]
    },
    "soybean": {
        "id": "soybean",
        "name": "Soybean",
        "scientific_name": "Glycine max",
        "categories": [
            "oilseed",
            "legume",
            "n_fixing",
            "industrial"
        ],
        "crop_family": "Fabaceae",
        "season": "kharif",
        "duration_range_days": [
            90,
            105
        ],
        "typical_duration": 95,
        "water_need_range_mm": [
            450,
            600
        ],
        "typical_water_mm": 500,
        "nitrogen_fixation_range_kg_ha": [
            30,
            55
        ],
        "nitrogen_fixation_kg_ha": 40,
        "root_type": "deep_taproot",
        "root_depth_range_cm": [
            60,
            100
        ],
        "soil_cover_rating": 4,
        "drought_tolerance": 3,
        "waterlogging_tolerance": 2,
        "market_stability": "high",
        "n_feeder": "low",
        "suitable_soils": [
            "black_cotton",
            "clay_loam",
            "alluvial"
        ],
        "regional_suitability": {
            "bihar": "moderate",
            "central": "high",
            "deccan": "high",
            "indo_gangetic": "moderate"
        },
        "data_source": "ICAR-IISR Indore Soybean Research Manual",
        "source_year": "2022",
        "data_confidence": "high",
        "limitations": [
            "Seed viability deteriorates rapidly under high humidity in eastern India",
            "Girdle beetle damage"
        ],
        "primary_category": "oilseeds",
        "water_need_mm": [
            450,
            600
        ],
        "duration_days": [
            90,
            105
        ],
        "root_depth_cm": [
            60,
            100
        ]
    },
    "cluster_bean": {
        "id": "cluster_bean",
        "name": "Cluster Bean (Guar)",
        "scientific_name": "Cyamopsis tetragonoloba",
        "categories": [
            "pulse",
            "legume",
            "industrial_gum",
            "drought_hardy"
        ],
        "crop_family": "Fabaceae",
        "season": "kharif",
        "duration_range_days": [
            85,
            105
        ],
        "typical_duration": 90,
        "water_need_range_mm": [
            200,
            300
        ],
        "typical_water_mm": 250,
        "nitrogen_fixation_range_kg_ha": [
            25,
            45
        ],
        "nitrogen_fixation_kg_ha": 35,
        "root_type": "deep_taproot",
        "root_depth_range_cm": [
            80,
            140
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 5,
        "waterlogging_tolerance": 1,
        "market_stability": "medium",
        "n_feeder": "low",
        "suitable_soils": [
            "sandy_loam",
            "alluvial"
        ],
        "regional_suitability": {
            "bihar": "moderate",
            "arid_west": "high",
            "indo_gangetic": "moderate",
            "central": "moderate"
        },
        "data_source": "ICAR-CAZRI Jodhpur Guar Package of Practices",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Highly sensitive to waterlogging",
            "Bacterial blight in humid monsoon zones"
        ],
        "primary_category": "pulses",
        "water_need_mm": [
            200,
            300
        ],
        "duration_days": [
            85,
            105
        ],
        "root_depth_cm": [
            80,
            140
        ]
    },
    "horse_gram": {
        "id": "horse_gram",
        "name": "Horse Gram (Kulthi)",
        "scientific_name": "Macrotyloma uniflorum",
        "categories": [
            "pulse",
            "legume",
            "drought_hardy",
            "fodder"
        ],
        "crop_family": "Fabaceae",
        "season": "kharif_or_rabi",
        "duration_range_days": [
            90,
            110
        ],
        "typical_duration": 100,
        "water_need_range_mm": [
            150,
            250
        ],
        "typical_water_mm": 200,
        "nitrogen_fixation_range_kg_ha": [
            15,
            30
        ],
        "nitrogen_fixation_kg_ha": 25,
        "root_type": "deep_taproot",
        "root_depth_range_cm": [
            50,
            90
        ],
        "soil_cover_rating": 4,
        "drought_tolerance": 5,
        "waterlogging_tolerance": 1,
        "market_stability": "medium",
        "n_feeder": "low",
        "suitable_soils": [
            "red_laterite",
            "sandy_loam",
            "alluvial"
        ],
        "regional_suitability": {
            "bihar": "high",
            "southern_peninsula": "high",
            "central": "high",
            "chota_nagpur": "high"
        },
        "data_source": "ICAR Pulses Manual & BAU Sabour Tribal Sub-Plan",
        "source_year": "2020",
        "data_confidence": "medium",
        "limitations": [
            "Low harvest index and lower yield potential than chickpea or lentil"
        ],
        "primary_category": "pulses",
        "water_need_mm": [
            150,
            250
        ],
        "duration_days": [
            90,
            110
        ],
        "root_depth_cm": [
            50,
            90
        ]
    },
    "mustard": {
        "id": "mustard",
        "name": "Mustard / Rapeseed (Sarson / Rai)",
        "scientific_name": "Brassica juncea",
        "categories": [
            "oilseed",
            "cash_crop"
        ],
        "crop_family": "Brassicaceae",
        "season": "rabi",
        "duration_range_days": [
            100,
            125
        ],
        "typical_duration": 115,
        "water_need_range_mm": [
            220,
            300
        ],
        "typical_water_mm": 250,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "deep_taproot",
        "root_depth_range_cm": [
            60,
            110
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 4,
        "waterlogging_tolerance": 1,
        "market_stability": "high",
        "n_feeder": "medium",
        "suitable_soils": [
            "alluvial",
            "sandy_loam",
            "clay_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "arid_west": "high",
            "central": "high"
        },
        "data_source": "ICAR-DRMR Bharatpur Mustard Production Guide",
        "source_year": "2023",
        "data_confidence": "high",
        "limitations": [
            "Mustard aphid (Lipaphis erysimi) attack during cloudy/humid spells",
            "Frost sensitivity during siliqua filling"
        ],
        "primary_category": "oilseeds",
        "water_need_mm": [
            220,
            300
        ],
        "duration_days": [
            100,
            125
        ],
        "root_depth_cm": [
            60,
            110
        ]
    },
    "groundnut": {
        "id": "groundnut",
        "name": "Groundnut / Peanut (Moongphali)",
        "scientific_name": "Arachis hypogaea",
        "categories": [
            "oilseed",
            "legume",
            "n_fixing",
            "cash_crop"
        ],
        "crop_family": "Fabaceae",
        "season": "kharif_or_zaid",
        "duration_range_days": [
            105,
            125
        ],
        "typical_duration": 115,
        "water_need_range_mm": [
            400,
            550
        ],
        "typical_water_mm": 450,
        "nitrogen_fixation_range_kg_ha": [
            25,
            45
        ],
        "nitrogen_fixation_kg_ha": 35,
        "root_type": "moderate_taproot",
        "root_depth_range_cm": [
            40,
            80
        ],
        "soil_cover_rating": 4,
        "drought_tolerance": 4,
        "waterlogging_tolerance": 1,
        "market_stability": "high",
        "n_feeder": "low",
        "suitable_soils": [
            "sandy_loam",
            "alluvial",
            "red_laterite"
        ],
        "regional_suitability": {
            "bihar": "moderate",
            "arid_west": "high",
            "deccan": "high",
            "southern_peninsula": "high",
            "indo_gangetic": "moderate"
        },
        "data_source": "ICAR-DGR Junagadh Groundnut Research Handbook",
        "source_year": "2022",
        "data_confidence": "high",
        "limitations": [
            "Requires light friable soil for peg penetration and easy pod harvesting",
            "Aflatoxin risk in wet storage"
        ],
        "primary_category": "oilseeds",
        "water_need_mm": [
            400,
            550
        ],
        "duration_days": [
            105,
            125
        ],
        "root_depth_cm": [
            40,
            80
        ]
    },
    "sesame": {
        "id": "sesame",
        "name": "Sesame (Til)",
        "scientific_name": "Sesamum indicum",
        "categories": [
            "oilseed",
            "cash_crop",
            "short_duration"
        ],
        "crop_family": "Pedaliaceae",
        "season": "kharif_or_zaid",
        "duration_range_days": [
            75,
            90
        ],
        "typical_duration": 80,
        "water_need_range_mm": [
            200,
            300
        ],
        "typical_water_mm": 250,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "deep_taproot",
        "root_depth_range_cm": [
            60,
            100
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 5,
        "waterlogging_tolerance": 1,
        "market_stability": "medium",
        "n_feeder": "low",
        "suitable_soils": [
            "sandy_loam",
            "alluvial",
            "red_laterite"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "eastern_coastal": "high",
            "central": "high",
            "arid_west": "high"
        },
        "data_source": "ICAR-AICRP on Oilseeds & TNAU Portal",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Extremely vulnerable to water stagnation even for 24 hours",
            "Phyllody disease transmitted by leafhoppers"
        ],
        "primary_category": "oilseeds",
        "water_need_mm": [
            200,
            300
        ],
        "duration_days": [
            75,
            90
        ],
        "root_depth_cm": [
            60,
            100
        ]
    },
    "sunflower": {
        "id": "sunflower",
        "name": "Sunflower (Surajmukhi)",
        "scientific_name": "Helianthus annuus",
        "categories": [
            "oilseed",
            "photo_insensitive"
        ],
        "crop_family": "Asteraceae",
        "season": "rabi_or_zaid",
        "duration_range_days": [
            85,
            100
        ],
        "typical_duration": 90,
        "water_need_range_mm": [
            350,
            480
        ],
        "typical_water_mm": 400,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "deep_taproot",
        "root_depth_range_cm": [
            70,
            120
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 4,
        "waterlogging_tolerance": 2,
        "market_stability": "medium",
        "n_feeder": "medium",
        "suitable_soils": [
            "alluvial",
            "black_cotton",
            "clay_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "deccan": "high",
            "southern_peninsula": "high"
        },
        "data_source": "ICAR-IIOR Hyderabad Sunflower Agronomy",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Bird damage (parrots) near harvest",
            "Requires managed bee pollination for optimal seed set"
        ],
        "primary_category": "oilseeds",
        "water_need_mm": [
            350,
            480
        ],
        "duration_days": [
            85,
            100
        ],
        "root_depth_cm": [
            70,
            120
        ]
    },
    "safflower": {
        "id": "safflower",
        "name": "Safflower (Kusum)",
        "scientific_name": "Carthamus tinctorius",
        "categories": [
            "oilseed",
            "deep_rooting",
            "drought_hardy"
        ],
        "crop_family": "Asteraceae",
        "season": "rabi",
        "duration_range_days": [
            120,
            140
        ],
        "typical_duration": 130,
        "water_need_range_mm": [
            200,
            300
        ],
        "typical_water_mm": 250,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "deep_taproot",
        "root_depth_range_cm": [
            100,
            200
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 5,
        "waterlogging_tolerance": 1,
        "market_stability": "medium",
        "n_feeder": "medium",
        "suitable_soils": [
            "black_cotton",
            "clay_loam"
        ],
        "regional_suitability": {
            "bihar": "moderate",
            "central": "high",
            "deccan": "high"
        },
        "data_source": "ICAR-IIOR Hyderabad Research Manual",
        "source_year": "2020",
        "data_confidence": "high",
        "limitations": [
            "Spiny foliage makes manual harvesting difficult",
            "Aphids during budding"
        ],
        "primary_category": "oilseeds",
        "water_need_mm": [
            200,
            300
        ],
        "duration_days": [
            120,
            140
        ],
        "root_depth_cm": [
            100,
            200
        ]
    },
    "linseed": {
        "id": "linseed",
        "name": "Linseed / Flax (Alsi)",
        "scientific_name": "Linum usitatissimum",
        "categories": [
            "oilseed",
            "industrial_fiber"
        ],
        "crop_family": "Linaceae",
        "season": "rabi",
        "duration_range_days": [
            110,
            130
        ],
        "typical_duration": 120,
        "water_need_range_mm": [
            200,
            280
        ],
        "typical_water_mm": 240,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "moderate_taproot",
        "root_depth_range_cm": [
            40,
            80
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 4,
        "waterlogging_tolerance": 2,
        "market_stability": "medium",
        "n_feeder": "low",
        "suitable_soils": [
            "alluvial",
            "clay_loam",
            "black_cotton"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "central": "high"
        },
        "data_source": "ICAR-IIPR / AICRP on Linseed Kanpur",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Often grown as utera/paira crop with low management leading to modest yields",
            "Rust vulnerability"
        ],
        "primary_category": "oilseeds",
        "water_need_mm": [
            200,
            280
        ],
        "duration_days": [
            110,
            130
        ],
        "root_depth_cm": [
            40,
            80
        ]
    },
    "castor": {
        "id": "castor",
        "name": "Castor (Arandi)",
        "scientific_name": "Ricinus communis",
        "categories": [
            "oilseed",
            "industrial_lubricant"
        ],
        "crop_family": "Euphorbiaceae",
        "season": "kharif",
        "duration_range_days": [
            150,
            180
        ],
        "typical_duration": 165,
        "water_need_range_mm": [
            400,
            550
        ],
        "typical_water_mm": 450,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "deep_taproot",
        "root_depth_range_cm": [
            100,
            180
        ],
        "soil_cover_rating": 4,
        "drought_tolerance": 5,
        "waterlogging_tolerance": 1,
        "market_stability": "high",
        "n_feeder": "medium",
        "suitable_soils": [
            "sandy_loam",
            "alluvial",
            "red_laterite"
        ],
        "regional_suitability": {
            "bihar": "moderate",
            "arid_west": "high",
            "southern_peninsula": "high",
            "central": "high"
        },
        "data_source": "ICAR-IIOR Hyderabad Castor Factsheet",
        "source_year": "2022",
        "data_confidence": "high",
        "limitations": [
            "Non-edible toxic oil (ricin in seeds)",
            "Long duration precludes immediate Rabi sowing on same plot"
        ],
        "primary_category": "oilseeds",
        "water_need_mm": [
            400,
            550
        ],
        "duration_days": [
            150,
            180
        ],
        "root_depth_cm": [
            100,
            180
        ]
    },
    "potato": {
        "id": "potato",
        "name": "Potato (Aloo)",
        "scientific_name": "Solanum tuberosum",
        "categories": [
            "vegetable",
            "tuber",
            "cash_crop"
        ],
        "crop_family": "Solanaceae",
        "season": "rabi",
        "duration_range_days": [
            80,
            100
        ],
        "typical_duration": 90,
        "water_need_range_mm": [
            400,
            550
        ],
        "typical_water_mm": 480,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "tuberous",
        "root_depth_range_cm": [
            30,
            50
        ],
        "soil_cover_rating": 4,
        "drought_tolerance": 2,
        "waterlogging_tolerance": 1,
        "market_stability": "medium",
        "n_feeder": "high",
        "suitable_soils": [
            "alluvial",
            "sandy_loam",
            "silt_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "hilly_north": "high",
            "eastern_coastal": "moderate"
        },
        "data_source": "ICAR-CPRI Shimla Potato Production Guide",
        "source_year": "2022",
        "data_confidence": "high",
        "limitations": [
            "Late blight (Phytophthora infestans) epidemics under cold humid spells",
            "Heavy input costs for seed tubers and cold storage"
        ],
        "primary_category": "vegetables",
        "water_need_mm": [
            400,
            550
        ],
        "duration_days": [
            80,
            100
        ],
        "root_depth_cm": [
            30,
            50
        ]
    },
    "onion": {
        "id": "onion",
        "name": "Onion (Pyaz)",
        "scientific_name": "Allium cepa",
        "categories": [
            "vegetable",
            "bulb",
            "cash_crop"
        ],
        "crop_family": "Amaryllidaceae",
        "season": "rabi_or_kharif",
        "duration_range_days": [
            110,
            130
        ],
        "typical_duration": 120,
        "water_need_range_mm": [
            400,
            550
        ],
        "typical_water_mm": 450,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "shallow_fibrous",
        "root_depth_range_cm": [
            20,
            35
        ],
        "soil_cover_rating": 2,
        "drought_tolerance": 2,
        "waterlogging_tolerance": 1,
        "market_stability": "high_value_volatile",
        "n_feeder": "medium",
        "suitable_soils": [
            "alluvial",
            "sandy_loam",
            "clay_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "deccan": "high",
            "arid_west": "high"
        },
        "data_source": "ICAR-DOGR Pune Onion Agronomy",
        "source_year": "2023",
        "data_confidence": "high",
        "limitations": [
            "High post-harvest storage loss (up to 30% rotting)",
            "Extreme price volatility across seasons"
        ],
        "primary_category": "vegetables",
        "water_need_mm": [
            400,
            550
        ],
        "duration_days": [
            110,
            130
        ],
        "root_depth_cm": [
            20,
            35
        ]
    },
    "tomato": {
        "id": "tomato",
        "name": "Tomato (Tamatar)",
        "scientific_name": "Solanum lycopersicum",
        "categories": [
            "vegetable",
            "cash_crop"
        ],
        "crop_family": "Solanaceae",
        "season": "rabi_or_kharif",
        "duration_range_days": [
            100,
            130
        ],
        "typical_duration": 115,
        "water_need_range_mm": [
            450,
            650
        ],
        "typical_water_mm": 550,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "deep_taproot",
        "root_depth_range_cm": [
            50,
            90
        ],
        "soil_cover_rating": 4,
        "drought_tolerance": 3,
        "waterlogging_tolerance": 1,
        "market_stability": "high_value_volatile",
        "n_feeder": "high",
        "suitable_soils": [
            "alluvial",
            "sandy_loam",
            "red_laterite"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "central": "high",
            "southern_peninsula": "high"
        },
        "data_source": "ICAR-IIVR Varanasi Vegetable Compendium",
        "source_year": "2022",
        "data_confidence": "high",
        "limitations": [
            "Tomato leaf curl virus (ToLCV) via whitefly",
            "Market price collapse during peak glut"
        ],
        "primary_category": "vegetables",
        "water_need_mm": [
            450,
            650
        ],
        "duration_days": [
            100,
            130
        ],
        "root_depth_cm": [
            50,
            90
        ]
    },
    "brinjal": {
        "id": "brinjal",
        "name": "Brinjal / Eggplant (Baingan)",
        "scientific_name": "Solanum melongena",
        "categories": [
            "vegetable"
        ],
        "crop_family": "Solanaceae",
        "season": "kharif_or_rabi",
        "duration_range_days": [
            120,
            150
        ],
        "typical_duration": 135,
        "water_need_range_mm": [
            500,
            700
        ],
        "typical_water_mm": 600,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "deep_taproot",
        "root_depth_range_cm": [
            60,
            100
        ],
        "soil_cover_rating": 4,
        "drought_tolerance": 3,
        "waterlogging_tolerance": 2,
        "market_stability": "medium",
        "n_feeder": "high",
        "suitable_soils": [
            "alluvial",
            "silt_loam",
            "clay_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "eastern_coastal": "high",
            "southern_peninsula": "high"
        },
        "data_source": "ICAR-IIVR Varanasi",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Shoot and fruit borer (Leucinodes orbonalis) requires intensive IPM"
        ],
        "primary_category": "vegetables",
        "water_need_mm": [
            500,
            700
        ],
        "duration_days": [
            120,
            150
        ],
        "root_depth_cm": [
            60,
            100
        ]
    },
    "cauliflower": {
        "id": "cauliflower",
        "name": "Cauliflower (Phool Gobhi)",
        "scientific_name": "Brassica oleracea var. botrytis",
        "categories": [
            "vegetable",
            "cash_crop"
        ],
        "crop_family": "Brassicaceae",
        "season": "rabi",
        "duration_range_days": [
            80,
            105
        ],
        "typical_duration": 90,
        "water_need_range_mm": [
            350,
            480
        ],
        "typical_water_mm": 400,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "shallow_fibrous",
        "root_depth_range_cm": [
            30,
            50
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 2,
        "waterlogging_tolerance": 1,
        "market_stability": "medium",
        "n_feeder": "high",
        "suitable_soils": [
            "alluvial",
            "sandy_loam",
            "clay_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "hilly_north": "high"
        },
        "data_source": "ICAR-IIVR Varanasi Vegetable Guide",
        "source_year": "2022",
        "data_confidence": "high",
        "limitations": [
            "Buttoning and riciness if temperatures fluctuate during curd initiation",
            "Diamondback moth"
        ],
        "primary_category": "vegetables",
        "water_need_mm": [
            350,
            480
        ],
        "duration_days": [
            80,
            105
        ],
        "root_depth_cm": [
            30,
            50
        ]
    },
    "cabbage": {
        "id": "cabbage",
        "name": "Cabbage (Patta Gobhi)",
        "scientific_name": "Brassica oleracea var. capitata",
        "categories": [
            "vegetable"
        ],
        "crop_family": "Brassicaceae",
        "season": "rabi",
        "duration_range_days": [
            80,
            110
        ],
        "typical_duration": 95,
        "water_need_range_mm": [
            350,
            480
        ],
        "typical_water_mm": 400,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "shallow_fibrous",
        "root_depth_range_cm": [
            30,
            50
        ],
        "soil_cover_rating": 4,
        "drought_tolerance": 2,
        "waterlogging_tolerance": 2,
        "market_stability": "medium",
        "n_feeder": "high",
        "suitable_soils": [
            "alluvial",
            "clay_loam",
            "silt_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "eastern_coastal": "high"
        },
        "data_source": "ICAR-IIVR Varanasi",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Black rot (Xanthomonas) in rainy transitions",
            "Diamondback moth infestation"
        ],
        "primary_category": "vegetables",
        "water_need_mm": [
            350,
            480
        ],
        "duration_days": [
            80,
            110
        ],
        "root_depth_cm": [
            30,
            50
        ]
    },
    "okra": {
        "id": "okra",
        "name": "Okra / Ladyfinger (Bhindi)",
        "scientific_name": "Abelmoschus esculentus",
        "categories": [
            "vegetable",
            "short_duration"
        ],
        "crop_family": "Malvaceae",
        "season": "kharif_or_zaid",
        "duration_range_days": [
            80,
            100
        ],
        "typical_duration": 90,
        "water_need_range_mm": [
            350,
            500
        ],
        "typical_water_mm": 420,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "moderate_taproot",
        "root_depth_range_cm": [
            40,
            70
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 3,
        "waterlogging_tolerance": 1,
        "market_stability": "medium",
        "n_feeder": "medium",
        "suitable_soils": [
            "alluvial",
            "sandy_loam",
            "clay_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "central": "high",
            "southern_peninsula": "high"
        },
        "data_source": "ICAR-IIVR Varanasi Okra Package",
        "source_year": "2022",
        "data_confidence": "high",
        "limitations": [
            "Yellow Vein Mosaic Virus (YVMV) requires resistant hybrids",
            "Requires picking every 2-3 days"
        ],
        "primary_category": "vegetables",
        "water_need_mm": [
            350,
            500
        ],
        "duration_days": [
            80,
            100
        ],
        "root_depth_cm": [
            40,
            70
        ]
    },
    "green_chilli": {
        "id": "green_chilli",
        "name": "Green Chilli (Mirchi)",
        "scientific_name": "Capsicum annuum",
        "categories": [
            "vegetable",
            "spice",
            "cash_crop"
        ],
        "crop_family": "Solanaceae",
        "season": "kharif_or_rabi",
        "duration_range_days": [
            120,
            160
        ],
        "typical_duration": 140,
        "water_need_range_mm": [
            450,
            600
        ],
        "typical_water_mm": 500,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "moderate_taproot",
        "root_depth_range_cm": [
            40,
            75
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 3,
        "waterlogging_tolerance": 1,
        "market_stability": "high_value_volatile",
        "n_feeder": "medium",
        "suitable_soils": [
            "alluvial",
            "sandy_loam",
            "black_cotton"
        ],
        "regional_suitability": {
            "bihar": "high",
            "southern_peninsula": "high",
            "central": "high",
            "indo_gangetic": "high"
        },
        "data_source": "ICAR-IIVR & TNAU Portal",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Chilli leaf curl and thrips/mites complex",
            "Water stagnation causes sudden wilt"
        ],
        "primary_category": "vegetables",
        "water_need_mm": [
            450,
            600
        ],
        "duration_days": [
            120,
            160
        ],
        "root_depth_cm": [
            40,
            75
        ]
    },
    "garlic": {
        "id": "garlic",
        "name": "Garlic (Lahsun)",
        "scientific_name": "Allium sativum",
        "categories": [
            "vegetable",
            "spice",
            "cash_crop"
        ],
        "crop_family": "Amaryllidaceae",
        "season": "rabi",
        "duration_range_days": [
            120,
            140
        ],
        "typical_duration": 130,
        "water_need_range_mm": [
            350,
            450
        ],
        "typical_water_mm": 400,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "shallow_fibrous",
        "root_depth_range_cm": [
            20,
            35
        ],
        "soil_cover_rating": 2,
        "drought_tolerance": 2,
        "waterlogging_tolerance": 1,
        "market_stability": "high",
        "n_feeder": "medium",
        "suitable_soils": [
            "alluvial",
            "sandy_loam",
            "clay_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "central": "high",
            "arid_west": "high"
        },
        "data_source": "ICAR-DOGR Pune Garlic Research",
        "source_year": "2022",
        "data_confidence": "high",
        "limitations": [
            "Bulb rot in poorly drained soil",
            "High initial seed clove purchase cost"
        ],
        "primary_category": "spices",
        "water_need_mm": [
            350,
            450
        ],
        "duration_days": [
            120,
            140
        ],
        "root_depth_cm": [
            20,
            35
        ]
    },
    "ginger": {
        "id": "ginger",
        "name": "Ginger (Adrak)",
        "scientific_name": "Zingiber officinale",
        "categories": [
            "vegetable",
            "spice",
            "tuber",
            "cash_crop"
        ],
        "crop_family": "Zingiberaceae",
        "season": "kharif",
        "duration_range_days": [
            200,
            240
        ],
        "typical_duration": 220,
        "water_need_range_mm": [
            1200,
            1500
        ],
        "typical_water_mm": 1350,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "tuberous",
        "root_depth_range_cm": [
            25,
            45
        ],
        "soil_cover_rating": 4,
        "drought_tolerance": 2,
        "waterlogging_tolerance": 1,
        "market_stability": "high",
        "n_feeder": "high",
        "suitable_soils": [
            "sandy_loam",
            "alluvial",
            "red_laterite"
        ],
        "regional_suitability": {
            "bihar": "moderate",
            "north_east": "high",
            "western_ghats": "high",
            "eastern_coastal": "moderate"
        },
        "data_source": "ICAR-IISR Kozhikode Spices Package",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Rhizome rot (Pythium) under excessive moisture",
            "Requires partial shade and mulch"
        ],
        "primary_category": "spices",
        "water_need_mm": [
            1200,
            1500
        ],
        "duration_days": [
            200,
            240
        ],
        "root_depth_cm": [
            25,
            45
        ]
    },
    "carrot": {
        "id": "carrot",
        "name": "Carrot (Gajar)",
        "scientific_name": "Daucus carota",
        "categories": [
            "vegetable",
            "root_crop"
        ],
        "crop_family": "Apiaceae",
        "season": "rabi",
        "duration_range_days": [
            80,
            100
        ],
        "typical_duration": 90,
        "water_need_range_mm": [
            300,
            420
        ],
        "typical_water_mm": 350,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "tuberous",
        "root_depth_range_cm": [
            30,
            50
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 3,
        "waterlogging_tolerance": 1,
        "market_stability": "medium",
        "n_feeder": "medium",
        "suitable_soils": [
            "alluvial",
            "sandy_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "hilly_north": "high"
        },
        "data_source": "ICAR-IIVR Varanasi",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Forking and splitting in heavy or compact clay soils",
            "Cavity spot in wet beds"
        ],
        "primary_category": "vegetables",
        "water_need_mm": [
            300,
            420
        ],
        "duration_days": [
            80,
            100
        ],
        "root_depth_cm": [
            30,
            50
        ]
    },
    "radish": {
        "id": "radish",
        "name": "Radish (Mooli)",
        "scientific_name": "Raphanus sativus",
        "categories": [
            "vegetable",
            "root_crop",
            "short_duration"
        ],
        "crop_family": "Brassicaceae",
        "season": "rabi_or_zaid",
        "duration_range_days": [
            45,
            60
        ],
        "typical_duration": 50,
        "water_need_range_mm": [
            180,
            260
        ],
        "typical_water_mm": 220,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "tuberous",
        "root_depth_range_cm": [
            25,
            45
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 3,
        "waterlogging_tolerance": 1,
        "market_stability": "medium",
        "n_feeder": "medium",
        "suitable_soils": [
            "alluvial",
            "sandy_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "central": "high"
        },
        "data_source": "ICAR-IIVR Varanasi",
        "source_year": "2020",
        "data_confidence": "high",
        "limitations": [
            "Pithiness and pungency if harvest delayed past 55 days",
            "Flea beetle damage"
        ],
        "primary_category": "vegetables",
        "water_need_mm": [
            180,
            260
        ],
        "duration_days": [
            45,
            60
        ],
        "root_depth_cm": [
            25,
            45
        ]
    },
    "bitter_gourd": {
        "id": "bitter_gourd",
        "name": "Bitter Gourd (Karela)",
        "scientific_name": "Momordica charantia",
        "categories": [
            "vegetable",
            "cucurbit"
        ],
        "crop_family": "Cucurbitaceae",
        "season": "kharif_or_zaid",
        "duration_range_days": [
            90,
            115
        ],
        "typical_duration": 100,
        "water_need_range_mm": [
            350,
            500
        ],
        "typical_water_mm": 420,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "moderate_taproot",
        "root_depth_range_cm": [
            40,
            70
        ],
        "soil_cover_rating": 4,
        "drought_tolerance": 3,
        "waterlogging_tolerance": 1,
        "market_stability": "medium",
        "n_feeder": "medium",
        "suitable_soils": [
            "alluvial",
            "sandy_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "southern_peninsula": "high",
            "eastern_coastal": "high"
        },
        "data_source": "ICAR-IIVR & TNAU Portal",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Fruit fly (Bactrocera cucurbitae) requires pheromone traps",
            "Downy mildew in rainy season"
        ],
        "primary_category": "vegetables",
        "water_need_mm": [
            350,
            500
        ],
        "duration_days": [
            90,
            115
        ],
        "root_depth_cm": [
            40,
            70
        ]
    },
    "sugarcane": {
        "id": "sugarcane",
        "name": "Sugarcane (Ganna)",
        "scientific_name": "Saccharum officinarum",
        "categories": [
            "commercial",
            "sugar",
            "perennial_or_annual"
        ],
        "crop_family": "Poaceae",
        "season": "annual",
        "duration_range_days": [
            300,
            365
        ],
        "typical_duration": 330,
        "water_need_range_mm": [
            1500,
            2200
        ],
        "typical_water_mm": 1800,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "deep_fibrous",
        "root_depth_range_cm": [
            80,
            150
        ],
        "soil_cover_rating": 5,
        "drought_tolerance": 3,
        "waterlogging_tolerance": 4,
        "market_stability": "high",
        "n_feeder": "high",
        "suitable_soils": [
            "alluvial",
            "clay_loam",
            "black_cotton"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "deccan": "high",
            "southern_peninsula": "high"
        },
        "data_source": "ICAR-IISR Lucknow Sugarcane Compendium",
        "source_year": "2022",
        "data_confidence": "high",
        "limitations": [
            "Extreme water demand (~1800 mm)",
            "Ties up land for 10-12 months",
            "Mill payment settlement delays"
        ],
        "primary_category": "commercial_cash",
        "water_need_mm": [
            1500,
            2200
        ],
        "duration_days": [
            300,
            365
        ],
        "root_depth_cm": [
            80,
            150
        ]
    },
    "cotton": {
        "id": "cotton",
        "name": "Cotton (Kapas)",
        "scientific_name": "Gossypium hirsutum",
        "categories": [
            "commercial",
            "fiber",
            "cash_crop"
        ],
        "crop_family": "Malvaceae",
        "season": "kharif",
        "duration_range_days": [
            150,
            180
        ],
        "typical_duration": 165,
        "water_need_range_mm": [
            650,
            900
        ],
        "typical_water_mm": 750,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "deep_taproot",
        "root_depth_range_cm": [
            100,
            180
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 4,
        "waterlogging_tolerance": 1,
        "market_stability": "high",
        "n_feeder": "high",
        "suitable_soils": [
            "black_cotton",
            "alluvial",
            "clay_loam"
        ],
        "regional_suitability": {
            "bihar": "low",
            "central": "high",
            "deccan": "high",
            "arid_west": "high",
            "southern_peninsula": "high"
        },
        "data_source": "ICAR-CICR Nagpur Cotton Research Manual",
        "source_year": "2023",
        "data_confidence": "high",
        "limitations": [
            "Pink bollworm resistance challenges",
            "Not traditionally suited to heavy flood-prone eastern plains"
        ],
        "primary_category": "commercial_cash",
        "water_need_mm": [
            650,
            900
        ],
        "duration_days": [
            150,
            180
        ],
        "root_depth_cm": [
            100,
            180
        ]
    },
    "jute": {
        "id": "jute",
        "name": "Jute (Patson)",
        "scientific_name": "Corchorus olitorius",
        "categories": [
            "commercial",
            "fiber"
        ],
        "crop_family": "Malvaceae",
        "season": "zaid_to_kharif",
        "duration_range_days": [
            110,
            130
        ],
        "typical_duration": 120,
        "water_need_range_mm": [
            800,
            1200
        ],
        "typical_water_mm": 1000,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "deep_taproot",
        "root_depth_range_cm": [
            60,
            100
        ],
        "soil_cover_rating": 5,
        "drought_tolerance": 2,
        "waterlogging_tolerance": 5,
        "market_stability": "high",
        "n_feeder": "medium",
        "suitable_soils": [
            "alluvial",
            "clay_loam",
            "silt_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "eastern_coastal": "high",
            "north_east": "high"
        },
        "data_source": "ICAR-CRIJAF Barrackpore Jute Factsheet",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Requires abundant clean slow-moving water bodies for microbial retting"
        ],
        "primary_category": "commercial_cash",
        "water_need_mm": [
            800,
            1200
        ],
        "duration_days": [
            110,
            130
        ],
        "root_depth_cm": [
            60,
            100
        ]
    },
    "tobacco": {
        "id": "tobacco",
        "name": "Tobacco (Tambaku)",
        "scientific_name": "Nicotiana tabacum",
        "categories": [
            "commercial",
            "cash_crop"
        ],
        "crop_family": "Solanaceae",
        "season": "rabi",
        "duration_range_days": [
            110,
            130
        ],
        "typical_duration": 120,
        "water_need_range_mm": [
            350,
            500
        ],
        "typical_water_mm": 420,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "moderate_taproot",
        "root_depth_range_cm": [
            50,
            90
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 3,
        "waterlogging_tolerance": 1,
        "market_stability": "medium",
        "n_feeder": "high",
        "suitable_soils": [
            "alluvial",
            "sandy_loam",
            "black_cotton"
        ],
        "regional_suitability": {
            "bihar": "high",
            "southern_peninsula": "high",
            "arid_west": "high"
        },
        "data_source": "ICAR-CTRI Rajahmundry Research Bulletin",
        "source_year": "2020",
        "data_confidence": "high",
        "limitations": [
            "Heavy chemical input requirements",
            "Strict curing barn infrastructure needed",
            "Soil health depleting"
        ],
        "primary_category": "commercial_cash",
        "water_need_mm": [
            350,
            500
        ],
        "duration_days": [
            110,
            130
        ],
        "root_depth_cm": [
            50,
            90
        ]
    },
    "betel_vine": {
        "id": "betel_vine",
        "name": "Betel Vine (Paan)",
        "scientific_name": "Piper betle",
        "categories": [
            "commercial",
            "perennial",
            "plantation"
        ],
        "crop_family": "Piperaceae",
        "season": "perennial",
        "duration_range_days": [
            365,
            730
        ],
        "typical_duration": 365,
        "water_need_range_mm": [
            1400,
            1800
        ],
        "typical_water_mm": 1600,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "shallow_fibrous",
        "root_depth_range_cm": [
            20,
            40
        ],
        "soil_cover_rating": 5,
        "drought_tolerance": 1,
        "waterlogging_tolerance": 1,
        "market_stability": "high",
        "n_feeder": "high",
        "suitable_soils": [
            "alluvial",
            "sandy_loam",
            "silt_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "eastern_coastal": "high",
            "southern_peninsula": "high"
        },
        "data_source": "ICAR-IIHR & BAU Sabour Horticulture Report",
        "source_year": "2021",
        "data_confidence": "medium",
        "limitations": [
            "Requires specialized thatched conservatories (bareja)",
            "High labor and constant disease monitoring"
        ],
        "primary_category": "commercial_cash",
        "water_need_mm": [
            1400,
            1800
        ],
        "duration_days": [
            365,
            730
        ],
        "root_depth_cm": [
            20,
            40
        ]
    },
    "banana": {
        "id": "banana",
        "name": "Banana (Kela)",
        "scientific_name": "Musa acuminata",
        "categories": [
            "fruit",
            "perennial_or_annual",
            "cash_crop"
        ],
        "crop_family": "Musaceae",
        "season": "annual",
        "duration_range_days": [
            330,
            380
        ],
        "typical_duration": 350,
        "water_need_range_mm": [
            1500,
            2200
        ],
        "typical_water_mm": 1800,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "shallow_fibrous",
        "root_depth_range_cm": [
            40,
            70
        ],
        "soil_cover_rating": 5,
        "drought_tolerance": 2,
        "waterlogging_tolerance": 2,
        "market_stability": "high",
        "n_feeder": "high",
        "suitable_soils": [
            "alluvial",
            "clay_loam",
            "silt_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "southern_peninsula": "high",
            "eastern_coastal": "high"
        },
        "data_source": "ICAR-NRCB Tiruchirappalli Banana Package",
        "source_year": "2022",
        "data_confidence": "high",
        "limitations": [
            "High continuous water demand",
            "Panama wilt (Fusarium oxysporum) and bunchy top virus"
        ],
        "primary_category": "fruits",
        "water_need_mm": [
            1500,
            2200
        ],
        "duration_days": [
            330,
            380
        ],
        "root_depth_cm": [
            40,
            70
        ]
    },
    "papaya": {
        "id": "papaya",
        "name": "Papaya (Papita)",
        "scientific_name": "Carica papaya",
        "categories": [
            "fruit",
            "perennial_or_annual",
            "quick_cash"
        ],
        "crop_family": "Caricaceae",
        "season": "annual",
        "duration_range_days": [
            270,
            365
        ],
        "typical_duration": 300,
        "water_need_range_mm": [
            1000,
            1400
        ],
        "typical_water_mm": 1200,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "moderate_taproot",
        "root_depth_range_cm": [
            40,
            80
        ],
        "soil_cover_rating": 4,
        "drought_tolerance": 3,
        "waterlogging_tolerance": 1,
        "market_stability": "medium",
        "n_feeder": "high",
        "suitable_soils": [
            "alluvial",
            "sandy_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "southern_peninsula": "high",
            "central": "high"
        },
        "data_source": "ICAR-IIHR Bengaluru Horticulture Manual",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Cannot tolerate even 12 hours of waterlogging (causes stem rot)",
            "Papaya ring spot virus (PRSV)"
        ],
        "primary_category": "fruits",
        "water_need_mm": [
            1000,
            1400
        ],
        "duration_days": [
            270,
            365
        ],
        "root_depth_cm": [
            40,
            80
        ]
    },
    "guava": {
        "id": "guava",
        "name": "Guava (Amrud)",
        "scientific_name": "Psidium guajava",
        "categories": [
            "fruit",
            "perennial",
            "hardy_orchard"
        ],
        "crop_family": "Myrtaceae",
        "season": "perennial",
        "duration_range_days": [
            365,
            730
        ],
        "typical_duration": 365,
        "water_need_range_mm": [
            800,
            1200
        ],
        "typical_water_mm": 1000,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "perennial_woody",
        "root_depth_range_cm": [
            80,
            150
        ],
        "soil_cover_rating": 5,
        "drought_tolerance": 4,
        "waterlogging_tolerance": 3,
        "market_stability": "high",
        "n_feeder": "medium",
        "suitable_soils": [
            "alluvial",
            "sandy_loam",
            "red_laterite"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "central": "high",
            "deccan": "high"
        },
        "data_source": "ICAR-CISH Lucknow Guava Handbook",
        "source_year": "2022",
        "data_confidence": "high",
        "limitations": [
            "Guava wilt (Fusarium oxysporum f. sp. psidii) in alkaline soils",
            "Fruit fly during rainy season crop"
        ],
        "primary_category": "fruits",
        "water_need_mm": [
            800,
            1200
        ],
        "duration_days": [
            365,
            730
        ],
        "root_depth_cm": [
            80,
            150
        ]
    },
    "mango": {
        "id": "mango",
        "name": "Mango (Aam)",
        "scientific_name": "Mangifera indica",
        "categories": [
            "fruit",
            "perennial",
            "orchard"
        ],
        "crop_family": "Anacardiaceae",
        "season": "perennial",
        "duration_range_days": [
            365,
            730
        ],
        "typical_duration": 365,
        "water_need_range_mm": [
            900,
            1300
        ],
        "typical_water_mm": 1100,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "perennial_woody",
        "root_depth_range_cm": [
            120,
            250
        ],
        "soil_cover_rating": 5,
        "drought_tolerance": 4,
        "waterlogging_tolerance": 2,
        "market_stability": "high",
        "n_feeder": "medium",
        "suitable_soils": [
            "alluvial",
            "sandy_loam",
            "red_laterite"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "southern_peninsula": "high",
            "eastern_coastal": "high"
        },
        "data_source": "ICAR-CISH Lucknow & BAU Sabour Mango Guide",
        "source_year": "2023",
        "data_confidence": "high",
        "limitations": [
            "Alternate bearing habit in traditional cultivars",
            "Mango malformation and hopper pests"
        ],
        "primary_category": "fruits",
        "water_need_mm": [
            900,
            1300
        ],
        "duration_days": [
            365,
            730
        ],
        "root_depth_cm": [
            120,
            250
        ]
    },
    "pomegranate": {
        "id": "pomegranate",
        "name": "Pomegranate (Anar)",
        "scientific_name": "Punica granatum",
        "categories": [
            "fruit",
            "perennial",
            "arid_orchard"
        ],
        "crop_family": "Lythraceae",
        "season": "perennial",
        "duration_range_days": [
            365,
            730
        ],
        "typical_duration": 365,
        "water_need_range_mm": [
            500,
            750
        ],
        "typical_water_mm": 600,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "perennial_woody",
        "root_depth_range_cm": [
            60,
            120
        ],
        "soil_cover_rating": 4,
        "drought_tolerance": 5,
        "waterlogging_tolerance": 1,
        "market_stability": "high",
        "n_feeder": "medium",
        "suitable_soils": [
            "sandy_loam",
            "alluvial",
            "black_cotton"
        ],
        "regional_suitability": {
            "bihar": "moderate",
            "deccan": "high",
            "arid_west": "high",
            "central": "high"
        },
        "data_source": "ICAR-NRCP Solapur Pomegranate Research",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Bacterial blight (Xanthomonas axonopodis pv. punicae) can wipe out orchards",
            "Sensitive to fruit cracking under erratic moisture"
        ],
        "primary_category": "fruits",
        "water_need_mm": [
            500,
            750
        ],
        "duration_days": [
            365,
            730
        ],
        "root_depth_cm": [
            60,
            120
        ]
    },
    "turmeric": {
        "id": "turmeric",
        "name": "Turmeric (Haldi)",
        "scientific_name": "Curcuma longa",
        "categories": [
            "spice",
            "rhizome",
            "cash_crop"
        ],
        "crop_family": "Zingiberaceae",
        "season": "kharif_to_rabi",
        "duration_range_days": [
            210,
            260
        ],
        "typical_duration": 240,
        "water_need_range_mm": [
            1100,
            1500
        ],
        "typical_water_mm": 1300,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "tuberous",
        "root_depth_range_cm": [
            30,
            50
        ],
        "soil_cover_rating": 5,
        "drought_tolerance": 2,
        "waterlogging_tolerance": 2,
        "market_stability": "high",
        "n_feeder": "high",
        "suitable_soils": [
            "sandy_loam",
            "alluvial",
            "red_laterite"
        ],
        "regional_suitability": {
            "bihar": "high",
            "southern_peninsula": "high",
            "eastern_coastal": "high",
            "central": "high"
        },
        "data_source": "ICAR-IISR Kozhikode Turmeric Compendium",
        "source_year": "2022",
        "data_confidence": "high",
        "limitations": [
            "Long 8-month field occupancy",
            "Rhizome rot and leaf blotch in waterlogged soils"
        ],
        "primary_category": "spices",
        "water_need_mm": [
            1100,
            1500
        ],
        "duration_days": [
            210,
            260
        ],
        "root_depth_cm": [
            30,
            50
        ]
    },
    "cumin": {
        "id": "cumin",
        "name": "Cumin (Jeera)",
        "scientific_name": "Cuminum cyminum",
        "categories": [
            "spice",
            "arid_cash_crop"
        ],
        "crop_family": "Apiaceae",
        "season": "rabi",
        "duration_range_days": [
            100,
            120
        ],
        "typical_duration": 110,
        "water_need_range_mm": [
            150,
            220
        ],
        "typical_water_mm": 180,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "moderate_taproot",
        "root_depth_range_cm": [
            30,
            60
        ],
        "soil_cover_rating": 2,
        "drought_tolerance": 5,
        "waterlogging_tolerance": 1,
        "market_stability": "high_value_volatile",
        "n_feeder": "low",
        "suitable_soils": [
            "sandy_loam",
            "alluvial"
        ],
        "regional_suitability": {
            "bihar": "low",
            "arid_west": "high",
            "central": "moderate"
        },
        "data_source": "ICAR-NRCSS Ajmer Seed Spices Manual",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Requires very dry cool climate during flowering",
            "High humidity causes devastating blight (Alternaria burnsii)"
        ],
        "primary_category": "spices",
        "water_need_mm": [
            150,
            220
        ],
        "duration_days": [
            100,
            120
        ],
        "root_depth_cm": [
            30,
            60
        ]
    },
    "coriander": {
        "id": "coriander",
        "name": "Coriander (Dhania)",
        "scientific_name": "Coriandrum sativum",
        "categories": [
            "spice",
            "condiment"
        ],
        "crop_family": "Apiaceae",
        "season": "rabi",
        "duration_range_days": [
            85,
            110
        ],
        "typical_duration": 95,
        "water_need_range_mm": [
            200,
            300
        ],
        "typical_water_mm": 240,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "moderate_taproot",
        "root_depth_range_cm": [
            30,
            60
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 4,
        "waterlogging_tolerance": 1,
        "market_stability": "medium",
        "n_feeder": "low",
        "suitable_soils": [
            "alluvial",
            "clay_loam",
            "black_cotton"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "central": "high",
            "arid_west": "high"
        },
        "data_source": "ICAR-NRCSS Ajmer",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Powdery mildew and stem gall disease under humid mornings"
        ],
        "primary_category": "spices",
        "water_need_mm": [
            200,
            300
        ],
        "duration_days": [
            85,
            110
        ],
        "root_depth_cm": [
            30,
            60
        ]
    },
    "fenugreek": {
        "id": "fenugreek",
        "name": "Fenugreek (Methi)",
        "scientific_name": "Trigonella foenum-graecum",
        "categories": [
            "spice",
            "legume",
            "n_fixing",
            "condiment"
        ],
        "crop_family": "Fabaceae",
        "season": "rabi",
        "duration_range_days": [
            80,
            100
        ],
        "typical_duration": 90,
        "water_need_range_mm": [
            200,
            280
        ],
        "typical_water_mm": 240,
        "nitrogen_fixation_range_kg_ha": [
            15,
            35
        ],
        "nitrogen_fixation_kg_ha": 25,
        "root_type": "moderate_taproot",
        "root_depth_range_cm": [
            30,
            60
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 4,
        "waterlogging_tolerance": 1,
        "market_stability": "medium",
        "n_feeder": "low",
        "suitable_soils": [
            "alluvial",
            "clay_loam",
            "sandy_loam"
        ],
        "regional_suitability": {
            "bihar": "high",
            "indo_gangetic": "high",
            "arid_west": "high",
            "central": "high"
        },
        "data_source": "ICAR-NRCSS Ajmer",
        "source_year": "2020",
        "data_confidence": "high",
        "limitations": [
            "Downy and powdery mildew in poorly aerated dense stands"
        ],
        "primary_category": "spices",
        "water_need_mm": [
            200,
            280
        ],
        "duration_days": [
            80,
            100
        ],
        "root_depth_cm": [
            30,
            60
        ]
    },
    "fennel": {
        "id": "fennel",
        "name": "Fennel (Saunf)",
        "scientific_name": "Foeniculum vulgare",
        "categories": [
            "spice",
            "cash_crop"
        ],
        "crop_family": "Apiaceae",
        "season": "rabi",
        "duration_range_days": [
            140,
            165
        ],
        "typical_duration": 150,
        "water_need_range_mm": [
            300,
            420
        ],
        "typical_water_mm": 350,
        "nitrogen_fixation_range_kg_ha": None,
        "nitrogen_fixation_kg_ha": None,
        "root_type": "deep_taproot",
        "root_depth_range_cm": [
            50,
            90
        ],
        "soil_cover_rating": 3,
        "drought_tolerance": 4,
        "waterlogging_tolerance": 1,
        "market_stability": "high",
        "n_feeder": "medium",
        "suitable_soils": [
            "alluvial",
            "sandy_loam",
            "black_cotton"
        ],
        "regional_suitability": {
            "bihar": "high",
            "arid_west": "high",
            "indo_gangetic": "high"
        },
        "data_source": "ICAR-NRCSS Ajmer Seed Spices Factsheet",
        "source_year": "2021",
        "data_confidence": "high",
        "limitations": [
            "Ramularia blight during cloudy humid weather at flowering",
            "Long duration extends into April"
        ],
        "primary_category": "spices",
        "water_need_mm": [
            300,
            420
        ],
        "duration_days": [
            140,
            165
        ],
        "root_depth_cm": [
            50,
            90
        ]
    }
}


# Keep the original Indian 53-crop set as the trusted baseline used by the
# existing India recommendations. Add the teammate's wider 1,232-crop registry
# for crop discovery, custom rotations and region-specific recommendation paths.
BASE_CROP_IDS = frozenset(CROPS.keys())
_CATEGORY_ALIASES = {
    "cereals_millets": "cereal", "pulses": "pulse", "oilseeds": "oilseed",
    "vegetables": "vegetable", "roots_tubers": "vegetable",
    "industrial_fibre": "commercial", "commercial_cash": "commercial",
    "fruits": "fruit", "spices_aromatics": "spice", "spices": "spice",
}
for _global_id, _global_crop in GLOBAL_CROPS.items():
    if _global_id in CROPS:
        # Preserve the already-reviewed, locally calibrated base crop record.
        continue
    _crop = dict(_global_crop)
    _crop["id"] = _global_id
    _crop.setdefault("name", _global_id.replace("_", " ").title())
    _crop.setdefault("scientific_name", "")
    _crop.setdefault("categories", [])
    _crop["categories"] = list(dict.fromkeys(
        list(_crop.get("categories") or []) +
        [_CATEGORY_ALIASES.get(_crop.get("primary_category", ""), _crop.get("primary_category", "other"))]
    ))
    _crop.setdefault("crop_family", "Unknown")
    _crop.setdefault("season", "annual")
    _crop.setdefault("duration_range_days", _crop.get("duration_days", [90, 120]))
    _crop.setdefault("typical_duration", int(sum(_crop["duration_range_days"]) / 2))
    _crop.setdefault("water_need_range_mm", _crop.get("water_need_mm", [300, 600]))
    _crop.setdefault("typical_water_mm", int(sum(_crop["water_need_range_mm"]) / 2))
    _crop.setdefault("nitrogen_fixation_range_kg_ha", None)
    _crop.setdefault("nitrogen_fixation_kg_ha", None)
    _crop.setdefault("root_type", "unspecified")
    _crop.setdefault("root_depth_range_cm", _crop.get("root_depth_cm", [0, 60]))
    _crop.setdefault("soil_cover_rating", 3)
    _crop.setdefault("drought_tolerance", 3)
    _crop.setdefault("waterlogging_tolerance", 2)
    _crop.setdefault("market_stability", "unknown")
    _crop.setdefault("n_feeder", "unknown")
    _crop.setdefault("suitable_soils", [])
    _crop.setdefault("regional_suitability", {})
    _crop.setdefault("data_source", "Global crop registry; see record metadata")
    _crop.setdefault("source_year", "not specified")
    _crop.setdefault("data_confidence", "medium")
    _crop.setdefault("limitations", ["Global catalogue record; check local suitability and conditions before planting."])
    _crop.setdefault("duration_days", _crop["duration_range_days"])
    _crop.setdefault("water_need_mm", _crop["water_need_range_mm"])
    _crop.setdefault("root_depth_cm", _crop["root_depth_range_cm"])
    CROPS[_global_id] = _crop


# Backward compatibility convenience accessors
for _cid, _c in CROPS.items():
    _c["id"] = _cid
    if "typical_water_mm" not in _c:
        _c["typical_water_mm"] = sum(_c["water_need_range_mm"]) // 2
    if "water_need_mm" not in _c:
        _c["water_need_mm"] = tuple(_c["water_need_range_mm"])
    if "duration_days" not in _c:
        _c["duration_days"] = tuple(_c["duration_range_days"])
    if "root_depth_cm" not in _c:
        _c["root_depth_cm"] = tuple(_c["root_depth_range_cm"])

PRIORITY_WEIGHTS: dict[str, dict[str, float]] = {
    "water_conservation": {
        "water_sustainability": 0.55,
        "soil_health": 0.10,
        "duration_fit": 0.10,
        "economic_stability": 0.05,
        "climate_resilience": 0.20,
    },
    "soil_improvement": {
        "water_sustainability": 0.10,
        "soil_health": 0.65,
        "duration_fit": 0.05,
        "economic_stability": 0.05,
        "climate_resilience": 0.15,
    },
    "income_stability": {
        "water_sustainability": 0.05,
        "soil_health": 0.05,
        "duration_fit": 0.05,
        "economic_stability": 0.75,
        "climate_resilience": 0.10,
    },
    "balanced": {
        "water_sustainability": 0.20,
        "soil_health": 0.25,
        "duration_fit": 0.20,
        "economic_stability": 0.20,
        "climate_resilience": 0.15,
    },
}

# These are explicit, explainable heuristics, not a substitute for a soil test or
# a block-level crop suitability map. Exact crop tolerances are added only where
# the project has source-backed evidence.
ACID_TOLERANT_CROPS = {"rice", "finger_millet", "pigeonpea", "ginger", "turmeric"}
PEARL_MILLET_PH_PREFERRED = (6.0, 8.0)

REGION_FALLBACKS: dict[str, tuple[str, ...]] = {
    "western_ghats": ("western_ghats", "southern_peninsula", "eastern_coastal", "deccan", "central"),
    "southern_peninsula": ("southern_peninsula", "deccan", "eastern_coastal", "central"),
    "deccan": ("deccan", "central", "southern_peninsula", "arid_west"),
    "eastern_coastal": ("eastern_coastal", "southern_peninsula", "bihar", "indo_gangetic"),
    "arid_west": ("arid_west", "central", "deccan", "indo_gangetic"),
    "central": ("central", "deccan", "arid_west", "indo_gangetic"),
    "chota_nagpur": ("chota_nagpur", "eastern_coastal", "bihar", "central"),
    "bihar": ("bihar", "indo_gangetic", "eastern_coastal", "central"),
    "north_east": ("north_east", "eastern_coastal", "western_ghats", "bihar"),
    "hilly_north": ("hilly_north", "indo_gangetic", "central"),
    "indo_gangetic": ("indo_gangetic", "bihar", "central", "eastern_coastal"),
}


DISCLAIMER = (
    "Rotation IQ evaluations are comparative heuristic agronomic models based on regional crop science parameters "
    "and historical climate observations across the Indian subcontinent. They provide comparative trade-off "
    "rankings and do not guarantee specific crop yields, market prices, gross margins, or physical soil improvement. "
    "Economic stability reflects relative price predictability and perishability heuristics based on historical MSP benchmarks "
    "and Agmarknet trends; it is not a live spot-price or profitability forecast, and MSP is not a guaranteed commercial procurement price. "
    "Crop water metrics represent estimated cumulative crop water demand (ETc), not calculated net irrigation requirements. "
    "A crop being present in the database does not mean it is suitable for every region or farm. "
    "Local field testing and Krishi Vigyan Kendra (KVK) / agricultural extension advice must always guide on-farm decisions."
)


def _score_water(crops_list: list[dict], irrigation: str) -> tuple[float, int, list[str]]:
    """Compare cumulative crop-water demand with the stated irrigation access.

    This remains a comparative heuristic using the crop catalogue's typical mm
    values. It is not a field water-balance calculation or net irrigation need.
    """
    total_water = sum(c.get("typical_water_mm", 400) for c in crops_list)
    rabi_zaid_water = 0
    for i, crop in enumerate(crops_list):
        season = crop.get("season", "")
        if season in ("rabi", "zaid", "rabi_or_zaid", "kharif_to_rabi"):
            rabi_zaid_water += crop.get("typical_water_mm", 0)
        elif i >= 1 and season in ("kharif_or_rabi", "kharif_or_zaid", "all_season"):
            rabi_zaid_water += crop.get("typical_water_mm", 0)

    if total_water <= 600:
        base = 92.0
    elif total_water <= 800:
        base = 82.0
    elif total_water <= 1200:
        base = 70.0
    elif total_water <= 1600:
        base = 50.0
    elif total_water <= 1900:
        base = 40.0
    else:
        base = 25.0

    warnings: list[str] = []
    irrigation = str(irrigation or "assured_tubewell").lower()

    if irrigation == "rainfed":
        if total_water > 1200 or rabi_zaid_water > 300:
            base -= 35.0
            warnings.append(
                f"High cumulative crop-water demand ({total_water} mm total, {rabi_zaid_water} mm off-monsoon) "
                "under rainfed conditions creates a substantial moisture-deficit risk."
            )
        elif total_water <= 700 and rabi_zaid_water <= 250:
            base += 8.0
        low_drought_tolerance = [c.get("name", c.get("id", "Crop")) for c in crops_list if c.get("drought_tolerance", 3) <= 2]
        if low_drought_tolerance:
            base -= 15.0
            warnings.append("Low drought-tolerance crop(s) included: " + ", ".join(low_drought_tolerance) + ".")
    elif irrigation == "partial":
        if rabi_zaid_water > 450:
            base -= 18.0
            warnings.append(f"Off-monsoon demand ({rabi_zaid_water} mm) may exceed partial irrigation capacity.")
        elif total_water >= 1800:
            base -= 15.0
            warnings.append(f"High cumulative demand ({total_water} mm) may exceed partial irrigation capacity.")
        else:
            base += 3.0
    elif irrigation == "assured_canal":
        # Canal access improves feasibility for water-demanding sequences, but
        # does not erase their basin-level water footprint.
        if total_water >= 1600:
            base += 8.0
        elif total_water >= 1000:
            base += 6.0
        else:
            base += 4.0
        if total_water >= 1800:
            warnings.append(
                f"High cumulative crop-water demand ({total_water} mm) still carries basin-level water-use risk, "
                "even where canal supply is available."
            )
    else:  # assured_tubewell
        if total_water >= 1800:
            base -= 8.0
            warnings.append(
                f"High annual crop-water demand ({total_water} mm) can increase groundwater drawdown pressure; "
                "use soil-moisture scheduling and micro-irrigation where appropriate."
            )
        elif total_water <= 800:
            base += 6.0
        elif total_water >= 1200:
            base += 1.0
        else:
            base += 2.0

    return max(10.0, min(100.0, base)), total_water, warnings


def _score_soil_health(
    crops_list: list[dict],
    soil_type: str,
    soil_ph: float | None = None,
    organic_carbon_pct: float | None = None,
) -> tuple[float, list[str]]:
    """Score soil-building value and compatibility using catalogue traits.

    Biological N fixation, family/root diversity and cover are comparative
    indicators. pH/organic-carbon adjustments are intentionally conservative
    and must not be read as a soil-fertility diagnosis.
    """
    score = 35.0
    warnings: list[str] = []
    total_n_fixed = sum(c.get("nitrogen_fixation_kg_ha") or 0 for c in crops_list)

    if total_n_fixed > 0:
        score += min(20.0, total_n_fixed * 0.45)

    families = {c.get("crop_family") for c in crops_list if c.get("crop_family")}
    if len(families) > 1:
        score += 8.0
        if "Fabaceae" in families and "Poaceae" in families:
            score += 5.0
        if "Brassicaceae" in families:
            score += 3.0
    elif len(crops_list) > 1 and len(families) == 1 and "Poaceae" in families:
        score -= 6.0
        warnings.append("Continuous cereal (Poaceae) cropping can build pest pressure and repeatedly draw nutrients from similar soil layers.")

    root_types = {c.get("root_type") for c in crops_list if c.get("root_type")}
    has_rice = any(c.get("id") == "rice" for c in crops_list)
    if len(root_types) > 1:
        score += 6.0
        deep_taproot = any(
            c.get("root_depth_range_cm", [0, 0])[1] >= 80
            for c in crops_list if "taproot" in c.get("root_type", "")
        )
        moderate_taproot = any("taproot" in c.get("root_type", "") for c in crops_list) and not deep_taproot
        if deep_taproot:
            score += 6.0
        elif moderate_taproot:
            if has_rice and soil_type in ("alluvial", "clay_loam", "silt_loam"):
                score -= 5.0
                warnings.append("A puddled-rice plow pan may restrict pulse taproots unless suitable relay or reduced-tillage practices are used.")
            else:
                score += 4.0

    avg_cover = sum(c.get("soil_cover_rating", 3) for c in crops_list) / max(1, len(crops_list))
    if avg_cover >= 4.0:
        score += 4.0

    if total_n_fixed == 0 and all(c.get("n_feeder") == "high" for c in crops_list):
        score -= 8.0
        warnings.append("Successive high nitrogen-demanding crops can increase nutrient and soil-organic-matter depletion risk.")

    for crop in crops_list:
        soils = crop.get("suitable_soils", [])
        if soils and soil_type not in soils and "all" not in soils:
            score -= 8.0
            crop_label = crop.get("name", crop.get("id", "Crop"))
            warnings.append(f"{crop_label} is not listed among the catalogue's preferred soils for {soil_type} texture.")

    # Soil pH: source-backed crop-specific handling for pearl millet and the
    # acid-tolerant crops documented by Indian agricultural extension sources.
    crop_ids = {c.get("id") for c in crops_list}
    if soil_ph is not None:
        try:
            ph_value = float(soil_ph)
        except (TypeError, ValueError):
            ph_value = None
        if ph_value is not None and ph_value < 5.5:
            acid_tolerant_share = sum(1 for cid in crop_ids if cid in ACID_TOLERANT_CROPS) / max(1, len(crop_ids))
            score += min(5.0, 5.0 * acid_tolerant_share)
            if "pearl_millet" in crop_ids:
                penalty = 15.0 if ph_value < 5.0 else 8.0
                score -= penalty
                warnings.append(
                    f"Soil pH {ph_value:.1f} is acidic for pearl millet; the crop's preferred pH range is approximately "
                    f"{PEARL_MILLET_PH_PREFERRED[0]:.1f}-{PEARL_MILLET_PH_PREFERRED[1]:.1f}. Consider a soil-test-based amendment plan."
                )
            elif acid_tolerant_share > 0:
                warnings.append(
                    f"Soil pH {ph_value:.1f} is acidic. This sequence includes crop(s) documented as relatively acid-tolerant, "
                    "but lime requirement and nutrient management should follow a local soil test."
                )
            else:
                warnings.append(
                    f"Soil pH {ph_value:.1f} is strongly acidic; crop-specific pH response is not encoded for every crop in this database."
                )
        elif ph_value is not None and ph_value > 8.5:
            if "pearl_millet" in crop_ids:
                score -= 8.0
                warnings.append("Very alkaline soil may reduce pearl-millet suitability; confirm with a local soil test and variety guidance.")
            else:
                warnings.append("Strongly alkaline soil detected; crop-specific alkaline-soil tolerance is not fully represented in this database.")

    # Low organic carbon increases the value of sequences that maintain more
    # surface cover. soil_cover_rating is an ordinal catalogue rating, not a
    # measured residue yield or a prediction of future soil-carbon gain.
    if organic_carbon_pct is not None:
        try:
            oc_value = float(organic_carbon_pct)
        except (TypeError, ValueError):
            oc_value = None
        if oc_value is not None and oc_value < 0.75:
            need_factor = max(0.0, min(1.0, (0.75 - oc_value) / 0.75))
            cover_bonus = max(0.0, avg_cover - 3.0) * 7.0 * need_factor
            legume_bonus = min(2.0, total_n_fixed / 30.0) * need_factor
            score += cover_bonus + legume_bonus
            warnings.append(
                f"Organic carbon is reported as {oc_value:.2f}%. The score gives additional comparative credit to crop cover and legume traits; "
                "it does not predict a future soil-carbon increase."
            )
        elif oc_value is not None and oc_value >= 0.75:
            warnings.append(
                f"Organic carbon is reported as {oc_value:.2f}%; no low-carbon bonus was applied. Maintain residue and organic-matter inputs where practical."
            )

    return max(10.0, min(100.0, score)), warnings


def _score_duration(crops_list: list[dict]) -> tuple[float, int, list[str]]:
    """Evaluates crop turnaround fit within the annual 365-day agricultural cycle."""
    warnings = []
    is_perennial = any(c.get("season") == "perennial" or "perennial" in c.get("categories", []) for c in crops_list)
    is_sugarcane = any(c.get("id") == "sugarcane" for c in crops_list)

    if is_perennial and len(crops_list) == 1:
        return 85.0, 0, ["Multi-year perennial system: duration scoring reflects orchard establishment rather than annual turnaround."]

    if is_sugarcane:
        if len(crops_list) == 1:
            return 88.0, 35, ["Full-season annual/ratoon cash crop (10-12 months); occupies field continuously throughout the agricultural year."]
        else:
            warnings.append(
                "Sugarcane requires 300-365 days; overlapping with other field crops within a single year "
                "causes severe calendar collision unless intercropped as autumn companion."
            )
            return 35.0, -100, warnings

    total_days = sum(c.get("typical_duration", 100) for c in crops_list)
    turnaround_days = 365 - total_days

    if total_days <= 240:
        return 92.0, turnaround_days, []
    elif total_days <= 290:
        return 84.0, turnaround_days, []
    elif total_days <= 335:
        return 75.0, turnaround_days, []
    elif total_days <= 365:
        warnings.append(
            f"Compressed turnaround window ({turnaround_days} days buffer between harvest and sowing). "
            "Requires rapid mechanization to avoid delayed sowing."
        )
        return 62.0, turnaround_days, warnings
    else:
        warnings.append(
            f"Cumulative duration ({total_days} days) exceeds annual 365-day calendar by {total_days - 365} days. "
            "Crops cannot complete their lifecycle within one year without overlapping."
        )
        return 25.0, turnaround_days, warnings


def _score_economic(crops_list: list[dict], priority: str) -> tuple[float, list[str]]:
    """Evaluates income predictability, market infrastructure, price stability, and perishability.
    
    IMPORTANT NOTE:
    Economic stability scores reflect relative price predictability and perishability heuristics based
    on historical MSP benchmarks and Agmarknet trends. They do NOT provide live price forecasts,
    profitability predictions, or guaranteed government procurement.
    """
    stability_map = {"high": 85.0, "medium": 72.0, "high_value_volatile": 60.0}
    scores = [stability_map.get(c.get("market_stability", "medium"), 70.0) for c in crops_list]
    avg_score = sum(scores) / max(1, len(scores))
    warnings = []

    has_volatile = any(c.get("market_stability") == "high_value_volatile" for c in crops_list)
    has_cereal = any("cereal" in c.get("categories", []) or c.get("id") in ("rice", "wheat", "maize") for c in crops_list)

    if has_volatile:
        if priority == "income_stability":
            avg_score -= 12.0
            warnings.append(
                "Includes perishable/volatile cash crops (vegetables/fruits) subject to price crashes; "
                "high capital and market risk for risk-averse farmers."
            )
        else:
            avg_score += 5.0

    if all(c.get("market_stability") == "high" for c in crops_list):
        avg_score = max(avg_score, 86.0)

    if has_cereal:
        warnings.append(
            "Cereal price stability references Government Minimum Support Price (MSP) benchmarks; "
            "note that open-market realization in non-APMC markets often falls below MSP without guaranteed public procurement."
        )

    return max(10.0, min(100.0, avg_score)), warnings


def _extract_rainfall_context(climate_summary: dict[str, Any] | None) -> tuple[float | None, float | None]:
    """Return (annual mean rainfall, mean Kharif-period rainfall) when available."""
    if not isinstance(climate_summary, dict) or not climate_summary.get("available", True):
        return None, None

    baseline = climate_summary.get("baseline") or {}
    annual = baseline.get("rainfall_mean_mm")
    try:
        annual = float(annual) if annual is not None else None
    except (TypeError, ValueError):
        annual = None

    kharif = None
    for row in climate_summary.get("seasonal_period_means") or []:
        if str(row.get("season", "")).lower() == "kharif":
            value = row.get("mean_rainfall_mm", row.get("rainfall_mm"))
            try:
                kharif = float(value) if value is not None else None
            except (TypeError, ValueError):
                kharif = None
            break

    if kharif is None:
        kharif_months = []
        for row in climate_summary.get("monthly_climatology") or []:
            try:
                month = int(row.get("month"))
                value = row.get("rainfall_mm")
                if month in (6, 7, 8, 9) and value is not None:
                    kharif_months.append(float(value))
            except (TypeError, ValueError):
                continue
        if len(kharif_months) >= 3:
            kharif = sum(kharif_months)

    return annual, kharif


def _score_climate_resilience(
    crops_list: list[dict],
    climate_summary: dict[str, Any] | None = None,
    region_key: str | None = None,
) -> tuple[float, list[str]]:
    """Compare drought and waterlogging tolerance with observed climate context."""
    warnings: list[str] = []
    drought_ratings = [c.get("drought_tolerance", 3) for c in crops_list]
    avg_drought = sum(drought_ratings) / max(1, len(drought_ratings))
    score = 30.0 + (avg_drought - 1.0) * 16.25

    annual_rain, kharif_rain = _extract_rainfall_context(climate_summary)
    wet_signal = (kharif_rain is not None and kharif_rain >= 1200) or (annual_rain is not None and annual_rain >= 2400)
    dry_signal = annual_rain is not None and annual_rain < 700
    avg_waterlogging = sum(c.get("waterlogging_tolerance", 3) for c in crops_list) / max(1, len(crops_list))

    if wet_signal:
        if avg_waterlogging <= 1.5:
            score -= 14.0
            warnings.append(
                "High observed rainfall combined with low crop waterlogging tolerance raises drainage/root-zone risk for this sequence."
            )
        elif avg_waterlogging <= 2.5:
            score -= 7.0
            warnings.append("Observed wet-season rainfall may require raised beds, drainage, or a better-drained plot for this sequence.")
        elif avg_waterlogging >= 4.0:
            score += 4.0
            warnings.append("The sequence includes crops with relatively high waterlogging tolerance for the observed wet climate.")
    elif dry_signal:
        if avg_drought < 2.5:
            score -= 10.0
            warnings.append("Low observed annual rainfall and low average drought tolerance make this sequence climate-sensitive.")
        elif avg_drought >= 4.0:
            score += 4.0
            warnings.append("The sequence's drought-tolerance traits are a relative advantage under the observed low-rainfall baseline.")
    elif annual_rain is not None or kharif_rain is not None:
        warnings.append("Observed rainfall totals were considered alongside crop drought and waterlogging traits.")

    # A broad regional prior is used only when site-level rainfall is unavailable.
    if not wet_signal and annual_rain is None and kharif_rain is None and region_key == "western_ghats":
        if avg_waterlogging <= 1.5:
            score -= 5.0
            warnings.append("Regional humid-west-coast caution applied because site-specific rainfall normals were unavailable; this is not a measured site result.")

    has_wheat = any(c.get("id") == "wheat" for c in crops_list)
    if has_wheat:
        march_max_temp = None
        if climate_summary and isinstance(climate_summary, dict):
            if "march_t2m_max" in climate_summary and climate_summary["march_t2m_max"] is not None:
                try:
                    march_max_temp = float(climate_summary["march_t2m_max"])
                except (TypeError, ValueError):
                    march_max_temp = None
            if march_max_temp is None:
                for m_row in climate_summary.get("monthly_climatology") or []:
                    if m_row.get("month") == 3 and m_row.get("t2m_mean_c") is not None:
                        march_max_temp = float(m_row["t2m_mean_c"]) + 7.5
                        break
        if march_max_temp is not None:
            if march_max_temp > 32.0:
                score -= 6.0
                warnings.append(
                    f"Potential terminal heat-risk warning: March maximum temperature averages about {march_max_temp:.1f}°C (>32°C). "
                    "This is environmental risk, not confirmed crop damage."
                )
            else:
                warnings.append(f"March temperature profile (~{march_max_temp:.1f}°C) is within safe physiological limits for wheat grain filling.")
        else:
            warnings.append("Wheat terminal heat sensitivity note: wheat can face terminal heat stress during grain filling; no site-specific March temperature profile was supplied.")

    return max(10.0, min(100.0, score)), warnings


def detect_indian_agroclimatic_zone(lat: float | None, lon: float | None) -> tuple[str, str]:
    """Approximate broad agro-climatic zone from coordinates (not a cadastral map)."""
    if lat is None or lon is None:
        return "pan_india", "Pan-Indian (coordinates not supplied)"
    try:
        lat = float(lat)
        lon = float(lon)
    except (TypeError, ValueError):
        return "pan_india", "Pan-Indian (invalid coordinates)"
    if not (6.0 <= lat <= 38.0 and 68.0 <= lon <= 98.0):
        return "pan_india", "Outside supported India coordinate envelope"

    # A smaller west-coast belt is separated because its humid monsoon context
    # differs materially from the interior southern dryland plateau.
    if 8.0 <= lat < 13.0 and 74.5 <= lon < 77.5:
        return "western_ghats", "Kerala / Humid South-West Coast (approximate zone)"
    if lat < 14.5:
        return "southern_peninsula", "Southern Peninsular Zone (Tamil Nadu / South Karnataka)"
    if 14.5 <= lat < 21.0 and lon < 79.5:
        return "deccan", "Deccan Plateau (Maharashtra / Karnataka / Telangana)"
    if 14.5 <= lat < 21.0 and lon >= 79.5:
        return "eastern_coastal", "Eastern Coastal Plains (Andhra Pradesh / Odisha)"
    # Include the eastern Rajasthan belt (e.g. Jaipur) before the broad
    # Indo-Gangetic fallback; the previous longitude cut-off misclassified it.
    if 21.0 <= lat < 30.0 and 68.0 <= lon < 77.0:
        return "arid_west", "Western Arid & Semi-Arid Zone (Gujarat / Rajasthan; approximate)"
    if 21.0 <= lat < 26.0 and 74.5 <= lon < 82.0:
        return "central", "Central India Plateau & Hills (Madhya Pradesh / Chhattisgarh)"
    if 21.0 <= lat < 25.0 and 82.0 <= lon < 88.0:
        return "chota_nagpur", "Chota Nagpur & Eastern Plateau (Jharkhand)"
    if 24.5 <= lat <= 27.6 and 83.0 <= lon <= 88.5:
        return "bihar", "Middle Gangetic Plains (Bihar)"
    if lat >= 24.0 and lon >= 88.5:
        return "north_east", "Eastern Himalayan & North-Eastern Region (Assam / NE Hills)"
    if lat >= 31.0:
        return "hilly_north", "Western Himalayan / Hilly North (J&K / Himachal Pradesh / Uttarakhand)"
    if 26.0 <= lat < 31.0 and lon < 83.0:
        return "indo_gangetic", "Trans & Upper Gangetic Plains (Punjab / Haryana / Uttar Pradesh)"
    return "indo_gangetic", "Indo-Gangetic & Sub-Humid Plains (approximate)"


def detect_global_climate_zone(lat: float | None, lon: float | None) -> tuple[str, str, str, str]:
    """Resolves worldwide coordinates to global agro-climatic zone, region name, hemisphere, and climate type.
    Returns: (zone_key, zone_name, hemisphere, eco_zone)
    """
    if lat is None or lon is None:
        return "bihar", "Middle Gangetic Plains (Bihar Hub)", "northern", "subtropical"

    hemisphere = "southern" if lat < 0 else "northern"

    # Check if coordinate is in Indian Subcontinent
    if 6.0 <= lat <= 38.0 and 68.0 <= lon <= 97.5:
        icar_key, icar_name = detect_indian_agroclimatic_zone(lat, lon)
        return icar_key, icar_name, "northern", "subtropical"

    # Global Agro-Climatic Zones
    # North America Corn Belt & Upper Midwest
    if 36.0 <= lat <= 49.0 and -104.0 <= lon <= -80.0:
        return "us_corn_belt", "North American Corn Belt & Upper Midwest (USA)", "northern", "temperate_continental"

    # North America Great Plains / Wheat Belt
    if 32.0 <= lat <= 52.0 and -115.0 <= lon < -100.0:
        return "us_great_plains", "North American Great Plains & Wheat Belt (USA/Canada)", "northern", "arid_semiarid"

    # North America Pacific / California Central Valley
    if 32.0 <= lat <= 46.0 and -125.0 <= lon < -115.0:
        return "us_mediterranean", "Pacific Southwest / California Central Valley", "northern", "mediterranean"

    # South America Cerrado (Mato Grosso, Goias)
    if -18.0 <= lat <= -8.0 and -60.0 <= lon <= -45.0:
        return "latin_america_cerrado", "Brazilian Cerrado Agricultural Frontier (Brazil)", "southern", "tropical_savanna"

    # South America Pampas (Argentina, Uruguay, Rio Grande do Sul)
    if -39.0 <= lat < -25.0 and -65.0 <= lon <= -50.0:
        return "latin_america_pampas", "Pampas Agricultural Plains (Argentina / Uruguay)", "southern", "temperate_subtropical"

    # Mediterranean Basin (Spain, Italy, Greece, Turkey, North Africa)
    if 30.0 <= lat <= 45.0 and -10.0 <= lon <= 36.0:
        return "mediterranean_basin", "Mediterranean Basin (Southern Europe / North Africa)", "northern", "mediterranean"

    # Western & Central European Agricultural Plain (France, Germany, UK, Poland)
    if 45.0 <= lat <= 58.0 and -10.0 <= lon <= 25.0:
        return "europe_temperate", "Western & Central European Plains (France / Germany / UK)", "northern", "temperate_maritime"

    # Eurasian Steppe & Black Earth Basin (Ukraine, Southern Russia, Kazakhstan)
    if 44.0 <= lat <= 55.0 and 25.0 <= lon <= 70.0:
        return "eurasian_steppe", "Black Earth Steppe Belt (Ukraine / Southern Russia)", "northern", "continental_temperate"

    # Sub-Saharan Africa & Savanna-Sahel (Nigeria, Kenya, Ethiopia, Ghana)
    if -15.0 <= lat <= 18.0 and -18.0 <= lon <= 50.0:
        return "sub_saharan_africa", "Sub-Saharan Africa & East African Plateau (Kenya / Nigeria)", "tropical", "tropical_savanna"

    # East Asian Agricultural Basin (China North Plain, Yangtze, Japan, Korea)
    if 22.0 <= lat <= 45.0 and 100.0 <= lon <= 145.0:
        return "east_asia", "East Asian Agricultural Basin (China / Korea / Japan)", "northern", "subtropical_temperate"

    # Australian Murray-Darling & Southwest Grain Belt
    if -42.0 <= lat <= -20.0 and 112.0 <= lon <= 154.0:
        return "australia_grain_belt", "Australian Grain Belt (Murray-Darling / Western Australia)", "southern", "mediterranean_arid"

    # General Latitudinal fallbacks
    abs_lat = abs(lat)
    if abs_lat <= 23.5:
        return "global_tropical", f"Global Tropical Lowlands ({hemisphere.capitalize()} Hemisphere)", hemisphere, "tropical"
    elif 23.5 < abs_lat <= 38.0:
        return "global_subtropical", f"Global Subtropical Belt ({hemisphere.capitalize()} Hemisphere)", hemisphere, "subtropical"
    elif 38.0 < abs_lat <= 55.0:
        return "global_temperate", f"Global Temperate Zone ({hemisphere.capitalize()} Hemisphere)", hemisphere, "temperate"
    else:
        return "global_boreal", f"High Latitude Boreal Zone ({hemisphere.capitalize()} Hemisphere)", hemisphere, "boreal"


def _global_candidate_rotations(reg_key: str) -> list[dict[str, Any]]:
    # Curated region-specific crop pathways imported from teammate source.
    candidate_rotations: list[dict[str, Any]] = []
    if reg_key == "us_corn_belt":
        candidate_rotations = [
            {
                "id": "corn_soybean",
                "name": "Dent Corn → Soybean (Corn Belt Standard)",
                "crop_ids": ["dent_corn", "soybean"],
                "description": "The benchmark agricultural rotation of the US Midwest, balancing high-yielding carbohydrate feed grain with legume nitrogen fixation.",
                "benefits": ["Proven agronomic stability across the US Corn Belt.", "Soybean nodulation fixes nitrogen reducing synthetic fertilizer needs for following corn.", "Breaks corn rootworm (Diabrotica) and foliar disease cycles."],
                "disadvantages": ["Two-crop annual cycle lacks winter ground cover without cover crops.", "Susceptible to soil erosion during spring thaw."],
                "assumptions": ["Assumes assured rainfall or center-pivot irrigation."],
            },
            {
                "id": "corn_soybean_winter_wheat",
                "name": "Dent Corn → Soybean → Winter Wheat",
                "crop_ids": ["dent_corn", "soybean", "hard_red_winter_wheat"],
                "description": "Diverse 3-crop extended sequence adding a winter cereal to reduce pest pressure and protect soil over winter.",
                "benefits": ["Winter wheat roots scavenge residual soil nitrogen.", "High soil cover throughout winter and spring.", "Spreads labor and cash flow across summer and autumn harvests."],
                "disadvantages": ["Requires tight harvest window for soybean to drill winter wheat."],
                "assumptions": ["Assumes moderate winter hardiness zone."],
            },
            {
                "id": "corn_alfalfa_dairy",
                "name": "Dent Corn → Alfalfa Hay (Dairy Forage)",
                "crop_ids": ["dent_corn", "alfalfa_hay"],
                "description": "High-value dairy and livestock forage rotation combining silage corn with perennial deep-rooting lucerne.",
                "benefits": ["Alfalfa taproots penetrate 2-3 meters deep breaking subsoil compaction.", "Fixes 150-250 kg N/ha, providing a massive nitrogen credit to following corn.", "Exceptional feed protein value for livestock."],
                "disadvantages": ["High total water consumption over perennial growth."],
                "assumptions": ["Requires dairy or livestock market infrastructure."],
            },
            {
                "id": "oats_red_clover_corn",
                "name": "Common Oat → Red Clover → Dent Corn",
                "crop_ids": ["oats_common", "red_clover", "dent_corn"],
                "description": "Regenerative soil-building system undersowing red clover into oats, terminated before high-yielding maize.",
                "benefits": ["Substantially reduces synthetic fertilizer requirements.", "Red clover provides dense winter ground cover preventing erosion.", "Oats provide high-fiber cool-season grain and straw bedding."],
                "disadvantages": ["Requires timely mechanical termination of clover."],
                "assumptions": ["Assumes mixed crop-livestock or organic farming goals."],
            },
            {
                "id": "soybean_cereal_rye",
                "name": "Soybean → Winter Rye Cover → Field Corn",
                "crop_ids": ["soybean", "rye_winter", "dent_corn"],
                "description": "No-till cover-crop rotation using winter cereal rye between soybean and corn for weed suppression.",
                "benefits": ["Winter rye allelopathy suppresses winter annual and spring weeds.", "Drastically reduces nutrient runoff into waterways.", "Builds active organic carbon in topsoil."],
                "disadvantages": ["Rye must be terminated at right height before corn planting."],
                "assumptions": ["Assumes no-till drill and roller-crimper or burndown."],
            },
        ]
    elif reg_key in ("latin_america_cerrado", "latin_america_pampas"):
        candidate_rotations = [
            {
                "id": "soybean_corn_safrinha",
                "name": "Soybean → Safrinha Corn (Cerrado Double-Crop)",
                "crop_ids": ["soybean", "dent_corn"],
                "description": "The quintessential Brazilian Cerrado double-crop system capitalizing on early-maturing soybeans followed immediately by dry-season maize.",
                "benefits": ["Maximizes annual land productivity with two commercial grain harvests per calendar year.", "Soybean fixes nitrogen for the following safrinha maize."],
                "disadvantages": ["Safrinha corn yields depend heavily on late rains before dry season."],
                "assumptions": ["Assumes tropical savanna climate with distinct rainy/dry seasons."],
            },
            {
                "id": "soybean_cotton",
                "name": "Soybean → Upland Cotton",
                "crop_ids": ["soybean", "cotton"],
                "description": "High-value cash rotation alternating legume grain with high-return commercial fibre.",
                "benefits": ["High gross revenue per hectare.", "Deep taproot of cotton utilizes subsoil moisture."],
                "disadvantages": ["High pesticide and intensive management requirement for cotton."],
                "assumptions": ["Assumes access to mechanized cotton harvesters."],
            },
            {
                "id": "soybean_black_oats",
                "name": "Soybean → Black Oat Cover",
                "crop_ids": ["soybean", "black_oats"],
                "description": "Conservation agriculture rotation using black oats as a winter cover and nematode-suppressing mulch.",
                "benefits": ["Black oats suppress root-knot nematodes in tropical soils.", "Produces thick straw blanket that conserves soil moisture."],
                "disadvantages": ["Oat residue requires specialized no-till seeders for following crop."],
                "assumptions": ["Zero-tillage management."],
            },
            {
                "id": "sunflower_soybean",
                "name": "High-Oleic Sunflower → Soybean",
                "crop_ids": ["sunflower_high_oleic", "soybean"],
                "description": "Oilseed-legume sequence leveraging deep sunflower taproots to mine subsoil potassium.",
                "benefits": ["Diversifies farm income across global vegetable oil markets.", "Breaks cereal monoculture pest complexes."],
                "disadvantages": ["Shared susceptibility to Sclerotinia requires careful scouting."],
                "assumptions": ["Good local oilseed crushing facilities."],
            },
        ]
    elif reg_key in ("mediterranean_basin", "us_mediterranean"):
        candidate_rotations = [
            {
                "id": "durum_wheat_chickpea",
                "name": "Durum Wheat → Kabuli Chickpea",
                "crop_ids": ["durum_wheat", "kabuli_chickpea"],
                "description": "The historic Mediterranean dryland rotation pairing premium pasta wheat with drought-hardy garbanzo legumes.",
                "benefits": ["Chickpea fixes 40-80 kg N/ha, boosting grain protein of succeeding durum wheat.", "Low annual water demand suited to dry Mediterranean summers.", "High commercial liquidity across Mediterranean food markets."],
                "disadvantages": ["Ascochyta blight risk in wet springs."],
                "assumptions": ["Assumes winter rainfall Mediterranean climate."],
            },
            {
                "id": "winter_barley_sunflower",
                "name": "Two-Row Malting Barley → High-Oleic Sunflower",
                "crop_ids": ["two_row_barley", "sunflower_high_oleic"],
                "description": "Water-efficient rotation combining cool-season malting barley with deep-rooted summer sunflower.",
                "benefits": ["Barley finishes before summer heat; sunflower extracts deep moisture reserves.", "Excellent weed competition from dense barley tillering."],
                "disadvantages": ["Sunflower needs sufficient soil moisture stored from winter rains."],
                "assumptions": ["Assumes winter moisture retention in soil profile."],
            },
            {
                "id": "faba_bean_durum",
                "name": "Broad Bean (Faba) → Durum Wheat",
                "crop_ids": ["faba_bean_broad", "durum_wheat"],
                "description": "High-nitrogen-building Mediterranean sequence using faba beans as a bio-fertilizer preceding premium durum.",
                "benefits": ["Faba beans fix up to 120-160 kg N/ha.", "Significantly boosts durum wheat vitreous kernel percentage."],
                "disadvantages": ["Faba beans require cool early vegetative conditions."],
                "assumptions": ["Assumes moderate winter rainfall."],
            },
            {
                "id": "tomato_winter_wheat",
                "name": "Processing Tomato → Hard Red Winter Wheat",
                "crop_ids": ["tomato_roma", "hard_red_winter_wheat"],
                "description": "Intensive horticultural-cereal rotation alternating high-return processing tomatoes with soil-resting winter wheat.",
                "benefits": ["High revenue from industrial processing tomato contract.", "Winter wheat scavenges leftover irrigation and fertilizer."],
                "disadvantages": ["Intensive field operations during tomato harvest."],
                "assumptions": ["Requires drip irrigation infrastructure."],
            },
        ]
    elif reg_key in ("europe_temperate", "eurasian_steppe"):
        candidate_rotations = [
            {
                "id": "winter_wheat_oilseed_rape",
                "name": "Winter Wheat → Winter Canola (Oilseed Rape)",
                "crop_ids": ["soft_red_winter_wheat", "canola_winter"],
                "description": "The dominant European crop rotation pairing high-yielding winter bread wheat with high-oil winter rapeseed.",
                "benefits": ["Rapeseed taproot breaks plow pan and aerates soil for wheat.", "Rapeseed biofumigant root exudates suppress wheat take-all fungus.", "Highest combined gross margin in temperate Western Europe."],
                "disadvantages": ["Heavy synthetic nitrogen demand requires careful split applications."],
                "assumptions": ["Temperate climate with reliable winter precipitation."],
            },
            {
                "id": "winter_wheat_sugar_beet",
                "name": "Winter Wheat → Sugar Beet",
                "crop_ids": ["soft_red_winter_wheat", "sugar_beet_commercial"],
                "description": "High-yield commercial cash rotation dominant in the European loess plains.",
                "benefits": ["Exceptional cash revenue per hectare from sugar processing quota.", "Sugar beet leaves loose, highly friable soil structure."],
                "disadvantages": ["Heavy harvesting machinery risks soil compaction in wet autumns."],
                "assumptions": ["Proximity to sugar processing factory."],
            },
            {
                "id": "spring_barley_field_pea",
                "name": "Two-Row Malting Barley → Yellow Field Pea",
                "crop_ids": ["two_row_barley", "yellow_field_pea"],
                "description": "Low-input, balanced rotation producing premium malting barley and plant protein peas.",
                "benefits": ["Field pea fixes 50-80 kg N/ha, keeping subsequent barley protein in optimal malting range.", "Low water requirement and short growing seasons."],
                "disadvantages": ["Field pea lodging can complicate wet harvests."],
                "assumptions": ["Standard grain combining equipment."],
            },
            {
                "id": "winter_rye_potato",
                "name": "Winter Rye → Russet Potato",
                "crop_ids": ["rye_winter", "potato"],
                "description": "Cold-hardy sandy soil rotation utilizing rye's allelopathy and biomass ahead of potato tuber production.",
                "benefits": ["Rye suppresses soil-borne potato pathogens and weeds.", "Excellent adaptation to light, sandy, slightly acidic soils."],
                "disadvantages": ["Potato harvest disturbs soil structure."],
                "assumptions": ["Cold temperate or continental climate."],
            },
        ]
    elif reg_key == "sub_saharan_africa":
        candidate_rotations = [
            {
                "id": "sorghum_cowpea",
                "name": "Red Grain Sorghum → Cowpea",
                "crop_ids": ["sorghum_grain_red", "cowpea"],
                "description": "The cornerstone resilient rotation of African drylands and savannas.",
                "benefits": ["High drought tolerance and heat resilience.", "Cowpea provides household nutrition and fixes soil nitrogen.", "Sorghum provides food grain and drought-proof livestock stover."],
                "disadvantages": ["Susceptible to Striga weed if soil fertility is severely depleted."],
                "assumptions": ["Semi-arid or savanna tropical ecology."],
            },
            {
                "id": "maize_pigeonpea",
                "name": "Flint Corn → Perennial Pigeonpea",
                "crop_ids": ["flint_corn", "pigeonpea"],
                "description": "Multi-story cropping system combining staple maize with deep-rooting pigeonpea.",
                "benefits": ["Pigeonpea leaf drop provides massive organic mulch.", "Mines phosphorus from subsoil horizons.", "Provides pulse grain and firewood."],
                "disadvantages": ["Pigeonpea occupies land longer than short-season crops."],
                "assumptions": ["Sub-humid to semi-arid tropical plateau."],
            },
            {
                "id": "cassava_groundnut",
                "name": "Sweet Cassava → Groundnut",
                "crop_ids": ["cassava_sweet", "groundnut"],
                "description": "Calorie and protein security system combining drought-proof cassava with high-oil groundnut.",
                "benefits": ["Cassava provides flexible harvest window up to 2 years.", "Groundnut fixes nitrogen and prevents soil erosion."],
                "disadvantages": ["Cassava removes high potassium amounts if tubers are exported."],
                "assumptions": ["Warm tropical climate."],
            },
            {
                "id": "teff_chickpea",
                "name": "Brown Teff → Desi Chickpea",
                "crop_ids": ["teff_brown", "desi_chickpea"],
                "description": "East African highland Vertisol rotation alternating staple teff grain with nitrogen-fixing chickpea.",
                "benefits": ["Both crops adapt to heavy cracking black clay soils.", "Teff commands high commercial market price in urban centers."],
                "disadvantages": ["Teff requires precise, fine seedbed preparation."],
                "assumptions": ["Tropical highland climate."],
            },
        ]
    else:
        # General Worldwide fallback
        candidate_rotations = [
            {
                "id": "global_cereal_legume",
                "name": "Small Grain Cereal → Grain Legume Pulse",
                "crop_ids": ["wheat", "chickpea"],
                "description": "Universal balanced cereal-legume sustainable rotation.",
                "benefits": ["Restores soil nitrogen and interrupts pest cycles.", "Balanced food and cash flow."],
                "disadvantages": ["Requires monitoring of soil moisture during transition."],
                "assumptions": ["Adaptable to general temperate and subtropical zones."],
            },
            {
                "id": "global_cereal_oilseed",
                "name": "Small Grain Cereal → Brassica Oilseed",
                "crop_ids": ["barley", "mustard"],
                "description": "Diverse taproot-fibrous sequence breaking monoculture cycles.",
                "benefits": ["Biofumigation from brassica glucosinolates.", "Deep subsoil moisture scavenging."],
                "disadvantages": ["Avoid back-to-back brassicas."],
                "assumptions": ["Standard agricultural practices."],
            },
            {
                "id": "global_water_saver",
                "name": "Drought-Resilient Millet → Pulse",
                "crop_ids": ["pearl_millet", "cowpea"],
                "description": "Climate-smart low-water pathway for semi-arid environments.",
                "benefits": ["Lowest water footprint and high heat tolerance.", "Protects farm income during dry years."],
                "disadvantages": ["Lower maximum yield ceiling than high-input cereals."],
                "assumptions": ["Rainfed or limited water environments."],
            },
        ]
    return candidate_rotations


def _score_regional_fit(crops_list: list[dict], region_key: str) -> tuple[float, list[str]]:
    """Score regional suitability without treating nearby-region tags as local proof.

    Exact regional entries receive their full catalogue rating. A rating borrowed
    from a neighbouring agro-climatic region is discounted and labelled as proxy
    evidence. Missing evidence remains unknown rather than being silently scored
    as highly suitable.
    """
    points = {"high": 95.0, "moderate": 72.0, "low": 25.0}
    keys = REGION_FALLBACKS.get(region_key, (region_key,))
    # Kerala / humid south-west coast: the state extension material specifically
    # identifies rice systems and rice-okra diversification; ginger also has an
    # explicit western-ghats entry in this crop catalogue. Other crops fall back
    # to neighbouring-region evidence and are deliberately discounted.
    west_coast_overrides = {
        "rice": "high",
        "okra": "moderate",
    } if region_key == "western_ghats" else {}

    per_crop: list[float] = []
    warnings: list[str] = []
    for crop in crops_list:
        crop_id = crop.get("id")
        reg_map = crop.get("regional_suitability", {}) or {}
        direct_rating = west_coast_overrides.get(crop_id) or reg_map.get(region_key)
        if direct_rating in points:
            rating_score = points[direct_rating]
            per_crop.append(rating_score)
            if direct_rating == "low":
                warnings.append(f"{crop.get('name', crop_id or 'Crop')} is marked low-suitability for the selected agro-climatic region.")
            elif direct_rating == "moderate":
                warnings.append(f"{crop.get('name', crop_id or 'Crop')} has moderate rather than high regional suitability in the selected agro-climatic region.")
            continue

        # A neighbouring-region high rating is not equivalent to a local high
        # rating. Cap proxy evidence at 60; moderate/low retain a conservative
        # confidence discount as well.
        proxy_rating = next((reg_map.get(key) for key in keys if reg_map.get(key) in points), None)
        if proxy_rating == "high":
            per_crop.append(60.0)
            warnings.append(f"Regional suitability for {crop.get('name', crop_id or 'this crop')} is inferred from a neighbouring zone, not directly documented for this location.")
        elif proxy_rating == "moderate":
            per_crop.append(52.0)
            warnings.append(f"Only moderate neighbouring-zone evidence is available for {crop.get('name', crop_id or 'this crop')}; verify locally.")
        elif proxy_rating == "low":
            per_crop.append(25.0)
            warnings.append(f"Neighbouring-zone evidence indicates low suitability for {crop.get('name', crop_id or 'this crop')}; verify locally.")
        else:
            per_crop.append(50.0)
            warnings.append(f"Regional evidence for {crop.get('name', crop_id or 'this crop')} is unavailable; suitability is unknown, not confirmed.")

    return sum(per_crop) / max(1, len(per_crop)), warnings


def evaluate_single_strategy(
    strat_id: str,
    strat_name: str,
    crop_ids: list[str],
    farmer_profile: dict[str, Any],
    description: str = "",
    benefits: list[str] | None = None,
    disadvantages: list[str] | None = None,
    assumptions: list[str] | None = None,
    climate_summary: dict[str, Any] | None = None,
) -> dict[str, Any]:
    priority = farmer_profile.get("priority", "balanced")
    if priority not in PRIORITY_WEIGHTS:
        priority = "balanced"
    weights = PRIORITY_WEIGHTS[priority]

    irrigation = str(farmer_profile.get("irrigation", "assured_tubewell")).lower()
    soil_type = str(farmer_profile.get("soil_type", "alluvial")).lower()
    soil_ph = farmer_profile.get("soil_ph")
    organic_carbon_pct = farmer_profile.get("organic_carbon_pct")
    crops_list = [{**CROPS[cid], "id": cid} for cid in crop_ids if cid in CROPS]
    if not crops_list:
        raise ValueError("At least one valid crop ID must be provided")

    lat = farmer_profile.get("lat")
    lon = farmer_profile.get("lon")
    is_indian_zone = (lat is None or lon is None) or (6.0 <= float(lat) <= 38.0 and 68.0 <= float(lon) <= 98.0)
    if is_indian_zone:
        reg_key, reg_name = detect_indian_agroclimatic_zone(lat, lon)
    else:
        reg_key, reg_name, _hemisphere, _eco_zone = detect_global_climate_zone(lat, lon)

    water_score, total_water, water_warn = _score_water(crops_list, irrigation)
    soil_score, soil_warn = _score_soil_health(
        crops_list, soil_type, soil_ph=soil_ph, organic_carbon_pct=organic_carbon_pct
    )
    if priority == "soil_improvement":
        # Under a soil-building objective, distinguish sequences with more
        # protective cover/residue traits. This uses the catalogue rating as
        # a relative preference, not a measured biomass or carbon forecast.
        avg_cover = sum(c.get("soil_cover_rating", 3) for c in crops_list) / max(1, len(crops_list))
        cover_priority_bonus = max(0.0, avg_cover - 3.0) * 6.0
        soil_score = max(10.0, min(100.0, soil_score + cover_priority_bonus))
        if cover_priority_bonus > 0:
            soil_warn.append("Soil-improvement priority gives extra weight to the sequence's crop-cover rating.")
    duration_score, turnaround_days, dur_warn = _score_duration(crops_list)
    econ_score, econ_warn = _score_economic(crops_list, priority)
    resilience_score, res_warn = _score_climate_resilience(
        crops_list, climate_summary=climate_summary, region_key=reg_key
    )
    global_region_aliases = {
        "us_corn_belt": "north_america", "us_great_plains": "north_america",
        "us_mediterranean": "north_america", "latin_america_cerrado": "latin_america",
        "latin_america_pampas": "latin_america", "mediterranean_basin": "mediterranean",
        "europe_temperate": "europe", "eurasian_steppe": "russia",
        "australia_grain_belt": "australia", "global_tropical": "global",
        "global_subtropical": "global", "global_temperate": "global", "global_boreal": "global",
    }
    score_region_key = global_region_aliases.get(reg_key, reg_key)
    regional_score, regional_warn = _score_regional_fit(crops_list, score_region_key)

    all_warnings = water_warn + soil_warn + dur_warn + econ_warn + res_warn + regional_warn
    criteria_scores = {
        "water_sustainability": round(water_score, 1),
        "soil_health": round(soil_score, 1),
        "duration_fit": round(duration_score, 1),
        "economic_stability": round(econ_score, 1),
        "climate_resilience": round(resilience_score, 1),
    }

    # Keep the five raw criterion scores separate from the user's priority
    # weights. A crop's growing duration, for example, does not change just
    # because the farmer selects "save water"; what changes is how strongly
    # that criterion contributes to the final ranking.
    weighted_contributions = {
        key: round(criteria_scores[key] * weights[key], 2)
        for key in criteria_scores
    }
    weighted_score = sum(weighted_contributions.values())
    # Regional evidence is a separate context correction, not a sixth user
    # preference. It can move candidates up or down, but cannot overwhelm the
    # five visible criteria.
    if reg_key == "pan_india":
        # No coordinates means no defensible local evidence: retain the
        # farmer-priority score without a regional bonus or penalty.
        regional_adjustment = 0.0
        overall_score = round(max(0.0, min(100.0, weighted_score)), 1)
    else:
        # Preserve 80% of the farmer's selected five-criteria objective while
        # reserving 20% for regional evidence. This prevents a high generic
        # score from masking poor or unknown local crop suitability.
        overall_score = weighted_score * 0.80 + regional_score * 0.20
        regional_adjustment = round(overall_score - weighted_score, 1)
        overall_score = round(max(0.0, min(100.0, overall_score)), 1)

    total_n_fixed = sum(c.get("nitrogen_fixation_kg_ha") or 0 for c in crops_list)
    total_days = sum(c.get("typical_duration", 100) for c in crops_list)
    crop_names = " → ".join(c["name"] for c in crops_list)
    if priority == "water_conservation":
        rationale = f"Uses an estimated {total_water} mm crop-water demand; water sustainability is weighted at 55%."
    elif priority == "soil_improvement":
        rationale = (
            f"Prioritises soil-building traits: about {round(total_n_fixed, 1)} kg/ha biological N fixation, "
            f"{len({c.get('root_type') for c in crops_list})} root architectures, and crop-cover traits."
        )
    elif priority == "income_stability":
        rationale = f"Prioritises relative market-stability ratings ({criteria_scores['economic_stability']}/100); this is not a profit forecast."
    else:
        rationale = f"Balances water, soil, calendar, market-stability and climate criteria for {crop_names}."

    default_benefits: list[str] = []
    if total_n_fixed > 0:
        default_benefits.append(f"Contains crops with an estimated {round(total_n_fixed, 1)} kg N/ha biological fixation credit under effective nodulation.")
    if len({c.get('root_type') for c in crops_list}) > 1:
        default_benefits.append("Combines different root architectures, potentially exploring different soil depths.")
    if total_water <= 700:
        default_benefits.append(f"Low catalogue water-demand total ({total_water} mm) relative to the other evaluated sequences.")

    default_disadvantages: list[str] = []
    if total_water > 1400:
        default_disadvantages.append(f"High cumulative catalogue water-demand total ({total_water} mm).")
    if total_n_fixed == 0:
        default_disadvantages.append("No biological nitrogen fixation is credited for this sequence.")
    if total_days > 330:
        default_disadvantages.append(f"The sequence has {total_days} crop-duration days, leaving limited turnaround buffer.")

    if regional_score >= 82:
        regional_fit = "high"
    elif regional_score >= 64:
        regional_fit = "moderate"
    else:
        regional_fit = "low"

    return {
        "id": strat_id,
        "name": strat_name,
        "description": description or f"Rotation sequence of {crop_names}.",
        "crops": [c["name"] for c in crops_list],
        "crop_ids": [c["id"] for c in crops_list],
        "kharif_crop": crops_list[0]["name"] if len(crops_list) > 0 else None,
        "rabi_crop": crops_list[1]["name"] if len(crops_list) > 1 else None,
        "zaid_crop": crops_list[2]["name"] if len(crops_list) > 2 else None,
        "overall_score": overall_score,
        "criteria_scores": criteria_scores,
        "weights_used": weights,
        "weighted_contributions": weighted_contributions,
        "five_criteria_score": round(weighted_score, 1),
        "water_demand_mm": total_water,
        "rabi_water_demand_mm": crops_list[1]["typical_water_mm"] if len(crops_list) > 1 else 0,
        "nitrogen_fixed_kg_ha": round(total_n_fixed, 1),
        "total_duration_days": total_days,
        "turnaround_days": turnaround_days,
        "regional_suitability": regional_fit,
        "regional_fit_score": round(regional_score, 1),
        "regional_adjustment": round(regional_adjustment, 1),
        "warnings": all_warnings,
        "benefits": benefits or default_benefits or ["Agronomic trade-offs should be checked against local extension advice."],
        "disadvantages": disadvantages or default_disadvantages or ["Subject to local seasonal conditions and market-price variation."],
        "assumptions": assumptions or ["Timely sowing and suitable local varieties and management practices."],
        "rationale": rationale,
    }


def evaluate_rotations(
    farmer_profile: dict[str, Any],
    climate_summary: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Generates and evaluates the top 4-6 viable rotation pathways tailored dynamically to farmer profile."""
    priority = farmer_profile.get("priority", "balanced")
    irrigation = str(farmer_profile.get("irrigation", "assured_tubewell")).lower()
    lat = farmer_profile.get("lat")
    lon = farmer_profile.get("lon")
    is_indian_zone = (lat is None or lon is None) or (6.0 <= float(lat) <= 38.0 and 68.0 <= float(lon) <= 98.0)
    if is_indian_zone:
        reg_key, reg_name = detect_indian_agroclimatic_zone(lat, lon)
    else:
        reg_key, reg_name, _hemisphere, _eco_zone = detect_global_climate_zone(lat, lon)

    candidate_rotations = [
        # Pathway 1: Staple / Baseline Rotation
        {
            "id": "rice_wheat",
            "name": "Rice → Wheat (Staple Baseline)",
            "crop_ids": ["rice", "wheat"],
            "description": "Traditional cereal-cereal staple dominant in the Indo-Gangetic Plains.",
            "benefits": [
                "Established local cultivation practices and assured seed supply.",
                "Established market liquidity referencing government Minimum Support Price (MSP) benchmarks; however, open-market realization varies significantly without guaranteed public procurement.",
            ],
            "disadvantages": [
                "High total water demand (~1600 mm/year), straining regional groundwater aquifers.",
                "Continuous shallow fibrous rooting creates a plow pan and depletes the same soil horizon.",
                "Zero biological nitrogen fixation; heavy synthetic fertilizer dependency.",
            ],
            "assumptions": ["Assured tubewell or canal irrigation available for multiple Rabi irrigations."],
        },
        # Pathway 2: Pulse / Soil-Regenerative Diversification
        {
            "id": "rice_pulse",
            "name": "Rice → Pulse (Chickpea / Lentil)",
            "crop_ids": ["rice", "chickpea"],
            "description": "Cereal-legume rotation introducing biological nitrogen fixation and deep taproot subsoil loosening.",
            "benefits": [
                "Saves approximately 170 mm of irrigation water compared to wheat.",
                "Biological nitrogen fixation contributes an estimated 35 kg N/ha net residual credit to the soil system.",
                "Deep taproot penetrates below the puddled rice hardpan, recycling deeper subsoil nutrients.",
            ],
            "disadvantages": [
                "Highly sensitive to unseasonal winter rainfall and waterlogging.",
                "Susceptible to pod borer (Helicoverpa armigera) and vascular wilt.",
            ],
            "assumptions": ["Plot has adequate surface drainage to prevent water stagnation."],
        },
        # Pathway 3: Oilseed Diversification
        {
            "id": "rice_mustard",
            "name": "Rice → Mustard (Sarson / Rai)",
            "crop_ids": ["rice", "mustard"],
            "description": "Cereal-oilseed rotation offering high economic return and lower water requirement.",
            "benefits": [
                "Requires ~35% less irrigation water than wheat (~250 mm in Rabi).",
                "Deep taproot (up to 110 cm) improves soil porosity and extracts deep residual moisture.",
                "Strong domestic edible oil market demand with remunerative prices.",
            ],
            "disadvantages": [
                "Susceptible to aphid infestation during cloudy winter spells and frost risk.",
                "Does not fix atmospheric nitrogen.",
            ],
            "assumptions": ["Timely sowing in October/early November to escape late aphid attacks."],
        },
        # Pathway 4: Vegetable / Cash-Crop Intensification
        {
            "id": "rice_potato_moong",
            "name": "Rice → Potato → Green Gram (3-Crop Intensification)",
            "crop_ids": ["rice", "potato", "green_gram"],
            "description": "High-intensity triple cropping maximizing land productivity with cash crops and catch legumes.",
            "benefits": [
                "Extremely high commercial revenue potential from early winter table potatoes.",
                "Green gram in Zaid fixes ~30 kg N/ha net residual credit and protects soil from harsh summer erosion.",
                "Diversified income streams across cereals, vegetables, and pulses.",
            ],
            "disadvantages": [
                "High capital investment required for seed tubers and cold storage logistics.",
                "Potato is a heavy nutrient extractor requiring disciplined irrigation.",
            ],
            "assumptions": ["Cold storage facilities and assured tubewell irrigation available."],
        },
        # Pathway 5: Millets / Climate-Resilient Dryland Rotation
        {
            "id": "pearl_millet_chickpea",
            "name": "Pearl Millet (Bajra) → Chickpea (Climate-Resilient)",
            "crop_ids": ["pearl_millet", "chickpea"],
            "description": "Drought-hardy cereal-pulse sequence tailored for water-scarce or light-textured upland soils.",
            "benefits": [
                "Extremely low total water demand (~650 mm/year), conserving over 55% water compared to Rice-Wheat.",
                "Chickpea adds 35 kg N/ha net residual nitrogen; Bajra produces nutritious coarse grain and stover.",
                "Exceptional climate resilience against delayed monsoons and mid-season dry spells.",
            ],
            "disadvantages": [
                "Lower gross commercial revenue compared to intensive cash crop or wheat rotations.",
                "Local consumer food preference in canal-irrigated zones leans toward rice and wheat.",
            ],
            "assumptions": ["Well-drained upland or medium land with low flood risk."],
        },
        # Pathway 6: Maize Diversification
        {
            "id": "rice_maize",
            "name": "Rice → Maize (Cereal Diversification)",
            "crop_ids": ["rice", "maize"],
            "description": "Cereal diversification breaking continuous wheat cultivation with high yield potential.",
            "benefits": [
                "Diversifies cereal rotation and avoids wheat terminal heat stress.",
                "Expanding local feed and industrial processing market with strong regional demand.",
                "Deeper root system (up to 90 cm) exploring greater soil volume than wheat.",
            ],
            "disadvantages": [
                "Demands ~500 mm water in Rabi; high fertilizer requirement with zero N-fixation.",
                "Hybrid seed must be purchased fresh every season.",
            ],
            "assumptions": ["Sufficient irrigation and fertilizer investment available."],
        },
    ]

    # Additional alternatives stop the engine from comparing only one dryland
    # winner against a small fixed baseline list. These are candidates, not
    # universal prescriptions; regional, soil, irrigation and climate scores decide.
    candidate_rotations.extend([
        {
            "id": "maize_green_gram",
            "name": "Maize → Green Gram (Cereal-Legume Sequence)",
            "crop_ids": ["maize", "green_gram"],
            "description": "A cereal-legume option with a short-duration summer pulse and biological nitrogen fixation.",
            "benefits": ["Adds a legume break after maize.", "Green gram has a short catalogue duration and adds a nitrogen-fixing crop."],
            "disadvantages": ["Maize is a relatively high water and nutrient-demand crop."],
            "assumptions": ["Suitable sowing windows and drainage are available."],
        },
        {
            "id": "groundnut_sesame",
            "name": "Groundnut → Sesame (Oilseed Diversification)",
            "crop_ids": ["groundnut", "sesame"],
            "description": "An oilseed-focused sequence for well-drained fields, subject to local sowing windows.",
            "benefits": ["Diversifies oilseed production and includes a legume crop.", "Sesame is relatively short duration in the catalogue."],
            "disadvantages": ["Both crops require good drainage; waterlogging can damage establishment."],
            "assumptions": ["Field is well drained and local market access is available."],
        },
    ])

    # Dynamically inject rainfed-specific dryland rotation when farm is rainfed
    if irrigation == "rainfed":
        candidate_rotations.insert(0, {
            "id": "sorghum_lentil",
            "name": "Sorghum (Jowar) → Lentil (Dryland Rotation)",
            "crop_ids": ["sorghum", "lentil"],
            "description": "Low-water dryland rotation for moisture-stressed soils with low synthetic input needs.",
            "benefits": [
                "Thrives on residual moisture with less than 600 mm total water requirement.",
                "Lentil fixes ~30 kg N/ha net residual credit; Sorghum provides rich livestock fodder.",
            ],
            "disadvantages": ["Lower yield ceiling than irrigated cereals."],
            "assumptions": ["Conserve monsoon moisture with deep summer plowing."],
        })

    # Dynamically inject region-specific candidate pathways across all India
    if reg_key in ("southern_peninsula", "deccan"):
        candidate_rotations.extend([
            {
                "id": "cotton_chickpea",
                "name": "Cotton → Chickpea (Peninsular Vertisol System)",
                "crop_ids": ["cotton", "chickpea"],
                "description": "Commercial fibre and legume sequence suited for Deccan and Peninsular black soils.",
                "benefits": ["High commercial cash returns from seed cotton.", "Chickpea fixes ~35 kg N/ha and breaks bollworm pest cycles."],
                "disadvantages": ["Requires pest management and well-drained soils."],
                "assumptions": ["Medium to deep black soils with supplementary irrigation."],
            },
            {
                "id": "finger_millet_groundnut",
                "name": "Finger Millet (Ragi) → Groundnut (Southern Dryland)",
                "crop_ids": ["finger_millet", "groundnut"],
                "description": "Nutritious drought-hardy millet and oilseed sequence with low synthetic input needs.",
                "benefits": ["Finger millet is exceptionally drought resilient.", "Groundnut contributes ~30 kg N/ha biological nitrogen fixation."],
                "disadvantages": ["Lower yield volume than flooded rice systems."],
                "assumptions": ["Light to medium red or loamy soils."],
            },
        ])
    elif reg_key in ("arid_west", "central"):
        candidate_rotations.extend([
            {
                "id": "soybean_wheat",
                "name": "Soybean → Wheat / Chickpea (Central India / Malwa System)",
                "crop_ids": ["soybean", "wheat"],
                "description": "Major oilseed-cereal rotation across Central India and Western Vertisol tracts.",
                "benefits": ["Soybean fixes ~35 kg N/ha and vacates the field early for timely wheat sowing.", "Robust industrial oilseed market demand."],
                "disadvantages": ["Soybean is sensitive to extended mid-season dry spells."],
                "assumptions": ["Assured irrigation available for winter crop."],
            },
            {
                "id": "groundnut_wheat",
                "name": "Groundnut → Wheat (Western / Saurashtra System)",
                "crop_ids": ["groundnut", "wheat"],
                "description": "Legume-cereal diversification common in Gujarat and Western semi-arid regions.",
                "benefits": ["Groundnut adds valuable nitrogen credit.", "Remunerative market demand for edible nuts and fodder oilcake."],
                "disadvantages": ["High seed cost for groundnut kernels."],
                "assumptions": ["Light sandy loam or well-drained medium black soil."],
            },
        ])

    # Kerala / humid south-west coast: include systems reflected in Kerala's
    # state and ICAR crop guidance instead of treating the entire south as dryland.
    if reg_key == "western_ghats":
        candidate_rotations.extend([
            {
                "id": "rice_okra",
                "name": "Rice → Okra (Humid South-West Coast)",
                "crop_ids": ["rice", "okra"],
                "description": "A rice-to-vegetable sequence included as a regionally relevant option for suitable Kerala lowlands.",
                "benefits": ["Rice is an established crop in Kerala; okra adds a diversified vegetable phase."],
                "disadvantages": ["Requires drainage planning and access to vegetable markets; not suitable for every flooded or saline plot."],
                "assumptions": ["Field is not persistently waterlogged during the vegetable phase."],
            },
            {
                "id": "rice_blackgram",
                "name": "Rice → Black Gram (Paddy-Pulse Sequence)",
                "crop_ids": ["rice", "black_gram"],
                "description": "A paddy-pulse option for suitable lowlands and post-rice windows.",
                "benefits": ["Combines a familiar lowland crop with a short-duration pulse."],
                "disadvantages": ["The pulse phase needs a drained seedbed and an appropriate sowing window."],
                "assumptions": ["Water recedes in time for black-gram establishment."],
            },
            {
                "id": "finger_millet_pigeonpea",
                "name": "Finger Millet → Pigeonpea (Peninsular Diversification)",
                "crop_ids": ["finger_millet", "pigeonpea"],
                "description": "A cereal-legume diversification option for suitable upland and well-drained fields.",
                "benefits": ["Both crops have documented regional relevance; pigeonpea adds biological nitrogen fixation."],
                "disadvantages": ["Not intended for poorly drained lowlands or fields with prolonged waterlogging."],
                "assumptions": ["Upland or sloping field with adequate drainage and a suitable local variety."],
            },
            {
                "id": "ginger_cowpea",
                "name": "Ginger → Cowpea (Humid Upland Sequence)",
                "crop_ids": ["ginger", "cowpea"],
                "description": "A higher-value spice and pulse option for well-drained humid uplands.",
                "benefits": ["Ginger has documented Western Ghats relevance; cowpea adds a legume phase."],
                "disadvantages": ["Ginger is input- and water-demanding and is vulnerable to poor drainage; market returns vary."],
                "assumptions": ["Raised beds, good drainage, healthy planting material and local market access are available."],
            },
        ])

    if not is_indian_zone:
        candidate_rotations = _global_candidate_rotations(reg_key)

    evaluated = []
    for strat in candidate_rotations:
        ev = evaluate_single_strategy(
            strat_id=strat["id"],
            strat_name=strat["name"],
            crop_ids=strat["crop_ids"],
            farmer_profile=farmer_profile,
            description=strat.get("description", ""),
            benefits=strat.get("benefits"),
            disadvantages=strat.get("disadvantages"),
            assumptions=strat.get("assumptions"),
            climate_summary=climate_summary,
        )
        evaluated.append(ev)

    evaluated.sort(key=lambda item: item["overall_score"], reverse=True)
    weights = PRIORITY_WEIGHTS.get(priority, PRIORITY_WEIGHTS["balanced"])

    return {
        "farmer_profile": {
            **farmer_profile,
            "priority": priority,
            "source": "farmer_reported",
        },
        "detected_region": {
            "key": reg_key,
            "name": reg_name,
        },
        "rotations": evaluated,
        "crops": {cid: dict(CROPS[cid]) for cid in BASE_CROP_IDS if cid in CROPS},
        "weights": weights,
        "disclaimer": DISCLAIMER,
    }


def evaluate_custom_rotation(
    crop_ids: list[str],
    farmer_profile: dict[str, Any],
    climate_summary: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Evaluates an arbitrary user-chosen sequence from the merged global crop catalogue."""
    valid_ids = [cid for cid in crop_ids if cid in CROPS]
    if not valid_ids:
        raise ValueError("At least one valid crop must be selected from the catalog")

    crop_names = [CROPS[cid]["name"] for cid in valid_ids]
    strat_id = "_".join(valid_ids)
    strat_name = " → ".join(crop_names)

    ev = evaluate_single_strategy(
        strat_id=strat_id,
        strat_name=strat_name,
        crop_ids=valid_ids,
        farmer_profile=farmer_profile,
        description=f"Custom rotation sequence: {strat_name}",
        climate_summary=climate_summary,
    )

    priority = farmer_profile.get("priority", "balanced")
    weights = PRIORITY_WEIGHTS.get(priority, PRIORITY_WEIGHTS["balanced"])

    return {
        "farmer_profile": {
            **farmer_profile,
            "priority": priority,
            "source": "farmer_reported",
        },
        "evaluation": ev,
        "weights": weights,
        "disclaimer": DISCLAIMER,
    }
