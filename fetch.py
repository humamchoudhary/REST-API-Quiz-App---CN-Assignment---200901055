import json
import random

def get_quiz_question():
    with open('questions.json', 'r') as f:
        quiz = json.load(f)
        questions = quiz['questions']
    if len(questions) < 1:
        return {"code": 1, "message": "Not enough questions in the file"}
    question = random.choice(questions)
    if len(question['options']) < 4:
        return {"code": 2, "message": "Not enough answer options for the question"}
    random.shuffle(question['options'])
    response = {
        "code": 0,
        "message": "Question fetched successfully",
        "data": {
            "question": question['question'],
            "options": question['options']
        }
    }

    return response

if __name__ == '__main__':
    result = get_quiz_question()
    print(result)
