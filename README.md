# CLI Assistant – LoRA Fine-Tuned TinyLlama (Internship Task)

This project is a command-line assistant trained on a custom dataset of 150+ CLI Q&A pairs. The model is fine-tuned using LoRA on TinyLlama (1.1B) and can convert natural language instructions into accurate shell commands.

---

##  Project Structure

```
fenrir_intern_task/
├──agent/ agent.py                # CLI assistant script (inference)
├── train_cpu.py            # LoRA training script (CPU-friendly)
├── report.md               # Final internship report
├── eval_static.md          # Manual evaluation (base vs fine-tuned)
├── eval_dynamic.md         # CLI usage evaluation via agent.py
├── README.md               # You're here
├── logs/
│   └── trace.jsonl         # CLI usage logs
├── model/
│   └── adapter_model.safetensors + config files
├── data/
│   └── cli_qa.json         # 150+ CLI Q&A dataset
├── demo.mp4                # Final recorded demonstration
└── venv/                   # (Optional) Virtual environment
```

---

##  Features

- Converts English instructions into real CLI commands
- Trained using lightweight LoRA technique (adapter < 500 MB)
- Dry-run shell simulation via `echo`
- Fully open-source and CPU-compatible
- CLI instruction logging and reproducibility

---

##  Setup Instructions

### 1. Clone the repository and setup virtualenv:

```bash
python -m venv venv
source venv/bin/activate  # Use venv\Scripts\activate on Windows
pip install -r requirements.txt
```

> If no requirements.txt is provided, install manually:
```bash
pip install transformers datasets peft accelerate
```

---

### 2. Run the Agent (Inference)

```bash
python agent.py "Create a new Git branch and switch to it"
```

This generates step-by-step instructions and simulates the first shell command using dry-run (echo).

---

### 3. Re-train Model (Optional)

To retrain the LoRA adapter on CPU:

```bash
python train_cpu.py
```

Trained LoRA adapter is saved in `./model/`.

---

##  Evaluation Summary

- Static Eval: Avg score 2.0 / 2.0
- Dynamic Eval: All commands valid, safe, and usable
- Adapter Size: ~50MB (LoRA)

---

##  Author

**Mukesh Choudhary**  
Task: AI/ML Intern – Fenrir Security Pvt. Ltd.  
Deadline: 18 June 2025, 10:00 PM IST

---

##  Demo Video

See `demo.mp4` in the root directory for usage demo of `agent.py`, logs, and evaluation.

---

##  License

This project is open-source and part of a technical internship evaluation task.

