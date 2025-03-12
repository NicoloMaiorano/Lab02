from dataclasses import dataclass, field
from typing import List


@dataclass
class Parola:
    parola: str
    traduzioni: List[int] = field(default_factory=list)
    numeroTraduzioni: int = 0

    def aggiungiTraduzione(self, entry):
        self.traduzioni.append(entry)
        self.numeroTraduzioni = self.numeroTraduzioni +1