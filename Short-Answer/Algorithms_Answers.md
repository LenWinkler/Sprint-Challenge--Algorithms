#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n). It scales linearly with input size. The code runs n times.


b) I want to say O(log(n)) here because the number of operations seems to scale slower than the input. I also 
"ran" the code with pen and paper a few times and plugged the number of loops into a log2 calculator and the 
result was ~n. 


c) Unless it's invoked with 0, I think this one runs forever. The base case is bunnies == 0 but each time the 
function calls itself, it's effectively calling bunnyEars(bunnies + 1.) 

## Exercise II

In this case, I think I'd use a binary search. I'd create a list that contains the number of floors in the 
building. I would start at the middle of the list and narrow it down based on whether the egg broke or not. 

For example:
    I start in the middle of the list and the egg breaks. I know that every floor to the right of the list is too
    high so I discard the values on the right and start again at the middle of the remaining values. If the egg
    doesn't break, I discard the values on the left and start over at the middle of what remains. I would do this
    until I found f. Big O for this algorithm would be O(logn(n))
