# ROTATION IQ — COMPREHENSIVE TESTING & VERIFICATION SUITE

This document outlines the testing architecture, test coverage, and execution instructions for ROTATION IQ.

## 1. Test Architecture Overview

The automated test suite consists of **7 test modules** totaling **70 test cases**:

```
tests/
├── test_analysis.py          # 9 Analytical Tests: Synthetic POWER/NDVI datasets, missing data handling, Mann-Kendall trends, MODIS quality masks
├── test_api.py               # 11 API Integration Tests: FastAPI endpoints, input validation, cache warming, production ASGI import via uvicorn
├── test_rotation.py          # 21 Unit Tests: 1,232-crop catalogue, 53 calibrated Indian crops, individual soil health formula components, dynamic wheat heat stress
├── test_e2e_integration.py   # 11 End-to-End Tests: farmer journey and mocked service recovery
├── test_modis_fallback.py    # 2 MODIS synthetic/observed labelling tests
├── test_profile_adaptation.py# 13 farmer input and scoring adaptation tests
└── test_global_catalogue_merge.py # 3 global crop registry and regional pathway tests
```

### Module Breakdown:
| Module | Tests | Test Scope & Nature |
| :--- | :---: | :--- |
| `tests/test_analysis.py` | 9 | **Synthetic Analytical Tests:** Evaluates Mann-Kendall trend tests, Sen's slopes, baseline departures, and MODIS sinusoidal pixel determinism using deterministic synthetic matrices. |
| `tests/test_api.py` | 11 | **API Integration Tests:** Verifies HTTP endpoints (`/api/health`, `/api/climate`, `/api/rotation/...`), coordinate/year bounds, and verifies production ASGI startup via `uvicorn.Config("backend.main:app")`. |
| `tests/test_rotation.py` | 21 | **Agronomic Unit Tests:** Verifies 1,232 global records, preserves the 53-crop Indian baseline and its 12 Fabaceae BNF records, null non-legume BNF, sugarcane/perennial handling, all individual components of the soil health index, and dynamic wheat heat stress. |
| `tests/test_e2e_integration.py` | 11 | **Simulated Workflow & Failure Mode Tests:** Tests the complete multi-step farmer journey through mock HTTP requests, dynamic priority shifts, and server unavailability recovery (`available: False`). |
| `tests/test_modis_fallback.py` | 2 | **MODIS fallback tests:** Checks explicit synthetic/observed labelling. |
| `tests/test_profile_adaptation.py` | 13 | **Farmer-profile tests:** Checks input-driven scoring changes. |
| `tests/test_global_catalogue_merge.py` | 3 | **Global catalogue tests:** Checks crop count, preserved base records and regional candidate references. |

*Note: Automated tests execute using synthetic datasets and mock HTTP transports to ensure deterministic execution without live network flakiness.*

---

## 2. Running Automated Tests

### Backend Unit & Integration Tests (Python):
```bash
python -m unittest discover -s tests -v
```

### Expected Output:
```
Ran 70 tests (duration depends on the machine)
OK
```

### Frontend TypeScript Verification & Production Build:
```bash
cd frontend
npm run build
```

### Expected Output:
```
vite v7.3.8 building client environment for production...
transforming...
✓ 452 modules transformed.
rendering chunks...
computing gzip size...
dist/index.html                            0.65 kB │ gzip:   0.33 kB
dist/assets/vendor-leaflet-CIGW-MKW.css   15.61 kB │ gzip:   6.46 kB
dist/assets/index-i3zvAIpk.css            27.67 kB │ gzip:   5.99 kB
dist/assets/vendor-leaflet-Bzw0dOc9.js   149.70 kB │ gzip:  43.36 kB
dist/assets/index-Bei3omWw.js            294.97 kB │ gzip:  84.07 kB
dist/assets/vendor-charts-DkEMDxJS.js    418.46 kB │ gzip: 114.94 kB
✓ built in 4.50s
```
