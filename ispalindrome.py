inp_str = int(input("Enter number : "))
str_inp = str(inp_str)
if str( inp_str) == str_inp[::-1]:
    print(inp_str , "is a palindrome")
else:
    print(inp_str," is not Palindrome")