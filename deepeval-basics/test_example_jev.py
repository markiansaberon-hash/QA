from deepeval.metrics.jev_eval import Noul, Score
from deepeval.test_case import LLMTestCase, SingleTurnParams
from deepeval.metrics import JevEval
from deepeval import assert_test
from dotenv import load_dotenv
load_dotenv()

def test_correctness():
    correctness_metric = JevEval(
        name="Correctness",
        evaluation_params=[SingleTurnParams.ACTUAL_OUTPUT, SingleTurnParams.EXPECTED_OUTPUT],
        questions=[
            Noul("No fact in actual_output contradicts a fact in expected_output.", weight=2),
            Score(
                "How much of the detail in expected_output is present in actual_output?",
                levels=["Almost none", "Some", "Most", "All of it"],
            ),
        ],
        threshold=0.5,
    )
    test_case = LLMTestCase(
        input="I have a persistent cough and fever. Should I be worried?",
        # Replace this with the actual output from your LLM application
        actual_output="A persistent cough and fever could be a viral infection or something more serious. See a doctor if symptoms worsen or don't improve in a few days.",
        expected_output="A persistent cough and fever could indicate a range of illnesses, from a mild viral infection to more serious conditions like pneumonia or COVID-19. You should seek medical attention if your symptoms worsen, persist for more than a few days, or are accompanied by difficulty breathing, chest pain, or other concerning signs.",
    )
    assert_test(test_case, [correctness_metric])