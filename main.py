from backup_helper import new_backup, parse_arguments


def main():
    outdir, directories, password = parse_arguments()
    for directory in directories:
        new_backup(outdir, directory, password)


if __name__ == '__main__':
    main()
