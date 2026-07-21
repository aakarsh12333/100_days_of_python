# Building a dice simulator
# Step 1 :- Importing the required modules
'''
We will import the following modules:

Tkinter: Imported to use Tkinter and make GUI applications.
Image, Imagetk: Imported from PIL, i.e. Python Imaging Library. We use it to perform operations involving images in our UI.
Random: Imported to generate random numbers.
'''
# code
import os
import tkinter
from PIL import Image, ImageTk
import random

# Step 2 :- Building a top level widget to make the main window for our application
'''
In this step, we will build the main window of our application, where the buttons, labels, and images will reside. We also give it a title by title() function.
'''
# top level widget which explains the main window of an application
root = tkinter.Tk()
root.geometry('500x500')
root.title('rolling the dice')

# Step 3 :- Designing the buttons
'''
Now, just think, what we need to roll a die? Just our hands!

The below code will add a label giving a heading to our dice simulator. Also, we will add an image area, which will display the image chosen by random numbers.
'''

# adding label with different font and formatting them to makes nice to user
HeadingLabel = tkinter.Label(root, text="Hello from DataFlair!",
                             fg="light green",
                             bg="dark green",
                             font="Helvetica 16 bold italic")
HeadingLabel.pack()

# images
image_folder = os.path.dirname(os.path.abspath(__file__))
dice = [os.path.join(image_folder, name) for name in ['die1.PNG', 'die2.PNG', 'die3.PNG', 'die4.PNG']]
# load the first image
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage
ImageLabel.pack(expand=True)

# function activated by button
def rolling_dice():
    new_image = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    ImageLabel.configure(image=new_image)
    ImageLabel.image = new_image

# adding buttons and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)
button.pack(expand=True)

# call the mainloop of Tk
# keeps window open
root.mainloop()