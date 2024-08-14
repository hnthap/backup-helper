from argument_helper import parse_arguments
from backup_helper import new_backup
from lock_helper import lock


def main():
    outdir, directories, password = parse_arguments()
    with lock(outdir / 'backup-helper.lock'):
        for directory in directories:
            new_backup(outdir, directory, password)


if __name__ == '__main__':
    main()
