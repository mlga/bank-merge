# -*- coding:utf-8 -*-
import os
from urllib.parse import urlsplit

import click

from bank_merge import inputs, outputs


class BankInputFile(click.Path):
    """
    Click type for handling bank input file arguments and delegating
    parsing of such files to selected handler based on file extension.

    Expected input is a local file path.
    """

    PARSERS = {
        '.csv': inputs.CSVFile,
    }

    def __init__(self, *, row_parser, **kwargs):
        self.row_parser = row_parser
        kwargs.setdefault('exists', True)

        super().__init__(**kwargs)

    def convert(self, value, param, ctx):
        path = super().convert(value, param, ctx)

        _, ext = os.path.splitext(path)
        if ext not in self.PARSERS:
            allowed_extensions = ','.join(self.PARSERS.keys())
            self.fail(
                f'input extension {ext} is not supported, allowed extensions: {allowed_extensions}',
                param,
                ctx,
            )

        return self.PARSERS[ext](path=path, row_parser=self.row_parser)


class BankOutput(click.ParamType):
    """
    Click type for handling output argument.

    Expected input is a local file path or destination URI, ex:

     - output.csv
     - /home/me/output.csv
     - /home/me/output.csv
     - file:///home/me/output.csv
     - postgresql://aaa:bbb@localhost/test
    """
    name = 'URI'

    # for local files, use extension to select proper handler
    EXTENSIONS = {
        '.csv': outputs.CSVFile,
    }

    # for non-file URIs, use scheme to select a handler
    SCHEMES = {
        # 'postgresql': outputs.PsqlDB,
    }

    def convert(self, value, param, ctx):
        parts = urlsplit(value)

        if not parts.scheme or parts.scheme == 'file':
            parsed_value = os.path.normpath(os.path.join(
                parts.netloc,
                parts.path.lstrip('/') if parts.netloc else parts.path
            ))

            _, ext = os.path.splitext(parsed_value)
            if ext not in self.EXTENSIONS:
                allowed_extensions = ','.join(self.EXTENSIONS.keys())
                self.fail(
                    f'output extension {ext} is not supported, allowed extensions: {allowed_extensions}',
                    param,
                    ctx,
                )

            destination_cls = self.EXTENSIONS[ext]
        else:
            parsed_value = value

            if parts.scheme not in self.SCHEMES:
                allowed_schemes = ','.join(self.SCHEMES.keys())
                self.fail(
                    f'output scheme {parts.scheme} is not supported, allowed schemes: {allowed_schemes}',
                    param,
                    ctx,
                )

            destination_cls = self.SCHEMES[parts.scheme]

        return destination_cls(parsed_value)
