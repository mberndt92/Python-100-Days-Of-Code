
# Quiz

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
results = question_data['results']
for question in results:
    model = Question(text=question['question'], answer=question['correct_answer'])
    question_bank.append(model)

brain = QuizBrain(question_bank)
brain.next_question()