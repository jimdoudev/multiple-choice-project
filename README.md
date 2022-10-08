# Multiple Choice Console App

This a Multiple Choice Console App I created for my MSc/ICT at UniWA in Python.

## General

There are three implemented question and answers categories[^1]. 

During each run the questions get shuffled and three of each category are randomly chosen to build the questionnaire, 
which finally consists of five questions. 

The answers to each question have been divided into three categories:
1. Right Answers
2. Semi-Right answers (not entirely wrong questions, that lead to a second chance question)
3. Wrong Answers

The player gets:
- twenty points for every correct answer
- ten points for every "second chance" question he answered correctly
- zero points for every wrong answer

In the end he gets an evaluation where he finds out his final grade and a message based on his performance.

Finally he gets a brief analysis about his performance in each of the question categories.


## Instructions

1. Clone the app to a local folder of your choice
2. Open `test.py` in your code editor
3. On lines 13, 131-136 change file paths to your local folder
4. Run `test.py` in your terminal

[^1]: - To add or remove questions just edit the desired `.txt` files in your local `q&a` folder.
      - The questions and answers have to be in the same order in each questions and answers file pair.
      - Add the characters c, s or f at the end of every line to define each answer as correct, semi-correct or wrong.
