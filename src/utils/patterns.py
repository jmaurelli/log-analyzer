import re
from typing import Dict, List

LEVEL_PATTERNS: Dict[str, List[str]] = {
    'errors': [r'error', r'exception', r'fail', r'critical'],
    'warnings': [r'warning', r'warn'],
    'info': [r'info', r'information']
}

COMPONENT_PATTERNS: Dict[str, str] = {
    'pid': r'(?:pid[=:]?\s*|^|\[)(\d+)(?:\]|$|\s)',
    'thread': r'(?:thread[=:]?\s*|^|\[)([0-9a-fA-F-]+)(?:\]|$|\s)',
    'function': r'(?:func(?:tion)?[=:]?\s*|^|\[)([a-zA-Z_][a-zA-Z0-9_\.]*)(?:\(.*?\))?(?:\]|$|\s)'
}

class PatternCompiler:
    @staticmethod
    def compile_patterns() -> Dict[str, re.Pattern]:
        return {
            name: re.compile(pattern) 
            for name, pattern in COMPONENT_PATTERNS.items()
        }