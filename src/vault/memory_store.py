from vault.documents import DocumentError, ProductDocument


class MemoryStore:
    def __init__(self) -> None:
        self._items: dict[str, ProductDocument] = {}

    def save(self, document: ProductDocument) -> ProductDocument:
        self._items[document.sku] = document
        return document

    def get(self, sku: str) -> ProductDocument:
        found = self._items.get(sku.upper())
        if found is None:
            raise DocumentError(f"{sku} was not found")
        return found

    def find_by_category(self, category: str) -> list[ProductDocument]:
        needle = category.strip().lower()
        return [item for item in self._items.values() if item.category == needle]
