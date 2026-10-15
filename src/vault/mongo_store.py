import os

from vault.documents import DocumentError, ProductDocument


class MongoStore:
    def __init__(self, uri: str | None = None, database: str = "catalog_vault") -> None:
        from pymongo import MongoClient

        self._collection = MongoClient(uri or os.environ["MONGO_URI"])[database]["products"]
        self._collection.create_index("sku", unique=True)

    def save(self, document: ProductDocument) -> ProductDocument:
        self._collection.replace_one({"sku": document.sku}, document.as_dict(), upsert=True)
        return document

    def get(self, sku: str) -> ProductDocument:
        row = self._collection.find_one({"sku": sku.upper()})
        if row is None:
            raise DocumentError(f"{sku} was not found")
        return ProductDocument(
            sku=row["sku"],
            name=row["name"],
            category=row["category"],
            price_cents=row["price_cents"],
            attributes=row.get("attributes") or {},
        )

    def find_by_category(self, category: str) -> list[ProductDocument]:
        rows = self._collection.find({"category": category.strip().lower()})
        return [
            ProductDocument(row["sku"], row["name"], row["category"], row["price_cents"], row.get("attributes") or {})
            for row in rows
        ]
