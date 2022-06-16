
#! Question 1
# What would the following code generate?
#? mydict = ["name":"John", "surname":"Smith"] 
#? print(mydict) 
# 1: ["name":"John", "surname":"Smith"] 
# 2: A TypeError.
# 3: A SyntaxError
# Correct Answer: 3: A SyntaxError
#* Explanation
# A SyntaxError would be generated because when you start with square brackets Python thinks you are about to define a list, but # then you use colons instead of commas so that is not the correct syntax to define a list, thus the SyntaxError.
#! Question 2
# Here's one more challenge. What would the code generate this time?
#? a = [1, 2, 3}
# 1: A SyntaxError
# 2: A TypeError
# 3: A NameError
# Correct Answer: 1: A SyntaxError
#* Explanation
# Again you would get a SyntaxError because Python thinks you are about to define a list since you start with square brackets but # then you close the array with a curly brackets which does not follow the Python syntax rules.
#! Question 3
# What would the below code output?
#? print(John)  
# 1: John
# 2: Smith
# 3: A SyntaxError
# 4: A NameError
# Correct Answer: 4: A NameError
#* Explanation
# You would get a NameError because variable name John was not defined in the code. Don't confuse variable names with strings. # Strings have quotes, variable names don't.
#! Question 4
# What would you get this time?
#? mylist = [John, Jack, Jim] 
#? print(mylist) 
# 1: [John, Jack, Jim] 
# 2: A SyntaxError
# 3: A NameError
# 4: A TypeError 
# Correct Answer: 3: A NameError
#* Explanation
# You would get a NameError again because John, Jack, and Jim names were not defined in the script. So, as soon as Python detects # that John was not defined, it interrupts the code with a NameError and it doesn't even check the rest of the code.