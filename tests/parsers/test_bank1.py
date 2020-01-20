# -*- coding:utf-8 -*-
from bank_merge.common import TransactionType
from bank_merge.row_parsers import bank1
from tests.parsers.base import BaseTest


class TestBank1(BaseTest):

    def _prepare_row(self, transaction_time, transaction_type, amount, from_account, to_account):
        return [
            transaction_time.strftime('%b %d %Y'),
            'add' if transaction_type is TransactionType.ADD else 'remove',
            str(amount),
            str(from_account),
            str(to_account),
        ]

    def _get_parser(self):
        return bank1
