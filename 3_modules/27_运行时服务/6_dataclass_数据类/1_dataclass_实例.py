from dataclasses import dataclass

@dataclass
class book:
    name: str = 'unkonw'
    price: float = 10.0
    author: str = 'unkonw'
    number: int = 0

hero_book = book()
