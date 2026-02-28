# ================================================================
# INTERACTIVE AI EMAIL & CALENDAR DEMO
# User Input + Tailored Reply Generation
# ================================================================

import streamlit as st

st.set_page_config(page_title="AI Email Demo", layout="wide")
st.title("📧 Interactive AI Email & Calendar Demo")

# =================== Simulated Calendar Events ===================

calendar_events = [
    {"title": "Team Strategy Meeting", "time": "2026-03-02 10:00"},
    {"title": "Client Call", "time": "2026-03-03 15:00"}
]

# =================== AI Logic ===================

def classify_importance(body):
    text = body.lower()
    if any(kw in text for kw in ["urgent", "today", "asap", "deadline"]):
        return "Very Important", "red"
    if any(kw in text for kw in ["meeting", "schedule", "call", "discuss"]):
        return "Medium", "orange"
    return "Not Important", "green"

def classify_relationship(sender):
    if "friend" in sender.lower():
        return "Friend"
    if "boss" in sender.lower():
        return "Boss"
    return "Professional"

def generate_reply(body, relationship, importance):
    # Tone variations
    if importance == "Very Important":
        base = "I’ve reviewed your message carefully and will prioritize this right away."
    elif importance == "Medium":
        base = "Thanks! I’ll review this and follow up shortly."
    else:
        base = "Thanks for the message! I got this and will return when needed."

    if relationship == "Friend":
        greeting = "Hey!"
        closer = "Talk soon!"
    elif relationship == "Boss":
        greeting = "Dear Sir/Madam,"
        closer = "Respectfully,"
    else:
        greeting = "Hello,"
        closer = "Kind regards,"

    return f"{greeting}\n\n{base}\n\n{closer}"

# =================== User Input Form ===================

st.subheader("📝 Create Your Own Email Example")

sender_input = st.text_input("📧 Sender Email", placeholder="example@domain.com")
subject_input = st.text_input("🖊️ Subject", placeholder="Enter email subject here")
body_input = st.text_area("💬 Message Body", placeholder="Type the email body here...")

if st.button("Generate Reply"):
    if not sender_input or not body_input:
        st.error("⬆️ Please enter at least sender and email body!")
    else:
        importance, color = classify_importance(body_input)
        relationship = classify_relationship(sender_input)
        reply = generate_reply(body_input, relationship, importance)

        st.markdown(f"**Importance:** <span style='color:{color}'>{importance}</span>", unsafe_allow_html=True)
        st.markdown(f"**Relationship:** {relationship}")

        # If scheduling detected
        if any(k in body_input.lower() for k in ["meeting", "schedule", "call", "free"]):
            next_event = calendar_events[0]
            st.markdown(f"📅 Next Calendar Event: {next_event['title']} at {next_event['time']}")

        st.write("### 📨 Suggested Reply")
        st.code(reply)

st.info("Enter an email above and click **Generate Reply** to see an AI‑style suggestion!")
