import pandas as pd
import gradio as gr
from src.components.helper import answer_questions, apply_answer_questions



def question_answering_interface(context, question):
    # Call answer_questions function with both context and question
    answer = answer_questions(context, question)  
    return answer

def df_interface(df_input):
    # Read the CSV file from the Gradio file input
    dataframe = pd.read_csv(df_input.name, encoding='utf-8')
    df_output = dataframe.apply(apply_answer_questions, axis=1, result_type="expand")
    df_output.columns = ['Question',  'Detected_answer']
    df_output.to_csv(r"D:\QA\Question-Answering\output2.csv", index=False)
    return df_output


   

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("Question Answering System")

    # Tab for answer_questions func 
    with gr.Tab("Single QAs"):
        context_input = gr.Textbox(label="context", type="text", placeholder="Enter context here...", lines=10)
        question_input = gr.Textbox(label="question", type="text",placeholder="Enter question here...")
        qa_button = gr.Button("Get Answer")
        qa_output = gr.Textbox(label="Answer", type="text", placeholder="Answer will be displayed here...")

        

    # Tab for  CSV file upload 
    with gr.Tab("Upload CSV File"):
        df_input = gr.File(label="Upload CSV File")
        df_button = gr.Button("Process")
        df_output = gr.Dataframe(headers=["Question, Detected_answer"])
        

    # Define actions when buttons are clicked
    qa_button.click(question_answering_interface, inputs=[context_input, question_input], outputs=qa_output)
    df_button.click(df_interface, inputs=df_input, outputs=df_output)
    

# Launch the Gradio interface
demo.launch()