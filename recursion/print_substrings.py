'''
Print all sub-string of a string : so basically print all subsets of a string

every single element or combinatio of elements from string is a subset of string including empty string
'''

def sub_string(input_string:str, index:int, result:str):
    # base case : if index increased to len of input then we have addressed each element, so return
    if (index == len(input_string)):
        print(result)
        return # return to stop the recursive stack


    char = input_string[index] 
    sub_string(input_string, index+1, result+char) # include it
    sub_string(input_string, index+1, result) 

# input_string = "abc"
# sub_string(input_string, 0, "")


## strings are immuatable in python so its already a backtracking as everytime we create a new result+char, it creates new string
## to explicit include the backtracking, we need to implement mutable obj, such as list. Below is the example

def sub_string_backtracking(string:str, index:int, result:list):
    if index == len(string):
        print("".join(result)) 
        return 

    char = string[index] 

    # include the characters
    result.append(char)
    sub_string_backtracking(string, index+1, result)

    # exclude it
    result.pop() 
    sub_string_backtracking(string, index+1, result) 

string = "abc" 
sub_string_backtracking(string, 0, []) 
