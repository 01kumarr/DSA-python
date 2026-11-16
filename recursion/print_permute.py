'''
Print all permutes of the string : permutation are re-arrangement of members
eg : abc : start with a, and swap bc -- > abc, acb
           start with b, and swap ac --> bac, bca
           start with c, and swap ab -- > cab, cba
'''

def print_permutation(input_str:str, output_str:str):
    # base case, input_str will keep on decreasing
    if len(input_str) == 0:
        print(output_str)
        return 

    for i, char in enumerate(input_str):
        new_str = input_str[0:i]+input_str[i+1:] # creating new string by removing char at poiter
        print_permutation(new_str, output_str+char) # creating new string in memory.

string = "abc" 
output = "" 
# print_permutation(string, output)

## the above approach is fine but it create new string at every recursive stack
## fix, use mutable obj and and backtrack if not required

def permute_backtracking(chars:list, index:int):
    if index == len(chars):
        print("".join(chars))
        return 

    for i in range(index, len(chars)):
        # swap the current element to the current index 
        chars[i], chars[index] = chars[index], chars[i]

        # call the recursion
        permute_backtracking(chars, index+1)

        # backtrack 
        chars[i], chars[index] = chars[index], chars[i] 

permute_backtracking(list("abc"), 0)


## yield method to print on the fly

def permute(string:str, output:str):
    if len(string) == 0:
        yield output
        return 

    for i, char in enumerate(string):
        new_string = string[0:i] + string[i+1:] 
        yield from permute(new_string, output+char) 


for p in permute("abc", ""):
    print(p)