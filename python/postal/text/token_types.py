from postal.utils.enum import Enum, EnumValue


class token_types(Enum):
    # Word types
    WORD = EnumValue(1)
    ABBREVIATION = EnumValue(2)
    IDEOGRAPHIC_CHAR = EnumValue(3)
    HANGUL_SYLLABLE = EnumValue(4)
    ACRONYM = EnumValue(5)

    # Special tokens
    EMAIL = EnumValue(20)
    URL = EnumValue(21)
    US_PHONE = EnumValue(22)
    INTL_PHONE = EnumValue(23)

    # Numbers and numeric types
    NUMERIC = EnumValue(50)
    ORDINAL = EnumValue(51)
    ROMAN_NUMERAL = EnumValue(52)
    IDEOGRAPHIC_NUMBER = EnumValue(53)

    # Punctuation types, may separate a phrase
    PERIOD = EnumValue(100)
    EXCLAMATION = EnumValue(101)
    QUESTION_MARK = EnumValue(102)
    COMMA = EnumValue(103)
    COLON = EnumValue(104)
    SEMICOLON = EnumValue(105)
    PLUS = EnumValue(106)
    AMPERSAND = EnumValue(107)
    AT_SIGN = EnumValue(108)
    POUND = EnumValue(109)
    ELLIPSIS = EnumValue(110)
    DASH = EnumValue(111)
    BREAKING_DASH = EnumValue(112)
    HYPHEN = EnumValue(113)
    PUNCT_OPEN = EnumValue(114)
    PUNCT_CLOSE = EnumValue(115)
    DOUBLE_QUOTE = EnumValue(119)
    SINGLE_QUOTE = EnumValue(120)
    OPEN_QUOTE = EnumValue(121)
    CLOSE_QUOTE = EnumValue(122)
    SLASH = EnumValue(124)
    BACKSLASH = EnumValue(125)
    GREATER_THAN = EnumValue(126)
    LESS_THAN = EnumValue(127)

    # Non-letters and whitespace
    OTHER = EnumValue(200)
    WHITESPACE = EnumValue(300)
    NEWLINE = EnumValue(301)

    WORD_TOKEN_TYPES = set([
        WORD,
        ABBREVIATION,
        IDEOGRAPHIC_CHAR,
        HANGUL_SYLLABLE,
        ACRONYM
    ])

    NUMERIC_TOKEN_TYPES = set([
        NUMERIC,
        ORDINAL,
        ROMAN_NUMERAL,
        IDEOGRAPHIC_NUMBER,
    ])
