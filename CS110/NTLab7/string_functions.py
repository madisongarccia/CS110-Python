def cs110_upper(string):
        capital_str=""
        for char in string:
                if (ord(char) >= 97) and (ord(char)<=122):
                        capital=ord(char)-32
                        capital_str=capital_str+chr(capital)
                else:
                        capital_str=capital_str+char
        return capital_str
cs110_upper(string)

def cs110_lstrip(string):
	new_string=""
	for char in string:
                if ord(char)!=32:
                        new_string=new_string+char
                else:
                        new_string=new_string+""
        return new_string
cs110_lstrip(string)


def cs110_replace (string,char1,char2):
	new_string=""
	for char in string:
                if char == char1:
                      char=char2
                      new_string=new_string+char
                else:
                     new_string=new_string+char
        return new_string
cs110_replace (string,char1,char2)

def cs110_in(shortString, longString):
	pass # Replace this line with code

def cs110_title (string):
	    new=""
    for char in string:
        if string[ord(char)]==32:
            string[char+1]=ord(char+1)+32
            capital=ord(char+1)+32
            new=new+capital
        else:
            new=new+char
    return new


# EXTRA CREDIT.  Implement this function only if functions 1-10 work properly
# No credit if functions 1-10 do not work properly
def cs110_remove_repeats(string):
	pass # Replace this line with code

# Do not add a main() function or any non-function code.
# Add only the code for the above functions.
