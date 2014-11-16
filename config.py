#!/usr/bin/python

FAMILY_NAME = 'Khand'

STYLE_NAMES = [
    'ExtraLight',
    'Light',
    'SemiLight',
    'Regular',
    'SemiBold',
    'Bold',
    'ExtraBold',
    'Black',
]

UFOIG_ARGS = [
    # '-kern',
    '-mark',
    # '-hint',
    '-flat',
    '-mkmk',
    '-clas',
    '-indi',
]

MATCH_mI_OFFSETS_DICT = {
    'ExtraLight': 0,
    'Light':      0,
    'SemiLight':  0,
    'Regular':    0,
    'SemiBold':   0,
    'Bold':       0,
    'ExtraBold':  0,
    'Black':      0,
}

MAKEOTF_ARGS = [
    '-r',
    '-shw',
]

OUTPUT_DIR = '/Library/Application Support/Adobe/Fonts'
