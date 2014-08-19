# coding: utf-8
"""
jinja2schema.visitors.util
~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import jinja2.nodes

from ..mergers import merge
from ..model import Dictionary, Scalar, Unknown


def visit(node, config, predicted_struct_cls=Scalar, return_struct_cls=Unknown):
    if isinstance(node, jinja2.nodes.Stmt):
        structure = visit_stmt(node, config)
    elif isinstance(node, jinja2.nodes.Expr):
        ctx = Context(predicted_struct=predicted_struct_cls.from_ast(node), return_struct_cls=return_struct_cls)
        _, structure = visit_expr(node, ctx, config)
    elif isinstance(node, jinja2.nodes.Template):
        structure = visit_many(node.body, config)
    return structure


def visit_many(nodes, config, predicted_struct_cls=Scalar, return_struct_cls=Unknown):
    """Visits ``nodes`` and merges results.

    :param nodes: list of :class:`jinja2.nodes.Node`
    :param predicted_struct_cls: ``predicted_struct`` for expression visitors will be constructed
                                   using this class by calling :meth:`from_ast` method
    :return: :class:`Dictionary`
    """
    rv = Dictionary()
    for node in nodes:
        structure = visit(node, config, predicted_struct_cls=predicted_struct_cls, return_struct_cls=return_struct_cls)
        rv = merge(rv, structure)
    return rv


# keep these at the end of file to avoid circular imports
from .expr import Context, visit_expr
from .stmt import visit_stmt
