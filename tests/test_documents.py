import pytest

from vault.documents import DocumentError, build_document
from vault.memory_store import MemoryStore


def test_save_and_filter_by_category():
    store = MemoryStore()
    store.save(build_document({"sku": "frame-100", "name": "Round Frame", "category": "Frames", "price_cents": 8900}))
    store.save(build_document({"sku": "LENS-1", "name": "Daily Lens", "category": "lenses", "price_cents": 1400, "attributes": {"pack": 30}}))
    frames = store.find_by_category("frames")
    assert [item.sku for item in frames] == ["FRAME-100"]
    assert store.get("lens-1").attributes["pack"] == 30


def test_invalid_price_is_rejected():
    with pytest.raises(DocumentError):
        build_document({"sku": "X1", "name": "Case", "category": "care", "price_cents": "free"})
