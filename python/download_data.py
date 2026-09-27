"""Download the DataCo Smart Supply Chain dataset from Kaggle into ./data/.

One-time setup: get a Kaggle API token from https://www.kaggle.com/settings
(API -> Create New Token) and save it to ~/.kaggle/kaggle.json.

Usage:
    python download_data.py
"""
from pathlib import Path

DATASET = "shashwatwork/dataco-smart-supply-chain-for-big-data-analysis"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "Data"


def main() -> None:
    from kaggle.api.kaggle_api_extended import KaggleApi

    DATA_DIR.mkdir(exist_ok=True)
    api = KaggleApi()
    api.authenticate()

    print(f"Downloading '{DATASET}' into {DATA_DIR}/ ...")
    api.dataset_download_files(DATASET, path=str(DATA_DIR), unzip=True)

    print("Done. Files:")
    for f in sorted(DATA_DIR.iterdir()):
        print(f"  - {f.name}")


if __name__ == "__main__":
    main()
