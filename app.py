from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import openai

app = Flask(__name__)
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        user_message = request.json.get('message', '')
        
        # Create chat completion with OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful problem-solving assistant. You help users break down problems and find solutions step by step."},
                {"role": "user", "content": user_message}
            ]
        )
        
        # Extract the assistant's response
        ai_response = response.choices[0].message.content
        
        return jsonify({'response': ai_response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
