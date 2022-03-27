# Instructions

### You are provided 2 TXT files
- Sample Question File_q.txt
- Sample Solution File_s.txt

You need to process those files, and generate the final CSV whose format can be referred from `Sample Expected Output.csv` file.

Pointers to understand the flow
1. Each question will have `@@@` and `###` and `a numeric digit` which can be ignored for now.
    - `@@@` - marks end of question body and beginning of options (if any)
    - `###{numeric_digit}` - marks end of question and beginning of next question.
2. While extracting options from question, option tags like `(a), (b), (c), (d) should not be extracted along with option text.
    - Each option will start in new line, each question will start in new line.
3. Each solution `###{numeric_digit}` which marks end of solution and beginning of next solution.
4. Every question/solution number will be followed by `.`(dot) and then ` `(space)
5. Every answer key will be enclosed in `()` in txt file.
6. If a question contains options, then `question type` is `Single Correct`
    - else, `question type` is `Numerical`

### Please compare the expected output csv file and given input txt files, to get better understanding of the pattern.

## Submission
1. python code file 
2. Final CSV File
