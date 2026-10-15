import argparse
import json

from vault.documents import build_document
from vault.mongo_store import MongoStore


def main() -> None:
    parser = argparse.ArgumentParser(description="Save one product document in MongoDB.")
    parser.add_argument("--sku", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--category", required=True)
    parser.add_argument("--price-cents", required=True, type=int)
    args = parser.parse_args()
    document = build_document(
        {
            "sku": args.sku,
            "name": args.name,
            "category": args.category,
            "price_cents": args.price_cents,
            "attributes": {},
        }
    )
    saved = MongoStore().save(document)
    print(json.dumps(saved.as_dict()))


if __name__ == "__main__":
    main()
