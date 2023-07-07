import sqlite3
from sqlite3 import Connection
from typing import Optional
from sqlite_utils import Database


def ram_connection(disk_connection: Connection, name: Optional[str]) -> Connection:
    db = Database(memory_name=name)
    disk_connection.backup(db)
    return db