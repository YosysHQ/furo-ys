from .MauLexer import MauLexer

__all__ = ['SBYLexer']

class SBYLexer(MauLexer):
    name = 'SBY config lexer'
    aliases = ['sby']

    ys_sections = ['script']
    options_sections = ['options']

    # TODO: figure out tags
