from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Riddle:
    question: str
    answer: str

    def check_answer(self, answer: str) -> bool:
        return answer.lower() == self.answer.lower()

    def get_hint(self) -> Iterator[str]:
        yield from iter(self.answer)
