# Step 1 : - Importaing all Libraries

from tkinter import *  # to make simple GUI interface using python
import random  # with the help of random module we will make our computer so that it can select randomly

# step 2 : - Initialize Window 

root = Tk()
root.geometry('500x500') # windows height and width
root.resizable(0,0) # by this command we fix the size of the window
root.title('dataflair-Rock,Paper,scissors') # This is the title which is show in the GUI as "As the heading"
root.config(bg='seashell3') # It is the property of Tkinter which is used to display background color

# know i will show the text which user can't change


Label(root, text='Rock, Paper ,Scissors' , font='arial 20 bold ', bg= 'seashell2').pack()



'''
here are other information in above code which u have to know :-
root :- is the name of our window
text :- which displays on the label as the title of that label
font :- in which form the text is written
pack :- used to the organized widget in form of block
'''

# step 3 :- know generating user choice 


user_take = StringVar()
Label(root, text='choose any one: rock, paper, scissors', font='arial 15 bold', bg='seashell2').place(x=20, y=70)
Entry(root, font='arial 15', textvariable=user_take, bg='antiquewhite2').place(x=90, y=130)

# step 4 :- For computer choice

def comp_choice():
    return random.choice(['rock', 'paper', 'scissors'])


# step 5 :- function to start Game
Result = StringVar()

def play():
    user_pick = user_take.get().strip().lower()
    comp_pick = comp_choice()
    if user_pick == comp_pick:
        Result.set('tie, you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you lose, computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win, computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you lose, computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win, computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you lose, computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win, computer select paper')
    else:
        Result.set('invalid: choose anyone -- rock, paper, scissors')



# Step 6 :- Function to Reset
def Reset():
    Result.set("") 
    user_take.set("")


# Step 7 :- Function to Exit
def Exit():
    root.destroy() # will quit the rock paper scissors program by stopping the mainloop().


# Step 8 :- Define Buttons
Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='antiquewhite2',width = 50,).place(x=25, y = 250)

Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell4' ,command = play).place(x=150,y=190)

Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell4' ,command = Reset).place(x=70,y=310)

Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell4' ,command = Exit).place(x=230,y=310)


root.mainloop()

'''
Button() widget used when we want to display a button.
command called the specific function when the button will be clicked.
root.mainloop() method executes when we run our program.
'''