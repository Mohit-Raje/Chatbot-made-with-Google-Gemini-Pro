import streamlit as st 
import os
import google.generativeai as genai

st.set_page_config(page_title="Chat Application" , page_icon="🤖")

st.sidebar.title("Enter the Google Gemini API Key")
API_KEY=st.sidebar.text_input("Enter the Google Gemini API Key" , type="password")
os.environ['GOOGLE_API_KEY']=API_KEY
genai.configure(api_key=API_KEY)

model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question , stream=True)
    return response

st.header("Polaris AI - A Chatbot made with Gemini Pro")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]


input=st.text_input("Input: " , key="input")

submit = st.button("Ask the question")

if submit and input:
    response=get_gemini_response(input)
    st.session_state['chat_history'].append(("You" , input))
    st.subheader("The response is ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot" , chunk.text))
st.subheader("Chat History")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")


st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: black;
            color: white;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
            z-index: 100;
        }
        .footer a {
            color: white;
            text-decoration: none;
        }
        .footer img {
            width: 30px;
            vertical-align: middle;
            margin-left: 10px;
        }
    </style>
    <div class="footer">
        <strong>Trademark © 2025 Mohit Raje</strong>
        <a href="https://github.com/Mohit-Raje" target="_blank">
            <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub">
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
    
