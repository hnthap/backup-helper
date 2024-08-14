from contextlib import contextmanager
from pathlib import Path


def invoke_lock(lock_path: Path):
    in_use_message = 'in use'
    if lock_path.exists():
        with open(lock_path, 'r') as f:
            if in_use_message == f.readline():
                raise PermissionError('Another compression are in process')
    with open(lock_path, 'w') as f:
        f.write(in_use_message)


def devoke_lock(lock_path: Path):
    lock_path.unlink()


@contextmanager
def lock(lock_path: Path):
    invoke_lock(lock_path)
    yield lock_path
    devoke_lock(lock_path)
