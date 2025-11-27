from dataclasses import dataclass

@dataclass
class Tratta:
    id_hub_A: int
    id_hub_B: int
    guadagno_medio: float

    def __str__(self):
        return f"{self.id_hub_A} ({self.id_hub_B})"

    def __hash__(self):
        return hash(self.id_hub_A)
