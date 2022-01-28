# Wordle Solver
A simple program to help you solve most (if not all) Wordle games in under 6 attempts.

## How to use
1. Run ```$ python app.py```
2. A random 5-letter word will be generated. Input the suggested word or your own word in Wordle.
3. After submitting in Wordle, input the results in the terminal. Let's say our attempt is 'HYPER' and the correct answer is 'HAPPY'.
    - Correct (i.e. green words): h_p__
    - Semicorrect (i.e. yellow words): _ y___
    - Incorrect (i.e. grey words): er
4. Based on the inputted results, a new suggested word will be generated. 
5. Repeat Step 3 & 4 until you get the answer or until you reach the max no. of attempt!