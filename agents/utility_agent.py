import json
import re

from llms.ollama_llm import get_llm


class UtilityAgent:
    def __init__(self, debug: bool = False):
        self.llm = get_llm()
        self.debug = debug

    def run_task(self, chunks, task_type):
        context = "\n".join([chunk.text for chunk in chunks])

        if task_type == "summary":
            prompt = f"Summarize the following text:\n{context}"
            result = self.llm.generate([prompt])
            return result.generations[0][0].text if result.generations else ""

        elif task_type == "translate":
            prompt = f"Translate the following text to Persian:\n{context}"
            result = self.llm.generate([prompt])
            return result.generations[0][0].text if result.generations else ""

        elif task_type == "checklist":
            prompt = f"""
You are given CONTEXT text. Create a checklist from it.

Return ONLY valid JSON (no markdown, no backticks, no explanations).
Return a JSON array (a list) of objects with keys:
- "task": string
- "done": boolean

Create EXACTLY 5 tasks based ONLY on the context.

CONTEXT:
{context}

OUTPUT (JSON array only):
""".strip()

            result = self.llm.generate([prompt])
            raw = result.generations[0][0].text if result.generations else "[]"
            raw = raw.strip()

            if self.debug:
                print("\n[DEBUG checklist raw]\n", raw, "\n[/DEBUG]\n")

            # 1) remove code fence if model returns ```json ... ```
            raw = re.sub(r"^```(?:json)?\s*", "", raw, flags=re.IGNORECASE)
            raw = re.sub(r"\s*```$", "", raw)

            # 2) extract first JSON array from the text (ignore explanations)
            m = re.search(r"\[[\s\S]*\]", raw)
            candidate = m.group(0) if m else "[]"

            # 3) parse with small repair attempts
            data = []
            try:
                parsed = json.loads(candidate)
                data = parsed if isinstance(parsed, list) else []
            except json.JSONDecodeError:
                # common repair: trailing "]]"
                candidate2 = candidate.replace("]]", "]")
                try:
                    parsed = json.loads(candidate2)
                    data = parsed if isinstance(parsed, list) else []
                except Exception:
                    data = []

            # 4) normalize + enforce EXACTLY 5 tasks
            # keep only dict items with "task"/"done"
            cleaned = []
            for item in data:
                if isinstance(item, dict) and "task" in item:
                    cleaned.append({
                        "task": str(item.get("task", "")).strip(),
                        "done": bool(item.get("done", False)),
                    })

            # fill if fewer than 5
            if len(cleaned) < 5:
                extras = [
                    {"task": "Review each section separately", "done": False},
                    {"task": "Extract key points from each section", "done": False},
                    {"task": "Answer questions using retrieved sections", "done": False},
                    {"task": "Add citations (source#chunk_id) to answers", "done": False},
                    {"task": "Write tests for chunking and retrieval", "done": False},
                ]
                for t in extras:
                    if len(cleaned) >= 5:
                        break
                    cleaned.append(t)

            # trim if more than 5
            return cleaned[:5]

        else:
            return ""
