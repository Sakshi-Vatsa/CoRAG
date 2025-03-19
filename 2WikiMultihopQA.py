import os
import json
import zipfile

# Step 1: Download the dataset from Dropbox
dropbox_url = "https://www.dropbox.com/scl/fi/heid2pkiswhfaqr5g0piw/data.zip?rlkey=ira57daau8lxfj022xvk1irju&dl=1"
dataset_zip = "data.zip"

!wget "$dropbox_url" -O "$dataset_zip"

# Step 2: Extract the ZIP file
with zipfile.ZipFile(dataset_zip, 'r') as zip_ref:
    zip_ref.extractall("data")

# Step 3: List extracted files
extracted_path = "data/"
files = os.listdir(extracted_path)
print("Extracted files:", files)

nested_data_path = os.path.join(extracted_path, "data")  # Possible nested folder
if os.path.isdir(nested_data_path):  
    nested_files = os.listdir(nested_data_path)
    print("Files in 'data/data/':", nested_files)

# Step 4: Load the JSON dataset (adjust filename if needed)
test_dataset_file = os.path.join(nested_data_path, "test.json")  # Change if different
with open(test_dataset_file, "r") as f:
    test_dataset = json.load(f)

# Step 5: Print a sample
print("Sample record:", test_dataset[0])

# Step 4: Load the JSON dataset (adjust filename if needed)
train_dataset_file = os.path.join(nested_data_path, "train.json")  # Change if different
with open(train_dataset_file, "r") as f:
    train_dataset = json.load(f)

# Step 5: Print a sample
print("Sample record:", train_dataset[0])


# Step 4: Load the JSON dataset (adjust filename if needed)
dev_dataset_file = os.path.join(nested_data_path, "dev.json")  # Change if different
with open(dev_dataset_file, "r") as f:
    dev_dataset = json.load(f)

# Step 5: Print a sample
print("Sample record:", dev_dataset[0])

# Step 1: Define the preprocessing function
def preprocess_example(example):
    # Ensure context is joined properly
    context = " ".join(" ".join(map(str, para)) if isinstance(para, list) else str(para) for para in example["context"])

    
    # Return a unified dictionary
    return {
        "question": example["question"], 
        "context": context, 
        "answers": example["answer"]
    }

# Step 2: Apply preprocessing to all examples in dev_dataset
pre_processed_dataset = [preprocess_example(example) for example in dev_dataset]

from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline

model_name = "deepset/roberta-base-squad2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

# Create a QA pipeline
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)


def get_prediction(example):
    # Using our QA pipeline
    result = qa_pipeline({
        "question": example["question"],
        "context": example["context"]
    })
    return result["answer"]

# Let's run on the first 5 examples for a quick demo:
for i in range(10):
    example = pre_processed_dataset[i]
    predicted_answer = get_prediction(example)
    print(f"Question: {example['question']}")
    print(f"Predicted Answer: {predicted_answer}")
    print(f"Ground Truth: {example['answers']}\n")


import re
import string

def normalize_answer(s):
    """Lower text and remove punctuation, articles and extra whitespace."""
    def remove_articles(text):
        return re.sub(r'\b(a|an|the)\b', ' ', text)
    
    def white_space_fix(text):
        return ' '.join(text.split())
    
    def remove_punc(text):
        exclude = set(string.punctuation)
        return ''.join(ch for ch in text if ch not in exclude)
    
    def lower(text):
        return text.lower()
    
    return white_space_fix(remove_articles(remove_punc(lower(s))))

def compute_f1(prediction, ground_truths):
    prediction = normalize_answer(prediction)
    f1_scores = []
    for gt in ground_truths:
        gt = normalize_answer(gt)
        pred_tokens = prediction.split()
        gt_tokens = gt.split()
        common = set(pred_tokens) & set(gt_tokens)
        if len(common) == 0:
            f1_scores.append(0)
            continue
        precision = len(common) / len(pred_tokens)
        recall = len(common) / len(gt_tokens)
        f1 = (2 * precision * recall) / (precision + recall)
        f1_scores.append(f1)
    return max(f1_scores)  # Use the maximum f1 among all ground truth answers

# Compute F1 for a few examples:
for i in range(10):
    example = pre_processed_dataset[i]
    predicted_answer = get_prediction(example)
    f1 = compute_f1(predicted_answer, example["answers"])
    print(f"Question: {example['question']}")
    print(f"Predicted Answer: {predicted_answer}")
    print(f"F1 Score: {f1:.4f}\n")
