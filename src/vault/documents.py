from dataclasses import dataclass


@dataclass(frozen=True)
class ProductDocument:
    sku: str
    name: str
    category: str
    price_cents: int
    attributes: dict

    def as_dict(self) -> dict:
        return {
            "sku": self.sku,
            "name": self.name,
            "category": self.category,
            "price_cents": self.price_cents,
            "attributes": self.attributes,
        }


class DocumentError(Exception):
    pass


def build_document(payload: dict) -> ProductDocument:
    sku = str(payload.get("sku", "")).strip().upper()
    name = " ".join(str(payload.get("name", "")).split())
    category = str(payload.get("category", "")).strip().lower()
    if len(sku) < 2 or " " in sku:
        raise DocumentError("sku must be at least 2 characters and contain no spaces")
    if not name:
        raise DocumentError("name is required")
    if not category:
        raise DocumentError("category is required")
    try:
        price_cents = int(payload.get("price_cents"))
    except (TypeError, ValueError) as exc:
        raise DocumentError("price_cents must be an integer") from exc
    if price_cents < 0:
        raise DocumentError("price_cents cannot be negative")
    attributes = payload.get("attributes") or {}
    if not isinstance(attributes, dict):
        raise DocumentError("attributes must be an object")
    return ProductDocument(sku, name, category, price_cents, attributes)
