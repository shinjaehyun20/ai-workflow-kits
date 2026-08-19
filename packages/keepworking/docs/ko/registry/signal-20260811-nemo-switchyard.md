---
id: signal-20260811-nemo-switchyard
title: NVIDIA NeMo Switchyard agent-routing signal
source_url: https://developer.nvidia.com/blog/route-ai-agent-workloads-across-models-with-nvidia-nemo-switchyard
captured_at: "2026-08-19"
signal_tags:
  - tech_signal
status: observed
next_review: "2026-11-19"
---

# NVIDIA NeMo Switchyard agent-routing signal

## Summary

NVIDIA describes a provider-neutral routing layer that selects models from capability, cost, latency, system, tool, and error signals. Its stage and escalation patterns can inform future agent control-plane research.

## Applicability

Keepworking already defines an evidence-first execution loop: goal → plan → execute → verify → repair → re-verify → close. Switchyard is not this package's behavior or a promised feature; it is an observed reference for a future, separately verified routing layer that could operate beside an agent loop.

## Action units

None. This signal remains observed until a provider-neutral routing contract, workload evaluation, quality threshold, and verifier are defined.

## Evidence refs

- `../knowledge-registry-format.md`
- `../benchmark-signal-tags.md`
- `../../README.md`

## Risk

- External benchmark outcomes are workload- and model-pair-specific.
- No Keepworking workload evaluation or automatic routing implementation has been performed.
