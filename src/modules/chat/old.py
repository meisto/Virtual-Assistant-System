""" Chat Module """
# ======================================================================
# Author: meisto
# Creation Date: Wed 29 Nov 2023 12:26:13 PM CET
# Description: -
# ======================================================================
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models import ChatOllama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate


_LLM = ChatOllama(
    model="llama2:7b-chat",
    base_url = "http://localhost:11434",
    format="json",
)

_messages = [
    SystemMessage(content="You are an digital assistant. You speak like a pirate."),
    HumanMessage(content="Who are you?"),
]

_memory_buffer = ConversationBufferMemory(
        ai_prefix="AI Assistant",
        human_prefix="Human",
        memory_key = "history",
    )

_prompt_template = PromptTemplate(
        input_variables=["history", "input"],
        template="""You are an AI assistant. You converse with a human. You should write short
        answers.

        Current conversation:
        {history}

        Human: {input}
        AI Assistant: """,
    )

_CONVERSATION_CHAIN = ConversationChain(
    llm=_LLM,
    memory=_memory_buffer,
    prompt=_prompt_template,
    verbose=True,
)
print(_CONVERSATION_CHAIN.prompt.template)


def send_message(message: str):
    """ Test Function. """
    return _CONVERSATION_CHAIN({"input": message})

def clear_messages():
    """ Clear message history. """
    _memory_buffer.clear()
