# import libraries and helper file
import helper as h
from datasets import load_dataset
import pandas as pd

#Load the squad dataset from hugging face hub
squad = load_dataset("squad")

# Get the first 100 records from the SQUAD dataset
val100 = squad["validation"][:100]

# Convert it to dataframe 
val_df100 = pd.DataFrame(val100)

# Apply the apply_answer_questions from the header file on each row in the dataframe
df = val_df100.apply(h.apply_answer_questions, axis=1, result_type="expand")

# save the answer as csv file called "output.csv"
df.to_csv("output.csv", index=False)