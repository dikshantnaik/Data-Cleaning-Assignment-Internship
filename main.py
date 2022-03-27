from pprint import pprint
import queue
from cv2 import TermCriteria_COUNT
import regex as re

def Questions():
    QUESTION_FILE  = "Source/QuestionFile.txt"
    options = {}
    question = {}
    NextQuetion = True
    isStartOfQuestion = True
    isOptionStarted = False
    isEndOfFile = False

    # Reading the File and assging it to var as an array with respect to newline
    with open(QUESTION_FILE) as f:
        QUESTION_FILE_CONTENT = f.read().splitlines()


    temp_question = ""
    temp_options = []
    for i in range(len(QUESTION_FILE_CONTENT)):
        try:
            # if NextQuetion == True :
            if isStartOfQuestion == True:
                Qno = QUESTION_FILE_CONTENT[i][:3]
                array = re.findall(r'[0-9]+', Qno)
                Qno = int(array[0])
                temp_question = QUESTION_FILE_CONTENT[i][3:]
                isStartOfQuestion = False
                continue
            if isStartOfQuestion == False:
                if "@@@" in QUESTION_FILE_CONTENT[i+1]:
                    temp_question = temp_question + QUESTION_FILE_CONTENT[i]
                    isOptionStarted = True
                    continue
                if "@@@" in QUESTION_FILE_CONTENT[i]:
                    isOptionStarted =True
                    continue
            if isOptionStarted == True:
                
                if "###" in QUESTION_FILE_CONTENT[i] or isEndOfFile ==True:
                    question[Qno] = temp_question
                    options[Qno] = temp_options
                    temp_question = ""
                    temp_options = []
                    isStartOfQuestion = True
                    continue
                else:
                    temp_options.append(QUESTION_FILE_CONTENT[i])   
        except IndexError:
            if "###" in QUESTION_FILE_CONTENT[i] or isEndOfFile ==True:
                    question[Qno] = temp_question
                    options[Qno] = temp_options
                    temp_question = ""
                    temp_options = []
                    isStartOfQuestion = True
                    continue
            else:
                temp_options.append(QUESTION_FILE_CONTENT[i])   
            # continue

    # pprint(question)
    return question,options

def SolutionPart():
    SOLUTION_FILE = "Source/SolutionFile.txt"
    NextQuestion = True
    isStartOfQuestion = True
    with open(SOLUTION_FILE) as f:
        SOLUTION_FILE_CONTENT = f.read().splitlines()
    

    for i in range(len(SOLUTION_FILE_CONTENT)):
        try:
            if NextQuestion == True :
                if isStartOfQuestion == True:
                    Qno = SOLUTION_FILE_CONTENT[i][:3]
                    array = re.findall(r'[0-9]+', Qno)
                    Qno = int(array[0])
                    temp_question = SOLUTION_FILE_CONTENT[i][3:]
                    isStartOfQuestion = False
                    continue
                if isStartOfQuestion == False:
                    if "@@@" in SOLUTION_FILE_CONTENT[i+1]:
                        temp_question = temp_question + SOLUTION_FILE_CONTENT[i]
                        isOptionStarted = True
                        continue
                    if "@@@" in SOLUTION_FILE_CONTENT[i]:
                        continue
               
        except IndexError:
            continue

if __name__ == "__main__":
    questions ,options = Questions()
    pprint(questions)
    pprint(options)
    
    # SolutionPart()
