"""Mau-style config lexer."""

from pygments.lexer import RegexLexer, bygroups, include, using
from pygments.lexers.hdl import SystemVerilogLexer, VerilogLexer, VhdlLexer
from pygments.token import (
    Comment,
    Keyword,
    Name,
    Number,
    Operator,
    Other,
    Punctuation,
    String,
    Text,
    Whitespace,
)

from .YoscryptLexer import YoscryptLexer

__all__ = ["MauLexer"]


class MauLexer(RegexLexer):
    """Mau-style config lexer."""

    name = "Mau-style config lexer"
    aliases = ["mau"]

    ys_sections = ["script"]
    options_sections = ["options"]

    tokens = {
        "common": [
            (r"\s+", Whitespace),
            (r"#.*", Comment.Single),
            (r"^\w+", Keyword),
            (r"on|off", Number.Bin),
            (r'"', String, "string"),
            (r"(\d+)(\')([bdho]? ?\w+)", bygroups(Number, Operator, Number)),
            (r"(\d+\.\d+)", Number.Float),
            (r"(\d+)", Number),
        ],
        "root": [
            (
                r"(\[)(files)(\])(\s*)$",
                bygroups(Punctuation, Name.Class, Punctuation, Whitespace),
                "files_content",
            ),
            (
                r"(\[)(file)(\s+)(\w+.sva?)(\])(\s*)$",
                bygroups(
                    Punctuation, Name.Class, Whitespace, String, Punctuation, Whitespace
                ),
                "sv_content",
            ),
            (
                r"(\[)(file)(\s+)(\w+.vh?)(\])(\s*)$",
                bygroups(
                    Punctuation, Name.Class, Whitespace, String, Punctuation, Whitespace
                ),
                "v_content",
            ),
            (
                r"(\[)(file)(\s+)(\w+.vhdl?)(\])(\s*)$",
                bygroups(
                    Punctuation, Name.Class, Whitespace, String, Punctuation, Whitespace
                ),
                "vhdl_content",
            ),
            (
                r"(\[)(file)(\s+)(\w+)(\])(\s*)$",
                bygroups(
                    Punctuation, Name.Class, Whitespace, String, Punctuation, Whitespace
                ),
                "file_content",
            ),
            (
                r"(\[)(" + "|".join(ys_sections) + r")(\])(\s*)$",
                bygroups(Punctuation, Name.Class, Punctuation, Whitespace),
                "ys_content",
            ),
            (
                r"(\[)(" + "|".join(options_sections) + r")(\])(\s*)$",
                bygroups(Punctuation, Name.Class, Punctuation, Whitespace),
                "options_content",
            ),
            (
                r"(\[)(.*)(\])(\s*)$",
                bygroups(Punctuation, Name.Class, Punctuation, Whitespace),
                "generic_content",
            ),
            include("common"),
            (r".", Other),  # to prevent errors
        ],
        "files_content": [
            (r"^(?=\s*\[)", Punctuation, "#pop"),
            (r"#.*", Comment.Single),
            (r".*\n", Name),
        ],
        "sv_content": [
            (r"^(?=\s*\[)", Punctuation, "#pop"),
            (r".*\n", using(SystemVerilogLexer)),
        ],
        "v_content": [
            (r"^(?=\s*\[)", Punctuation, "#pop"),
            (r".*\n", using(VerilogLexer)),
        ],
        "vhdl_content": [
            (r"^(?=\s*\[)", Punctuation, "#pop"),
            (r".*\n", using(VhdlLexer)),
        ],
        "file_content": [
            (r"^(?=\s*\[)", Punctuation, "#pop"),
            (r".*\n", Text),
        ],
        "ys_content": [
            (r"^(?=\s*\[)", Punctuation, "#pop"),
            (r".*\n", using(YoscryptLexer)),
        ],
        "options_content": [
            (r"^(?=\s*\[)", Punctuation, "#pop"),
            include("common"),
            (r".*\n", Name),
        ],
        "generic_content": [
            (r"^(?=\s*\[)", Punctuation, "#pop"),
            include("common"),
            (r".*\n", Text),
        ],
        "string": [
            (r'"', String, "#pop"),
            (r'\\([\\abfnrtv"\']|x[a-fA-F0-9]{2,4}|[0-7]{1,3})', String.Escape),
            (r'[^\\"\n]+', String),  # all other characters
            (r"(\\)(\n)", bygroups(String.Escape, Whitespace)),  # line continuation
            (r"\\", String),  # stray backslash
        ],
    }
