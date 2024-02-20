# Challenge title: Wimpy’s diet 

Wimpy is always hungry, but his doctor put him on a diet: he’s only allowed to eat sandwiches in a
strictly decreasing order of weight at any given meal.
His favorite restaurant, however, only serves sandwiches in a fixed order, so Wimpy has to decide which ones to pick.

You are to help him: write a program that removes sandwiches from a menu of N sandwiches so that the remaining sandwiches have the maximum possible total weight and are served in a strictly decreasing order of weight.

Example:
Given a menu of 8 sandwiches:
> 389 207 155 300 299 170 158 65

We can remove the sanwiches 207 and 155 to obtain a decreasing sequence:

 > 389 300 299 170 158 65
 
 Of maximum total weight 1381.


## Solution

 My solution is not very efficient; it tests all potential lists before discarding a value that interrupts a decreasing sequence. I can elaborate up to input 5.
