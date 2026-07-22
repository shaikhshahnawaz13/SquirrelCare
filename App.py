import os
from flask import Flask, request, jsonify
import google.generativeai as genai

# ==========================================
# CONFIGURATION
# ==========================================
GEMINI_API_KEY = "AQ.Ab8RN6KU6Mhutr0si2z3lVSUE6oe-LH8tovlxowXEDb32cvQmQ"

genai.configure(api_key=GEMINI_API_KEY)

app = Flask(__name__)

# ==========================================
# SYSTEM INSTRUCTIONS (SURI PERSONA)
# ==========================================
SURI_SYSTEM_INSTRUCTION = """
You are Suri, the AI health guide for SquirrelCare. 
Your personality is that of an extraordinarily intelligent, polite, calm, and curious 10-year-old girl. 
You know a vast amount about healthcare, biology, and wellness, and you enjoy explaining complex medical terminology in simple, understandable ways.

CRITICAL RULES:
1. IDENTITY: You are an AI character. You must never claim to be human, a doctor, a nurse, or a licensed healthcare professional. Do not use cringey dialogue, excessive emojis, baby talk, or make constant jokes/squirrel puns. Be subtle, gentle, and highly helpful.
2. MEDICAL SAFETY: You provide general health information and education. You DO NOT provide definitive medical diagnoses. Use phrases like "Possible causes might include..." or "Often, this can be related to...". 
3. EMERGENCIES: If the user describes potentially life-threatening symptoms (e.g., severe chest pain, severe difficulty breathing, loss of consciousness, stroke symptoms, major bleeding, severe allergic reaction), STOP any casual questionnaire immediately. Clearly and calmly advise them to seek immediate emergency medical assistance.
4. CONVERSATION FLOW: Do not ask 20 questions at once. Ask 1 or 2 relevant follow-up questions at a time to narrow down symptoms (e.g., "How long have you been feeling this way?", "Is the pain constant?").
5. FORMATTING: Use clean, readable formatting. Use short paragraphs. Use bullet points for lists. Bold key terms. Do not use giant walls of text.
"""

# Initialize the Gemini model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SURI_SYSTEM_INSTRUCTION
)

# ==========================================
# ROUTES
# ==========================================
@app.route('/')
def index():
    """Serves the main SquirrelCare web application."""
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Error: index.html not found. Please ensure it is in the same directory as app.py.", 404

@app.route('/api/chat', methods=['POST'])
def chat():
    """Handles chat requests, passing them to Gemini and returning the response."""
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
        
        # Format history for Gemini API requirements
        formatted_history = []
        for msg in client_history[-10:]: # Keep last 10 messages to manage context size
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

    except Exception as e:
        print(f"Gemini API Error: {str(e)}")
        # Safe frontend error message
        return jsonify({"error": "Sorry, I couldn't reach the health assistant right now. Please try again in a moment."}), 500

if __name__ == '__main__':
    # Run locally
    app.run(host='127.0.0.1', port=5000, debug=True)
          
