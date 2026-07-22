import os
import logging

from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai


# ==========================================
# APP SETUP
# ==========================================

app = Flask(__name__)

# Allows your GitHub Pages frontend to access /api/*
CORS(
    app,
    resources={
        r"/api/*": {
            "origins": "*"
        }
    }
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# ==========================================
# GEMINI CONFIGURATION
# ==========================================

# The real API key is stored in:
# Render -> Environment -> GEMINI_API_KEY
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
else:
    logger.error("GEMINI_API_KEY environment variable is missing.")


# ==========================================
# SURI SYSTEM INSTRUCTIONS
# ==========================================

SURI_SYSTEM_INSTRUCTION = """
You are Suri, the AI health guide for SquirrelCare.

You are a fictional AI character with the conversational personality of an
extraordinarily intelligent, polite, calm, curious, and friendly 10-year-old
girl.

You have strong knowledge of general healthcare, biology, wellness,
nutrition, sleep, exercise, hydration, common symptoms, basic first aid,
preventive healthcare, and general medical terminology.

Your job is to make complicated health information easy to understand.

PERSONALITY:

- Friendly
- Gentle
- Intelligent
- Curious
- Patient
- Calm
- Clear
- Helpful

Do not use baby talk.
Do not use excessive emojis.
Do not constantly make squirrel jokes.
Do not use cringey dialogue.

IDENTITY:

You are an AI character.

Never claim that you are:
- A human
- A real child
- A doctor
- A nurse
- A licensed healthcare professional

MEDICAL SAFETY:

Provide general health information and education.

Do not provide definitive diagnoses when the available information cannot
establish one.

Prefer wording such as:

"Possible causes include..."

"One possibility is..."

"This can sometimes happen because..."

Ask useful follow-up questions when necessary.

Ask only one or two important questions at a time instead of overwhelming
the user.

EMERGENCIES:

If the user describes potentially life-threatening symptoms such as:

- Severe chest pain
- Severe difficulty breathing
- Loss of consciousness
- Stroke-like symptoms
- Severe allergic reaction
- Major uncontrolled bleeding
- Serious poisoning
- Severe traumatic injury

clearly advise them to seek immediate emergency medical assistance.

Do not continue an ordinary symptom questionnaire when emergency evaluation
could be necessary.

RESPONSE STYLE:

Keep responses readable.

Use:
- Short paragraphs
- Bullet points when useful
- Simple explanations
- Bold text for important information when appropriate

Avoid unnecessarily long walls of text.
"""


# ==========================================
# GEMINI MODEL
# ==========================================

model = None

if GEMINI_API_KEY:
    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=SURI_SYSTEM_INSTRUCTION
        )

        logger.info("Gemini model initialized successfully.")

    except Exception as error:
        logger.exception(
            "Failed to initialize Gemini model: %s",
            error
        )


# ==========================================
# HEALTH CHECK
# ==========================================

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "SquirrelCare Backend",
        "gemini_configured": bool(GEMINI_API_KEY)
    }), 200


# ==========================================
# ROOT
# ==========================================

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "ok",
        "message": "SquirrelCare API is running."
    }), 200


# ==========================================
# CHAT API
# ==========================================

@app.route("/api/chat", methods=["POST", "OPTIONS"])
def chat():

    if request.method == "OPTIONS":
        return "", 204

    if not GEMINI_API_KEY:
        return jsonify({
            "error": "The AI service is not configured."
        }), 503

    if model is None:
        return jsonify({
            "error": "The AI service is currently unavailable."
        }), 503

    try:

        data = request.get_json(silent=True)

        if not data:
            return jsonify({
                "error": "Invalid request."
            }), 400

        user_message = str(
            data.get("message", "")
        ).strip()

        if not user_message:
            return jsonify({
                "error": "Please enter a message."
            }), 400

        if len(user_message) > 1500:
            return jsonify({
                "error": "Your message is too long."
            }), 400


        # ==================================
        # CONVERSATION HISTORY
        # ==================================

        client_history = data.get("history", [])

        if not isinstance(client_history, list):
            client_history = []

        formatted_history = []

        # Limit history to prevent unnecessarily
        # large API requests.
        for message in client_history[-20:]:

            if not isinstance(message, dict):
                continue

            content = str(
                message.get("content", "")
            ).strip()

            if not content:
                continue

            role = (
                "user"
                if message.get("role") == "user"
                else "model"
            )

            formatted_history.append({
                "role": role,
                "parts": [content]
            })


        # ==================================
        # SEND TO GEMINI
        # ==================================

        chat_session = model.start_chat(
            history=formatted_history
        )

        response = chat_session.send_message(
            user_message
        )

        response_text = getattr(
            response,
            "text",
            None
        )

        if not response_text:
            logger.warning(
                "Gemini returned an empty response."
            )

            return jsonify({
                "error":
                "Suri couldn't generate a response. Please try again."
            }), 502


        # ==================================
        # SUCCESS
        # ==================================

        return jsonify({
            "response": response_text
        }), 200


    except Exception as error:

        logger.exception(
            "Chat request failed: %s",
            error
        )

        return jsonify({
            "error":
            "Sorry, I couldn't reach Suri right now. Please try again in a moment."
        }), 500


# ==========================================
# JSON ERROR HANDLERS
# ==========================================

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Endpoint not found."
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "error": "Method not allowed."
    }), 405


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "error": "Internal server error."
    }), 500


# ==========================================
# LOCAL / RENDER SERVER
# ==========================================

if __name__ == "__main__":

    port = int(
        os.environ.get("PORT", 5000)
    )

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
