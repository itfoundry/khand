#! /usr/bin/env AFDKOPython
# encoding: UTF-8
from __future__ import division, absolute_import, print_function, unicode_literals

import hindkit

STYLES_KHAND = [
    ("ExtraLight",  0.0, 250),
    ("Light",       7.6, 300),
    ("SemiLight",  17.7, 350),
    ("Regular",    28.5, 400),
    ("SemiBold",   42.0, 600),
    ("Bold",       58.0, 700),
    ("ExtraBold",  77.0, 800),
    ("Black",     100.0, 900),
]

def main():

    family = hindkit.Family(
        trademark = "Khand",
        script_name = "Devanagari",
        append_script_name = False,
        client_name = "Google Fonts",
        initial_release_year = 2014,
    )

    i = family.info
    i.openTypeNameDesigner = "Sanchit Sawaria and Jyotish Sonowal (Devanagari), Satya Rajpurohit (Latin)"
    i.openTypeHheaAscender, i.openTypeHheaDescender, i.openTypeHheaLineGap = 1050, -350, 100
    i.openTypeOS2TypoAscender, i.openTypeOS2TypoDescender, i.openTypeOS2TypoLineGap = 1050, -350, 100
    i.openTypeOS2WinAscent, i.openTypeOS2WinDescent = 1100, 400

    family.set_masters()
    family.set_styles(STYLES_KHAND)

    project = hindkit.Project(
        family,
        fontrevision = "2.010",
        options = {
            "prepare_kerning": True,
            "prepare_mark_positioning": True,
            "match_mI_variants": 1,
                "position_marks_for_mI_variants": True,
            "do_style_linking": True,
            "additional_unicode_range_bits": [0, 1, 2],
            "use_os_2_version_4": True,
                "prefer_typo_metrics": True,
            "build_ttf": True,
        },
    )
    project.build()

# --- Overriding ---

hindkit.filters.POTENTIAL_BASES_FOR_LONG_mII.append("K_TA")
hindkit.FeatureMatches.mI_VARIANT_NAME_PATTERN = r"mI\.a\d\d"

# --- Executing ---

main()
