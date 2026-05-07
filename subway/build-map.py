#!/usr/bin/env python3
"""Build the Notion API tube-style map.

Notion's OpenAPI exposes 6 tags. Rendered as a single closed-hexagon loop
since the surface is a tightly-coupled graph (Pages contain Blocks; Pages
live in Databases; Users own Comments; etc.) with no clear start/end.
"""

import sys
import math
from pathlib import Path

sys.path.insert(0, "/Users/kinlane/GitHub/all/.claude/skills")
from _subway_engine import build_subway  # noqa: E402


# Hexagon centered at (640, 470), radius 130.
def hex_point(idx, n=6, cx=640, cy=470, r=130):
    angle = -math.pi / 2 + idx * 2 * math.pi / n
    return (round(cx + r * math.cos(angle)), round(cy + r * math.sin(angle)))


LINES = [
    {
        "name": "Notion Workspace",
        "color": "#7B3FE4",  # Notion-ish purple
        "closed": True,
        "stations": [
            ("Pages",     hex_point(0)),  # 12 o'clock
            ("Databases", hex_point(1)),
            ("Search",    hex_point(2)),
            ("Users",     hex_point(3)),  # 6 o'clock
            ("Comments",  hex_point(4)),
            ("Blocks",    hex_point(5)),
        ],
    },
]

NOTION_API = "https://apis.apis.io/apis/notion/notion-api/"
URL_OVERRIDES = {st: NOTION_API for ln in LINES for (st, _) in ln["stations"]}


def main():
    n = len({st for ln in LINES for (st, _) in ln["stations"]})
    build_subway(
        title="The Notion API · Underground Map",
        subtitle=f"{n} functional areas · 1 closed loop · click any station for the apis.io page",
        lines=LINES,
        source_label="Source: notion/openapi/notion-openapi.yml · github.com/api-evangelist/notion",
        out_dir=Path(__file__).resolve().parent,
        out_basename="notion-subway-map",
        provider_id="notion",
        station_url_overrides=URL_OVERRIDES,
    )


if __name__ == "__main__":
    main()
