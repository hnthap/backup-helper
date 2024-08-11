import json
import time

from backup_helper import new_backup, parse_arguments


def main():
    outdir, directories, password = parse_arguments()
    for directory in directories:
        new_backup(outdir, directory, password)
    now_unix_secs = time.time()
    now_local = time.localtime(now_unix_secs)
    info = {
        'compressing_local_time': {
            'year': now_local[0],
            'month': now_local[1],
            'month_day': now_local[2],
        },
    } 
    with open(outdir / 'info.json', 'w', encoding='utf-8') as f:
        json.dump(info, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
