from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path
import re
import sqlite3


class SaveIntentJournal:
    def __init__(self, path: Path) -> None:
        self._path: Path = path
        with closing(sqlite3.connect(path)) as connection, connection:
            _ = connection.execute(
                """CREATE TABLE IF NOT EXISTS save_intents (
                slot_key TEXT PRIMARY KEY NOT NULL,
                package_digest TEXT NOT NULL,
                intent_recorded_at TEXT NOT NULL)"""
            )

    def claim(self, slot_key: str, package_digest: str) -> bool:
        if not slot_key or slot_key != slot_key.strip():
            raise ValueError("slot_key must be nonempty without outer whitespace")
        if re.fullmatch(r"[0-9a-f]{64}", package_digest) is None:
            raise ValueError("package_digest must be a lowercase SHA-256 digest")
        with closing(sqlite3.connect(self._path)) as connection, connection:
            _ = connection.execute("PRAGMA synchronous = FULL")
            cursor = connection.execute(
                """INSERT INTO save_intents
                (slot_key, package_digest, intent_recorded_at) VALUES (?, ?, ?)
                ON CONFLICT(slot_key) DO NOTHING""",
                (slot_key, package_digest, datetime.now(timezone.utc).isoformat()),
            )
            claimed = cursor.rowcount == 1
        return claimed
