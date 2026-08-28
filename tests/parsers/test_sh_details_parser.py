"""
Copyright (c) 2026 MongoDB Inc.

DISCLAIMER: THESE CODE SAMPLES ARE PROVIDED FOR EDUCATIONAL AND ILLUSTRATIVE PURPOSES ONLY,
TO DEMONSTRATE THE FUNCTIONALITY OF SPECIFIC MONGODB FEATURES.
THEY ARE NOT PRODUCTION-READY AND MAY LACK THE SECURITY HARDENING, ERROR HANDLING, AND TESTING REQUIRED FOR A LIVE ENVIRONMENT.
YOU ARE RESPONSIBLE FOR TESTING, VALIDATING, AND SECURING THIS CODE WITHIN YOUR OWN ENVIRONMENT BEFORE IMPLEMENTATION.
THIS MATERIAL IS PROVIDED "AS IS" WITHOUT WARRANTY OR LIABILITY.
"""

from mongo_x_ray_gmd.parsers.sh_details_parser import SHDetailsParser  # type: ignore

GMD_ITEM = {
    "shards": [
        {
            "_id": "shard01",
            "host": "shard01/localhost:30018,localhost:30019,localhost:30020",
        },
        {
            "_id": "shard02",
            "host": "shard02/localhost:30021,localhost:30022,localhost:30023",
        },
    ],
    "csrs": "configRepl/localhost:30024",
}


def test_sh_details_parser() -> None:
    parser = SHDetailsParser()
    result = parser.parse(GMD_ITEM)
    assert len(result) == 1
    details_table = result[0]
    assert details_table["type"] == "table"
    assert details_table["caption"] == "Component Details - `shards/csrs`"
    assert details_table["header"] == [
        {"text": "Component", "width": "200px"},
        {"text": "Hosts", "width": "*"},
    ]
    assert details_table["rows"] == [
        ["shard01", "localhost:30018,localhost:30019,localhost:30020"],
        ["shard02", "localhost:30021,localhost:30022,localhost:30023"],
        ["configRepl", "localhost:30024"],
    ]
