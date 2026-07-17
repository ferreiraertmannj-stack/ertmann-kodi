# Versioning

The Ertmann Kodi Platform follows [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html).

## Format

```text
MAJOR.MINOR.PATCH
```

- `MAJOR` changes when a public contract changes incompatibly.
- `MINOR` changes when a compatible capability is added.
- `PATCH` changes when a compatible defect is corrected.

Pre-release identifiers, such as `1.0.0-beta.1`, may be used for testing and
must not be treated as stable releases.

## Kodi add-ons

For each published add-on, the version in `addon.xml`, the ZIP filename, the
entry in `addons.xml`, the Git tag, and the changelog release heading must
match exactly.

Repository metadata uses the same versioning policy. Increment it only when
the repository add-on's public manifest or metadata changes.

## Git tags and releases

Release tags use `vMAJOR.MINOR.PATCH` and should be signed. A release is
created only after review, validation, changelog update, and confirmation that
the target Kodi compatibility remains supported.
