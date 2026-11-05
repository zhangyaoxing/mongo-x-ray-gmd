# mongo-x-ray-gmd — Release Notes

## 2.1.2

Version alignment with the x-ray 2.1.2 release — one configuration key is added, the plugin's own behaviour is unchanged.

### Changed
- **Snapshot history window threshold is configurable**: gmd reuses the health check rule, which now reads `min_snapshot_history_window_seconds` from `gmd.item_config.ServerStatusItem` (default `5`) instead of a constant.

## 2.1.1

Dependency and automation release — the plugin's own behaviour is unchanged.

### Dependencies
- Build: `setuptools` 84.0.0 → 84.2.1 ([`GHSA-xmj3-9gf7-h52w`](https://github.com/advisories/GHSA-xmj3-9gf7-h52w), low — Windows path escape via `namespace_packages.txt` during a legacy wheel install).

### Automation
- **Dependabot auto-merge repaired**: the workflow counted its own in-progress `auto-merge` check when waiting for "every check to pass", so it always timed out and updates stayed open. It now ignores its own check, retries a merge that lost a race with a sibling update, requests a rebase when the branch conflicts, and tolerates branches modified by hand.
- Repository labels `dependencies`, `python` and `github-actions` added, so Dependabot can tag its pull requests.

The getMongoData analysis plugin for x-ray.

## 2.1.0

### Added
- **Copyable values**: important table contents are wrapped in backticks, so the new report copy icons can copy them with one click.
- **Risk scan logging**: a message is logged before the risk register vector search, so a long-running enrichment is visible in the output.

### Fixed
- **Sharded collection rows**: a `<br>` is now inserted between the namespace and the shard key, and after values that are followed by shard distributions — the table cells no longer run together.

### Dependencies
- Requires `mongo-x-ray-hc>=2.1.0`: the healthcheck plugin owns the shared issue catalog (`mongo_x_ray_hc.issues`) and hc 2.0.0 imports `mongo_x_ray.issues`, which core 2.1.0 no longer ships.

### Development
- **CI now runs on pull requests** as well as on pushes to `main`, so a dependency bump is linted and tested before it can land.
- **Dependabot** is enabled for `pip` and GitHub Actions (weekly). Patch and minor updates merge automatically once every check is green, as do major updates of the CI actions and the build/lint/test tooling; a major update of a runtime dependency (`mongo-x-ray`, `mongo-x-ray-hc`) is left for review, and a failing or missing check leaves the pull request open instead of merging.
- **Tooling bumped**: `setuptools` 83.0.0 → 84.0.0, `actions/checkout` v4 → v7, `actions/setup-python` v5 → v7.

### Inherited from core (applies to every gmd report)
- **Copy icons** for inline code, code blocks (top-right icon instead of the "Copy" text) and table `<pre>` blocks, preserving line breaks and indentation when copied.
- **Output folder naming**: report folders are prefixed with the plugin name (`gmd-default-<timestamp>`, `gmd-<hostname>-default-<timestamp>`), including with `--discover`.

## 2.0.0

The getMongoData analysis was split out of the core into the `mongo-x-ray-gmd` plugin, reusing the health-check rules and the shared `mongo_x_ray` core. It added replica-set health checks (journaling, chained replication, write concern), server parameter checks (snapshot window, SBE, FTDC configuration), security checks (TLS protocols), optional risk-register integration with a Known Risks summary column, and CI/CodeQL/PyPI publishing.
