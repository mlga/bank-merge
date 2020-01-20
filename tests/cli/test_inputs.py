# -*- coding:utf-8 -*-
from typing import List

import pytest

from bank_merge.__main__ import cli


@pytest.mark.parametrize(
    'params',
    [
        ['-f1', '1.csv'],
        ['-f2', '2.csv'],
        ['-f3', '3.csv'],
        ['-f1', '1.csv', '-f2', '2.csv', '-f3', '3.csv'],
    ]
)
def test_csv_is_ok(click_runner, params: List[str]):
    """
    Test that .csv input extensions are working.
    """
    with click_runner.isolated_filesystem():
        with open('1.csv', 'w'): pass
        with open('2.csv', 'w'): pass
        with open('3.csv', 'w'): pass

        result = click_runner.invoke(cli, params + ['out.csv'])

        assert result.exit_code == 0, result.output.encode('utf-8')


@pytest.mark.parametrize(
    'params',
    [
        ['-f1', '1.xls'],
        ['-f2', '2.png'],
        ['-f3', '3.doc'],
        ['-f1', '1.csv', '-f2', '2.csv', '-f3', '3.zip'],
    ]
)
def test_noncsv_is_err(click_runner, params: List[str]):
    """
    Test that non-csv files cause error.
    """
    with click_runner.isolated_filesystem():
        with open('1.csv', 'w'): pass
        with open('2.csv', 'w'): pass
        with open('3.csv', 'w'): pass

        result = click_runner.invoke(cli, params + ['out.csv'])

        assert result.exit_code != 0, result.output.encode('utf-8')
