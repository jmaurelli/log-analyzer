from typing import Any
from collections import defaultdict

def convert_sets_to_lists(obj: Any) -> Any:
    """Convert sets and defaultdicts to serializable types"""
    if isinstance(obj, (dict, defaultdict)):
        return {k: convert_sets_to_lists(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_sets_to_lists(v) for v in obj]
    elif isinstance(obj, set):
        return sorted(list(obj))
    return obj