# ================================================================
# AI EMAIL & CALENDAR INTELLIGENCE – STREAMLIT DASHBOARD
# ================================================================

import streamlit as st

st.set_page_config(page_title="AI Email Demo", layout="wide")
st.title("📧 AI Email & Calendar Intelligence")

# ========== Simulated Inbox Data ==========

inbox = [
    {
        "from": "boss@company.com",
        "subject": "Urgent report",
        "body": "Can you send the Q4 report today? It’s urgent."
    },
    {
        "from": "friend@email.com",
        "subject": "Lunch plans?",
        "body": "You free for lunch tomorrow?"
    },
    {
        "from": "newclient@biz.com",
        "subject": "Meeting request",
        "body": "Can we schedule a meeting to discuss collaboration?"
    }
]

sent_emails = [
    {
        "to": "boss@company.com",
        "body": "Dear John,\n\nPlease find the report attached.\n\nBest regards,"
    },
    {
        "to": "friend@email.com",
        "body": "Hey! Sounds good for lunch! 😄\n\nCheers,"
    }
]

calendar_events = [
    {"title": "Team Strategy Meeting", "time": "2026-03-02 10:00"},
    {"title": "Client Call", "time": "2026-03-03 15:00"}
]

# ========== Simple Classifiers ==========

def classify_importance(body):
    text = body.lower()
    if any(keyword in text for keyword in ["urgent", "asap", "report"]):
        return "Very Important", "red"
    if any(keyword in text for keyword in ["meeting", "schedule", "call"]):
        return "Medium", "orange"
    return "Not Important", "green"

def classify_relationship(sender):
    if "friend" in sender:
        return "Friend"
    if "boss" in sender:
        return "Boss"
    return "Professional"

def generate_reply(body, relationship):
    if relationship == "Friend":
        tone = "Casual and friendly"
    elif relationship == "Boss":
        tone = "Professional and respectful"
    else:
        tone = "Formal and polite"
    return f"Tone: {tone}\nAI Reply: Thanks for your message! (Simulated)"

# ========== Display Dashboard ==========

st.subheader("📥 Inbox Overview")

for idx, email in enumerate(inbox):
    importance, color = classify_importance(email["body"])
    relationship = classify_relationship(email["from"])
    reply = generate_reply(email["body"], relationship)

    with st.expander(f"{idx+1}. From: {email['from']} | Subject: {email['subject']}"):
        st.markdown(f"**Body:** {email['body']}")
        st.markdown(
            f"**Importance:** <span style='color:{color}'>{importance}</span>", 
            unsafe_allow_html=True
        )
        st.markdown(f"**Relationship:** {relationship}")

        if any(word in email["body"].lower() for word in ["meeting", "schedule", "free", "call"]):
            next_event = calendar_events[0]
            st.markdown(f"**Next Calendar Event:** {next_event['title']} at {next_event['time']}")

        st.code(reply)

st.success("✅ Demo Loaded Successfully!")
