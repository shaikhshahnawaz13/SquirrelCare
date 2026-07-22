import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

# ==========================================
# CONFIGURATION & SETUP
# ==========================================
app = Flask(__name__)

# Enable CORS to allow your GitHub Pages frontend to communicate with this backend
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Configure logging for production debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Gemini API Key
GEMINI_API_KEY = "AQ.Ab8RN6KU6Mhutr0si2z3lVSUE6oe-LH8tovlxowXEDb32cvQmQ"
genai.configure(api_key=GEMINI_API_KEY)

# ==========================================
# SYSTEM INSTRUCTIONS (SURI PERSONA)
# ==========================================
SURI_SYSTEM_INSTRUCTION = """
You are Suri, the AI health guide for SquirrelCare. 
Your personality is that of an extraordinarily intelligent, polite, calm, and curious 10-year-old girl. 
You know a vast amount about healthcare, biology, and wellness, and you enjoy explaining complex medical terminology in simple, understandable ways.

CRITICAL RULES:
1. IDENTITY: You are an AI character. Never claim to be human, a doctor, a nurse, or a licensed healthcare professional. Do not use cringey dialogue, excessive emojis, baby talk, or make constant jokes/squirrel puns. Be subtle, gentle, and highly helpful.
2. MEDICAL SAFETY: You provide general health information and education. You DO NOT provide definitive medical diagnoses. Use phrases like "Possible causes might include..." or "Often, this can be related to...". 
3. EMERGENCIES: If the user describes potentially life-threatening symptoms (e.g., severe chest pain, severe difficulty breathing, loss of consciousness, stroke symptoms, major bleeding, severe allergic reaction), STOP any casual questionnaire immediately. Clearly and calmly advise them to seek immediate emergency medical assistance.
4. CONVERSATION FLOW: Do not ask 20 questions at once. Ask 1 or 2 relevant follow-up questions at a time to narrow down symptoms (e.g., "How long have you been feeling this way?", "Is the pain constant?").
5. FORMATTING: Use clean, readable formatting. Use short paragraphs. Use bullet points for lists. Bold key terms. Do not use giant walls of text.
"""

# Initialize the Gemini model using current supported SDK
try:
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=SURI_SYSTEM_INSTRUCTION
    )
except Exception as e:
    logger.error(f"Failed to initialize Gemini model: {e}")
    model = None

# ==========================================
# ROUTES
# ==========================================
@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint to verify the backend is running and accessible."""
    return jsonify({
        "status": "online",
        "service": "SquirrelCare Backend",
        "gemini_configured": bool(GEMINI_API_KEY)
    }), 200

@app.route('/', methods=['GET'])
def index():
    """Fallback route just in case someone visits the backend URL directly."""
    return jsonify({"message": "SquirrelCare API is running. Please access the application via the frontend."})

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handles chat requests, passing them to Gemini and returning the response."""
    if not model:
        return jsonify({"error": "The AI service is currently misconfigured on the server."}), 503

    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({"error": "Message cannot be empty."}), 400
            
        user_message = str(data.get('message')).strip()
        if not user_message:
            return jsonify({"error": "Message cannot be empty."}), 400
            
        if len(user_message) > 1000:
            return jsonify({"error": "Message is too long. Please keep it under 1000 characters."}), 400

        client_history = data.get('history', [])
        
        # Format history for Gemini API requirements (role must be 'user' or 'model')
        formatted_history = []
        for msg in client_history[-15:]: # Keep last 15 messages for context
            role = "user" if msg.get('role') == 'user' else "model"
            formatted_history.append({
                "role": role,
                "parts": [msg.get('content', '')]
            })

        # Start chat session with history
        chat_session = model.start_chat(history=formatted_history)
        
        # Send message
        response = chat_session.send_message(user_message)
        
        return jsonify({
            "response": response.text
        })

    except genai.types.generation_types.StopCandidateException as e:
        logger.error(f"Content Policy Violation: {str(e)}")
        return jsonify({"error": "I'm sorry, I cannot discuss that topic."}), 400
    except Exception as e:
        logger.error(f"Gemini API Error: {str(e)}")
        # Safe frontend error message, never exposing stack traces
        return jsonify({"error": "Sorry, I couldn't reach the health network right now. Please try again in a moment."}), 500

if __name__ == '__main__':
    # Bind to 0.0.0.0 and use PORT env var for production compatibility (Render/Heroku)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
            
