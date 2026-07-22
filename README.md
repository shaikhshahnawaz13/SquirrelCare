<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=soft&color=0:0B3D2E,50:145A42,100:2E7D5B&height=230&section=header&text=SquirrelCare&fontSize=72&fontColor=F4FBF7&fontAlignY=38&desc=AI-Powered%20Health%20Guidance%20with%20Suri&descAlignY=60&descSize=20&descColor=B8DDCB&animation=fadeIn"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=500&size=20&duration=3000&pause=900&color=2E7D5B&center=true&vCenter=true&width=700&lines=Meet+Suri%2C+your+AI+health+guide.;Ask.+Understand.+Learn.;Health+information%2C+made+easier+to+understand.;Powered+by+Gemini+2.5+Flash." alt="Typing SVG" />

<br/><br/>

[![Live App](https://img.shields.io/badge/OPEN_SQUIRRELCARE-LIVE-145A42?style=for-the-badge&logo=googlechrome&logoColor=white)](https://shaikhshahnawaz13.github.io/SquirrelCare)
&nbsp;
[![Backend](https://img.shields.io/badge/API-ONLINE-2E7D5B?style=for-the-badge&logo=render&logoColor=white)](https://squirrelcare.onrender.com/health)
&nbsp;
[![Gemini](https://img.shields.io/badge/AI-Gemini_2.5_Flash-4285F4?style=for-the-badge&logo=googlegemini&logoColor=white)](https://ai.google.dev/)
&nbsp;
[![License](https://img.shields.io/badge/License-MIT-6B9F85?style=for-the-badge)](LICENSE)

<br/><br/>

### 🌿 Health information should feel understandable, not overwhelming.

**SquirrelCare** is a full-stack AI health information platform built around **Suri**, an AI health guide designed to turn everyday health questions into clear, structured conversations.

Instead of immediately throwing medical terminology at the user, Suri asks relevant follow-up questions, explains possible causes in accessible language, and recognizes situations where professional or emergency medical attention may be appropriate.

<br/>

`Educational Health Information` · `Conversational AI` · `Responsive UI` · `Full-Stack` · `Free Hosting`

</div>

---

## 🐿️ Meet Suri

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Georgia&weight=400&size=24&duration=3500&pause=1200&color=145A42&center=true&vCenter=true&width=750&lines=%22Hi!+I'm+Suri.%22;%22What+health+topic+would+you+like+to+explore+today%3F%22;%22Tell+me+a+little+more+about+what+you're+feeling.%22" alt="Suri typing animation"/>

</div>

Suri is the conversational intelligence at the center of SquirrelCare.

She is designed as a **calm, curious and highly knowledgeable AI health guide** capable of discussing general health, biology and wellness while keeping explanations understandable.

Suri is intentionally designed **not** to behave like a diagnostic engine.

Instead, the conversation follows a more responsible pattern:

```text
You describe what you're experiencing
                 │
                 ▼
       Suri understands the question
                 │
                 ▼
       Relevant follow-up questions
                 │
                 ▼
       General health information
                 │
                 ▼
        Possible explanations
                 │
                 ▼
      Appropriate next-step guidance
```

### Suri's Core Behaviour

| Principle | Behaviour |
|---|---|
| 🧠 **Understand first** | Considers the user's question before generating guidance |
| 💬 **Conversational** | Asks one or two useful questions instead of interrogating the user |
| 📖 **Educational** | Explains medical concepts in understandable language |
| 🩺 **Non-diagnostic** | Discusses possibilities rather than presenting definitive diagnoses |
| 🚨 **Emergency aware** | Can prioritize urgent-care guidance for potentially dangerous symptoms |
| 🌿 **Calm communication** | Avoids unnecessarily alarming language |
| 🧒 **Distinct personality** | Suri has her own friendly and curious conversational identity |
| 📝 **Readable answers** | Uses paragraphs, emphasis and structured information |

---

# 🌱 What is SquirrelCare?

SquirrelCare started with a simple idea:

> **What if asking a basic health question felt more like having a clear conversation than searching through dozens of confusing webpages?**

Searching symptoms online can quickly become overwhelming.

A simple search such as:

```text
"Why does my head hurt?"
```

can expose someone to everything from dehydration to extremely rare diseases without context.

SquirrelCare approaches the problem differently.

Instead of treating the first message as enough information, **Suri can continue the conversation**.

For example:

```text
USER
Why does my head hurt?

            ↓

SURI
What does the headache feel like?
Is it dull, throbbing, sharp, or something else?

Where does it hurt?
Front, back, one side, or all over?

            ↓

USER
Mostly behind my head and my neck feels stiff.

            ↓

SURI
Continues the conversation using the additional context...
```

The goal is not to replace medical professionals.

The goal is to make **general health information easier to understand and interact with.**

---

# ✨ Features

<table>
<tr>
<td width="50%" valign="top">

### 🤖 Suri AI Assistant

A dedicated conversational health assistant powered by Google's Gemini model.

Suri can:

- Understand natural-language health questions
- Explain general health concepts
- Ask contextual follow-up questions
- Remember recent conversation context
- Structure complex answers
- Discuss possible causes without claiming a diagnosis

</td>
<td width="50%" valign="top">

### 🧠 Context-Aware Conversations

SquirrelCare sends recent conversation history to the backend.

This means Suri can understand:

```text
User: My neck hurts.

Suri: How long has it been hurting?

User: Since yesterday.
```

The second message is interpreted within the existing conversation instead of being treated as an unrelated question.

</td>
</tr>

<tr>
<td width="50%" valign="top">

### 🚨 Safety-Oriented Behaviour

Suri's system instructions explicitly distinguish ordinary health questions from potentially serious symptoms.

Potential emergencies can cause the normal conversational flow to be interrupted in favor of recommending immediate professional assistance.

</td>
<td width="50%" valign="top">

### 📱 Responsive Interface

The SquirrelCare interface is designed for both desktop and mobile devices.

The Suri chat experience includes:

- Responsive layout
- Chat bubbles
- Dynamic AI messages
- Loading states
- Error states
- Suggested prompts
- Conversation reset
- Touch-friendly controls

</td>
</tr>

<tr>
<td width="50%" valign="top">

### 🔐 Protected AI Credentials

The Gemini API key is **not stored in the public frontend**.

Instead:

```text
Browser
   ↓
Render Backend
   ↓
Environment Variable
   ↓
Gemini API
```

The browser never needs direct access to the private Gemini credential.

</td>
<td width="50%" valign="top">

### ☁️ Fully Deployed

SquirrelCare uses separate frontend and backend deployments.

The static frontend runs through **GitHub Pages**, while the Python API runs independently through **Render**.

</td>
</tr>
</table>

---

# 🏗️ System Architecture

<div align="center">

### From question → intelligence → response

</div>

```text
┌──────────────────────────────────────────────────────────────┐
│                         USER DEVICE                          │
│                                                              │
│                  SquirrelCare Interface                      │
│                                                              │
│             HTML + CSS + Vanilla JavaScript                  │
└─────────────────────────────┬────────────────────────────────┘
                              │
                              │ HTTPS
                              │ POST /api/chat
                              │ JSON
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                        GITHUB PAGES                          │
│                                                              │
│                   Frontend Distribution                      │
└─────────────────────────────┬────────────────────────────────┘
                              │
                              │ fetch()
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                         RENDER                               │
│                                                              │
│                 Python + Flask Backend                       │
│                                                              │
│      ┌─────────────────────────────────────────────┐         │
│      │               Flask REST API                │         │
│      │                                             │         │
│      │   /                 API information         │         │
│      │   /health           Health check            │         │
│      │   /api/chat         Suri conversations      │         │
│      └──────────────────────┬──────────────────────┘         │
│                             │                                │
│                    Gunicorn WSGI Server                      │
└─────────────────────────────┼────────────────────────────────┘
                              │
                              │ Gemini SDK
                              ▼
┌──────────────────────────────────────────────────────────────┐
│                     GOOGLE GEMINI API                        │
│                                                              │
│                     Gemini 2.5 Flash                         │
│                                                              │
│                  Suri System Instruction                     │
│                            +                                 │
│                  Conversation History                        │
│                            +                                 │
│                       User Message                           │
└─────────────────────────────┬────────────────────────────────┘
                              │
                              │ Generated response
                              ▼
                     Flask JSON Response
                              │
                              ▼
                     JavaScript Renderer
                              │
                              ▼
                         SURI REPLIES
```

---

# 🔄 Request Lifecycle

Every Suri conversation travels through several layers.

```text
1. User enters a health question
                 ↓
2. JavaScript captures the message
                 ↓
3. Recent conversation history is collected
                 ↓
4. Browser sends POST /api/chat
                 ↓
5. Flask validates the request
                 ↓
6. Conversation history is formatted
                 ↓
7. Gemini receives:
      • Suri system instruction
      • Conversation history
      • Current question
                 ↓
8. Gemini 2.5 Flash generates a response
                 ↓
9. Flask returns JSON
                 ↓
10. Frontend renders Suri's response
```

A simplified request looks like:

```json
{
  "message": "Why does my head hurt?",
  "history": []
}
```

And the backend returns:

```json
{
  "response": "There are several possible reasons for a headache..."
}
```

---

# 🧠 AI Architecture

SquirrelCare does not simply send raw prompts directly from the webpage.

Suri's behaviour is defined on the **server**.

```text
┌──────────────────────────┐
│ SURI SYSTEM INSTRUCTION  │
├──────────────────────────┤
│ Identity                 │
│ Medical safety           │
│ Emergency behaviour      │
│ Conversation style       │
│ Formatting rules         │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ CONVERSATION HISTORY     │
├──────────────────────────┤
│ User                     │
│ Model                    │
│ User                     │
│ Model                    │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ CURRENT USER MESSAGE     │
└────────────┬─────────────┘
             │
             ▼
       GEMINI 2.5 FLASH
             │
             ▼
        SURI RESPONSE
```

This separation allows Suri to maintain a more consistent identity and safety policy across conversations.

---

# 🩺 Medical Safety Design

SquirrelCare is an **educational health-information project**, not a medical diagnostic service.

Suri follows several important constraints.

### 01 · No definitive diagnosis

Instead of:

```diff
- You have migraine.
```

Suri should prefer language such as:

```diff
+ Headaches like this can have several possible causes,
+ including dehydration, tension or migraine.
```

### 02 · Context before conclusions

For ambiguous symptoms, Suri can ask relevant questions before providing more specific information.

```text
How long has this been happening?

Is the pain constant or does it come and go?

Where exactly do you feel it?
```

### 03 · Emergency escalation

Potentially dangerous symptoms are treated differently from routine questions.

Examples include:

- Severe difficulty breathing
- Loss of consciousness
- Stroke-like symptoms
- Severe chest pain
- Major bleeding
- Severe allergic reactions

The assistant is instructed to prioritize **immediate professional medical assistance** rather than continue an ordinary symptom questionnaire.

---

# 🧱 Technology Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=html,css,js,python,flask,git,github&theme=light" />

<br/><br/>

![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-4285F4?style=for-the-badge&logo=googlegemini&logoColor=white)
&nbsp;
![Render](https://img.shields.io/badge/Render-Backend-145A42?style=for-the-badge&logo=render&logoColor=white)
&nbsp;
![Gunicorn](https://img.shields.io/badge/Gunicorn-WSGI-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
&nbsp;
![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-Frontend-222222?style=for-the-badge&logo=githubpages&logoColor=white)

</div>

<br/>

| Layer | Technology | Responsibility |
|---|---|---|
| **Structure** | HTML5 | Application markup |
| **Design** | CSS3 | Responsive interface, animations and visual system |
| **Client Logic** | Vanilla JavaScript | Chat behaviour, DOM updates and API communication |
| **Backend** | Python | Server-side application logic |
| **Framework** | Flask | REST API |
| **Cross-Origin Access** | Flask-CORS | Frontend/backend communication |
| **Production Server** | Gunicorn | Runs Flask in production |
| **AI SDK** | Google Generative AI | Python ↔ Gemini communication |
| **AI Model** | Gemini 2.5 Flash | Natural-language reasoning and response generation |
| **Protocol** | REST + JSON | Client/server data exchange |
| **Secrets** | Environment Variables | Gemini credential protection |
| **Version Control** | Git | Source history |
| **Repository** | GitHub | Source-code hosting |
| **Frontend Hosting** | GitHub Pages | Public static deployment |
| **Backend Hosting** | Render | Python API deployment |

---

# 📁 Project Structure

```text
SquirrelCare/
│
├── index.html
│   ├── Application structure
│   ├── Suri chat interface
│   └── Frontend JavaScript
│
├── style.css
│   ├── Design system
│   ├── Responsive layout
│   └── Animations
│
├── app.py
│   ├── Flask application
│   ├── Gemini integration
│   ├── Suri system instructions
│   ├── Chat endpoint
│   ├── Health endpoint
│   └── Error handling
│
├── requirements.txt
│   └── Python dependencies
│
├── README.md
│
└── LICENSE
```

> The exact frontend file structure may differ depending on the current version of the repository.

---

# 🔌 Backend API

## `GET /`

Returns basic information confirming that the SquirrelCare backend is available.

Example:

```json
{
  "message": "SquirrelCare API is running. Please access the application via the frontend."
}
```

---

## `GET /health`

Used to verify whether the backend is operational.

Example response:

```json
{
  "status": "online",
  "service": "SquirrelCare Backend",
  "gemini_configured": true
}
```

Live endpoint:

**https://squirrelcare.onrender.com/health**

---

## `POST /api/chat`

The primary Suri conversation endpoint.

### Request

```json
{
  "message": "Why does my head hurt?",
  "history": [
    {
      "role": "user",
      "content": "I've been feeling tired."
    },
    {
      "role": "model",
      "content": "How long have you been feeling this way?"
    }
  ]
}
```

### Successful response

```json
{
  "response": "Several things can contribute to headaches..."
}
```

### Invalid request

```json
{
  "error": "Message cannot be empty."
}
```

---

# 🔐 API Key Security

**Never put your Gemini API key inside `index.html`, JavaScript, or a public GitHub repository.**

SquirrelCare uses a server-side environment variable:

```python
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
```

The deployment environment stores:

```text
GEMINI_API_KEY = your_private_key
```

Therefore the architecture remains:

```text
PUBLIC

Browser
   │
   ▼
GitHub Pages
   │
   │ HTTPS
   ▼

──────────────── SECURITY BOUNDARY ────────────────

PRIVATE

Render Backend
   │
   ├── GEMINI_API_KEY
   │
   ▼
Gemini API
```

The secret does not need to be shipped to the browser.

---

# 🚀 Run SquirrelCare Locally

### 1 · Clone the repository

```bash
git clone https://github.com/shaikhshahnawaz13/SquirrelCare.git
cd SquirrelCare
```

### 2 · Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 3 · Install dependencies

```bash
pip install -r requirements.txt
```

### 4 · Configure Gemini

Linux/macOS:

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

### 5 · Start Flask

```bash
python app.py
```

The development backend should then become available locally.

---

# 📦 Python Dependencies

```txt
Flask
Flask-Cors
google-generativeai
gunicorn
```

| Package | Purpose |
|---|---|
| `Flask` | Backend web framework |
| `Flask-Cors` | Cross-origin request handling |
| `google-generativeai` | Gemini integration |
| `gunicorn` | Production WSGI server |

---

# ☁️ Deployment

SquirrelCare deliberately separates its static frontend from its AI backend.

## Frontend · GitHub Pages

```text
GitHub Repository
        │
        ▼
     main branch
        │
        ▼
   GitHub Pages
        │
        ▼
  SquirrelCare UI
```

## Backend · Render

Render configuration:

```text
Runtime
Python 3

Build Command
pip install -r requirements.txt

Start Command
gunicorn app:app
```

Environment:

```text
GEMINI_API_KEY = <secret>
```

After deployment:

```text
https://squirrelcare.onrender.com
```

The frontend communicates with:

```text
https://squirrelcare.onrender.com/api/chat
```

---

# 🛡️ Backend Validation

The API performs validation before forwarding messages to Gemini.

Messages must:

- Exist in the request
- Not be empty
- Be convertible to text
- Remain within the configured length limit

The backend also limits the amount of conversation history sent with each request.

This prevents an indefinitely growing conversation from being forwarded on every request.

---

# ⚠️ Error Handling

SquirrelCare separates common backend failure states.

```text
USER REQUEST
     │
     ▼
┌───────────────┐
│ VALID REQUEST?│
└───────┬───────┘
        │
    ┌───┴───┐
   NO      YES
    │        │
  400        ▼
       GEMINI REQUEST
             │
        ┌────┴────┐
      ERROR      SUCCESS
        │           │
       500          ▼
                 RESPONSE
```

The frontend converts server failures into readable interface messages instead of exposing raw Python errors to users.

---

# 🎨 Design Language

SquirrelCare intentionally avoids the typical neon AI aesthetic.

Its visual language is based around:

```text
Deep Forest Green
        +
Soft Sage
        +
Warm White
        +
Subtle Bord
