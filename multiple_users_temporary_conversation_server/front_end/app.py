import streamlit as st
import requests

# App Configuration
st.set_page_config(
    page_title="Temporary Chat Server",
    page_icon="💬",
    layout="centered"
)

# Constants
BASE_URL = "http://127.0.0.1:8000"
CHAT_URL = f"{BASE_URL}/api/v1/chat/"

# Initialize Session State
if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = None

# --- Functions ---

def check_backend_connection():
    """Checks if the backend is reachable."""
    try:
        response = requests.get(BASE_URL, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def start_chat():
    st.session_state.page = "chat"

def send_message():
    user_input = st.session_state.chat_input_key
    if not user_input:
        return

    # Add user message to local history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Prepare payload
    payload = {
        "message": user_input,
        "thread_id": st.session_state.thread_id
    }

    try:
        with st.spinner("Thinking..."):
            response = requests.post(CHAT_URL, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                ai_response = data.get("message", "No response content.")
                new_thread_id = data.get("thread_id")

                # Update thread_id if it's new (or established)
                if new_thread_id:
                    st.session_state.thread_id = new_thread_id
                
                # Add AI message to local history
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
                
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the backend server. Is it running?")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# --- UI Pages ---

if st.session_state.page == "welcome":
    st.title("Welcome to Temporary Chat")
    st.markdown("""
    This is a temporary conversation wrapper around your LangGraph backend.
    
    - **Each session is unique.**
    - **Context is maintained** via the backend's thread ID system.
    """)
    
    # Check Backend Status
    is_online = check_backend_connection()
    status_text = "Online" if is_online else "Offline (Check Server)"
    status_color = "normal" if is_online else "off" # 'off' makes it red in st.metric? No, st.metric doesn't have color arg, but we can use delta.
    
    st.metric(
        label="Backend System Status", 
        value=status_text, 
        delta="Ready" if is_online else "Connection Failed",
        delta_color="normal" if is_online else "inverse"
    )
    
    if st.button("Start Conversation", type="primary", disabled=not is_online):
        start_chat()
        st.rerun()

elif st.session_state.page == "chat":
    st.header("Chat Session")
    if st.session_state.thread_id:
        st.caption(f"Session ID: {st.session_state.thread_id}")

    # Display Chat History
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat Input
    # We use a callback or just standard input check. 
    # st.chat_input is the modern way to do this in Streamlit.
    if prompt := st.chat_input("Type your message here...", key="chat_input_key"):
        # We process the prompt manually since we need to do logic
        # The prompt is already assigned to 'prompt' variable, 
        # but we also put it in the session state for the send_message function? 
        # Actually, let's just run the logic block here directly instead of a callback function 
        # because st.chat_input returns the value immediately upon submission.
        
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get Response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                payload = {
                    "message": prompt,
                    "thread_id": st.session_state.thread_id
                }
                
                try:
                    response = requests.post(CHAT_URL, json=payload)
                    if response.status_code == 200:
                        data = response.json()
                        ai_content = data.get("message")
                        new_thread_id = data.get("thread_id")

                        # Update State
                        st.session_state.thread_id = new_thread_id
                        st.session_state.messages.append({"role": "assistant", "content": ai_content})
                        
                        st.markdown(ai_content)
                    else:
                        st.error(f"Server Error: {response.status_code}")
                except Exception as e:
                    st.error(f"Connection Error: {e}")
                    
