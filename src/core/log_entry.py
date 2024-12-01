from dataclasses import dataclass, asdict
from typing import Dict

@dataclass
class LogEntry:
    line: str
    line_number: int
    frequency: int = 1
    first_occurrence: int = 0
    last_occurrence: int = 0

    def to_dict(self) -> Dict:
        return {
            'line': self.line,
            'line_number': self.line_number,
            'frequency': self.frequency,
            'first_occurrence': self.first_occurrence,
            'last_occurrence': self.last_occurrence
        }