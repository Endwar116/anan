# AnAn

**Making AI systems easier to understand, hand off, and govern.**
**讓 AI 系統更容易理解、交接與治理。**

AnAn works on the layer beneath AI applications: semantic state, protocol integrity, runtime governance, multi-model handoff, and semantic mapping.

AnAn 的工作位於 AI 應用的底層：語義狀態、協議完整性、運行治理、多模型交接，以及語義映射。

This is the public front door. Designed so a first-time reader can understand the shape of the work quickly, while a technical reviewer can see where the depth begins.

這是公開前門。設計上讓初次讀者能快速理解工作的輪廓，也讓技術審查者能看到深度從哪裡開始。

---

## The simple idea / 核心概念

When AI systems work together, they should not only pass messages. They should pass state, intent, inherited constraints, unresolved work, review conditions, and proof.

當 AI 系統協作時，不應只傳遞訊息。它們應該傳遞狀態、意圖、繼承的約束、未解決的工作、審查條件，以及證明。

Start with / 從這裡開始: [`simple/FIRST_LOOK.md`](simple/FIRST_LOOK.md)

---

## The technical spine / 技術脊線

```text
Semantic State → SIC-JS → SIC/T → AGR → Runtime Gates → IDDP / SLT → Semantic Mapping
語義狀態 → SIC-JS → SIC/T → AGR → 運行閘門 → IDDP / SLT → 語義映射
```

Read / 閱讀: [`00-front-door/TECHNICAL_SPINE.md`](00-front-door/TECHNICAL_SPINE.md)

---

## Five exhibits / 五個展示

| Exhibit / 展示 | What it means / 含義 |
|---|---|
| [Semantic State / 語義狀態](01-exhibits/01-semantic-state.md) | AI needs inspectable state, not only memory. / AI 需要可檢查的狀態，而不只是記憶。 |
| [Semantic Integrity / 語義完整性](01-exhibits/02-semantic-integrity.md) | Handoff needs protocol rules, not only summaries. / 交接需要協議規則，而不只是摘要。 |
| [Runtime Governance / 運行治理](01-exhibits/03-runtime-governance.md) | Governance should appear in runtime decisions. / 治理應體現在運行決策中。 |
| [Multi-LLM Coordination / 多模型協調](01-exhibits/04-multi-llm-coordination.md) | Multiple models need shared handoff records and disagreement surfaces. / 多個模型需要共享交接記錄和分歧面。 |
| [Semantic Mapping / 語義映射](01-exhibits/05-semantic-mapping.md) | Large artifact universes need navigable maps and closure states. / 大型構件宇宙需要可導航的地圖和閉合狀態。 |

Read the relationship map / 閱讀關係圖: [`01-exhibits/EXHIBIT_RELATION_MAP.md`](01-exhibits/EXHIBIT_RELATION_MAP.md)

---

## Proof objects / 證明物件

Small public-safe artifacts. Not full production traces — inspection windows into how the system thinks about state, governance, handoff, and mapping.

小型公開安全的構件。不是完整生產追蹤——是系統如何思考狀態、治理、交接與映射的檢視窗口。

| Object | Shows / 展示 |
|---|---|
| `sic_js_minimal_state.json` | Minimal SIC-JS state carrier. / 最小 SIC-JS 狀態載體。 |
| `runtime_gate_trace.json` | Runtime decision surface. / 運行決策介面。 |
| `multi_agent_routing_trace.json` | Public-safe multi-agent routing surface. / 公開安全的多代理路由介面。 |
| `semantic_mapping_sample.json` | Raw inventory to governed semantic map. / 從原始清單到治理語義地圖。 |
| `agr_decision_trace_sample.json` | Governance rule → decision → state change. / 治理規則→決策→狀態變化。 |

Read / 閱讀: [`02-proof-objects/PROOF_OBJECT_INDEX.md`](02-proof-objects/PROOF_OBJECT_INDEX.md)

---

## Deep technical route / 深度技術路線

For full technical review, use AN∞Node. This repository is the entry layer; AN∞Node is the deep technical universe.

完整技術審查請使用 AN∞Node。本倉庫是入口層；AN∞Node 是深度技術宇宙。

Route map / 路線圖: [`03-deep-routes/TECHNICAL_DEPTH_ROUTES.md`](03-deep-routes/TECHNICAL_DEPTH_ROUTES.md)

---

## Public boundary / 公開邊界

Does not publish: private operational logs, full Babel internals, private AGR rulebook, production routing topology, full SFT derivation chains, deployment-specific governance rules.

不發布：私有操作日誌、完整 Babel 內部、私有 AGR 規則手冊、生產路由拓撲、完整 SFT 推導鏈、特定部署的治理規則。

Read / 閱讀: [`04-boundaries/PUBLIC_BOUNDARY.md`](04-boundaries/PUBLIC_BOUNDARY.md)

---

## Status / 狀態

**Public entry repository. / 公開入口倉庫。**

---

## Runnable demo / 可運行示範

```bash
cd demo
python demo.py
```

No installation required. Three demos: false continuity detection, runtime gate, SIC-JS state carrier.
無需安裝。三個示範：假連續偵測、運行閘門、SIC-JS 狀態載體。
