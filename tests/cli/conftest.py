# -*- coding:utf-8 -*-
import pytest
from click.testing import CliRunner


@pytest.fixture
def click_runner():
    return CliRunner()
