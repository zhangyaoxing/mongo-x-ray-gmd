"""
Copyright (c) 2026 MongoDB Inc.

DISCLAIMER: THESE CODE SAMPLES ARE PROVIDED FOR EDUCATIONAL AND ILLUSTRATIVE PURPOSES ONLY,
TO DEMONSTRATE THE FUNCTIONALITY OF SPECIFIC MONGODB FEATURES.
THEY ARE NOT PRODUCTION-READY AND MAY LACK THE SECURITY HARDENING, ERROR HANDLING, AND TESTING REQUIRED FOR A LIVE ENVIRONMENT.
YOU ARE RESPONSIBLE FOR TESTING, VALIDATING, AND SECURING THIS CODE WITHIN YOUR OWN ENVIRONMENT BEFORE IMPLEMENTATION.
THIS MATERIAL IS PROVIDED "AS IS" WITHOUT WARRANTY OR LIABILITY.
"""

from mongo_x_ray.parsers.base_parser import BaseParser


class SHDetailsParser(BaseParser):
    def parse(self, data: dict, **kwargs) -> list:
        """
        Parse sharding detailed information data.

        Args:
            data (dict): Information about shards and config servers.

        Returns:
            list: The parsed sharding detailed information as a list of table items.
        """
        rows: list = []
        for shard in data["shards"]:
            sh_name = shard["_id"]
            hosts = shard["host"].split("/")[1]
            rows.append([sh_name, hosts])
        csrs: list[str] = data["csrs"].split("/")
        rows.append(csrs)

        details_table = {
            "type": "table",
            "caption": "Component Details - `shards/csrs`",
            "header": [
                {"text": "Component", "width": "200px"},
                {"text": "Hosts", "width": "*"},
            ],
            "rows": rows,
        }
        return [details_table]
