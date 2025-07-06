import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import streamlit.components.v1 as components

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Groq-compatible OpenAI client
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key
)
def referral_prompt(patient, sender, recipient, reason, tone):
    if tone == "formal":
        return f"""
        Please write a formal medical referral letter.

        Patient Name: {patient}
        Referring Doctor: Dr. {sender}
        Specialist Name: Dr. {recipient}
        Reason for Referral: {reason}

        Use professional and medically appropriate language. Explain the reason for referral clearly and politely request evaluation.
        """
    else:
        return f"""
        Write an informal referral note from Dr. {sender} to Dr. {recipient}.

        Patient: {patient}
        Reason: {reason}

        Keep the tone light but informative, like a trusted colleague sending a note about a mutual patient.
        """

def appeal_prompt(patient, sender, recipient, reason, tone):
    if tone == "formal":
        return f"""
        Please write a formal insurance appeal letter on behalf of a patient.

        Patient Name: {patient}
        Doctor: Dr. {sender}
        Insurance Provider: {recipient}
        Denial Reason: {reason}

        The letter should:
        - Clearly state the clinical concern and justification for referral.
        - Mention any prior treatments or relevant history.
        - Politely request evaluation and/or management.
        - Maintain a professional, concise tone suitable for inter-provider communication.

        Do not include placeholders like [Insert Date of Birth] or [Clinic Name]; focus on producing a realistic and readable referral letter.
        """
    else:
        return f"""
        Write a kind and casual appeal letter to {recipient} insurance company.

        Doctor: Dr. {sender}
        Patient: {patient}
        Issue: {reason}

        Ask them to reconsider a denial in a respectful but friendly tone. Keep it persuasive and understandable.
        """

def reminder_prompt(patient, sender, recipient, reason, tone, date):
    if tone == "formal":
        return f"""
        Please write a formal appointment reminder letter from {sender} to {patient}.

        The letter should:
        - Confirm the date, time, and location of the appointment.
        - Be concise, polite, and professional.
        - Avoid discussing insurance, denials, or treatments.
        - Use clear and direct language suitable for a healthcare setting.

        Patient: {patient}  
        Recipient: {recipient}  
        Appointment Details: {reason}
        Appointment Date:  {date}

        Do not include placeholders in brackets like [Insert Date of Birth] or [Clinic Name]; focus on producing a realistic and readable reminder letter.
        """
    else:
        return f"""
        Write an informal appointment reminder note from {sender} to {patient}.

        The note should be friendly, clear, and remind the patient about their upcoming appointment.

        Patient: {patient}  
        Recipient: {recipient}  
        Appointment Details: {reason}
        Appointment Date:  {date}
        
        avoid using placeholders in brackets
        """


# ---- Streamlit UI ----

st.title("Healthcare Letter Assistant 🏥✉️")

letter_type = st.selectbox("Letter Type", ["Referral", "Appeal", "Reminder"])
tone = st.radio("Tone", ["Formal", "Informal"])
patient_name = st.text_input("Patient Name")
sender_name = st.text_input("Sender Name (Doctor or Clinic)")
recipient = st.text_input("Recipient (Doctor or Insurance Provider)")
date = st.date_input("Select a date",)
reason = st.text_area("Reason for Letter")


# Check if a letter already exists
if "letter" not in st.session_state:
    st.session_state.letter = ""


if st.button("Generate Letter"):
    if not all([letter_type, tone, patient_name, sender_name, recipient, reason]):
        st.warning("Please fill out all fields.")
    else:
        with st.spinner("Generating letter..."):
            if letter_type == "Referral":
                prompt = referral_prompt(patient_name, sender_name, recipient, reason, tone.lower())
            elif letter_type == "Appeal":
                prompt = appeal_prompt(patient_name, sender_name, recipient, reason, tone.lower())
            elif letter_type == "Reminder":
                prompt = reminder_prompt(patient_name, sender_name, recipient, reason, tone.lower(), date)

            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )

            st.session_state.letter = response.choices[0].message.content.strip()
            st.success("Letter generated successfully!")

# Show the letter if it's stored
if st.session_state.letter:
    st.text_area("Generated Letter", value=st.session_state.letter, height=300, key="letter_area")

    st.markdown("""
        <small>Highlight the text inside the box above, then press <kbd>Ctrl+C</kbd> (Windows) or <kbd>Cmd+C</kbd> (Mac) to copy the text.</small>
    """, unsafe_allow_html=True)

    st.download_button(
        label="Download Letter",
        data=st.session_state.letter,
        file_name="letter.txt",
        mime="text/plain"
    )


