import torch
import sys
import json
import os
import datetime
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from peft import PeftModel, PeftConfig

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# Load base model and LoRA adapter
base_model = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
adapter_path = "../model"

print(" Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(base_model)

print(" Loading base model...")
model = AutoModelForCausalLM.from_pretrained(base_model)

print(" Loading LoRA adapter...")
model = PeftModel.from_pretrained(model, adapter_path)

# Move model to CPU (or GPU if available)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Inference pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0 if device == "cuda" else -1)

# Take CLI input
if len(sys.argv) < 2:
    print(" Please provide an instruction.")
    sys.exit(1)

instruction = sys.argv[1]

# Build prompt
prompt = f"""### Question:
{instruction}

### Answer:
"""

print(f" Instruction: {instruction}")
print(" Generating steps...")

output = generator(prompt, max_new_tokens=200, do_sample=True, temperature=0.7)
response = output[0]['generated_text'].split("### Answer:")[-1].strip()

print("\n Step-by-step plan:")
print(response)

# Dry-run first shell command if applicable
first_line = response.splitlines()[0].strip()
dry_run_result = ""

if first_line.startswith(("git", "tar", "gzip", "ls", "grep", "python", "./", "sudo", "bash", "cd", "mkdir", "rm", "cp")):
    print("\n Dry-run (simulated execution):")
    print(f"echo {first_line}")
    dry_run_result = f"echo {first_line}"
else:
    print("\nℹ First line is not a shell command, skipping dry-run.")

# Log everything
log_entry = {
    "timestamp": str(datetime.datetime.now()),
    "instruction": instruction,
    "response": response,
    "dry_run_command": dry_run_result
}

with open("logs/trace.jsonl", "a") as f:
    f.write(json.dumps(log_entry) + "\n")

print("\n Logged to logs/trace.jsonl")

