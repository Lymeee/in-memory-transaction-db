# main.py

from in_memory_db import InMemoryDB, TransactionError


def demo_from_assignment() -> None:
    db = InMemoryDB()

    def safe_call(label, func, *args, **kwargs):
        print(f">>> {label}")
        try:
            result = func(*args, **kwargs)
            if result is not None:
                print(f"Result: {result}")
        except TransactionError as e:
            print(f"TransactionError: {e}")
        except Exception as e:
            print(f"Error: {e}")
        print()

    safe_call('db.get("A")', db.get, "A")

    safe_call('db.put("A", 5)', db.put, "A", 5)

    safe_call("db.begin_transaction()", db.begin_transaction)

    safe_call('db.put("A", 5)', db.put, "A", 5)

    safe_call('db.get("A")', db.get, "A")

    safe_call('db.put("A", 6)', db.put, "A", 6)

    safe_call("db.commit()", db.commit)

    safe_call('db.get("A")', db.get, "A")

    safe_call("db.commit()", db.commit)

    safe_call("db.rollback()", db.rollback)

    safe_call('db.get("B")', db.get, "B")

    safe_call("db.begin_transaction()", db.begin_transaction)

    safe_call('db.put("B", 10)', db.put, "B", 10)

    safe_call("db.rollback()", db.rollback)

    safe_call('db.get("B")', db.get, "B")


if __name__ == "__main__":
    demo_from_assignment()
