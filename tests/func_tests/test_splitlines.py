# coding: utf-8
from jinja2schema.core import infer
from jinja2schema.model import Dictionary, String


def test_splitlines():
    template = '''
{% macro NL2BR (text) -%}
  {% for line in (text or '').splitlines() %}
    {{line}}<br>
  {% endfor %}
{%- endmacro %}
    {{ NL2BR(vin) }}
    '''

    struct = infer(template)
    expected_struct = Dictionary({
        'vin': String(label="vin", linenos=[2, 7], value=""),
    })
    assert struct == expected_struct
