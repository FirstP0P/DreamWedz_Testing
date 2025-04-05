import os
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create Flask app
app = Flask(__name__)

# Configure Gemini model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="You are a joyful chatbot named Hera for a company named DreamWedz and you are supposed to help them plan their wedding by providing them all the necessary services like guest accommodation, transportation, and other event logistics, ensuring no detail is overlooked. As Hera, your responsibilities span across all key aspects of wedding planning to ensure a seamless and memorable experience for every couple. You assist in arranging guest accommodation by booking hotel rooms or private villas and managing check-in/check-out logistics while considering guest preferences. You handle transportation services with precision, including airport pickups, shuttle coordination between venues, bridal party limousines, and even emergency transport needs. You oversee event logistics such as vendor coordination, venue setup, timeline management, and transitions between multiple wedding functions. You offer personalized assistance by providing real-time suggestions, reminders, and support for tasks like RSVP tracking, seating arrangements, makeup trials, and dress fittings. Additionally, you recommend and help book trusted vendors for catering, photography, floral design, entertainment, and decorations based on the couple style and budget. Your personality is cheerful, warm, and empathetic—always ready to reduce stress, provide thoughtful solutions, and add a personal touch to every moment. Whether couples seek support months ahead or on the big day itself, Hera is always just a message away.Remember to format the response properly because the space for text in a chatbot window is less.",
)

# Store chat sessions
chat_sessions = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    session_id = data.get('session_id', 'default')

    # Create a new chat session if it doesn't exist
    if session_id not in chat_sessions:
        chat_sessions[session_id] = model.start_chat(history=[])

    # Get response from Gemini
    response = chat_sessions[session_id].send_message(user_message)

    return jsonify({'response': response.text})

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    if not os.path.exists('templates'):
        os.makedirs('templates')

    # Write the HTML to a template file
    with open('templates/index.html', 'w', encoding='utf-8') as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DreamWedz with Hera</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f9f5f6;
        }

        .chat-circle {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background-color: #ff6b81;
            color: white;
            text-align: center;
            line-height: 60px;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            transition: all 0.3s;
            z-index: 1000;
        }

        .chat-circle:hover {
            transform: scale(1.1);
        }

        .chat-box {
            position: fixed;
            bottom: 100px;
            right: 30px;
            width: 350px;
            height: 450px;
            background-color: white;
            border-radius: 15px;
            box-shadow: 0 5px 25px rgba(0, 0, 0, 0.2);
            display: flex;
            flex-direction: column;
            overflow: hidden;
            transition: all 0.3s;
            opacity: 0;
            pointer-events: none;
            transform: translateY(20px);
            z-index: 999;
        }

        .chat-box.active {
            opacity: 1;
            pointer-events: all;
            transform: translateY(0);
        }

        .chat-header {
            background-color: #ff6b81;
            color: white;
            padding: 15px;
            text-align: center;
            font-weight: bold;
            position: relative;
        }

        .close-chat {
            position: absolute;
            right: 15px;
            top: 50%;
            transform: translateY(-50%);
            cursor: pointer;
            font-size: 18px;
        }

        .chat-messages {
            flex: 1;
            padding: 15px;
            overflow-y: auto;
        }

        .message {
            margin-bottom: 15px;
            max-width: 80%;
            padding: 10px;
            border-radius: 15px;
        }

        .bot-message {
            background-color: #f0f0f0;
            color: #333;
            margin-right: auto;
            border-bottom-left-radius: 5px;
        }

        .user-message {
            background-color: #ff6b81;
            color: white;
            margin-left: auto;
            border-bottom-right-radius: 5px;
        }

        .chat-input {
            padding: 15px;
            display: flex;
            border-top: 1px solid #eee;
        }

        .chat-input input {
            flex: 1;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 20px;
            outline: none;
        }

        .chat-input button {
            background-color: #ff6b81;
            color: white;
            border: none;
            padding: 10px 15px;
            margin-left: 10px;
            border-radius: 20px;
            cursor: pointer;
            transition: all 0.3s;
        }

        .chat-input button:hover {
            background-color: #ff5268;
        }

        .typing-indicator {
            display: none;
            padding: 10px;
            background-color: #f0f0f0;
            color: #333;
            border-radius: 15px;
            border-bottom-left-radius: 5px;
            margin-bottom: 15px;
            max-width: 80%;
            margin-right: auto;
        }

        .typing-indicator span {
            display: inline-block;
            width: 7px;
            height: 7px;
            background-color: #888;
            border-radius: 50%;
            margin-right: 3px;
            animation: typing 1s infinite;
        }

        .typing-indicator span:nth-child(2) {
            animation-delay: 0.2s;
        }

        .typing-indicator span:nth-child(3) {
            animation-delay: 0.4s;
        }

        @keyframes typing {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-5px);
            }
        }
    </style>
</head>
<body>
    <div class="chat-circle">
        <i>💬</i>
    </div>

    <div class="chat-box">
        <div class="chat-header">
            Hera - Your Wedding Assistant
            <span class="close-chat">✕</span>
        </div>
        <div class="chat-messages">
            <div class="message bot-message">
                Hi there! I'm Hera, your personal wedding planning assistant! How can I help you plan your dream wedding today?
            </div>
            <div class="typing-indicator">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
        <div class="chat-input">
            <input type="text" placeholder="Type your message...">
            <button>Send</button>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const chatCircle = document.querySelector('.chat-circle');
            const chatBox = document.querySelector('.chat-box');
            const closeChat = document.querySelector('.close-chat');
            const chatInput = document.querySelector('.chat-input input');
            const sendButton = document.querySelector('.chat-input button');
            const chatMessages = document.querySelector('.chat-messages');
            const typingIndicator = document.querySelector('.typing-indicator');

            // Generate a unique session ID
            const sessionId = 'session_' + Date.now();

            // Toggle chat box visibility
            chatCircle.addEventListener('click', function() {
                chatBox.classList.add('active');
                chatCircle.style.display = 'none';
                chatInput.focus();
            });

            closeChat.addEventListener('click', function() {
                chatBox.classList.remove('active');
                chatCircle.style.display = 'block';
            });

            // Send message function
            async function sendMessage() {
                const message = chatInput.value.trim();
                if (message === '') return;

                // Add user message to chat
                const userMessageDiv = document.createElement('div');
                userMessageDiv.classList.add('message', 'user-message');
                userMessageDiv.textContent = message;
                chatMessages.appendChild(userMessageDiv);

                // Clear input
                chatInput.value = '';

                // Scroll to the bottom
                chatMessages.scrollTop = chatMessages.scrollHeight;

                // Show typing indicator
                typingIndicator.style.display = 'block';

                try {
                    // Send message to backend
                    const response = await fetch('/api/chat', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            message: message,
                            session_id: sessionId
                        })
                    });

                    const data = await response.json();

                    // Hide typing indicator
                    typingIndicator.style.display = 'none';

                    // Add bot response
                    const botMessageDiv = document.createElement('div');
                    botMessageDiv.classList.add('message', 'bot-message');
                    botMessageDiv.textContent = data.response;
                    chatMessages.appendChild(botMessageDiv);

                } catch (error) {
                    console.error('Error:', error);
                    // Hide typing indicator
                    typingIndicator.style.display = 'none';

                    // Add error message
                    const botMessageDiv = document.createElement('div');
                    botMessageDiv.classList.add('message', 'bot-message');
                    botMessageDiv.textContent = "Sorry, I'm having trouble connecting. Please try again later.";
                    chatMessages.appendChild(botMessageDiv);
                }

                // Scroll to the bottom again
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }

            // Send message on button click
            sendButton.addEventListener('click', sendMessage);

            // Send message on Enter key
            chatInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    sendMessage();
                }
            });
        });
    </script>
</body>
</html>''')

    app.run(debug=True)
