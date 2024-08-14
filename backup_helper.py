import argparse
import json
from pathlib import Path
import subprocess
import time
from typing import Dict, Union


def extract_arguments():
    parser = argparse.ArgumentParser(
        prog='Backup Helper',
        description='Help you quickly create backup as compressed directory',
        epilog='Have fun backing up'
    )
    parser.add_argument('directories', nargs='+')
    parser.add_argument('-o', '--outdir')
    parser.add_argument('-p', '--password')
    parser.add_argument('-s', '--nosamedate', action='store_true')
    args = parser.parse_args()
    return args


def get_today_string():
    now = time.time()
    now_local = time.localtime(now)
    now_string = time.strftime('%Y-%m-%d', now_local)
    return now_string


def load_time_log(log_path: Path, not_exists_ok = True) -> Dict[str, str]:
    if log_path.exists():
        with open(log_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    if not_exists_ok:
        return {}
    raise FileExistsError(log_path)


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


def parse_arguments():
    args = extract_arguments()
    outdir = parse_arg_outdir(args)
    directories = parse_arg_directories(args)
    password = args.password
    no_same_date = args.nosamedate
    return outdir, directories, password, no_same_date


def parse_arg_directories(args: argparse.Namespace):
    directories = [Path(d) for d in args.directories]
    assert all(d.exists() for d in directories)
    return directories


def parse_arg_outdir(args: argparse.Namespace):
    outdir = Path('backup' if args.outdir is None else args.outdir)
    if not outdir.exists():
        outdir.mkdir()
    return outdir


def save_time_log(log: Dict[str, str], log_path: Path):
    with open(log_path, 'w', encoding='utf-8') as f:
        json.dump(log, f, ensure_ascii=False, indent=4)

