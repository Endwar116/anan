# Runnable Demo

Demonstrates two core concepts from AnAn's semantic state infrastructure:

1. **False continuity detection** — SLT catches what a plain summary misses.
2. **Runtime integrity gate** — Three-tier gate decision (PASS / CAUTION / HALT).
3. **SIC-JS state carrier** — Inspectable structured state packet.

## Run

```bash
cd demo
python demo.py
```

No installation required. Python 3.8+ stdlib only.

## Evidence used

| File | Source |
|---|---|
| `without_slt_failure_case.json` | AN∞Node `09-evidence/slt/` |
| `with_slt_detection_case.json` | AN∞Node `09-evidence/slt/` |
| `halt_case.json` | AN∞Node `09-evidence/runtime-governance/` |
| `sic_js_minimal_state.json` | AN∞Node `02-proof-objects/inspectable/` |

Full technical depth: AN∞Node / an-node. See ../03-deep-routes/TECHNICAL_DEPTH_ROUTES.md.

## Boundary / 邊界說明

This demo is a public-safe simplified demonstration. It does not validate the full SIC/T, AGR, SLT, or runtime governance stack. Full technical evidence belongs in AN∞Node.

這個 demo 是公開安全的簡化展示，不代表完整 SIC/T、AGR、SLT 或運行治理系統已被完整驗證。完整技術證據位於 AN∞Node。
