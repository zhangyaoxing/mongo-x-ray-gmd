# mongo-x-ray-gmd — Release Notes

The getMongoData analysis plugin for x-ray (39 commits since its first commit on 2026-08-23).

## Highlights

- **Initial plugin extraction (v2.0.0)** — split the getMongoData analysis out of the core into the `mongo-x-ray-gmd` plugin, with the health-check rules and core imported as `mongo_x_ray_hc` / `mongo_x_ray`.
- **Replica set health checks** — new alerts for `writeConcernMajorityJournalDefault: false`, chained replication, non-default write concern (`w` ≠ majority) and a zero write-concern timeout.
- **Server parameter checks** — new alerts for a high `minSnapshotHistoryWindowInSeconds`, SBE enabled on MongoDB 6.0/7.0, and FTDC configuration issues.
- **Security checks** — new alerts for insecure (TLS1_0/TLS1_1) or unrecognizable disabled TLS protocols.
- **Risk register integration** — the risk register (`mongo_x_ray_risk`) is now an optional plugin; the "Known Risks" summary column is hidden when no risk register is detected.
- **Report fixes** — known-risk tooltips keep multi-line descriptions on a single table line (`<br>`), fixing broken markdown tables.

## Changes by area

**Features**
- Alert when `writeConcernMajorityJournalDefault` is `false` (durability risk)
- Alert when chained replication is possible (`chainingAllowed` or override parameter)
- Alert when the default write concern is not `majority`, or its `wtimeout` is 0
- Alert on high `minSnapshotHistoryWindowInSeconds` (MongoDB 5.0+, recommended 5s)
- Alert when SBE is enabled on MongoDB 6.0/7.0 (`internalQueryForceClassicEngine` / `internalQueryFrameworkControl`)
- Alert on FTDC issues: `diagnosticDataCollectionEnabled=false`, samples-per-chunk below 300
- Alert on insecure or unrecognizable TLS protocols in `net.tls.disabledProtocols`
- Declare the plugin distribution for `x-ray <name> --version`

**Fixes**
- Keep risk tooltips on one line in markdown tables

**Refactors**
- Import core as `mongo_x_ray`; health-check rules as `mongo_x_ray_hc`; package renamed to `mongo_x_ray_gmd`
- Risk register treated as an optional plugin

**CI / Tooling**
- GitHub Actions CI with ruff lint target; CodeQL enabled
- Publish to (Test)PyPI on release via trusted publishing
- VSCode ruff/pyright config; explicit direct dependencies; deterministic isort; unified 2026 copyright headers

**Docs**
- README rewrite: usage, command parameters, analysis items, MongoDB 5.0+ compatibility, PyPI badge
