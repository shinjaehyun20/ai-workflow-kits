# Keepworking Hooks

Hooks are optional. Use them only when the runtime supports reliable event capture.

Recommended event families:

- worker start
- worker stop
- tool batch complete
- verification complete
- failure or stop failure

Every hook should write public-safe audit events and avoid secrets, local-only paths, or private project labels.
