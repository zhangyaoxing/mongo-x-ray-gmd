# mongo-x-ray-gmd

[![CI](https://github.com/zhangyaoxing/mongo-x-ray-gmd/actions/workflows/ci.yml/badge.svg)](https://github.com/zhangyaoxing/mongo-x-ray-gmd/actions/workflows/ci.yml)

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

## Development

Requires Python 3.10+, the [mongo-x-ray](https://github.com/mongodb-ps/ce-mongo-x-ray) core and the
[mongo-x-ray-hc](https://github.com/zhangyaoxing/mongo-x-ray-hc) plugin (gmd reuses its parsers and rules).

```bash
make unit-test   # run the unit tests
make lint        # ruff check + ruff format --check
make minify      # minify templates
```
