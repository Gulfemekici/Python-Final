class Question:
    def __init__(self, question, option1, option2, option3, option4, correct_answer):
        """
        Initialize a Question instance with the provided data.

        Parameters:
        - question (str): The trivia question.
        - option1, option2, option3, option4 (str): The possible answer options.
        - correct_answer (int): The correct answer index (1-4).
        """
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4
        self.correct_answer = correct_answer

    def get_question(self):
        # Retrieve the trivia question.

        return self.question

    def get_options(self):
        # Retrieve the list of possible answer options.

        return [self.option1, self.option2, self.option3, self.option4]

    def get_correct_answer(self):
        # Retrieve the correct answer index.

        return self.correct_answer

    def set_question(self, question):
        # Set a new trivia question.

        self.question = question

    def set_options(self, option1, option2, option3, option4):
        # Set new possible answer options.

        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.option4 = option4

    def set_correct_answer(self, correct_answer):
        # Set a new correct answer index.

        self.correct_answer = correct_answer


def run_trivia_game(questions):
    # Run a trivia game with the provided list of Question objects.

    # Parameters: questions (list): List of Question objects.

    player1_score = 0
    player2_score = 0

    for i, question in enumerate(questions, start=1):
        print(f"Question {i}: {question.get_question()}")
        options = question.get_options()

        for j, option in enumerate(options, start=1):
            print(f"{j}. {option}")

        # Get player 1's answer
        player1_answer = int(input("Player 1, enter your answer (1-4): "))
        if player1_answer == question.get_correct_answer():
            player1_score += 1

        # Get player 2's answer
        player2_answer = int(input("Player 2, enter your answer (1-4): "))
        if player2_answer == question.get_correct_answer():
            player2_score += 1

        print()

    print("Game Over! Results:")
    print(f"Player 1 Score: {player1_score}")
    print(f"Player 2 Score: {player2_score}")

    if player1_score > player2_score:
        print("Player 1 wins!")
    elif player2_score > player1_score:
        print("Player 2 wins!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    # Create trivia questions
    questions_data = [
        ("Which city is the capital of Turkey?", "Istanbul", "Ankara", "Izmir", "Antalya", 2),
        ("What is the famous historical site in Ephesus?", "Hagia Sophia", "Library of Celsus", "Topkapi Palace",
         "Blue Mosque", 2),
        # and more questions...
    ]

    trivia_questions = [Question(*data) for data in questions_data]

    # Run the trivia game with the created questions
    run_trivia_game(trivia_questions)
