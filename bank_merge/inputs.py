# -*- coding:utf-8 -*-
import csv
import itertools
from abc import ABCMeta, abstractmethod
from typing import Callable, Sequence, Generator

from bank_merge.common import Row


class AbstractInput(metaclass=ABCMeta):
    """
    Base class for all input types.
    """

    @abstractmethod
    def __init__(self, *, path: str, row_parser: Callable[[Sequence[str]], Row]) -> None:
        """
        Initialise input parser.

        :param path: path to a input file or source URI
        :param row_parser: callable to be applied to every row to convert it to common form
        """

    @abstractmethod
    def __iter__(self) -> Generator[Row, None, None]:
        """
        This method should yield normalised rows from input file.

        :return: Row instances
        """


class CSVFile(AbstractInput):

    def __init__(self, *, path, row_parser) -> None:
        # pylint: disable=super-init-not-called
        self.path = path
        self.row_parser = row_parser

    def __iter__(self) -> Generator[Row, None, None]:
        with open(self.path, 'r') as fh:
            reader = csv.reader(fh)

            for row in itertools.islice(reader, 1, None):
                yield self.row_parser(row)
