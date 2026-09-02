#!/usr/bin/env python3

"""
@Time    : 2023-12-29
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Base methods module.
    Provides common base methods and shared dependencies used by other modules.
"""

from __future__ import annotations
from typing import Any, Protocol
from types import MethodType
from reydb import DatabaseEngine, DatabaseEngineAsync
from reykit.rbase import Base

__all__ = (
    'ClientBase',
    'ClientWithDatabase',
    'ClientDatabaseRecord',
    'ClientDatabaseRecordItem'
)

class ClientBase(Base):
    """
    Client base type.
    """

class ClientWithDatabase(Protocol):
    """
    With database method reuqest API fetch type.
    Can create database used `self.build_db` method.
    """

    db_engine: DatabaseEngine | DatabaseEngineAsync | None
    build_db: MethodType

class ClientDatabaseRecord(ClientBase):
    """
    Client type of record into the database.
    """

    def __init__(
        self,
        client: ClientWithDatabase | None = None,
        table: str | None = None
    ) -> None:
        """
        Build instance attributes.

        Parameters
        ----------
        client : Client instance.
            - `None`: Not record.
        table : Table name.
        """

        # Build.
        self.client = client
        self.table = table

    def get_item(self) -> ClientDatabaseRecordItem:
        """
        Build `ClientDatabaseRecordItem` instance.
        """

        # Get.
        item = ClientDatabaseRecordItem(self)

        return item

class ClientDatabaseRecordItem(ClientBase):
    """
    Client type of record one item into the database.
    """

    def __init__(
        self,
        db_record: ClientDatabaseRecord
    ) -> None:
        """
        Build instance attributes.

        Parameters
        ----------
        db_record : `ClientDatabaseRecord` instance.
        """

        # Build.
        self.db_record = db_record
        self.data: dict[str, Any] = {}

    def __setitem__(self, key: str, value: Any) -> None:
        """
        Update record data parameter.

        Parameters
        ----------
        key : Parameter key.
        value : Parameter value.
        """

        # Check.
        if self.db_record.client.db_engine is None:
            return

        # Update.
        self.data[key] = value

    def record(self) -> None:
        """
        Insert record to table of database.
        """

        # Check.
        if self.db_record.client.db_engine is None:
            return

        # Insert.
        self.db_record.client.db_engine.sync_engine.execute.insert(self.db_record.table, self.data)

        # Delete.
        self.data = {}

    async def async_record(self) -> None:
        """
        Asynchronous insert record to table of database.
        """

        # Check.
        if self.db_record.client.db_engine is None:
            return

        # Insert.
        await self.db_record.client.db_engine.async_engine.execute.insert(self.db_record.table, self.data)

        # Delete.
        self.data = {}
