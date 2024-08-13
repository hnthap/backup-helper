# Backup Helper using 7Zip and Python

Helps you automatically compress specified directories into a backup directory, using 7Zip and Python 3. I made this to conveniently back up my data.

## Requirements

- 7Zip: running `7z` in your shell must be available.
- Python 3.

## Installation

```{bash}
git clone https://github.com/hnthap/backup-helper --branch=main --depth=1
cd backup-helper
```

## Usage

### Example 1: Compressing with a password

Assume in the working directory, there are two directories: `homework` and `practice`. Run this command:

```{bash}
python main.py homework practice -o backup -p ThisIsSomePassword!!
```

Result:

```{plaintext}
    ├─── homework
    |     ├─── ...
    |     └─── ...
    ├─── practice
    |     ├─── ...
    |     └─── ...
    └─── backup
          ├─── log.json
          ├─── fold
          └─── folder2.7z
```

The compressed files in `backup` would be opened with the password `ThisIsSomePassword!!`, as specified in this example. That password can be replaced with anything you want.

### Example 2: Compressing without a password

```{bash}
python main.py homework practice -o backup
```

The result would be the same as the first example, but there is no passwords required to use the compressed files.
