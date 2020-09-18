# DBS-snake-game-challenge

Probably all of us remember a game called snake, where you have to eat as many apples as you can. As you may have guessed it, your task is to write a program which determines whether our snake wins the game or it ends up eating itself. Snake moves along an infinitely large board. It can turn left, right or go straight. Also, the snake – when going straight – can eat an apple under the condition that it is in front of him. If such a scenario occurs our friend extends onto a cell where the meal took place. The initial snake length is 1.

## Input

The first line of the input contains number of tests t (t<1001). Each of the next t lines consists of an integer n (n<2401) and n characters describing snake's movements. Each character is one of four letters: 'L','R','F','E'.

'L' - snake goes on the field on his left
'R' - snake goes right
'F' - snake goes on the field in front of him
'E' - like 'F' but with eating an apple

## Output

For each test you should print YES if the snake survived the current game without dying or otherwise print number of the step in which the snake bites itself.

## Example

Input:

2
6 FLERFF
8 EEEELLLL

Output:

YES
7
