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
        if k in ["options_content", "generic_content"]:
            tokens[k].insert(
                0,
                (
                    r"(~?)(\w+)(\s*)(:)(\s*)(\w+)",
                    bygroups(
                        Operator, Name.Label, Whitespace, Operator, Whitespace, Keyword
                    ),
                ),
            )
    tokens.update(
        {
            "all": [
                (
                    r"(\s*)(--pycode-begin--)(\s*)",
                    bygroups(Whitespace, Name.Decorator, Whitespace),
                    "py-content",
                ),
                (
                    r"(~?)(\w+)(\s*)(:)(\s*)",
                    bygroups(Operator, Name.Label, Whitespace, Operator, Whitespace),
                ),
                (r"(--)(\s*)", bygroups(Operator, Whitespace)),
            ],
            "py-content": [
                (
                    r"(\s*)(--pycode-end--)(\s*)",
                    bygroups(Whitespace, Name.Decorator, Whitespace),
                    "#pop",
                ),
                (r".*\n", using(PythonLexer)),
            ],
            "tasks": [
                (
                    r"(\s*)(--pycode-begin--)(\s*)",
                    bygroups(Whitespace, Name.Decorator, Whitespace),
                    "py-content",
                ),
                (r"^(?=\s*\[)", Punctuation, "#pop"),
                (r"#.*", Comment.Single),
                (r"\bdefault\b", Keyword.Reserved),
                (r"^(.*)(\s*)(:)", bygroups(Text, Whitespace, Operator)),
                (r"^(\s*)(\w+)", bygroups(Whitespace, Name)),
                (r"\b\w+\b", Name.Tag),
                (r"\s+", Whitespace),
                (r":", Operator),
                (r".*\n", Number),
            ],
        }
    )
