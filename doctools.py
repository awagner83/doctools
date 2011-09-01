"""Docblock manipulation utilities."""

from itertools import ifilter
from pprint import pformat


def append_to_docs(fn, text):
    """Append text to a functions existing docblock."""
    min_indent = _getindent(fn.__doc__)
    fn.__doc__ = '%s\n\n%s' % (fn.__doc__, _indent(text, min_indent))


def append_var_to_docs(fn, label, value):
    """Append text & pformatted value to docblock."""
    value_width = 76 - _getindent(fn.__doc__)
    append_to_docs(
            fn,
            "%s:\n%s" % (
                label,
                _indent(pformat(value, width=value_width))
            )
        )


def _indent(string, indent_level=4):
    """Indent each line by `indent_level` of spaces."""
    return '\n'.join('%s%s' % (' '*indent_level, x) for x in
            string.splitlines())


def _getindent(string):
    try:
        indent_levels = (_nspaces(x) for x in string.splitlines() if x)
        return min(ifilter(lambda x: x != 0, indent_levels)) or 0
    except (AttributeError, ValueError):
        # Things that don't look like strings and strings with no
        # indentation should report indentation of 0
        return 0


def _nspaces(line):
    for idx, char in enumerate(line):
        if char != ' ':
            return idx

