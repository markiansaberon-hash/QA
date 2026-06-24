import pytest
import litellm
from dotenv import load_dotenv
from deepeval import assert_test
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import GEval
from deepeval.models import LiteLLMModel

load_dotenv()

litellm.drop_params = True  # Ollama doesn't support logprobs; drop it before sending

def test_correctness():
    test_case = LLMTestCase(
        input="What is the capital of France?",
        actual_output="Paris",
        expected_output="France is the capital of France.",
    )
    correctness = GEval(
        name="Correctness",
        criteria="Does actual_output give the correct answer compared to the expected_output?",
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT,
                             LLMTestCaseParams.EXPECTED_OUTPUT],
        threshold=0.5,
        model=LiteLLMModel(model="ollama/llama3.2"),
    )
    assert_test(test_case, [correctness])