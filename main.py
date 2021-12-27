# from data import question_data
from data import new_questions
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in new_questions:
    question_bank.append(Question(question['question'], question['correct_answer']))

quiz_b = QuizBrain(question_bank)

while quiz_b.still_has_questions():
    quiz_b.next_question()

# print(new_questions)
print("You've completed the quiz")
print(f"Your final score was {quiz_b.score}/{quiz_b.question_number}")