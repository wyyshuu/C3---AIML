from typing import Dict, Any


class Product:
    def __init__(
        self,
        name: str,
        category: str = "General",
        quantity: int = 1,
        quality_grade: str = "A",
        origin: str = "Local",
        base_market_price: int = 100,
        attributes: Dict[str, Any] = None,
    ):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.quality_grade = quality_grade
        self.origin = origin
        self.base_market_price = base_market_price
        self.attributes = attributes or {}
