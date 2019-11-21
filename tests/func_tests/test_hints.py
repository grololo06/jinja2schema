# coding: utf-8
import pytest
from jinja2 import PackageLoader, Environment

from jinja2schema.config import Config
from jinja2schema.core import infer
from jinja2schema.model import Dictionary, String


@pytest.fixture
def env():
    loader = PackageLoader('tests', 'templates')
    return Environment(loader=loader)


# noinspection PyUnusedLocal
def url_for(endpoint: str) -> str:
    pass


# noinspection PyUnusedLocal
def get_flashed_messages(with_categories: bool = True) -> [[str]]:
    pass


@pytest.fixture
def config():
    ret = Config(PACKAGE_NAME='tests')
    ret.add_hint(url_for)
    ret.add_hint(get_flashed_messages)
    return ret


def test_hints_1(config):
    template = """
    <html>
    <script src="{{ url_for(a, filename='vue.js') }}"></script>
    </html>
    """
    struct = infer(template, config)
    expected_struct = Dictionary({
        'a': String(label='a', linenos=[3]),
    })
    assert struct == expected_struct


def test_hints_2(config):
    template = """
  {% for message in get_flashed_messages(true) %}
    <div class="alert alert-{{ message[0]|replace("message","info")|replace("error","danger") }} alert-dismissible" role="alert" >{{ message[1] }}</div>
  {% endfor %}
    """
    struct = infer(template, config)
    expected_struct = Dictionary()
    assert struct == expected_struct
