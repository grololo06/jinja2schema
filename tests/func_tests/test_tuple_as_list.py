# coding: utf-8
from jinja2schema.core import infer
from jinja2schema.model import Dictionary, String


def test_tuple_as_list():
    template = '''
{% macro selectinputtuple(name, values, value='') -%}
    <select class="form-control" name="{{ name }}" id="{{ name }}">
    {% for v2 in values %}
        <option value="{{ v2[0] }}"  {{ 'selected' if value==v2[0] }}>{{ v2[1] }}</option>
    {% endfor %}
    </select>
{%- endmacro %}
    </td><td style="padding-right: 5px;">{{ selectinputtuple("ipp",[('0','Fit'),('1','1'),('1000','1000')],data.ipp) }}
    '''

    struct = infer(template)
    expected_struct = Dictionary({
        'data': Dictionary(label="data", data={
            'ipp': String(label="ipp", linenos=[2, 9], value=""),
        }, linenos=[9]),
    })
    assert struct == expected_struct
