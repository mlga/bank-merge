# -*- coding:utf-8 -*-
import pytest

from bank_merge.__main__ import cli


@pytest.mark.parametrize(
    'out',
    [
        'out.csv',
        'file://out.csv',
        'file://./out.csv',
    ]
)
def test_output_param_ok(click_runner, out):
    """
    Test different ways of specifying output destination. Currently, only
    local csv file is supported.
    """
    with click_runner.isolated_filesystem():
        with open('1.csv', 'w'): pass

        result = click_runner.invoke(cli, ['-f1', '1.csv'] + [out])

        assert result.exit_code == 0, result.output.encode('utf-8')


@pytest.mark.parametrize(
    'out',
    [
        'postgresql://aaa:bbb@localhost/test',
    ]
)
def test_output_param_unsupported(click_runner, out):
    """
    Test that unsupported output format causes error.
    """
    with click_runner.isolated_filesystem():
        with open('1.csv', 'w'): pass

        result = click_runner.invoke(cli, ['-f1', '1.csv'] + [out])

        assert result.exit_code != 0, result.output.encode('utf-8')
