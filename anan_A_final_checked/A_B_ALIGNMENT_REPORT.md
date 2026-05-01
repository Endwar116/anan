# A–B Alignment Report / A–B 對齊報告

**A repository** (this repo / 本倉庫): public showroom / bilingual entrance
**B repository** (AN∞Node): deep technical reviewer repository / 深度技術審查倉庫

---

## Mapping / 對應關係

| A Exhibit / A 展示 | A Entry Point / A 入口 | B Directory / B 目錄 | Notes / 備註 |
|---|---|---|---|
| Semantic State / 語義狀態 | `01-exhibits/01-semantic-state.md` | `06-vce/` | State representation, coordinate system, induction surfaces |
| Semantic Integrity / 語義完整性 | `01-exhibits/02-semantic-integrity.md` | `02-protocols/` (sic-js, sic-t, babel) | SIC-JS format, SIC/T protocol, Babel governance |
| Runtime Governance / 運行治理 | `01-exhibits/03-runtime-governance.md` | `03-runtime/` + `07-agr-governance-runtime/` | Encoding gate, integrity gate, AGR rulebook surface |
| Multi-LLM Coordination / 多模型協調 | `01-exhibits/04-multi-llm-coordination.md` | `04-multi-agent/` (IDDP, SLT) | Disagreement records, handoff verification, receiver challenge |
| Semantic Mapping / 語義映射 | `01-exhibits/05-semantic-mapping.md` | `05-semantic-mapping/` | Raw inventory → classified → governance state |
| Proof Objects / 證明物件 | `02-proof-objects/inspectable/` | `09-evidence/` + `EVIDENCE_STATUS_MATRIX.md` | Public-safe samples → full evidence matrix with claim labels |

---

## What A does that B does not / A 做的而 B 不做的

- Bilingual presentation (EN + ZH) / 雙語呈現（英文 + 中文）
- Simple first-look for non-technical readers / 給非技術讀者的簡單初覽
- Runnable demo without installation / 無需安裝的可運行示範
- Bounded proof objects with explicit non-claims / 有明確非聲稱的有界證明物件
- Single-page overview of the entire technical spine / 整個技術脊線的單頁概覽

---

## What B does that A does not / B 做的而 A 不做的

- Complete protocol specifications (SIC-JS, SIC/T, IDDP, SLT, AGR) / 完整協議規格
- Runnable sic-toolkit with 416 passing tests / 416 測試通過的可運行 sic-toolkit
- Evidence matrix with labeled claims (E_LOCAL / QUALITATIVE_ONLY / BENCHMARK_PENDING) / 帶標籤聲稱的證據矩陣
- Theory layer (SFT, Ψ_s field, proof sketches) / 理論層（SFT、Ψ_s 場、證明草圖）
- VCE state coordinate system documentation / VCE 狀態座標系統文檔
- Full CHANGELOG and CLEAN_RELEASE_NOTES / 完整的 CHANGELOG 和清潔發布說明
- CONTRIBUTING.md and SECURITY.md / 貢獻指南和安全政策

---

## How to read both together / 如何一起閱讀

1. Start in A / 從 A 開始: read README + TECHNICAL_SPINE + five exhibits (10 min)
2. Inspect A proof objects / 檢查 A 的證明物件: five JSON samples (5 min)
3. Run A demo / 運行 A 的示範: `cd demo && python demo.py` (2 min)
4. Continue to B / 繼續到 B: follow `03-deep-routes/TECHNICAL_DEPTH_ROUTES.md` to the relevant AN∞Node directories

---

*A is the door. B is the room.*
*A 是門。B 是房間。*
