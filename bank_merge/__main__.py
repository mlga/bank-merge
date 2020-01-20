# -*- coding:utf-8 -*-
import itertools

import click

from bank_merge import row_parsers, inputs, outputs, cli


@click.command(
    help='CLI tool that merges multiple bank transaction documents into one, '
         'unified report.'
)
@click.option(
    '--file-bank1', '-f1', 'bank1_files',
    type=cli.BankInputFile(row_parser=row_parsers.bank1),
    multiple=True,
    help='File to merge, following "bank1" row format. Can be repeated.',
)
@click.option(
    '--file-bank2', '-f2', 'bank2_files',
    type=cli.BankInputFile(row_parser=row_parsers.bank2),
    multiple=True,
    help='File to merge, following "bank2" row format. Can be repeated.',
)
@click.option(
    '--file-bank3', '-f3', 'bank3_files',
    type=cli.BankInputFile(row_parser=row_parsers.bank3),
    multiple=True,
    help='File to merge, following "bank3" row format. Can be repeated.',
)
@click.argument('output', type=cli.BankOutput())
def cli(
        bank1_files: inputs.AbstractInput,
        bank2_files: inputs.AbstractInput,
        bank3_files: inputs.AbstractInput,
        output: outputs.AbstractOutput,
):
    all_input_files = itertools.chain(bank1_files, bank2_files, bank3_files)

    with output as out:
        for bank_file in all_input_files:
            for row in bank_file:
                out.write_row(row)

    print('DONE')
