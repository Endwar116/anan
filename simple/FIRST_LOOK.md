# First Look / 初覽

This repository is the front door to AnAn's technical work.
本倉庫是 AnAn 技術工作的前門。

---

The simplest way to understand it / 最簡單的理解方式:

> When AI systems pass work to each other, they should not only pass text. They should pass state, intent, rules, boundaries, and proof.
>
> 當 AI 系統互相交接工作時，不應只傳遞文字。它們應該傳遞狀態、意圖、規則、邊界，以及證明。

Imagine several people building a complex model city together. If one person leaves and another arrives, the newcomer needs more than notes. They need to know what the team is building, what must not be changed, what is unfinished, what has already been checked, and when to stop for review.

想像幾個人一起建造一座複雜的模型城市。如果一個人離開、另一個人到來，新來者需要的不只是筆記。他們需要知道團隊在建造什麼、什麼不能改變、什麼尚未完成、什麼已被檢查，以及何時應停下來審查。

AnAn's work turns that idea into a technical system for multi-LLM workflows.
AnAn 的工作將這個概念轉化為多 LLM 工作流的技術系統。

---

## The five ideas / 五個概念

1. **Semantic State / 語義狀態** — what the AI is currently holding as meaning. / AI 當前持有的語義狀態。
2. **Semantic Integrity / 語義完整性** — rules for preserving that meaning across handoff. / 在交接過程中保持語義的規則。
3. **Runtime Governance / 運行治理** — gates that decide when to continue, stop, or review. / 決定何時繼續、停止或審查的閘門。
4. **Multi-LLM Coordination / 多模型協調** — shared records for multiple models working together. / 多個模型協作的共享記錄。
5. **Semantic Mapping / 語義映射** — turning messy technical archives into navigable maps. / 將雜亂的技術檔案轉化為可導航的地圖。

---

This is the simple layer. The deeper routes are in `for-experts/` and `03-deep-routes/`.
這是簡單層。更深的路線在 `for-experts/` 和 `03-deep-routes/`。
