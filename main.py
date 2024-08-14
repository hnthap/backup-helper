from backup_helper import get_today_string, load_time_log, new_backup, parse_arguments, save_time_log


def main():
    outdir, directories, password, no_same_date = parse_arguments()
    log_path = outdir / 'log.json'
    log = load_time_log(log_path)
    today = get_today_string()
    for directory in directories:
        key = str(directory.absolute())
        if no_same_date and log.get(key, None) == today:
            continue
        new_backup(outdir, directory, password)
        log[key] = today
    save_time_log(log, log_path)


if __name__ == '__main__':
    main()
