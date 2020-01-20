# Bank document merger
[![build](https://github.com/mlga/bank-merge/workflows/Build/badge.svg)](#)
[![codecov](https://codecov.io/gh/mlga/bank-merge/branch/master/graph/badge.svg)](https://codecov.io/gh/mlga/bank-merge)

CLI tool that merges multiple bank transaction documents into one, unified report.

## Usage
This tool is not available on [PyPi](https://pypi.org/), clone the repository and then install package
```bash
git clone https://github.com/mlga/bank-merge.git && cd bank-merge
pip install .
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

### What input methods are available?
Currently, only local .csv files are supported.

### What output methods are available?
Currently, only .csv files are supported. However, you can specify an output destination using an [URI](https://pl.wikipedia.org/wiki/Uniform_Resource_Identifier).  
Following output arguments are equivalent:
 - `file://output.csv` - fetching remote files might be future improvement
 - `output.csv`
 
This is to support external output destinations in the future, like databases:
 - `postgresql://user:pass@localhost/otherdb`
 
### How add support for new input source?
1. Inherit from [`bank_merge.inputs.AbstractInput`](bank_merge/inputs.py) and implement all abstract methods. `CSVFile` class might serve as an example.
1. Add your class to [`bank_merge.cli_types.BankInputFile.PARSERS`](bank_merge/cli_types.py) mapping.

### How to parse new row structure?
1. In [`bank_merge.row_parsers`](bank_merge/row_parsers.py) module, create a function that accepts `List[str]` (row as present in a file) and returns [`bank_merge.common.Row`](bank_merge/common.py) instance.
1. Add new option to [`bank_merge.__main__.cli`](bank_merge/__main__.py) passing your function as a `row_parser`.

### How to implement new output destination?
1. Inherit from [`bank_merge.outputs.AbstractOutput`](bank_merge/outputs.py) and implement all abstract methods. `CSVFile` class might serve as an example.
1. Add your class to [`bank_merge.cli_types.BankOutput`](bank_merge/cli_types.py) `EXTENSIONS` or `SCHEMAS` mapping.
   - `EXTENSIONS` is for local destinations: `output.xls` or `output.doc`
   - `SCHEMAS` is for remote destinations in URI form, like databases: `postgresql://user:pass@localhost/otherdb`
