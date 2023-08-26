import helper as h
from datasets import load_dataset
import pandas as pd

#Load the squad dataset from hugging face hub
squad_df = load_dataset("squad")
val_df = squad_df["validation"][:100]
val_df100 = pd.DataFrame(val_df)

df = val_df100.apply(h.apply_answer_questions, axis=1, result_type="expand")

df.to_csv("output.csv", index=False)