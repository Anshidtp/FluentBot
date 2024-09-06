import streamlit as st
from model import get_memory,get_chat_response


# #Initialize the model and persona
# conversation_chain = initialize_model_and_persona()

# # Streamlit UI#st.title("Chat with Sarah - Your Marketing and SDXL Prompt Expert")
# # Store LLM generated responses
# if "chat_history" not in st.session_state.keys():
#     st.session_state.chat_history = [{"role": "assistant", "content": "Hi, I'm Sarah, Your Personal Assisatant ,How may I assist you today?"}]

# # Display or clear chat messages
# for message in st.session_state.chat_history:
#     with st.chat_message(message["role"]):
#         st.write(message["content"])

# def clear_chat_history():
#     st.session_state.chat_history = [{"role": "assistant", "content": "Hi, I'm Sarah, Your Personal Assisatant ,How may I assist you today?"}]
# st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []
#     # st.session_state.messages = []

# # User-provided prompt
# if prompt := st.chat_input(disabled=not conversation_chain):
#     st.session_state.chat_history.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.write(prompt)

# # Generate a new response if last message is not from assistant
# if st.session_state.chat_history and st.session_state.chat_history[-1]["role"] != "assistant":
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             response_text = generate_llama3_response(conversation_chain, prompt)
#             placeholder = st.empty()
#             full_response = ''
#             for item in response_text:
#                 full_response += item
#                 placeholder.markdown(full_response)
#             placeholder.markdown(full_response)
#     message = {"role": "assistant", "content": full_response}
#     st.session_state.chat_history.append(message)

# #Display chat_history
# if st.session_state.chat_history:
#     for message in st.session_state.chat_history:
#         st.write(message)


if 'memory' not in st.session_state:
    st.session_state.memory = get_memory()  

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []  # Initialize the chat history

# for message in st.session_state.chat_history:
#     with st.chat_message(message["role"]):
#         st.markdown(message["text"])

input_text = st.chat_input("Chat with your bot here")  # Display a chat input box

if input_text:  # Check if the user has entered text
    # Process and display the user's message
    with st.chat_message("user"):
        st.markdown(input_text)
    # Append the user's message to the chat history
    st.session_state.chat_history.append({"role": "user", "text": input_text})
    # Generate and display the chatbot's response
    chat_response = get_chat_response(input_text=input_text, memory=st.session_state.memory)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            st.markdown(chat_response)
    # Append the chatbot's response to the chat history
    st.session_state.chat_history.append({"role": "assistant", "text": chat_response})

# if st.session_state.chat_history:
#     for message in st.session_state.chat_history:
#         st.write(message)