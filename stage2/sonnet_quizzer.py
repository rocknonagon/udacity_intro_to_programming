import os
import random
import re


def read_sonnet():
    """
    Selects a random sonnet from the directory 'sonnets'
    :return: returns a dictionary with attributes:
    text -- the lines of the sonnet
    title --  the number of the sonnet
    """
    sonnet_filename = random.choice(
        [name for name in os.listdir('sonnets') if os.path.isfile(os.path.join('sonnets', name))])
    f = open(os.path.join('sonnets', sonnet_filename), 'r')
    return {'title': sonnet_filename.strip(".txt"), 'text': f.readlines()}


def create_quiz(num_blanks=4):
    """
    Returns a quiz dictionary with attributes
    title --  the number of the sonnet being quizzed
    text -- the lines of the sonnet with four words blanked out
    answers -- the words (in order of appearance) that have been blanked out
    """
    quiz_answers = []
    sonnet = read_sonnet()
    text = sonnet.get('text')
    quiz_lines = sorted(random.sample(range(len(text)), num_blanks))
    for n in xrange(num_blanks):
        split_line = [word for word in re.split('([ \.,;])', text[quiz_lines[n]]) if word != ""]
        blank_position = random.choice([i for i in xrange(len(split_line)) if split_line[i].isalpha()])
        answer = split_line[blank_position]
        split_line[blank_position] = "___" + str(n + 1) + "___"
        text[quiz_lines[n]] = "".join(split_line)
        quiz_answers.append(answer)
    return dict(title=sonnet.get('title'), text=text, answers=quiz_answers)


def play_game(difficulty_level=3):
    """
    Given a difficulty level (equal to 0,1,2,3),
    interacts with the user to allow them chances
    at guessing the blank words in a sonnet.
    The difficulty level is just the number of hints
    that will be given.
    """
    quiz = create_quiz()
    title = quiz.get('title')
    test_text = "".join(quiz.get('text'))
    answers = quiz.get('answers')
    for blank in xrange(len(answers)):
        number_of_hints = difficulty_level
        print "*******************************************"
        print title
        print "*******************************************"
        print test_text
        print "*******************************************"
        while True:
            response = raw_input("What should go in blank number {}?\n".format(blank + 1))
            if response.lower().strip() == answers[blank].lower().strip():
                print "Well done!"
                test_text = test_text.replace("___" + str(blank + 1) + "___", answers[blank])
                break
            if number_of_hints == 3:
                print "Hint: the word begins with {}.".format(answers[blank][0])
            if number_of_hints == 2:
                print "Hint: the word is {} letters long.".format(len(answers[blank]))
            if number_of_hints == 1:
                print "Hint: the word ends with {}.".format(answers[blank][-1])
            if number_of_hints == 0:
                want_to_quit = raw_input("Would you like to give up?")
                if want_to_quit.lower().startswith("y"):
                    print "The word is {}.".format(answers[blank])
                    test_text = test_text.replace("___" + str(blank + 1) + "___", answers[blank])
                    break
            number_of_hints -= 1


def initiate_game():
    """
    prompts the user to indicate their chosen difficulty level,
    then starts a quiz.
    :return: This does not return anything.
    """
    difficulty_level = 0
    while True:
        response = raw_input("Please select a difficulty level from easy/medium/hard.\n")
        if response.lower().startswith("e"):
            difficulty_level = 3
        if response.lower().startswith("m"):
            difficulty_level = 2
        if response.lower().startswith("h"):
            difficulty_level = 1
        play_game(difficulty_level)
        response = raw_input("Would you like to play again? (y/n)\n")
        if response.lower().startswith("n"):
            break


initiate_game()
