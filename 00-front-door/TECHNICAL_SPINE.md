# Technical Spine / 技術脊線

This repository is intentionally simple on the surface, but it is not a shallow portfolio.
本倉庫表面上刻意簡單，但並非膚淺的作品集。

The work has one technical spine / 工作有一條技術脊線:

```text
Semantic State / 語義狀態
  ↓ represented as / 表示為
SIC-JS state objects / SIC-JS 狀態物件
  ↓ governed by / 受治理於
SIC/T semantic integrity protocol / SIC/T 語義完整性協議
  ↓ constrained by / 受約束於
Babel and AGR governance rules / Babel 和 AGR 治理規則
  ↓ executed through / 通過執行
Runtime Gates: PASS / HALT / CAUTION / VERIFY_REQUIRED
運行閘門：通過 / 停止 / 警告 / 需要驗證
  ↓ transferred through / 通過傳輸
IDDP and SLT handoff records / IDDP 和 SLT 交接記錄
  ↓ organized across artifacts by / 通過組織構件
Semantic Mapping Governance / 語義映射治理
```

---

## What each layer does / 每層的功能

| Layer / 層 | Public meaning / 公開含義 | Technical role / 技術角色 |
|---|---|---|
| Semantic State / 語義狀態 | The system knows what state it is in. / 系統知道自己處於什麼狀態。 | VCE / ACV-style state representation and re-entry surfaces. |
| SIC-JS | The state has a carrier format. / 狀態有一個載體格式。 | JSON state object for entity, state, relation, event, intent, handoff, and boundary. |
| SIC/T | The handoff has integrity rules. / 交接有完整性規則。 | Protocol layer for continuity, failure modes, and fail-closed behavior. |
| AGR | Governance becomes decision rules. / 治理成為決策規則。 | Rulebook surface for inherited constraints, artifact status, closure, tombstone, and proof requirements. |
| Runtime Gates / 運行閘門 | Rules become behavior. / 規則成為行為。 | Gate decisions: PASS, HALT, CAUTION, VERIFY_REQUIRED. |
| IDDP / SLT | Multi-model handoff becomes inspectable. / 多模型交接可被檢查。 | Disagreement records, lineage transfer, receiver challenge, and handoff verification. |
| Semantic Mapping / 語義映射 | The surrounding archive becomes navigable. / 周圍的檔案變得可導航。 | Raw inventory → semantic snapshot → classified layer → governance state. |

---

## Why this matters / 為何重要

Most AI systems pass text and hope the next model understands the same thing.
大多數 AI 系統傳遞文字，希望下一個模型理解相同的事情。

This work asks for a stronger operating layer / 這項工作要求一個更強的操作層:

> pass state, preserve constraints, expose drift, require proof, and leave a reviewable trail.
> 傳遞狀態、保留約束、暴露漂移、要求證明，並留下可審查的軌跡。

For the full technical repository / 完整技術倉庫: follow [`03-deep-routes/TECHNICAL_DEPTH_ROUTES.md`](../03-deep-routes/TECHNICAL_DEPTH_ROUTES.md).
