import os
import json
import zipfile
import requests
import re
import string
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline

# Step 1: Download the dataset from Dropbox
dropbox_url = "https://www.dropbox.com/scl/fi/heid2pkiswhfaqr5g0piw/data.zip?rlkey=ira57daau8lxfj022xvk1irju&dl=1"
dataset_zip = "data.zip"

# Download with requests instead of wget
response = requests.get(dropbox_url, stream=True)
with open(dataset_zip, "wb") as f:
    for chunk in tqdm(response.iter_content(chunk_size=1024), desc="Downloading dataset"):
        if chunk:
            f.write(chunk)

# Step 2: Extract the ZIP file
with zipfile.ZipFile(dataset_zip, 'r') as zip_ref:
    zip_ref.extractall("data")

# Step 3: List extracted files
extracted_path = "data/data/"
files = os.listdir(extracted_path)
print("Extracted files:", files)

# Load datasets
def load_json_file(filename):
    file_path = os.path.join(extracted_path, filename)
    with open(file_path, "r") as f:
        return json.load(f)

train_dataset = load_json_file("train.json")
dev_dataset = load_json_file("dev.json")
test_dataset = load_json_file("test.json")

# Print a sample
print("Sample record:", dev_dataset[0])

# Step 4: Preprocessing function
def preprocess_example(example):
    # Handling different context structures
    if isinstance(example["context"], list):
      context = " ".join(" ".join(map(str, para)) if isinstance(para, list) else str(para) for para in example["context"])
    else:
      context = example["context"]

    return {
        "question": example["question"],
        "context": context,
        "answers": example["answer"] if isinstance(example["answer"], list) else [example["answer"]]
    }

# Apply preprocessing to all examples
pre_processed_dataset = [preprocess_example(example) for example in dev_dataset]

# Load QA model
model_name = "deepset/roberta-base-squad2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

# Prediction function
def get_prediction(example):
    result = qa_pipeline({
        "question": example["question"],
        "context": example["context"]
    })
    return result["answer"]

# Normalization function for EM and F1
def normalize_answer(s):
    """Lower text and remove punctuation, articles, and extra whitespace."""
    def remove_articles(text):
        return re.sub(r'\b(a|an|the)\b', ' ', text)

    def white_space_fix(text):
        return ' '.join(text.split())

    def remove_punc(text):
        return ''.join(ch for ch in text if ch not in string.punctuation)

    def lower(text):
        return text.lower()

    return white_space_fix(remove_articles(remove_punc(lower(s))))

# EM score function
def compute_em(prediction, ground_truths):
    prediction = normalize_answer(prediction)
    return max([1 if prediction == normalize_answer(gt) else 0 for gt in ground_truths])

# F1 score function
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
    
    return max(f1_scores)

# Compute EM and F1 for dev set
em_scores = []
f1_scores = []

for example in tqdm(pre_processed_dataset[:50], desc="Evaluating Model"):  # Adjust number of examples as needed
    predicted_answer = get_prediction(example)
    em = compute_em(predicted_answer, example["answers"])
    f1 = compute_f1(predicted_answer, example["answers"])
    
    em_scores.append(em)
    f1_scores.append(f1)

    print(f"Q: {example['question']}")
    print(f"Pred: {predicted_answer}")
    print(f"GT: {example['answers']}")
    print(f"EM: {em}, F1: {f1:.4f}\n")

# Print Final Benchmark
final_em = sum(em_scores)*100 / len(em_scores)
final_f1 = sum(f1_scores)*100 / len(f1_scores)

print(f"Final EM Score: {final_em:.4f}")
print(f"Final F1 Score: {final_f1:.4f}")
