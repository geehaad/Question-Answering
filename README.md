# Question Answering system using Pre-trained Bert based model 

Question Answering models can retrieve the answer to a question from a given text, which is useful for searching for an answer in a document. <br> Some question answering models can generate answers without context! (Hugging Face)

<h2>Types of Questions Answering Models</h2>
<ul>
<li>Extractive Question Answering 
<li>Open Generative Question Answering 
<li>Closed Generative Question Answering 
</ul>

Our system is the Extractive Question Answering system, which means that you have a context and a question to ask, and the model assume that the answer is inside the context provided.

<h2>Dataset Overview</h2>
The Question Answering system in this project is evaluated using the Stanford Question Answering Dataset (SQUAD). <br>SQUAD is a widely used benchmark dataset for evaluating machine reading comprehension and question answering systems.<br>
The SQUAD dataset contains a diverse set of passages from a variety of topics and genres.
<br>
<h3>Each example in the dataset consists of the following components:</h3>
<ul>
<li>Context Paragraph: A corpus  that contains the information from which the answer can be extracted.
<li>Question: A question related to the context, formulated to prompt the model to extract the relevant answer.
<li>Answer Span: The exact span of text within the context paragraph that serves as the answer to the question.
</ul>
The dataset can be find here:<a href= "https://huggingface.co/datasets/squad"> squad linl </a>

<h2>Model and Question Answering System</h2>
    <ul>
    <li>Model used:
        <ul>
          <li> <b> Model name:'distilbert-base-cased-distilled-squad'</b> a variant of the DistilBERT model that has been fine-tuned specifically for the Stanford Question Answering Dataset (SQuAD). This model is designed to accurately extract answers from a given context.
          </ul>
    <li>How the System Works:
        <ul>
            <li> 
        </ul>
    </ul>

<h2>Project Directory Structure</h2>
The project directory is organized in a structured manner to facilitate easy navigation and understanding. Below is an overview of the key folders and files within the project:<br>
        
        Question-Answering/
        |-- notebooks/
        |   |-- trails.ipynb
        |-- src/
        |   |-- __init__.py
        |   |-- components/
        |   |   |-- __init__.py
        |   |   |-- helper.py
        |   |   |-- main.py
        |-- |-- tests/
        |   |-- |-- __init__.py
        |   |-- |-- test_answer_questions.py
        |-- requirements.txt
        |-- README.md
        
<h3>Project Directory Structure</h3>

<p><code>src/</code>: This folder contains the main source code of the project.</p>
<p><code>components/</code>: The heart of the project, where the primary functionality resides.</p>
<p><code>helper.py</code>: Houses the <code>answer_questions</code> function responsible for processing context and questions to extract answers, as well as the <code>apply_answer_questions</code> function that applies the process to a dataset.</p>
<p><code>main.py</code>: The entry point of the project, where the main function utilizes the <code>apply_answer_questions</code> function on a subset of the dataset and saves the results in a CSV file.</p>
<p><code>notebooks/</code>: Contains Jupyter notebooks used for exploration and experimentation.</p>
<p><code>exploration.ipynb</code>: Notebook where various models and techniques were explored and tested.</p>
<p><code>tests/</code>: Holds the pytest test suite for verifying the functionality of the implemented functions.</p>
<p><code>test.py</code>: Contains pytest test cases that validate the accuracy of the question answering system.</p>
<p><code>requirements.txt</code>: Lists the Python packages required for the project to run successfully.</p>
<p><code>README.md</code>: The central documentation file containing essential information about the project, its usage, and directory structure.</p>

<h3>How Files Are Used</h3>

<p><code>helper.py</code>: This file contains the core functions that enable the question answering system. The <code>answer_questions</code> function takes a context and question as input and extracts answers using the chosen model. The <code>apply_answer_questions</code> function applies the process to a dataset, generating dictionaries containing the question, original answer, and detected answer.</p>

<p><code>main.py</code>: The <code>main.py</code> script serves as the entry point of the project. It utilizes the <code>apply_answer_questions</code> function to process a subset of the dataset, extracting and saving answers in a CSV file.</p>

<p><code>exploration.ipynb</code>: The Jupyter notebook <code>exploration.ipynb</code> is a sandbox for experimentation. It's used to explore different models, techniques, and variations before integrating them into the main system.</p>

<p><code>test.py</code>: The <code>test.py</code> file hosts pytest test cases that validate the accuracy of the implemented functions. These tests help ensure the reliability and correctness of the question answering system.</p>

<p>By organizing the project in this manner, we maintain clarity and modularity, making it easier to manage, test, and iterate upon the various components.</p>

<p>Feel free to customize this description to match your actual project's file structure and usage.</p>



<h2> Setup Instructions </h2>

<h3>Requirements:</h3>
<ul>
    <li>Python version => 3.6 is recommended
    <li>Operating System: Windows
</ul>

<h3>Python Packages Required: </h3>
<ul> 
    <li>
        datasets==2.14.4
    <li>
        numpy==1.24.4
    <li>
        pandas==2.0.3
    <li>
        tokenizers==0.13.3
    <li>
        torch==2.0.1
    <li>
        transformers
    <li>
        import torch
    <li>
        pytest

</ul>

<h3>To use the question answering system, follow these steps:<h3>

1. Clone the source
* In CMD write: 

	```
	git clone https://github.com/geehaad/Question-Answering.git
	```
* Then:
    ```
    cd Question-Answering
    ```
2. Create a virtual environment, while you are in the project directory (replace venv with your virtual environment name):
* using conda, in cmd write:
    ```
    Conda create -p venv python==3.8
    ```

3. Activate the virtual environment:
    ```
    conda sctivate venv
    ```

4. Run the main script:s
    ```
    python src/components/main.py
    ```
