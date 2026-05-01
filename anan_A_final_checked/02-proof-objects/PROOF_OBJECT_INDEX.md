# Proof Object Index / 證明物件索引

This folder contains small public-safe proof objects.
本資料夾包含小型公開安全的證明物件。

They are not full production traces. They are inspectable surfaces that show how the system thinks about state, governance, handoff, and mapping.
它們不是完整的生產追蹤記錄。它們是可檢查的介面，展示系統如何思考狀態、治理、交接與映射。

| Proof object | Technical line / 技術線 | Shows / 展示 | Does not prove / 不證明 | Deep route / 深度路線 |
|---|---|---|---|---|
| `sic_js_minimal_state.json` | Semantic Integrity / 語義完整性 | Minimal SIC-JS state carrier. / 最小 SIC-JS 狀態載體。 | Full runtime behavior or private state graph. / 完整運行行為或私有狀態圖。 | AN∞Node → SIC-JS |
| `runtime_gate_trace.json` | Runtime Governance / 運行治理 | A PASS/HALT-style decision surface. / PASS/HALT 式決策介面。 | Production policy or universal safety. / 生產策略或通用安全性。 | AN∞Node → Runtime Governance |
| `multi_agent_routing_trace.json` | Multi-LLM Coordination / 多模型協調 | Public-safe handoff and routing structure. / 公開安全的交接和路由結構。 | Private agent logs or full topology. / 私有代理日誌或完整拓撲。 | AN∞Node → IDDP / SLT |
| `semantic_mapping_sample.json` | Semantic Mapping / 語義映射 | Raw inventory → classified layer → governance state. / 原始清單→分類層→治理狀態。 | Full archive interpretation. / 完整檔案解讀。 | AN∞Node → Semantic Mapping |
| `agr_decision_trace_sample.json` | AGR Governance Runtime / AGR 治理運行 | Governance rule → decision → state change. / 治理規則→決策→狀態變化。 | Full private AGR rulebook. / 完整私有 AGR 規則手冊。 | AN∞Node → AGR |

---

## Evidence standard / 證據標準

A proof object is useful when it is small enough to inspect, clear about what it demonstrates, explicit about what it does not demonstrate, and connected to a deeper technical route.

一個證明物件有用的條件：足夠小可以檢查、清楚說明它展示什麼、明確說明它不展示什麼，以及連結到更深的技術路線。

This repository uses proof objects to avoid empty claims. The deeper AN∞Node repository is responsible for complete evidence matrices, claim labels, test reports, and implementation details.

本倉庫使用證明物件來避免空洞的聲稱。更深的 AN∞Node 倉庫負責完整的證據矩陣、聲稱標籤、測試報告和實現細節。
