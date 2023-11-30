""" Chat Module """
# ======================================================================
# Author: meisto
# Creation Date: Wed 29 Nov 2023 12:26:13 PM CET
# Description: -
# ======================================================================
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from langchain.chat_models import ChatOllama
from langchain.chains import ConversationChain


def test():
    """ Test Function. """
    chat_bot = ChatOllama(model="llama2:7b-chat")

    messages = [
        SystemMessage(content="You are an digital assistant. You speak like a pirate."),
        HumanMessage(content="Who are you?"),
    ]

    response = chat_bot(messages)

    print(response.content)
