# -*- coding:utf-8 -*-
from bank_merge.common import TransactionType
from bank_merge.row_parsers import bank3
from tests.parsers.base import BaseTest


class TestBank1(BaseTest):

    def _prepare_row(self, transaction_time, transaction_type, amount, from_account, to_account):
        euro, *maybe_cents = str(amount).split('.')
        if maybe_cents:
            cents = maybe_cents[0]
        else:
            cents = '0'

        return [
            transaction_time.strftime('%d %b %Y'),
            'add' if transaction_type is TransactionType.ADD else 'remove',
            euro,
            cents,
            str(to_account),
            str(from_account),
        ]

    def _get_parser(self):
        return bank3
