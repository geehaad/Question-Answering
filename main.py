# Import libraries 
from datasets import load_dataset, load_metric
import pandas as pd 
import numpy as np 
import transformers
from transformers import AutoTokenizer, BertForQuestionAnswering
import torch

# Initialize model and tokenizer
model_checkpoint = "distilbert-base-uncased"
model = BertForQuestionAnswering.from_pretrained(model_checkpoint)
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

def answer_questions(question, context, tokenizer):
    print("Context:", context)
    print("Question:", question, "\n")

    
    inputs = tokenizer(question, context, add_special_tokens=True, return_tensors="pt")

    outputs = model(**inputs)
    
    answer_start_index = torch.argmax(outputs.start_logits)
    answer_end_index = torch.argmax(outputs.end_logits) + 1  # Add 1 to include the end index

    print("Answer Start Index:", answer_start_index)
    print("Answer End Index:", answer_end_index, "\n")

    if answer_end_index <= answer_start_index:
        return "No answer found"
    
    predict_answer_tokens = inputs.input_ids[0, answer_start_index : answer_end_index]

    predicted_answer = tokenizer.decode(predict_answer_tokens)

    print("Predicted Answer:", predicted_answer)
    
    
    
    return predicted_answer

