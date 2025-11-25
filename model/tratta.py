from dataclasses import dataclass

@dataclass
class Tratta:
    id_hab_A: int
    id_hab_B: int
    guadagno_medio: float

    def __eq__(self, other):
        return isinstance(other, Hub) and self.id == other.id

    def __str__(self):
        return f"{self.nome} ({self.stato})"

    def __repr__(self):
        return f"{self.nome} ({self.stato})"

    def __hash__(self):
        return hash(self.id)
