from deepeval.test_case import LLMTestCase, ToolCall

# Day 2: Three LLMTestCase shapes
# LLMTestCase is one class but models different use cases depending on which
# fields you populate. The shape determines which metrics make sense to pair with it.


def test_three_shapes():
    # RAG shape — populate retrieval_context with what the retriever fetched.
    # Use this with ContextualRelevancyMetric or FaithfulnessMetric to verify
    # the LLM's answer is grounded in the retrieved documents.
    rag_case = LLMTestCase(
        input="What is the capital of France?",
        actual_output="Paris",
        retrieval_context=["France is a country in Europe. Its capital is Paris."],
    )

    # Chatbot shape — expected_output describes the desired behavior, not a literal match.
    # Use this with GEval so the judge scores tone, helpfulness, and correctness
    # against a behavioral description rather than an exact string.
    chatbot_case = LLMTestCase(
        input="What is the capital of France?",
        actual_output="Sorry for the delay, The capital of France is Paris.",
        expected_output="Emphathetic response + gives correct answer",
    )

    # Tool-use shape — tools_called is what the LLM actually invoked,
    # expected_tools is what it should have invoked.
    # Use this with ToolCorrectnessMetric to catch wrong or missing tool calls.
    tool_case = LLMTestCase(
        input="What is the weather in Manila?",
        actual_output="It's 32 degrees Celsius in Manila and it's humid",
        tools_called=[ToolCall(name="get_weather")],
        expected_tools=[ToolCall(name="get_weather")],
    )

    # repr() shows all field values stored inside the object — useful for
    # verifying the test cases were constructed correctly without running metrics.
    print(repr(rag_case))
    print(repr(chatbot_case))
    print(repr(tool_case))
