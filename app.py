import random

def advanced_reply_generator(subject, body, relationship, importance):
    """
    Generates a complex and natural-sounding reply that:
      - Considers relationship (Friend, Boss, Professional, Unknown)
      - Considers importance (Very Important, Medium, Not Important)
      - Incorporates subject keywords, body context,
        clarifying questions, and variable phrasing
    """

    text = body.lower()
    subject_text = subject.lower()

    # =========== Base Intent & Emotion Detection ===========
    # Check for common intents
    intents = []
    if any(w in text for w in ["meeting", "schedule", "call", "discussion"]):
        intents.append("schedule")
    if any(w in text for w in ["thanks", "thank you", "appreciate"]):
        intents.append("gratitude")
    if any(w in text for w in ["urgent", "asap", "priority"]):
        intents.append("urgent")
    if any(w in text for w in ["question", "ask", "clarify"]):
        intents.append("question")

    # Add subject keywords if relevant
    if "report" in subject_text:
        intents.append("report")
    if "lunch" in subject_text or "dinner" in subject_text:
        intents.append("social")

    # =========== Phrasing Pools ===========
    # Greeting options based on relationship
    greetings = {
        "Friend": ["Hey!", "Hi there!", "What's up?"],
        "Boss": ["Dear", "Hello", "Good day"],
        "Professional": ["Hello", "Greetings"],
        "Unknown": ["Hello", "Hi"]
    }

    closers = {
        "Friend": ["Talk soon!", "Catch you later!", "Cheers!"],
        "Boss": ["Respectfully,", "Kind regards,", "Thank you,"],
        "Professional": ["Best regards,", "Sincerely,"],
        "Unknown": ["Regards,", "Thank you,"]
    }

    # Choose random greeting + closer
    greeting = random.choice(greetings.get(relationship, ["Hello"]))
    closer = random.choice(closers.get(relationship, ["Regards,"]))

    # =========== Content Variation Pools ===========
    variation_pools = {
        "urgent": [
            ("I see this is quite important, so I’ll prioritise it immediately.",
             "This looks like it needs prompt attention — I’ll get on it right away.",
             "Given the urgency, I’ll begin working on this as soon as possible.")
        ],
        "schedule": [
            ("Let’s coordinate on a good time for this.",
             "I’m available for a call; what times work best for you?",
             "Before finalising, could you confirm a preferred schedule?")
        ],
        "gratitude": [
            ("Thanks for the update!",
             "Appreciate the details — this helps a lot.",
             "Thanks a bunch for the information!")
        ],
        "question": [
            ("Could you clarify your question regarding (…)?",
             "Can you provide a bit more detail on that point?",
             "Just a quick follow‑up — I need a bit more context here."),
        ],
        "report": [
            ("I’ll prepare the latest version of the report for you.",
             "I’m reviewing the data now and will send an updated summary.",
             "Let me gather the report details and follow up shortly.")
        ],
        "social": [
            ("That sounds fun!",
             "Looking forward to it!",
             "Count me in — let’s make plans!")
        ],
        "default": [
            ("Thanks for the note!",
             "I’ve received your message and will respond properly.",
             "Thank you for reaching out — I’ll handle this.")
        ]
    }

    # =========== Complex Response Assembly ===========
    response_parts = []

    # Core lines based on detected intents
    for intent in intents:
        if intent in variation_pools:
            response_parts.append(random.choice(variation_pools[intent]))

    # If no strong intent, use default
    if not response_parts:
        response_parts.append(random.choice(variation_pools["default"]))

    # Tailor extra follow‑ups based on importance
    if importance == "Very Important":
        follow_up = random.choice([
            "I’ll provide a more detailed update soon.",
            "Please let me know if you need this by a specific time.",
            "I’ll keep you updated step by step."
        ])
        response_parts.append(follow_up)
    elif importance == "Medium":
        medium_follow = random.choice([
            "I’ll get back with more info within the day.",
            "Let me know if anything changes.",
            "I’m on it and will touch base soon."
        ])
        response_parts.append(medium_follow)
    else:
        casual_follow = random.choice([
            "Let me know if there’s more to discuss.",
            "Feel free to reach out anytime!",
            "Hope that helps!"
        ])
        response_parts.append(casual_follow)

    # Build final text
    final_body = " ".join(response_parts)

    # Add optional clarification for missing info
    clarification = ""
    if "schedule" in intents and not any(w in text for w in ["am", "pm", "today", "tomorrow"]):
        clarification = "\n\nP.S. Could you clarify the exact time you'd prefer?"

    return f"""{greeting},

{final_body}{clarification}

{closer}"""
