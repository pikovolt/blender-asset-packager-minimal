# Result: 000_scan_validate_plan

Implemented in the minimal sample.

## Implemented

- `scan`: creates a deterministic manifest from a file tree
- `validate`: validates schema version, source root, duplicate paths, and unsafe relative paths
- `plan-export`: creates a dry-run export plan only
- `fast` validation profile
- boundary guard for forbidden application behavior tokens

## Not implemented

- actual export/copy
- Blender `bpy` integration
- real `.blend` parsing
- extension-specific content validation
