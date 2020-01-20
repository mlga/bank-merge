# -*- coding:utf-8 -*-
from bank_merge.__main__ import cli


BANK1_CSV = '''timestamp,type,amount,from,to
Oct 1 2019,remove,99.10,198,182
Oct 2 2019,add,2000.10,188,198'''

BANK2_CSV = '''date,transaction,amounts,to,from
03-10-2019,remove,99.99,182,198
04-10-2019,add,2123.99,198,188'''

BANK3_CSV = '''date_readable,type,euro,cents,to,from
5 Oct 2019,remove,5,44,182,198
6 Oct 2019,add,1060,44,198,188'''

OUT_CSV = ''',date,transaction_type,amount,from_account,to_account
0,2019-10-01,remove,99.10,198,182
1,2019-10-02,add,2000.10,188,198
2,2019-10-03,remove,99.99,198,182
3,2019-10-04,add,2123.99,188,198
4,2019-10-05,remove,5.44,198,182
5,2019-10-06,add,1060.44,188,198
'''


def test_merge_pipeline(click_runner):
    """
    Test that merging three example files works. This is an integration test
    of whole CLI tool.
    """
    with click_runner.isolated_filesystem():
        with open('1.csv', 'w') as fh:
            fh.write(BANK1_CSV)
        with open('2.csv', 'w') as fh:
            fh.write(BANK2_CSV)
        with open('3.csv', 'w') as fh:
            fh.write(BANK3_CSV)

        result = click_runner.invoke(cli, ['-f1', '1.csv', '-f2', '2.csv', '-f3', '3.csv', 'out.csv'])

        assert result.exit_code == 0, result.output.encode('utf-8')

        with open('out.csv', 'r') as fh:
            assert fh.read() == OUT_CSV
