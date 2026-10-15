# Catalog Vault

Portfolio project by Shagun Sharma. Product documents are stored in MongoDB. Unit tests use an in-memory store with the same rules. Original sample code.

## Stack

Python, PyMongo, MongoDB 7, Docker, pytest.

## Run

```bash
docker compose up -d
export PYTHONPATH=src
export MONGO_URI=mongodb://127.0.0.1:27017
python3 -m vault --sku FRAME-100 --name "Round Frame" --category frames --price-cents 890000
python3 -m pytest
```

## Documents

System design, architecture, the database, the team plan, the delivery plan, and report notes are in `docs/`. Diagrams are in `docs/images/`.
