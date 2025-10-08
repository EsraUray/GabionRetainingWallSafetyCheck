# Gabion Retaining Wall — Safety Check (Jupyter Notebook)

## 🇬🇧 Quick Start (EN)

This repo contains a Jupyter notebook for **gabion retaining wall safety checks**: `notebooks/GabionRetainingWallSafetyCheck_LibraryManual.ipynb`.

### 1) Setup
**Conda**
```bash
conda env create -f environment.yml
conda activate gabionretainingwallsafetycheck-librarymanual
```

**or** `venv + pip`
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

(Optional) Register a Jupyter kernel:
```bash
python -m ipykernel install --user --name gabionretainingwallsafetycheck-librarymanual --display-name "gabionretainingwallsafetycheck-librarymanual"
```

### 2) Run the notebook
```bash
jupyter notebook
```
Then open `notebooks/GabionRetainingWallSafetyCheck_LibraryManual.ipynb`.

### License & Citation
- License: MIT (see `LICENSE`)
- Citation: see `CITATION.cff`
