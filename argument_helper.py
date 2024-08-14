import argparse
from pathlib import Path


def extract_arguments():
    parser = argparse.ArgumentParser(
        prog='Backup Helper',
        description='Help you quickly create backup as compressed directory',
        epilog='Have fun backing up'
    )
    parser.add_argument('directories', nargs='+')
    parser.add_argument('-o', '--outdir')
    parser.add_argument('-p', '--password')
    args = parser.parse_args()
    return args


def parse_arguments():
    args = extract_arguments()
    outdir = parse_arg_outdir(args)
    directories = parse_arg_directories(args)
    password = args.password
    return outdir, directories, password


def parse_arg_directories(args: argparse.Namespace):
    directories = [Path(d) for d in args.directories]
    assert all(d.exists() for d in directories)
    return directories


def parse_arg_outdir(args: argparse.Namespace):
    outdir = Path('backup' if args.outdir is None else args.outdir)
    if not outdir.exists():
        outdir.mkdir()
    return outdir
