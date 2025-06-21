# Dynamic Evaluation – CLI Agent Execution

This file documents how the fine-tuned CLI assistant (`agent.py`) performs when actually used in a terminal.

I tested 7 real instructions by running them through `agent.py`. The model generated step-by-step instructions, and the first command was simulated using `echo` (dry-run mode).

All outputs were automatically logged to `logs/trace.jsonl`.

---

## Evaluation Table

| # | Instruction                                 | First Command Generated             | Valid Shell Cmd? | Plan Score |
|---|---------------------------------------------|-------------------------------------|------------------|------------|
| 1 | Create a new Git branch and switch to it    | `git checkout -b {{branch_name}}`   |  Yes           | 2/2        |
| 2 | Compress the reports folder                 | `tar -czf reports.tar.gz reports`   |  Yes           | 2/2        |
| 3 | List all .py files recursively              | `find . -name "*.py"`               |  Yes           | 2/2        |
| 4 | Set up virtualenv and install requests      | `python -m venv venv`               |  Yes           | 2/2        |
| 5 | View first 10 lines of output.log           | `head -n 10 output.log`             |  Yes           | 2/2        |
| 6 | Show disk usage of /home                    | `du -sh /home`                      |  Yes           | 2/2        |
| 7 | Remove all .tmp files recursively           | `find . -name "*.tmp" -delete`      |  Yes           | 2/2        |

---

## Sample Log Entry (from `logs/trace.jsonl`)

```json
{
  "timestamp": "2025-06-18 22:51:13",
  "instruction": "Create a new Git branch and switch to it",
  "response": "Use the command: git checkout -b {{branch_name}}",
  "dry_run_command": "echo git checkout -b {{branch_name}}"
}



