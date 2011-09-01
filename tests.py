from doctools import append_to_docs, append_var_to_docs, _getindent


def test_append_to_docs():
    def foo():
        """some

        multiline
        docstring"""
        pass

    append_to_docs(foo, 'more random docs')
    assert foo.__doc__ == """some

        multiline
        docstring

        more random docs"""


def test_append_var_to_docs():
    def foo():
        """some

        docstring"""
        pass

    append_var_to_docs(foo, 'My Var', [1, 2, 3, 4])
    assert foo.__doc__ == """some

        docstring

        My Var:
            [1, 2, 3, 4]"""


def test_getindent():
    assert _getindent("""Foo

            bar
            baz""") == 12


def test_getindent():
    assert _getindent("foo") == 0

