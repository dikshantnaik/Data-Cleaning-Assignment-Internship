import csv
from pprint import pprint
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
    solution = {}
    error = {}
    # {
    #     1:["a","Solution explaiation "]
    # }
    NextQuestion = True
    isStartOfQuestion = True

    TEMP_RIGHT_OPTION = ""
    TEMP_EXPLANATION = ""
    with open(SOLUTION_FILE) as f:
        SOLUTION_FILE_CONTENT = f.read().splitlines()
    

    for i in range(len(SOLUTION_FILE_CONTENT)):
        
        # try:
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
                # print(TEMP_RIGHT_OPTION)
                isStartOfQuestion = False
                continue
            if isStartOfQuestion == False:
                if "###" in SOLUTION_FILE_CONTENT[i]:
                    # temp = 
                    solution[Qno] = [TEMP_RIGHT_OPTION,TEMP_EXPLANATION]
                    TEMP_EXPLANATION = ""
                    isStartOfQuestion = True
                    continue
                else:
                    TEMP_EXPLANATION = TEMP_EXPLANATION + SOLUTION_FILE_CONTENT[i]
            # if i == 30:
            #     break
        # except IndexError as e: 
        #     print(e)
            # continue
    # pprint(solution)
    return solution,error

def WriteToExcel(questions,options,solution,error):
    
    with open("text.csv","w") as file:
        writer = csv.writer(file)
        writer.writerow(["Qno","Question Text","Option 1","Option 2","Option 3","Option 4","Error if any","Answer Key","Solution"])

        questions_error = {}   
        temp_array = []
        # print(questions)
        for Qno in questions:
            temp_array.append(Qno)
            temp_array.append(questions[Qno])
            # temp_array.append()
            for option in options[Qno]:
                # print(option)
                temp_array.append(option[3:])      
            if options[Qno]==[]:
                for _ in range(4):
                    temp_array.append("NULL")
                    questions_error[Qno] = "No Options Found"

            try:
                temp_error = questions_error[Qno]+" || "+ error[Qno] 
                temp_array.append(temp_error)
            except KeyError:
                temp_array.append("NULL")
            
            temp_array.append(solution[Qno][0])
            temp_array.append(solution[Qno][1])

            # if Qno==2:
            #     break
            # print(type(temp_array[3]))
            # print(temp_array[5])
            writer.writerows([temp_array])
            temp_array = []
                
if __name__ == "__main__":
    questions ,options = Questions()
    solution,error = SolutionPart()
    WriteToExcel(questions,options,solution,error)
    
   
