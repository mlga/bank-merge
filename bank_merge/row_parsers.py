# -*- coding:utf-8 -*-
"""
Functions to normalise rows in different formats (coming from
different banks).
Each function must return a Row instance.
"""
from datetime import datetime
from decimal import Decimal
from typing import Sequence

from bank_merge.common import Row, TransactionType


def _transaction_type(value):
    # it happen to be common now
    if value == 'add':
        return TransactionType.ADD
    elif value == 'remove':
        return TransactionType.REMOVE

    raise KeyError(value)


def bank1(row: Sequence[str]) -> Row:
    return Row(
        date=datetime.strptime(row[0], '%b %d %Y').date(),
        transaction_type=_transaction_type(row[1]),
        amount=Decimal(row[2]),
        from_account=int(row[3]),
        to_account=int(row[4]),
    )


def bank2(row: Sequence[str]) -> Row:
    return Row(
        date=datetime.strptime(row[0], '%d-%m-%Y').date(),
        transaction_type=_transaction_type(row[1]),
        amount=Decimal(row[2]),
        from_account=int(row[4]),
        to_account=int(row[3]),
    )


def bank3(row: Sequence[str]) -> Row:
    return Row(
        date=datetime.strptime(row[0], '%d %b %Y').date(),
        transaction_type=_transaction_type(row[1]),
        amount=Decimal(f"{row[2]}.{row[3]}"),
        from_account=int(row[5]),
        to_account=int(row[4]),
    )
