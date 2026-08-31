# mongo-x-ray-gmd

[![CI](https://github.com/zhangyaoxing/mongo-x-ray-gmd/actions/workflows/ci.yml/badge.svg)](https://github.com/zhangyaoxing/mongo-x-ray-gmd/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/mongo-x-ray-gmd.svg)](https://pypi.org/project/mongo-x-ray-gmd/)

getMongoData analysis plugin for [x-ray](https://github.com/mongodb-ps/ce-mongo-x-ray).

## Install

```bash
pip install mongo-x-ray mongo-x-ray-hc mongo-x-ray-gmd
```

## Usage

```bash
x-ray gmd /path/to/getMongoData-output.json
x-ray gmd /path/to/getMongoData-output.json -f html -o /path/to/output/
```

## Compatibility

Supports MongoDB 5.0 and above on all topologies:

| Replica Set | Sharded Cluster | Standalone |
| :---------: | :-------------: | :--------: |
| ✅ | ✅ | ✅ |

## Parameters

```bash
x-ray gmd [-h] [-s CHECKSET] [-o OUTPUT] [-f {markdown,html,pdf}] [--no-browser]
          gmd_file
```

| Argument | Description | Default |
| --- | --- | --- |
| `gmd_file` | Path to the getMongoData output JSON file. | required |
| `-s, --checkset` | Checkset to run. | `default` |
| `-o, --output` | Output folder path. | `output/` |
| `-f, --format` | Output format: `markdown`, `html` or `pdf` (PDF also keeps Markdown and HTML). | `html` |
| `--no-browser` | Do not open the generated report in the browser. | `false` |

## Analysis Items

| Item | Purpose |
| --- | --- |
| `SummaryItem` | Overall summary of the getMongoData output. |
| `BuildInfoItem` | Build information (reuses the healthcheck build info parser and version EOL rule). |
| `CollInfoItem` | Collection statistics: sizes and fragmentation. |
| `DBItem` | Database-level information. |
| `HostInfoItem` | Host filesystem type, NUMA settings and host properties. |
| `IndexInfoItem` | Index information. |
| `RSInfoItem` | Replica set topology, oplog window and status. |
| `SecurityItem` | Security posture. |
| `ServerStatusItem` | Cache, connections and query targeting status. |
| `SHInfoItem` | Sharding architecture and shard details. |

## Development

Requires Python 3.10+, MongoDB 5.0 or later, the [mongo-x-ray](https://github.com/mongodb-ps/ce-mongo-x-ray) core and the
[mongo-x-ray-hc](https://github.com/zhangyaoxing/mongo-x-ray-hc) plugin (gmd reuses its parsers and rules).

```bash
make unit-test   # run the unit tests
make lint        # ruff check + ruff format --check
make minify      # minify templates
```
