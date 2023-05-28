from flask import Flask, request, jsonify, render_template
import openai
openai.api_key = 'open api key'


app = Flask(__name__)


def summarise(text):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=f"{text}\n\nSummarize and keep it short!:",
      temperature=0.3,
      max_tokens=100
    )

    return response.choices[0].text.strip()

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    summarized_text = summarise(data['text'])
    return jsonify({'summary': summarized_text})



@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
