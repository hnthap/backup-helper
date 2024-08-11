import argparse
from pathlib import Path
import subprocess
from typing import Union


def extract_arguments():
    parser = argparse.ArgumentParser(
        prog='Backup Helper',
        description='Help you quickly create backup as compressed directory',
        epilog='Have fun backing up'
    )
    parser.add_argument('outdir', action='store_const', const='backup')
    parser.add_argument('directories', nargs='+')
    parser.add_argument('-p', '--password')
    args = parser.parse_args()
    return args


def parse_arguments():
    args = extract_arguments()
    outdir = Path(args.outdir)
    if not outdir.exists():
        outdir.mkdir()
    directories = [Path(d) for d in args.directories]
    assert all(d.exists() for d in directories)
    password = args.password
    return outdir, directories, password


def new_backup(outdir: Path, directory: Path, password: Union[str, None]):
    print('Compressing {}'.format(directory))
    out_name = directory.name
    out_path = outdir / '{}.7z'.format(out_name)
    subprocess.run([
        '7z', 
        'a', 
        out_path, 
        directory / '*', 
        '-p' if password is None else '-p{}'.format(password), 
        '-mhe=on'
    ])
