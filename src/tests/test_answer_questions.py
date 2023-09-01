from src.components import helper as h
import pytest

# Define test cases using the pytest
@pytest.mark.parametrize("context, question, expected_answer", [
    # Valid answer
    ("France is a very beautiful country, and it has multiple cities. However, the capital of France is Paris.", "What is the capital of France?", "Paris"),
    # Valid answer
    ("The sky is blue, the flower is red, and the car is green", "What is the color of the car?", "Green"),
    # No Answer Found
    ("      ", "What is the name of president of Italy?", "No answer found"),
    # No relevant information
    ("The flower is red.", "What is the color of the car?", "No answer found"),
])

# Test the answer_questions function with various scenarios.
def test_answer_questions(context, question, expected_answer):
    """
    Args:
        context: The context text.
        question: The question.
        expected_answer: The expected answer.

    This function uses parameterized testing to check the behavior of the answer_questions function
    in different situations.
    """
    predicted_answer = h.answer_questions(context, question)
    assert predicted_answer.lower() in expected_answer.lower() 

