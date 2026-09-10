# mongo-x-ray-gmd — Release Notes

The getMongoData analysis plugin for x-ray.

## 2.1.0

### Added
- **Copyable values**: important table contents are wrapped in backticks, so the new report copy icons can copy them with one click.
- **Risk scan logging**: a message is logged before the risk register vector search, so a long-running enrichment is visible in the output.

### Fixed
- **Sharded collection rows**: a `<br>` is now inserted between the namespace and the shard key, and after values that are followed by shard distributions — the table cells no longer run together.

### Inherited from core (applies to every gmd report)
- **Copy icons** for inline code, code blocks (top-right icon instead of the "Copy" text) and table `<pre>` blocks, preserving line breaks and indentation when copied.
- **Output folder naming**: report folders are prefixed with the plugin name (`gmd-default-<timestamp>`, `gmd-<hostname>-default-<timestamp>`), including with `--discover`.

## 2.0.0

The getMongoData analysis was split out of the core into the `mongo-x-ray-gmd` plugin, reusing the health-check rules and the shared `mongo_x_ray` core. It added replica-set health checks (journaling, chained replication, write concern), server parameter checks (snapshot window, SBE, FTDC configuration), security checks (TLS protocols), optional risk-register integration with a Known Risks summary column, and CI/CodeQL/PyPI publishing.
