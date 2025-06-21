import json
import os

INPUT_FILE = "data/cli_qa_raw.json"
OUTPUT_FILE = "data/cli_qa.json"

if not os.path.exists(INPUT_FILE):
    print(f"File not found: {INPUT_FILE}")
    exit()

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

cleaned = []
seen_questions = set()

for item in data:
    question = item.get("question", "").strip()
    answer = item.get("answer", "").strip()

    if not question or not answer:
        continue

    question_lower = question.lower()
    if question_lower in seen_questions:
        continue

    cleaned.append({
        "question": question,
        "answer": answer
    })
    seen_questions.add(question_lower)

print(f"Total cleaned Q&A: {len(cleaned)}")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(cleaned, f, indent=2, ensure_ascii=False)

print(f"Final saved to: {OUTPUT_FILE}")
