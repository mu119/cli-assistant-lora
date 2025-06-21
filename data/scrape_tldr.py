import requests
import os
import json

os.makedirs("data", exist_ok=True)

topics = [
    "git", "bash", "tar", "grep", "python", "npm", "chmod", "find", "curl", "ls",
    "cd", "mv", "cp", "rm", "mkdir", "cat", "head", "tail", "touch", "ps"
]

qa_pairs = []

for topic in topics:
    url = f"https://raw.githubusercontent.com/tldr-pages/tldr/main/pages/common/{topic}.md"
    print(f"Fetching: {url}")
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code != 200:
            print(f" Not found: {topic}")
            continue
        lines = resp.text.splitlines()
        question, answer = "", ""
        for i in range(len(lines)):
            line = lines[i].strip()
            if line.startswith("- "):  # description
                question = "How to " + line[2:].strip("?").strip().lower()
            elif line.startswith("`") and line.endswith("`"):  
                answer = "Use the command: " + line.strip("`")
                if question and answer:
                    qa_pairs.append({
                        "question": question,
                        "answer": answer
                    })
                    question, answer = "", ""
    except Exception as e:
        print("Error:", e)

with open("data/cli_qa_raw.json", "w") as f:
    json.dump(qa_pairs, f, indent=2)

print(f"\n DONE! Total Q&A collected: {len(qa_pairs)}")
