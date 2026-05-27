# Keepworking Hooks

Hooks are optional. Use them only when the runtime supports reliable event capture.

## Recommended event families

- worker start (`SubagentStart`)
- worker stop (`SubagentStop`)
- tool batch complete (`PostToolBatch`)
- verification complete
- failure or stop failure (`StopFailure`)

Every hook should write public-safe audit events and avoid secrets, local-only paths, or private project labels.

## Example: event log hook

A minimal Python hook that records keepworking worker lifecycle events:

```python
import json, os, pathlib, sys, time

EVENTS_PATH = pathlib.Path("runtime/audit/keepworking/events.jsonl")
PREFIX = "keepworking-"

def main():
    event_type = sys.argv[1] if len(sys.argv) > 1 else "unknown"
    raw = sys.stdin.buffer.read().decode("utf-8", errors="replace")
    payload = json.loads(raw) if raw.strip() else {}

    agent_type = payload.get("agent_type") or ""
    if not agent_type.startswith(PREFIX):
        sys.exit(0)

    record = {
        "ts": int(time.time()),
        "event": event_type,
        "agent_type": agent_type,
        "session_id": payload.get("session_id"),
        "task_id": payload.get("task_id"),
    }

    EVENTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(EVENTS_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    try:
        main()
    except Exception:
        sys.exit(0)
```

Register in `.claude/settings.json`:

```json
{
  "hooks": {
    "SubagentStart": [{
      "hooks": [{
        "type": "command",
        "command": "python hooks/keepworking-event-log.py subagent_start",
        "async": true,
        "timeout": 5
      }]
    }],
    "SubagentStop": [{
      "hooks": [{
        "type": "command",
        "command": "python hooks/keepworking-event-log.py subagent_stop",
        "async": true,
        "timeout": 5
      }]
    }]
  }
}
```

## Verified behavior

- `SubagentStart` fires when a keepworking worker is spawned
- `SubagentStop` fires when the worker completes
- The hook filters by `agent_type` prefix so non-keepworking agents are ignored
- `async: true` prevents the hook from blocking the main chat
