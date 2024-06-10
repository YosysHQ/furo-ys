"""SBY specific subclass of mau config lexer."""

from copy import deepcopy

from pygments.lexer import bygroups, include, using
from pygments.lexers.python import PythonLexer
from pygments.token import (
    Comment,
    Keyword,
    Name,
    Number,
    Operator,
    Punctuation,
    String,
    Text,
    Whitespace,
)

from .MauLexer import MauLexer

__all__ = ["SBYLexer"]


class SBYLexer(MauLexer):
    """SBY config lexer."""

    name = "SBY config lexer"
    aliases = ["sby"]

    ys_sections = ["script"]
    options_sections = ["options"]

    tokens = {}
    for k, v in MauLexer.tokens.items():
        tokens[k] = deepcopy(v)
        if k == "root":
            tokens[k].insert(
                0,
                (
                    r"(\[)(tasks)(\])(\s*)$",
                    bygroups(Punctuation, Name.Class, Punctuation, Whitespace),
                    "tasks",
                ),
            )
        tokens[k].insert(0, include("all"))
    tokens.update(
        {
            "all": [
                (
                    r"(\s*)(--pycode-begin--)(\s*)",
                    bygroups(Whitespace, Number, Whitespace),
                    "py-content",
                ),
                (
                    r"(\w+)(\s*)(:)(\s*)",
                    bygroups(Name.Decorator, Whitespace, Punctuation, Whitespace),
                ),
                (r"(--)(\s*)", bygroups(Operator, Whitespace)),
            ],
            "py-content": [
                (
                    r"(\s*)(--pycode-end--)(\s*)",
                    bygroups(Whitespace, Number, Whitespace),
                    "#pop",
                ),
                (r".*\n", using(PythonLexer)),
            ],
            "tasks": [
                (r"^(?=\s*\[)", Punctuation, "#pop"),
                (r"#.*", Comment.Single),
                (r"\bdefault\b", Keyword.Reserved),
                (r"^(.*)(\s*)(:)", bygroups(Text, Whitespace, Punctuation)),
                (r"^(\s*)(\w+)", bygroups(Whitespace, Name.Decorator)),
                (r"\b\w+\b", Name.Tag),
                (r"\s+", Whitespace),
                (r":", Punctuation),
                (r".*\n", String),
            ],
        }
    )
