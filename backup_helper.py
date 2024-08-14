from pathlib import Path
import subprocess
from typing import Union


def new_backup(outdir: Path, directory: Path, password: Union[str, None]):
    print('\033[92m[INFO] Compressing {}\033[0m'.format(directory))
    out_name = directory.name
    out_path = outdir / '{}.7z'.format(out_name)
    parts = [
        '7z', 
        'a', 
        out_path, 
        directory / '*', 
        '-mhe=on'
    ]
    if password is not None:
        parts.append('-p{}'.format(password))
    subprocess.run(parts)

