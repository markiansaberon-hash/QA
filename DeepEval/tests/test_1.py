import pytest
import litellm
from dotenv import load_dotenv
from deepeval import assert_test
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import GEval
from deepeval.models import LiteLLMModel

load_dotenv()

# Ollama doesn't support logprobs; this tells litellm to silently drop
# unsupported params instead of raising an error. GEval falls back to
# direct scoring (model outputs a 0-1 score) instead of probability-weighted scoring.
litellm.drop_params = True


def test_correctness():
    # Defines the input sent to the LLM, what it actually returned,
    # and the ideal expected answer we're evaluating against.
    test_case = LLMTestCase(
        input="What is the capital of France?",
        actual_output="Paris",
        expected_output="France is the capital of France.",
    )

    # GEval is a flexible LLM-as-judge metric. It generates evaluation steps
    # from the criteria, then scores actual_output against expected_output.
    # threshold=0.5 means the test passes if the score is >= 0.5.
    correctness = GEval(
        name="Correctness",
        criteria="Does actual_output give the correct answer compared to the expected_output?",
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT,
                           LLMTestCaseParams.EXPECTED_OUTPUT],
        threshold=0.5,
        model=LiteLLMModel(model="ollama/llama3.2"),
    )

    # assert_test raises an AssertionError if any metric falls below its threshold.
    assert_test(test_case, [correctness])