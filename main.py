from backup_helper import get_today_string, load_time_log, new_backup, parse_arguments, save_time_log


def main():
    outdir, directories, password = parse_arguments()
    log_path = outdir / 'log.json'
    log = load_time_log(log_path)
    for directory in directories:
        log[str(directory.absolute())] = get_today_string()
        new_backup(outdir, directory, password)
    save_time_log(log, log_path)


if __name__ == '__main__':
    main()
