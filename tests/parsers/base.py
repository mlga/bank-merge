# -*- coding:utf-8 -*-
import pytest
from hypothesis import given
from hypothesis.strategies import dates, one_of, decimals, integers, just

from bank_merge.common import TransactionType


class BaseTest:

    def _prepare_row(self, transaction_time, transaction_type, amount, from_account, to_account):
        raise NotImplementedError()

    def _get_parser(self):
        raise NotImplementedError()

    @given(
        transaction_time=dates(),
        transaction_type=one_of(*[just(variant) for variant in TransactionType]),
        amount=decimals(min_value=0, allow_nan=False, allow_infinity=False),
        from_account=integers(min_value=0),
        to_account=integers(min_value=0),
    )
    def test_parse_row__ok(self, transaction_time, transaction_type, amount, from_account, to_account):
        row = self._prepare_row(transaction_time, transaction_type, amount, from_account, to_account)
        parsed_row = self._get_parser()(row)

        assert parsed_row.date == transaction_time
        assert parsed_row.transaction_type == transaction_type
        assert parsed_row.amount == amount
        assert parsed_row.from_account == from_account
        assert parsed_row.to_account == to_account

    @pytest.mark.parametrize(
        'row',
        [
            ['05 October 2011 14:48 UTC', 'remove', '0.99999999999999999961033714813378812947', '7163', '28568'],
            ['Feb 28 1996', 'delete', '0.610440886', '2566321103514746383', '7163'],
            ['Mar 12 7902', 'remove', '5.23x10', '28214', '32'],
            ['Mar 12 7902', 'remove', '0.0047832405', '3sd3', '32'],
            ['Mar 12 7902', 'remove', '0.9999394527', '28214', 'fffa'],
        ]
    )
    def test_parse_row__err(self, row):
        with pytest.raises(Exception):
            self._get_parser()(row)
