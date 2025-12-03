# in_memory_db.py

from typing import Optional


class TransactionError(Exception):
    """Custom exception for invalid transaction operations."""
    pass


class InMemoryDB:
    """In-memory key-value database with transaction support."""

    def __init__(self) -> None:
        self._main_store: dict[str, int] = {}
        self._transaction_store: Optional[dict[str, int]] = None

    def get(self, key: str) -> Optional[int]:
        return self._main_store.get(key, None)

    def put(self, key: str, val: int) -> None:
        """Set value by key in current transaction."""
        if self._transaction_store is None:
            raise TransactionError("put() called without an active transaction")

        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        if not isinstance(val, int):
            raise TypeError("Value must be an integer")

        self._transaction_store[key] = val

    def begin_transaction(self) -> None:
        """Start a new transaction."""
        if self._transaction_store is not None:
            raise TransactionError("A transaction is already in progress")
        self._transaction_store = {}

    def commit(self) -> None:
        """Commit the current transaction."""
        if self._transaction_store is None:
            raise TransactionError("commit() called with no active transaction")

        for key, val in self._transaction_store.items():
            self._main_store[key] = val

        self._transaction_store = None

    def rollback(self) -> None:
        """Roll back the current transaction."""
        if self._transaction_store is None:
            raise TransactionError("rollback() called with no active transaction")

        self._transaction_store = None
