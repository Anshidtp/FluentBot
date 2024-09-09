import os
from dotenv import load_dotenv
from langchain.chains.conversation.base  import ConversationChain
from langchain_community.llms.replicate import Replicate
from langchain.chains.conversation.memory import (ConversationBufferMemory,
                                                  ConversationSummaryBufferMemory,
                                                  ConversationBufferWindowMemory,
                                                  ConversationKGMemory)

from app.utils.character import *
from app.utils.prompt import get_system_prompt
from app.utils.persona import few_shot_examples,persona

# from getpass import getpass

# REPLICATE_API_TOKEN = getpass()

# Load environment variables
load_dotenv()
REPLICATE_API_TOKEN = os.environ["REPLICATE_API_TOKEN"]


def get_llm():   
    model_kwargs =model_kwargs={
                 "temperature": 0.75,
                 "top_p": 0.95,
                 "max_length":512,
                 "top_k": 0 
    }
    
    llm =Replicate(
        model="meta/meta-llama-3-8b-instruct",
        replicate_api_token=REPLICATE_API_TOKEN,
        streaming=True, 
        model_kwargs=model_kwargs) #configure the properties 
    
    return llm

#Creating a Memory Buffer
def get_memory(): #create memory for this chat session
    llm = get_llm()
    memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=512,memory_key="chat_history", input_key="input") #Maintains a summary of previous messages
    return memory



def get_chat_response(input_text, memory): #chat client function
    
    llm = get_llm()
    Prompt = get_system_prompt(few_shot_examples,persona)
    conversation_with_summary = ConversationChain( 
        prompt=Prompt,
        llm = llm, 
        memory = memory,
        verbose = True 
    )
    
    chat_response = conversation_with_summary.predict(input=input_text)
    
    return chat_response