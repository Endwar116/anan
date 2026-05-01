#!/usr/bin/env python3
"""
AnAn / AN∞Node — Runnable Demo
================================

This script demonstrates two core concepts:

  1. False continuity detection via SLT (Semantic Lineage Transfer)
  2. Runtime gate decision via integrity gate

No external dependencies. Python 3.8+ stdlib only.

Run:
    python demo.py
"""

import json
import pathlib
import sys

RESET  = "\033[0m"
RED    = "\033[31m"
YELLOW = "\033[33m"
GREEN  = "\033[32m"
BOLD   = "\033[1m"
CYAN   = "\033[36m"
DIM    = "\033[2m"


# ── helpers ──────────────────────────────────────────────────────────────────

def banner(title: str) -> None:
    width = 64
    print()
    print(BOLD + CYAN + "=" * width + RESET)
    print(BOLD + CYAN + f"  {title}" + RESET)
    print(BOLD + CYAN + "=" * width + RESET)
    print()


def load(rel: str) -> dict:
    p = pathlib.Path(__file__).parent / rel
    return json.loads(p.read_text())


# ── Demo 1: SLT false-continuity detection ───────────────────────────────────

def demo_slt() -> None:
    banner("Demo 1 — SLT: Detecting False Continuity")

    print(DIM + "Scenario: an AI agent finishes a task and hands off to a successor.\n" + RESET)

    # --- Condition A: no SLT ---
    print(BOLD + "Condition A — plain summary handoff (no SLT)" + RESET)
    failure = load("without_slt_failure_case.json")
    state = failure["receiver_state"]
    print(f"  task intent lost      : {RED}{state['task_intent_lost']}{RESET}")
    print(f"  constraints lost      : {RED}{state['constraint_lost']}{RESET}")
    print(f"  failure history lost  : {RED}{state['failure_history_lost']}{RESET}")
    print(f"  action boundary lost  : {RED}{state['action_boundary_lost']}{RESET}")
    print(f"  outcome               : {RED}{failure['outcome']}{RESET}")
    print()

    # --- Condition B: with SLT ---
    print(BOLD + "Condition B — SLT handoff with lineage verification" + RESET)
    detection = load("with_slt_detection_case.json")
    expected  = detection["expected_lineage_items"]
    claimed   = detection["receiver_claimed_items"]
    missing   = detection["missing_items_detected"]

    print(f"  expected lineage      : {expected}")
    print(f"  receiver claimed      : {claimed}")
    print(f"  {YELLOW}missing detected{RESET}      : {YELLOW}{missing}{RESET}")
    print(f"  gate decision         : {YELLOW}{detection['decision']}{RESET}")
    print(f"  action                : {GREEN}{detection['action']}{RESET}")
    print()

    print(DIM + "What SLT adds over a plain summary:" + RESET)
    print("  · Structured lineage record (intent, constraints, failure history)")
    print("  · Receiver challenge — successor must prove it inherited the state")
    print("  · Action gating — execution blocked until lineage is verified")
    print()


# ── Demo 2: Runtime integrity gate ───────────────────────────────────────────

GATE_RULES = [
    {"id": "R-SQL-RESTRICTED", "pattern": "DROP TABLE",
     "risk": "CRITICAL", "decision": "HALT"},
    {"id": "R-EXTERNAL-SEND",  "pattern": "send_email",
     "risk": "HIGH",     "decision": "CAUTION"},
    {"id": "R-READ-ONLY",      "pattern": "SELECT",
     "risk": "LOW",      "decision": "PASS"},
]


def runtime_gate(input_text: str) -> dict:
    """Minimal rule-based integrity gate (no ML, no external deps)."""
    for rule in GATE_RULES:
        if rule["pattern"].lower() in input_text.lower():
            return {
                "input":        input_text,
                "matched_rule": rule["id"],
                "risk_signal":  rule["risk"],
                "decision":     rule["decision"],
                "reason":       f"Pattern '{rule['pattern']}' matched rule {rule['id']}.",
            }
    return {
        "input":    input_text,
        "decision": "PASS",
        "reason":   "No rule matched.",
    }


def print_gate_result(result: dict) -> None:
    colour = {"HALT": RED, "CAUTION": YELLOW, "PASS": GREEN}.get(
        result["decision"], RESET
    )
    print(f"  input    : {result['input']!r}")
    if "matched_rule" in result:
        print(f"  rule     : {result['matched_rule']}")
        print(f"  risk     : {result['risk_signal']}")
    print(f"  decision : {colour}{BOLD}{result['decision']}{RESET}")
    print(f"  reason   : {result['reason']}")
    print()


def demo_gate() -> None:
    banner("Demo 2 — Runtime Integrity Gate")

    print(DIM + "The gate evaluates each agent action before execution.\n" + RESET)

    cases = [
        "DROP TABLE users;",
        "send_email(to='external@partner.com', body=summary)",
        "SELECT * FROM audit_log WHERE session_id = 42;",
    ]

    for c in cases:
        print_gate_result(runtime_gate(c))

    # also load the proof object from an_node
    try:
        proof = load("halt_case.json")
        print(DIM + "Proof object (from evidence archive):" + RESET)
        print(f"  input    : {proof['input']!r}")
        print(f"  decision : {RED}{BOLD}{proof['decision']}{RESET}")
        print(f"  reason   : {proof['reason']}")
        print()
    except FileNotFoundError:
        pass


# ── Demo 3: SIC-JS minimal state ─────────────────────────────────────────────

def demo_sic_js() -> None:
    banner("Demo 3 — SIC-JS: Inspectable State Carrier")

    try:
        state = load("sic_js_minimal_state.json")
    except FileNotFoundError:
        print(RED + "  proof object not found (run from anan_A/anan/)" + RESET)
        return

    print(DIM + "A SIC-JS packet encodes who is acting, what they are doing, and why.\n" + RESET)
    for key, val in state.items():
        print(f"  {key:<14}: {json.dumps(val, ensure_ascii=False)}")
    print()
    print(DIM + "Machine-readable. Human-inspectable. Transfer-safe." + RESET)
    print()


# ── main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    print()
    print(BOLD + "AnAn — Semantic State & Coordination Infrastructure" + RESET)
    print(DIM  + "Runnable demo  ·  stdlib only  ·  no installation required" + RESET)

    demo_slt()
    demo_gate()
    demo_sic_js()

    print(BOLD + GREEN + "All demos completed." + RESET)
    print()
    print(DIM + "For full technical depth: AN∞Node / an-node" + RESET)
    print()


if __name__ == "__main__":
    main()
