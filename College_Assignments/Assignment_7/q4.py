# Sequences of questions and corresponding answers
questions = ["What is your name?", "How old are you?", "Where do you live?"]
answers = ["Surajit", "21", "West Bengal"]

# Use zip() to combine questions and answers
qa_series = zip(questions, answers)

# Print the question-answer series
print("Question-Answer Series:")
for question, answer in qa_series:
    print(f"Q: {question}")
    print(f"A: {answer}")
    print()  # Adding a new line for better formatting
