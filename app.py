from flask import Flask, request, jsonify
import json
import random

app = Flask(__name__, static_folder='.')

# Load questions from JSON file
with open('questions.json') as f:
    data = json.load(f)

# Endpoint to get random questions for the quiz
@app.route('/quiz', methods=['POST'])
def quiz():
    num_questions = int(request.form['num_questions'])
    questions = random.sample(data, num_questions)
    quiz_data = []
    for q in questions:
        q_data = {}
        q_data['question'] = q['question']
        q_data['options'] = q['options']
        q_data['answer'] = q['answer']
        quiz_data.append(q_data)
    return jsonify({'quiz_data': quiz_data})

# Endpoint to check answers and calculate score
@app.route('/quiz', methods=['PUT'])
def submit():
    quiz_data = request.get_json()
    score = 0
    results = []
    for i, q in enumerate(data):
        q_result = {}
        q_result['question'] = q['question']
        q_result['selected_answer'] = quiz_data[str(i)]
        q_result['correct_answer'] = q['answer']
        if q_result['selected_answer'] == q['answer']:
            q_result['correct'] = True
            score += 1
        else:
            q_result['correct'] = False
        results.append(q_result)
    score_percentage = round(score / len(data) * 100, 2)
    return jsonify({'score': score_percentage, 'quiz_data': results})


if __name__ == '__main__':
    app.run(debug=True)