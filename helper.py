# Import libraries 
from datasets import load_dataset
import pandas as pd 
import transformers
from transformers import AutoTokenizer, BertForQuestionAnswering, AutoModelForQuestionAnswering
import torch

# Load the pretrained model and tokenizer.
model_checkpoint = "distilbert-base-cased-distilled-squad"
model = AutoModelForQuestionAnswering.from_pretrained(model_checkpoint)
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)


# A function that extract the answer from a given context.
def answer_questions(context, question, tokenizer = tokenizer):

    """
    Args:
        context (str): The context corpus that contains the relevant answer.
        question (str): The question asked to be answerd.
        tokenizer: The tokenizer instance (optional).

    Returns:
        atr: The extracted answer,
             or "No answer found" if not found.
    """
    # Print the given the context and the question.
    print("Context:", context)
    print("Question:", question, "\n")

    # Tokenize the context and the question using the given tokenizer.
    inputs = tokenizer(question, context, add_special_tokens=True, return_tensors="pt")

    # Get the model output.
    outputs = model(**inputs)
    
    # Get the indices of the start and end of the answer.
    answer_start_index = torch.argmax(outputs.start_logits)
    answer_end_index = torch.argmax(outputs.end_logits) + 1  

    # Print answer indices for debugging.
    print("Answer Start Index:", answer_start_index)
    print("Answer End Index:", answer_end_index, "\n")

    # Check if the stard index is before the end index: the answer is valid.
    if answer_end_index <= answer_start_index:
        return "No answer found"
    
    # Extract the answer tokens from the input using start and end index.
    predict_answer_tokens = inputs.input_ids[0, answer_start_index : answer_end_index]

    # Decode the answer tokens.
    predicted_answer = tokenizer.decode(predict_answer_tokens)

    # Print the predicted answer.
    print("Predicted Answer:", predicted_answer)
    
    return predicted_answer

# Define a function to apply 'answer_questions' to each row in a dataset
def apply_answer_questions(row):

    """
    Args:
        row (pandas.Series): a Dataset row that contains context ans question cols. 

    Returns:
        dict: A dictionary contains: question, original_answer, and detected_answer.

    """
    # Get the context and question from the dataframe raw.
    context = row["context"]
    question = row["question"]

    # Call the answer_questions function to get the detected answer.
    answer = answer_questions(context, question)

    # A dictionary contains the results.
    result = 
            {
              "Question": question, 
              "Original_answer": row["answers"]["text"][0],
               "Detected_answer": answer
            }

    return result