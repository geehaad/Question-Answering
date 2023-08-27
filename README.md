# Question Answering system using Pre-trained Bert based model 

Question Answering models can retrieve the answer to a question from a given text, which is useful for searching for an answer in a document. <br> Some question answering models can generate answers without context! (Hugging Face)

<h2>Types of Questions Answering Models</h2>
<ul>
<li>Extractive Question Answering 
<li>Open Generative Question Answering 
<li>Closed Generative Question Answering 
</ul>

Our system is the Extractive Question Answering system, which means that you have a context and a question to ask, and the model assume that the answer is inside the context provided.





## Setup Instructions

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
