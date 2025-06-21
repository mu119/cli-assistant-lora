# Report: Terminal CLI Assistant

##  Goal
Build a terminal assistant that understands natural language commands and returns short, correct shell commands — by fine-tuning a lightweight language model using LoRA.

---

##  Dataset

- Format:  
  `{ "question": "How to delete .tmp files?", "answer": "find . -name '*.tmp' -delete" }`
- Size: ~150 Q&A examples
- Source: Manually created and cleaned by Mukesh
- Saved in: `data/cli_qa.json`

---

##  Model & Training Details

- Base model: `TinyLlama/TinyLlama-1.1B-Chat-v1.0`
- Fine-tuning: **LoRA** (8-bit), using `peft` library
- Trained on CPU using `train_cpu.py`
- Epochs: 1  
- Batch size: 1  
- Final training loss: ~1.38

> Note: No GPU used. Training completed in ~8 hours on CPU.

---

##  Output Artifacts

-  Trained adapter: `model/adapter_model.safetensors`
-  Inference script: `agent.py`
-  Dataset: `data/cli_qa.json`
-  Logs: `logs/trace.jsonl`
-  Demo: `demo.mp4`

---

##  Results

- The agent is able to generate correct shell commands for common Linux, Git, and Python-related tasks.
- Dry-run mode (via `echo`) helps safely preview output.
- Average plan score: **2.0 / 2.0**
- All commands logged and reproducible.

---

##  Learnings

- How LoRA adapters can be trained quickly and cheaply
- CLI assistant logic via prompt + generation + dry-run
- Evaluation using both static and dynamic techniques
- Dataset design matters a lot in few-shot cases

---

##  Author

**Name:** Mukesh Choudhary  
**Task:** 2025 Fenrir AI/ML Internship Technical Task  
**Deadline:** 18 June 2025, 10:00 PM IST

