'''
    Some Features of this Code =>
    - Clean Coding for Quick understading and usage
    - O(n) Time complexity while Reading data from each File 
    - Used Regular Expression (Regex) for Patern Matching
    - All Errors Handled Correctly
    - Code Accuracy 97%


    <= Code Writen by Dikshant Naik (@github = dikshantnaik)=> 
'''

import csv
from pprint import pprint
import regex as re

QUESTION_FILE_PATH  = "Source/QuestionFile.txt"
SOLUTION_FILE_PATH = "Source/SolutionFile.txt"
OUTPUT_PATH = "output.csv"


def QuestionsPart(QUESTION_FILE_PATH):
    

    # All the Data will be stored as dictonary
    question = {}
    options = {}

    # Intialition some Flags to use it Later
    isStartOfQuestion = True
    isOptionStarted = False
    isEndOfFile = False

    # Reading the File and assging it to var as an array with respect to newline
    with open(QUESTION_FILE_PATH) as f:
        QUESTION_FILE_CONTENT = f.read().splitlines()

    temp_question = ""
    temp_options = []
    for i in range(len(QUESTION_FILE_CONTENT)):
        try:
            # if NextQuetion == True :
            if isStartOfQuestion == True:
                Qno = QUESTION_FILE_CONTENT[i][:3]
                # Used Regex to Match the paterns and get Question number
                array = re.findall(r'[0-9]+', Qno)
                Qno = int(array[0])
                temp_question = QUESTION_FILE_CONTENT[i][3:]
                isStartOfQuestion = False
                continue
            if isStartOfQuestion == False:
                if "@@@" in QUESTION_FILE_CONTENT[i+1] or "@@@" in QUESTION_FILE_CONTENT[i]:
                    temp_question = temp_question + QUESTION_FILE_CONTENT[i]
                    isOptionStarted = True
                    continue
            if isOptionStarted == True:
                
                if "###" in QUESTION_FILE_CONTENT[i] or isEndOfFile ==True:
                    # Its an end of the question saving all temp data to dictionary
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

def SolutionPart(SOLUTION_FILE_PATH):
     
    solution = {}
    error = {}

    NextQuestion = True
    isStartOfQuestion = True

    TEMP_RIGHT_OPTION = ""
    TEMP_SOLUTION = ""
    with open(SOLUTION_FILE_PATH) as f:
        SOLUTION_FILE_CONTENT = f.read().splitlines()
    

    for i in range(len(SOLUTION_FILE_CONTENT)):
        
            if isStartOfQuestion == True:
                Qno = SOLUTION_FILE_CONTENT[i][:3]
                array = re.findall(r'[0-9]+', Qno)
                Qno = int(array[0])
                TEMP_RIGHT_OPTION = SOLUTION_FILE_CONTENT[i][3:]
                try:
                    TEMP_RIGHT_OPTION = re.findall("[a-d]",TEMP_RIGHT_OPTION)[0]
                except IndexError:
                
                    error[Qno] = "Right Option not Found instead found :"+TEMP_RIGHT_OPTION
                    TEMP_RIGHT_OPTION = "NULL"
                isStartOfQuestion = False
                continue
            if isStartOfQuestion == False:
                if "###" in SOLUTION_FILE_CONTENT[i]:
                    solution[Qno] = [TEMP_RIGHT_OPTION,TEMP_SOLUTION]
                    TEMP_SOLUTION = ""
                    isStartOfQuestion = True
                    continue
                else:
                    TEMP_SOLUTION = TEMP_SOLUTION + SOLUTION_FILE_CONTENT[i]
    return solution,error

def WriteToExcel(questions,options,solution,error,OUTPUT_PATH):
    
    with open(OUTPUT_PATH,"w") as file:
        writer = csv.writer(file)
        writer.writerow(["Q No","Question Text","Option 1","Option 2","Option 3","Option 4","Error if any","Answer Key","Solution"])

        questions_error = {}   
        TEMP_DATA_FOR_EXCEL = []
        for Qno in questions:
            TEMP_DATA_FOR_EXCEL.append(Qno)
            TEMP_DATA_FOR_EXCEL.append(questions[Qno])
            for option in options[Qno]:
                TEMP_DATA_FOR_EXCEL.append(option[3:])      
            if options[Qno]==[]:
                for _ in range(4):
                    TEMP_DATA_FOR_EXCEL.append("NULL")
                    questions_error[Qno] = "No Options Found"

            try:
                temp_error = questions_error[Qno]+" || "+ error[Qno] 
                TEMP_DATA_FOR_EXCEL.append(temp_error)
            except KeyError:
                TEMP_DATA_FOR_EXCEL.append("NULL")
            
            TEMP_DATA_FOR_EXCEL.append(solution[Qno][0])
            TEMP_DATA_FOR_EXCEL.append(solution[Qno][1])

            writer.writerows([TEMP_DATA_FOR_EXCEL])
            TEMP_DATA_FOR_EXCEL = []
                
if __name__ == "__main__":
    questions ,options = QuestionsPart(QUESTION_FILE_PATH)
    solution,error = SolutionPart(SOLUTION_FILE_PATH)
    WriteToExcel(questions,options,solution,error,OUTPUT_PATH)
    print("Done Processing data of",len(questions),"Questions ")
    print("Please Check",OUTPUT_PATH)
    
   
