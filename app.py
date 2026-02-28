# ================================================================
# AI EMAIL & CALENDAR INTELLIGENCE – STREAMLIT DASHBOARD
# with Advanced, Context‑Sensitive Reply Generation
# ================================================================

import streamlit as st
import random

st.set_page_config(page_title="Advanced AI Email Demo", layout="wide")
st.title("📧 Advanced AI Email & Calendar Intelligence")

# ========== Simulated Inbox Data ==========

inbox = [
    {
        "from": "boss@company.com",
        "subject": "Urgent report deadline",
        "body": "Can you send the final Q4 report *today*? The board needs it."
    },
    {
        "from": "friend@email.com",
        "subject": "Weekend plans",
        "body": "Hey! You around this weekend? Maybe grab a bite?"
    },
    {
        "from": "newclient@biz.com",
        "subject": "Meeting request",
        "body": "We’d like to schedule a meeting to discuss our future collaboration."
    }
]

calendar_events = [
    {"title": "Team Strategy Meeting", "time": "2026-03-02 10:00"},
    {"title": "Client Call", "time": "2026-03-03 15:00"},
    {"title": "Project Review", "time": "2026-03-04 09:00"}
]

# ========== IMPORTANCE & RELATIONSHIP CLASSIFICATION ==========

def classify_importance(body):
    text = body.lower()
    if any(kw in text for kw in ["urgent", "today", "asap", "deadline"]):
        return "Very Important", "red"
    if any(kw in text for kw in ["meeting", "schedule", "call", "discuss"]):
        return "Medium", "orange"
    return "Not Important", "green"

def classify_relationship(sender):
    sender_lower = sender.lower()
    if "friend" in sender_lower:
        return "Friend"
    if "boss" in sender_lower:
        return "Boss"
    return "Professional"

# ========== ADVANCED REPLY GENERATOR ==========

def advanced_reply_generator(subject, body, relationship, importance):
    """
    Generates a context‑rich reply that considers:
      - Intent extracted from subject/body
      - Relationship of sender
      - Importance level
      - Follow‑up actions and optional clarifications
    """

    text = body.lower()
    subject_text = subject.lower()

    # --- Intent detection ---
    intents = []
    if any(w in text for w in ["meeting", "schedule", "call"]):
        intents.append("schedule")
    if any(w in text for w in ["thanks", "appreciate"]):
        intents.append("gratitude")
    if any(w in text for w in ["urgent", "asap", "deadline"]):
        intents.append("urgent")
    if any(w in text for w in ["question", "clarify", "help"]) or "?" in text:
        intents.append("question")
    if "report" in subject_text:
        intents.append("report")
    if any(w in subject_text for w in ["lunch", "dinner", "plans"]):
        intents.append("social")

    # --- Phrasing libraries ---
    greetings = {
        "Friend": ["Hey!", "Hi there!", "What's up?"],
        "Boss": ["Dear", "Good day", "Hello"],
        "Professional": ["Hello", "Greetings"],
        "Unknown": ["Hello", "Hi"]
    }
    closers = {
        "Friend": ["Cheers!", "Talk soon!", "Catch you later!"],
        "Boss": ["Respectfully,", "Kind regards,", "Thank you,"],
        "Professional": ["Best regards,", "Sincerely,"],
        "Unknown": ["Regards,", "Thanks,"]
    }

    greeting = random.choice(greetings.get(relationship, ["Hello"]))
    closer = random.choice(closers.get(relationship, ["Regards,"]))

    # Variation pools for different intents
    variation_pools = {
        "urgent": [
            "I understand this is a priority, and I’m acting on it right away.",
            "Given the urgency, I'm moving this to the top of my list.",
            "I will start work immediately and keep you updated."
        ],
        "schedule": [
            "Let’s plan around the best time — do you have preferences?",
            "I can join a meeting — please confirm a suitable time.",
            "Before finalising, could you tell me your availability?"
        ],
        "gratitude": [
            "Thanks for the update — it’s much appreciated.",
            "Thank you for the detailed information!",
            "I appreciate your message and will follow up."
        ],
        "report": [
            "I’ll prepare and share the latest report details.",
            "Reviewing the report now — you’ll have an update soon.",
            "Let me consolidate the data and send the report promptly."
        ],
        "social": [
            "That sounds fun — I’d be glad to join!",
            "Definitely count me in for that!",
            "Looking forward to it — sounds great!"
        ]
    }

    # Build the body of the reply
    response_parts = []
    for intent in intents:
        if intent in variation_pools:
            response_parts.append(random.choice(variation_pools[intent]))

    if not response_parts:
        response_parts.append("Thank you for your message — I’ve read through it carefully.")

    # Importance‑based follow‑up
    if importance == "Very Important":
        response_parts.append(random.choice([
            "I’ll provide a clear update within the hour.",
            "Please let me know if you need this by a specific time.",
            "Expect a detailed follow‑up shortly."
        ]))
    elif importance == "Medium":
        response_parts.append(random.choice([
            "I’ll get back to you with more details soon.",
            "Let me know if anything changes.",
            "I’m reviewing this and will touch base shortly."
        ]))
    else:
        response_parts.append(random.choice([
            "Feel free to reach out if there’s more to add.",
            "I’ve noted this.",
            "Hope this helps!"
        ]))

    # Optional clarification
    clarification = ""
    if "schedule" in intents and not any(x in text for x in ["am", "pm", "today", "tomorrow"]):
        clarification = "\n\nP.S. Could you specify the ideal time?"

    final_body = " ".join(response_parts)

    return f"""{greeting},

{final_body}{clarification}

{closer}"""

# ========== DISPLAY DASHBOARD ==========

st.subheader("📥 Inbox Overview")

for idx, email in enumerate(inbox):
    importance, color = classify_importance(email["body"])
    relationship = classify_relationship(email["from"])
    reply = advanced_reply_generator(
        email["subject"],
        email["body"],
        relationship,
        importance
    )

    with st.expander(f"{idx+1}. From: {email['from']} | Subject: {email['subject']}"):
        st.markdown(f"**Body:** {email['body']}")
        st.markdown(
            f"**Importance:** <span style='color:{color}'>{importance}</span>",
            unsafe_allow_html=True
        )
        st.markdown(f"**Relationship:** {relationship}")

        if any(word in email["body"].lower() for word in ["meeting", "schedule", "free", "call"]):
            next_event = calendar_events[0]
            st.markdown(
                f"**Next Calendar Event:** {next_event['title']} at {next_event['time']}"
            )

        st.code(reply)

st.success("✅ Enhanced Demo Live!")
