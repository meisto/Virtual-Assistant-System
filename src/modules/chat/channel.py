""" Channel object. """
# ======================================================================
# Author: meisto
# Creation Date: Tue 05 Dec 2023 11:54:23 PM CET
# Description: -
# ======================================================================
from typing import List, Optional

from langchain.chat_models import ChatOllama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate

from api.chat.message import Message


class Channel:
    """ TODO """
    def __init__(self, name: str, buffer_length: Optional[int] = None):
        self.name = name
        self.messages: List[Message] = []
        self.buffer_length: Optional[int] = buffer_length

        # TODO: Make this configurable
        llm = ChatOllama(
            model="llama2:7b-chat",
            base_url = "http://localhost:11434",
            format="json",
        )

        if self.buffer_length is None:
            memory_buffer = ConversationBufferMemory(
                ai_prefix="AI Assistant",
                human_prefix="Human",
                memory_key = "history",
            )
        else:
            memory_buffer = ConversationBufferWindowMemory(
                ai_prefix = "AI Assistant",
                human_prefix = "Human",
                memory_key = "history",
                k = self.buffer_length,
            )

        # TODO: Make this configurable
        prompt_template = PromptTemplate(
            input_variables=["history", "input"],
            template="""You are an AI assistant. You converse with a human. You should write short
            answers.

            Current conversation:
            {history}

            Human: {input}
            AI Assistant: """,
        )

        self._conversation_chain = ConversationChain(
            llm=llm,
            memory=memory_buffer,
            prompt=prompt_template,
            verbose=True,
        )

    def reset(self):
        """ Remove all messages from this channel. """

        self.messages = []
        self._conversation_chain.memory.clear()

    def send_message(self, message: Message) -> Message:
        """ 
        Save the given message and forward it to the chain. Format the answer as a message object,
        save and return it.
        """
        response_content = self._conversation_chain({"input": message.content})["response"]
        response = Message(id = 0, source = "AI", timestamp = "Today", content=response_content)

        self.messages.append(message)
        self.messages.append(response)

        return response
