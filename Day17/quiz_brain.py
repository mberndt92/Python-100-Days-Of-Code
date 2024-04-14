
class QuizBrain:

    def __init__(self, questions):
        self.questions = questions
        self.question_number = 0
        self.score = 0

    def next_question(self):
        if self.question_number >= len(self.questions):
            print(f"Your final score is: {self.score}/{self.question_number}")
            exit()
        question = self.questions[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number}: {question.text} (True/False): \n")
        if response == question.answer:
            print("You got it right!")
            self.score += 1
        print(f"The correct answer was: {question.answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        self.next_question()

