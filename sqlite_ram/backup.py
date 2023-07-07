import sqlite3
from sqlite3 import Connection
from typing import Optional, Tuple
from sqlite_utils import Database


def ram_connection(disk_path: str, name: Optional[str] = None) -> Tuple[Database, Database]:
    if name:
        ram_db = Database(memory_name=name)
    else:
        ram_db = Database(memory=True)
    disk_db = Database(disk_path)
    disk_connection = sqlite3.connect(disk_path)
    disk_connection.backup(ram_db.conn)
    return ram_db, disk_db