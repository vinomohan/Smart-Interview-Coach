import streamlit as st
import uuid

from evaluator.scorer import score_answer, get_questions_by_category
from speech.transcriber import transcribe_audio
from recommender.recommender import get_recommendations

st.set_page_config(page_title="Smart AI Interview Coach", layout="wide")
st.sidebar.title("Navigation")

# Step 1: Input user ID
st.sidebar.markdown("## 👤 User Info")
user_id = st.sidebar.text_input("Enter your name (display ID):")

# Step 2: Generate or load session ID
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

session_id = st.session_state.session_id

# Show session ID (optional for debug)
# st.sidebar.code(f"Session ID: {session_id}")

# Step 3: Page Routing
page = st.sidebar.radio("Go to", ["🏠 Home", "🧠 Answer Evaluation", "🎤 Voice Input", "📚 Recommendations"])

# --- Page: Home ---
if page == "🏠 Home":
    st.title("Smart AI Interview Coach")
    st.write("""
        Welcome to your personal AI-powered interview coach.
        Use the side panel to:
        - Evaluate your answers
        - Speak your responses
        - Get personalized topic suggestions
    """)
    if user_id:
        st.success(f"Hello, {user_id}! Your session is ready.")
    else:
        st.info("Please enter your name in the sidebar to begin.")

# --- Page: Answer Evaluation ---
elif page == "🧠 Answer Evaluation":
    st.title("🧠 Answer Evaluation")
    if not user_id:
        st.warning("Please enter your name in the sidebar.")
    else:
        category = st.selectbox("Choose Question Type", ["personal", "technical"])
        questions = get_questions_by_category(category)
        selected_question = st.selectbox("Select Interview Question", questions)

        user_answer = st.text_area("Enter Your Answer:")
        if st.button("Evaluate"):
            if selected_question and user_answer:
                score, feedback = score_answer(user_answer, selected_question, user_id=user_id, session_id=session_id)
                st.success(f"Score: {score:.2f}")
                st.write("💬 Feedback:", feedback)
            else:
                st.warning("Please select a question and write your answer.")

# --- Page: Voice Input ---
elif page == "🎤 Voice Input":
    st.title("🎤 Speak Your Answer")
    st.write("Upload your voice recording (.wav):")
    audio_file = st.file_uploader("Upload .wav file", type=["wav"])
    if audio_file:
        with open("temp_audio.wav", "wb") as f:
            f.write(audio_file.read())
        transcript = transcribe_audio("temp_audio.wav")
        st.write("📝 Transcript:")
        st.text_area("Transcribed Text", value=transcript)

# --- Page: Recommendations ---
elif page == "📚 Recommendations":
    st.title("📚 Topic Recommendations")
    if not user_id:
        st.warning("Please enter your name in the sidebar.")
    else:
        if st.button("Get Recommendations"):
            recs = get_recommendations(session_id)
            st.write("🔁 Topics to focus on:")
            for r in recs:
                st.markdown(f"- {r}")
