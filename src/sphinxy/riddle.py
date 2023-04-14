from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Riddle:
    question: str
    answer: str

    def check_answer(self, answer: str) -> bool:
        """Evaluates given answer against the actual riddle answer.

        Args:
            answer (str): The answer to the riddle question.

        Returns:
            bool: The result of the evaluation; True if answer is correct, False otherwise.
        """
        return answer.lower() == self.answer.lower()

    def get_hint(self) -> Iterator[str]:
        """Gives the next letter of the answer as a hint to the question

        Yields:
            Iterator[str]: The next character of the answer.
        """

        yield from iter(self.answer)
