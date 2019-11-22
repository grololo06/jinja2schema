# coding: utf-8
from jinja2schema.core import infer
from jinja2schema.model import Dictionary, String


def test_dict_get():
    template = '''
  {%if g.get(slswtch, 0) == 2 %}
    <link rel=stylesheet type=text/css href="/css/select2.css')">
  {%endif %}
  {{ slswtch | safe }}
    '''

    struct = infer(template)
    expected_struct = Dictionary({
        'slswtch': String(label="slswtch", linenos=[2, 5])
    })
    assert struct == expected_struct
