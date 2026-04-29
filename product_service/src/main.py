from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Product Service")

PRODUCTS = {
    "prod_123": {"id": "prod_123", "name": "Laptop", "price": 999.99, "available": True},
    "prod_456": {"id": "prod_456", "name": "Mouse", "price": 29.99, "available": True},
    "prod_789": {"id": "prod_789", "name": "Keyboard", "price": 79.99, "available": False},
}


class ProductResponse(BaseModel):
    id: str
    name: str
    price: float
    available: bool


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "product-service"}


@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: str) -> ProductResponse:
    product = PRODUCTS.get(product_id)
    if not product:
        raise HTTPException(
            status_code=404,
            detail=f"Product '{product_id}' not found"
        )
    return ProductResponse(**product)
