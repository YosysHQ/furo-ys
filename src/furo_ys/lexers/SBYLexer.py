"""SBY specific subclass of mau config lexer."""

from .MauLexer import MauLexer

__all__ = ["SBYLexer"]


class SBYLexer(MauLexer):
    """SBY config lexer."""

    name = "SBY config lexer"
    aliases = ["sby"]

    ys_sections = ["script"]
    options_sections = ["options"]

    # TODO: figure out tags
