# Bank document merger
CLI tool that merges multiple bank transaction documents into one, unified report.

## Usage
Clone the repository and install package
```bash
git clone https://github.com/mlga/bank-merge.git
python bank-merge/setup.py
```

Use `bank-merge` command to merge files and get help
```bash
$ bank-merge --help
Usage: bank-merge [OPTIONS] OUTPUT

  CLI tool that merges multiple bank transaction documents into one, unified
  report.

Options:
  -f1, --file-bank1 PATH  File to merge, following "bank1" row format. Can be
                          repeated.
  -f2, --file-bank2 PATH  File to merge, following "bank2" row format. Can be
                          repeated.
  -f3, --file-bank3 PATH  File to merge, following "bank3" row format. Can be
                          repeated.
  --help                  Show this message and exit.
```

Simple example. Merge two files:
```bash
$ bank-merge -f1 bank1.csv -f2 bank2.csv output.csv
```

Merge two files from the same bank:
```bash
$ bank-merge -f1 bank1a.csv -f1 bank1b.csv output.csv
```

Merge two files from the same bank and one file from another:
```bash
$ bank-merge -f1 bank1a.csv -f1 bank1b.csv -f2 bank2.csv output.csv
```

## FAQ

TBA
