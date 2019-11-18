# coding: utf-8
import pytest

from jinja2schema import InvalidExpression
from jinja2schema.core import infer
from jinja2schema.model import Dictionary


def test_items():
    template = '''
{% macro selectinputdict(name, values, value=0, addemptyrow=false ,extrataginfo='') -%}
    <select name="{{ name }}" id="{{ name }}" {{ extrataginfo }}>
    {% if addemptyrow %}
      <option></option>
    {% endif %}
    {% for k,v in values.items() %}
        <option value="{{ k or '' }}"  {{ 'selected' if value==k+1 }}>{{ v }}</option>
    {% endfor %}
    </select>
{%- endmacro %}
<td>{{ selectinputdict('priv_new_member', g.users, 5,true) }}</td>
'''

    struct = infer(template)
    expected_struct = Dictionary({
        'g': Dictionary(label="g", data={
            'users': Dictionary(label="users", data={}, linenos=[2, 12]),
        }, linenos=[12]),
    })
    assert struct == expected_struct

def test_items_noarg():
    template = '''
{% macro selectinputdict(name, values, value=0, addemptyrow=false ,extrataginfo='') -%}
    <select name="{{ name }}" id="{{ name }}" {{ extrataginfo }}>
    {% for k,v in values.items(456) %}
        <option value="{{ k or '' }}"  {{ 'selected' if value==k+1 }}>{{ v }}</option>
    {% endfor %}
    </select>
{%- endmacro %}
<td>{{ selectinputdict('priv_new_member', g.users, 5,true) }}</td>
'''
    with pytest.raises(InvalidExpression):
        infer(template)
