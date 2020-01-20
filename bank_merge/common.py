# -*- coding:utf-8 -*-
from datetime import date
from dataclasses import dataclass
from decimal import Decimal
from enum import Enum


class TransactionType(Enum):
    ADD = 'add'
    REMOVE = 'remove'


@dataclass
class Row:
    date: date
    transaction_type: TransactionType
    amount: Decimal
    from_account: int
    to_account: int
