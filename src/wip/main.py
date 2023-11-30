""" Test """
# ======================================================================
# Author: meisto
# Creation Date: Fri 17 Nov 2023 05:31:36 PM CET
# Description: -
# ======================================================================
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import tool
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.tools.render import format_tool_to_openai_function

@tool
def test_function(word: str) -> str:
    """ Returns the given word with its length appended. """
    return f"{word}: {len(word)}"
tools = [test_function]

def main():
    """
    Main function.

    Parameters:
        None
    Returns:
        None
    """

    llm = Ollama(model="llama2", callback_manager=CallbackManager([StreamingStdOutCallbackHandler]))

    resp = llm(
    """
    Your are an assistant designed for function calling. You only return JSON files.
    The expected output from you has to be:
    { "function": {function_name} }
    Do not answer the question. Only return the most suitable function. If none of the given 
    functions matches the prompt return an empty JSON Document.
    The available functions are:
    - function_length: Return the function length.
    - function_date: Return the date on which this function was written.
    - function_test: Start a test.
    - none: This is the default value that should be returned when no function matches.

    Prompt:
    Who are you?
    """
   )
    print(type(resp))
    print(resp)





if __name__ == "__main__":
    main()
