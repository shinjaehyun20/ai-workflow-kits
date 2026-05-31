# OpenClaw Provider Notes

Treat OpenClaw as a provider example, not a first-class runtime in this repository.

## Recommended Flow

1. Map a static avatar first.
2. Keep the shared `companion-state.json` file separate from the runtime control plane.
3. Add animated rendering only after the avatar path is stable.

## Mode

`avatar_plus_companion`

## Notes

- The shared bundle can stay the same as long as the runtime-specific bridge writes allowed states.
- Avoid claiming native sprite-sheet support unless it is verified in the target OpenClaw surface.
