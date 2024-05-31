from flask import Flask, request, jsonify
from flask_cors import CORS
import openai


app = Flask(__name__)
CORS(app)

# Substitua 'your-openai-api-key' pela sua chave API real do OpenAI.
openai.api_key = 'sk-proj-0ElB2AkHOQflRoNXXaOIT3BlbkFJV2WxQkFsvYuijpFlzxCf'

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    name = data['name']
    question = data['question']

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": question}]
    )

    answer_text = response.choices[0].message.content
    answer = f"Olá {name}, {answer_text}"

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
