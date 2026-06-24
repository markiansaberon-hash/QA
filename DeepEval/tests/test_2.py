from deepeval.test_case import LLMTestCase, ToolCall


def test_three_shapes():
    # RAG shape — fill context + retrieval_context
    rag_case = LLMTestCase(
        input="What is the capital of France?",
        actual_output="Paris",
        retrieval_context=["France is a country in Europe. Its capital is Paris."],
    )

    # Chatbot shape — multi-field, conversational
    chatbot_case = LLMTestCase(
        input="What is the capital of France?",
        actual_output="Sorry for the delay, The capital of France is Paris.",
        expected_output="Emphathetic response + gives correct answer",
    )

    # Tool-use shape — tools_called vs expected_tools
    tool_case = LLMTestCase(
        input="What is the weather in Manila?",
        actual_output="It's 32 degrees Celsius in Manila and it's humid",
        tools_called=[ToolCall(name="get_weather")],
        expected_tools=[ToolCall(name="get_weather")],
    )

    print(repr(rag_case))
    print(repr(chatbot_case))
    print(repr(tool_case))
