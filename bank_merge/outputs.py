# -*- coding:utf-8 -*-
import csv
from abc import ABCMeta, abstractmethod

from bank_merge.common import Row, TransactionType


class AbstractOutput(metaclass=ABCMeta):
    """
    Base class for all output types.
    """

    # internal API
    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    # public API
    @abstractmethod
    def open(self) -> None:
        """
        Open destination for writing, file or DB connection.
        """

    @abstractmethod
    def write_row(self, row: Row) -> None:
        """
        Write a row to destination.

        :param row: Row instance
        """

    @abstractmethod
    def close(self) -> None:
        """
        Close destination, file or DB connection.
        """


class CSVFile(AbstractOutput):

    def __init__(self, path: str) -> None:
        self.path = path
        self.fh = None
        self.writer = None
        self.index = 0

    def open(self) -> None:
        self.fh = open(self.path, 'w')
        self.writer = csv.writer(self.fh)

        self.writer.writerow([None, 'date', 'transaction_type', 'amount', 'from_account', 'to_account'])

    def write_row(self, row: Row) -> None:
        self.writer.writerow([
            self.index,
            row.date.strftime('%Y-%m-%d'),
            'add' if row.transaction_type is TransactionType.ADD else 'remove',
            row.amount,
            row.from_account,
            row.to_account,
        ])

        self.index += 1

    def close(self) -> None:
        self.fh.close()
