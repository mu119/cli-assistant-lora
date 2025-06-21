from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments
from peft import LoraConfig, get_peft_model, TaskType
from transformers import Trainer, DataCollatorForLanguageModeling
import json

# Load Q&A dataset
with open("data/cli_qa.json", "r") as f:
    raw_data = json.load(f)

# Convert into list of prompt-formatted text
train_data = [{"text": f"### Question:\n{item['question']}\n### Answer:\n{item['answer']}"} for item in raw_data]

from datasets import Dataset
dataset = Dataset.from_list(train_data)

# Load model and tokenizer
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Tokenize
def tokenize(example):
    return tokenizer(example["text"], truncation=True, padding="max_length", max_length=512)

tokenized = dataset.map(tokenize, batched=True)

# Apply LoRA
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.CAUSAL_LM
)
model = get_peft_model(model, lora_config)

# Training Arguments
training_args = TrainingArguments(
    per_device_train_batch_size=1,
    num_train_epochs=1,
    learning_rate=2e-4,
    output_dir="./model",
    save_strategy="epoch",
    save_total_limit=1,
    fp16=False,
    logging_steps=10
)

data_collator = DataCollatorForLanguageModeling(tokenizer, mlm=False)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized,
    data_collator=data_collator
)

# Train
trainer.train()
model.save_pretrained("./model")
tokenizer.save_pretrained("./model")
