import re
from hashlib import md5

class LogNormalizer:
    @staticmethod
    def normalize_line(line: str) -> str:
        """
        Normalize log line by removing variable parts
        """
        # Remove timestamps
        line = re.sub(
            r'\d{4}-\d{2}-\d{2}[T ]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:[+-]\d{4})?', 
            'TIMESTAMP', 
            line
        )
        # Remove hex addresses
        line = re.sub(r'0x[0-9a-fA-F]+', 'HEXADDR', line)
        # Remove numbers but preserve PIDs
        line = re.sub(r'(?<![\w])\d+(?![\w])', 'NUM', line)
        return line.strip()

    @staticmethod
    def get_line_hash(line: str) -> str:
        """
        Generate hash for normalized line
        """
        normalized = LogNormalizer.normalize_line(line)
        return md5(normalized.encode()).hexdigest()