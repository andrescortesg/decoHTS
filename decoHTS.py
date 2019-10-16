#function defined to get an array of the digits from the text
#returns a list of strings

def read_text(t):
    res_array = []
    digit = ''
    flag = False
    bit = t.read(1)
    while bit != '':
        if bit.isdigit():
            flag = True
            digit = digit + bit
        else:
            if flag:
                flag = False
                res_array.append(digit)
                digit = ''
        bit = t.read(1)
    return res_array 

#crunches the string array and returns an int array
def crunch_array(arr):
    count = 0
    num = 0
    num_arr = []
    for i in arr:
        num = num + int(i)
        count = count + 1
        if count == 3:
            num_arr.append(num)
            count = num = 0
    return num_arr

def deco(num_arr, # array of numbers 
        offset): # initial guess 
    msg = "" 
    for i in num_arr:
        msg = msg + chr(i - offset) 
    return msg

#--------------------------------------------
#script -------------------------------------
#--------------------------------------------

print("beggining to process text")
print("-------------------------")
print("-------------------------")
print("--Notes: needs more interactivity--")
print("-------------------------")
print("Reading Message...")

#fetch the values from the text (strings)
text = open('message.txt', 'r')
dig_arr= read_text(text)
text.close()

print("-------------------------")
print(" -- Message processed -- ")

#convert string to numbers 
num_arr = crunch_array(dig_arr)
print(num_arr)

print("MESSAGE: "+deco(num_arr, 762))
