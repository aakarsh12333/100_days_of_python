# Step 1 :- Import Library
from tkinter import *
import base64 # it will encode our binary data into ASCII character and decode that ASCII characters back to binary data

# Step 2 :- Initialize Window
root = Tk()

root.geometry('500x500')
root.resizable(0,0)
root.title("DataFlair - Message Encode and Decode")

'''
tk() -> iniatialized tkinter which means window created
geometry() -> set the width and height of the window.
resizable(0,0) -> set the fixed size of the window.
title() -> set the title of the window.
'''

Label(root, text='ENCODE DECODE', font= 'arial 20 bold').pack()

Label(root, text='DataFlair', font= 'arial 20 bold').pack(side=BOTTOM)

'''
Label() widget use to display one or more than one line of text that users aren’t able to modify.

root is the name which we refer to our window
text which we display on the label
font in which the text is written
pack organized widget in block
'''

# Step 3 :- Define Variables
Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

'''
Text -> variable stores the message to encode and decode.
private_key -> variable store the private key used to encode and decode.
mode -> is used to select that is either encoding or decoding.
Result -> store the result.
'''


# Step 4 :- Function to encode
def Encode(key,message):
    enc = []

    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        return
    base64.urlsafe_b64encode("".join(enc).encode()).decode()
'''
Encode function have arguments key and message

•enc = [] is an empty list
•We run loop till the length of the message
i% of len(key) gives the remainder of division between i and len(key) and that remainder used as an index of key the value of key at that index is stored in key_c
•ord() function takes string argument of a single unicode character and return its integer unicode value
•chr() function takes an integer argument and returns the string.
•ord (message[i]) convert the value of message at index i into the integer value
•ord(key_c) converts the key_c value to integer value
•ord(message[i]) + ord(key_c)) % 256 gives the remainder of division of addition of ord(message[i]) and ord( key_c) with 256 and passes that remainder to chr() function
•chr() function converts that integer value to string and store to enc
base64.urlsafe_b64encode encode a string.
•The join() method joins each element of list, string, and tuple by a string separator and returns the concatenated string.
•encode() method returns utf-8 encoded message of the string.
•decode() method decodes the string.
return gives the result of the encoded string.
'''

# step 5 :- Function to decode
def Decode(key,message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)


'''
Decode() function has arguments – key, message

•dec=[] is an empty list
•Decode the content from input and write the result in binary to the output
•We ran the loop till the length of the message
•256 + ord(message[i]) – ord(key_c)) % 256 gives the remainder of addition of 256 with subtraction of ord(message[i]) – ord( key_c) and then division with 256 and passes that remainder to chr() function
•chr() function convert integer value to string and store to dec
•return “”.join(dec) return the result
'''

# Step 6 :- Function to set mode

def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(),Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

'''
•If the mode set by the user is e then the Encode() function will be called
•If the mode set to d then the Decode() function will be called
•Else print invalid mode
•private_key.get() and Text.get() values are pass to the arguments of Encode() and Decode() function
'''

# Step 7 :- Function to exit window
def Exit():
    root.destroy()
# root.destroy() will quit the program by stopping the mainloop()


# Step 8 :- Function to reset window
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")
# This function set all variables to empty string

# Step 9 :- Labels and Buttons
Label(root, font= 'arial 12 bold',text='MESSAGE').place(x=60,y=60)
Entry(root, font= 'arial 10', textvariable=Text, bg ='ghost white').place(x=290, y=60)
Label(root, font = 'arial 12 bold', text ='KEY').place(x=60, y = 90)
Entry(root, font = 'arial 10', textvariable = private_key , bg ='ghost white').place(x=290, y = 90)
Label(root, font = 'arial 12 bold', text ='MODE(e-encode, d-decode)').place(x=60, y = 120)
Entry(root, font = 'arial 10', textvariable = mode , bg= 'ghost white').place(x=290, y = 120)
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='ghost white').place(x=290, y = 150)
Button(root, font = 'arial 10 bold', text = 'RESULT'  ,padx =2,bg ='LightGray' ,command = Mode).place(x=60, y = 150)
Button(root, font = 'arial 10 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'LimeGreen', padx=2).place(x=80, y = 190)
Button(root, font = 'arial 10 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'OrangeRed', padx=2, pady=2).place(x=180, y = 190)
root.mainloop()

'''
•Label() widget use to display one or more than one line of text that users aren’t able to modify.

•Entry() widget used to create an input text field.

•Button() widget used to display button on our window

•root is the name which we refer to our window
•text which we display on the label
•font in which the text is written
•insertwidth use to set the width of the insertion cursor
•bg sets the background colour
•command is call when the button is click
•textvariable used to retrieve the current text to the entry widget
•root.mainloop() is a method that executes when we want to run our program.
'''