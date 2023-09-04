import gradio as gr
from src.components.helper import answer_questions, apply_answer_questions



def question_answering_interface(context, question):
    # Call answer_questions function with both context and question
    answer = answer_questions(context, question)  
    return answer

def df_interface(df):
    # Call apply_answer_questions function with df
    dataframe = df.apply(apply_answer_questions, axis=1, result_type="expand")
    dataframe.to_csv("output.csv", index=False)
    return dataframe


# Initialize an empty conversation history
conversation_history = []

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("Question Answering System")

    # Tab for answer_questions func 
    with gr.Tab("Single QAs"):
        context_input = gr.Textbox(label="Context", type="text", placeholder="Enter context here...", lines=10)
        question_input = gr.Textbox(label="Question", type="text",placeholder="Enter question here...")
        qa_button = gr.Button("Get Answer")
        qa_output = gr.Textbox(label="Answer", type="text", placeholder="Answer will be displayed here...")

        

        # Tab for DataFrame upload (func1)
    with gr.Tab("Upload DataFrame"):
        df_input = gr.File(label="Upload DataFrame (CSV)")
        df_output = gr.Dataframe(headers=["Original DataFrame"])
        df_button = gr.Button("Process")

    # Define actions when buttons are clicked
    qa_button.click(question_answering_interface, inputs=[context_input, question_input], outputs=qa_output)
    df_button.click(df_interface, inputs=df_input, outputs=df_output)
    

# Launch the Gradio interface
demo.launch()