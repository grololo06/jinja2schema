# coding: utf-8
from jinja2schema.core import infer
from jinja2schema.model import Dictionary, Scalar, List, String


def test_list_becomes_dict():
    template = '''
{%   for r in PrjList %}
<tr><td><a class='btn btn-primary' href='/part/prj/{{ r[0] }}'>Select</a></td>
  <td> {{ r[1] }} [{{ r[0] }}] {{ ("<a href='mailto:"+r['email']+"'>") |safe if r['email'] }}</td>
  <td>{{ r['samplecount'] }}</td>
  </tr>
{%  endfor %}
    '''

    struct = infer(template)
    expected_struct = Dictionary({'PrjList': List(
        Dictionary({
            0: Scalar(),
            1: Scalar(),
            'email': String(label="email", linenos=[4]),
            'samplecount': Scalar(label="samplecount", linenos=[5]),
        }, label="r", linenos=[3, 4, 5]),
            label="PrjList", linenos=[2]
    ), })
    assert struct == expected_struct
