from question_model import Question
from quiz_brain import QuizBrain
import requests

N_QUESTIONS = 5

new_questions = requests.get(f'https://opentdb.com/api.php?amount={N_QUESTIONS}&type=boolean').json()['results']


question_bank = []
for question in new_questions:
    question_bank.append(Question(question['question'], question['correct_answer']))

quiz_b = QuizBrain(question_bank)

while quiz_b.still_has_questions():
    quiz_b.next_question()

# print(new_questions)
print("You've completed the quiz")
print(f"Your final score is {quiz_b.score}/{quiz_b.question_number}")
