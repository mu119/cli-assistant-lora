# Static Evaluation – Base Model vs Fine-tuned CLI Assistant

This document compares responses from the base TinyLlama model and my fine-tuned version trained on around 150 CLI-related Q&A pairs. I tested 7 prompts — 5 from the task and 2 additional ones that I added to cover edge cases.

For each prompt, I checked if the fine-tuned model gave a more complete, accurate, and usable shell command compared to the base model.

---

### 1. Create a new Git branch and switch to it

- **Base model output:**  
  `git branch`

- **Fine-tuned output:**  
  `git checkout -b {{branch_name}} {{path/to/directory}}`

The base model just listed branches, but didn’t actually create or switch. The fine-tuned one gave the correct `checkout -b` usage.

**Score:** 2/2

---

### 2. Compress the folder `reports` into `reports.tar.gz`

- **Base model output:**  
  `tar -czf file.tar.gz folder`

- **Fine-tuned output:**  
  `tar -czf reports.tar.gz reports`

Both commands work, but the fine-tuned one reflected the actual folder and archive names from the instruction.

**Score:** 2/2

---

### 3. List all Python files recursively in the current directory

- **Base model output:**  
  `ls -R *.py`

- **Fine-tuned output:**  
  `find . -name "*.py"`

The base version might miss files in nested folders. The fine-tuned one correctly used `find`, which is the standard way to search recursively.

**Score:** 2/2

---

### 4. Set up a virtual environment and install `requests`

- **Base model output:**  
  `pip install requests`

- **Fine-tuned output:**  
  Explained that first a virtual environment should be created using `venv`, then activated, and finally `requests` should be installed using pip.

The base model just shows package installation, but the fine-tuned one explained the full environment setup process in simple steps.

**Score:** 2/2

---

### 5. Show the first 10 lines of a file named `output.log`

- **Base model output:**  
  `cat output.log`

- **Fine-tuned output:**  
  `head -n 10 output.log`

The base model shows the full file, not just the first few lines. The fine-tuned response directly uses `head`, which is the correct tool for this.

**Score:** 2/2

---

### 6. (Custom Prompt) Show disk usage of the `/home` directory

- **Base model output:**  
  `df`

- **Fine-tuned output:**  
  `du -sh /home`

The fine-tuned model provides a better command for showing just the usage of one folder, while the base model lists all mounted filesystems.

**Score:** 2/2

---

### 7. (Custom Prompt) Delete all `.tmp` files recursively

- **Base model output:**  
  `rm *.tmp`

- **Fine-tuned output:**  
  `find . -name "*.tmp" -delete`

The base model only deletes `.tmp` files from the current folder. The fine-tuned version uses `find` to go through all subdirectories, which is safer and more complete.

**Score:** 2/2

---

### Summary

The fine-tuned model consistently gave better outputs across all prompts. It understood the task more accurately and produced correct, real-world shell commands. In almost every case, the base model was either too generic or incomplete.

**Average Score:** 2.0 / 2.0
