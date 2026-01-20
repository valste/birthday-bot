import json
from pathlib import Path
from typing import Any


def load_history(path: Path) -> dict[str, list[dict[str, str]]]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def save_history(path: Path, history: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(history, fh, ensure_ascii=False, indent=2)
