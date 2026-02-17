from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    id: Optional[int] = None
    name: str = ""
    lastname: str = ""
    membership: str = ""

    def __str__(self) -> str:
        return f"Id: {self.id} | Name: {self.name} | Lastname: {self.lastname} | Membership: {self.membership}"
