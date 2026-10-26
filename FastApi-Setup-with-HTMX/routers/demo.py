from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field

router = APIRouter(prefix="/api", tags=["demo"])


class DemoItem(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    description: str | None = None


items_db: list[DemoItem] = [
    DemoItem(id=1, name="Laptop", description="Gaming laptop"),
    DemoItem(id=2, name="Phone", description="Smartphone"),
    DemoItem(id=3, name="Tablet", description="Tablet device"),
]


@router.get("/hello")
async def hello_demo():
    return {"message": "Hello from APIRouter demo"}


@router.get("/items")
async def get_items():
    return {"items": items_db}


@router.get("/items/{item_id}")
async def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@router.post("/items", response_model=DemoItem)
async def create_item(item: DemoItem):
    items_db.append(item)
    return item


@router.put("/items/{item_id}", response_model=DemoItem)
async def update_item(item_id: int, item: DemoItem):
    for index, current_item in enumerate(items_db):
        if current_item.id == item_id:
            items_db[index] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(index)
            return {"message": f"Item {item_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")


@router.get("/search")
async def search_items(q: str = Query(..., min_length=1, description="Search by item name")):
    results = [item for item in items_db if q.lower() in item.name.lower()]
    return {"query": q, "results": results}
