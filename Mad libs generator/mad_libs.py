from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('700x700')
root.title('DataFlair - Mad Libs Generator')
root.configure(bg='white')

Label(root, text='Mad Libs Generator\nHave Fun!', font='arial 20 bold', bg='white').pack(pady=10)
Label(root, text='Choose a story:', font='arial 15 bold', bg='white').pack()

selected_story = StringVar(value='story_1') # here i used stringVar which help me to store value intead of input()
entry_fields = []  # to enter value 

entry_frame = Frame(root, bg='white') # defining our input window how does it looks
entry_frame.pack(pady=10) 

output_frame = Frame(root, bg='white') # designing output frame
output_frame.pack(pady=10)

Label(output_frame, text='Your Story:', font='arial 12 bold', bg='white').pack(anchor='w')
output_text = Text(output_frame, width=80, height=12, font='arial 11', wrap=WORD)
output_text.pack()


def clear_fields():
    for widget in entry_frame.winfo_children():
        widget.destroy()
    entry_fields.clear()

# We take the input from the user and define an story using loops we have designed an algorithm
def show_story_fields(story_name):
    clear_fields()
    selected_story.set(story_name)

    if story_name == 'story_1':
        prompts = [
            'animal name', 'profession name', 'cloth name', 'thing name',
            'name', 'place name', 'verb in ing form', 'food name'
        ]
    elif story_name == 'story_2':
        prompts = [
            'adjective', 'color name', 'thing name', 'place name', 'person name',
            'another adjective', 'insect name', 'food name', 'verb name'
        ]
    else:
        prompts = [
            'person name', 'color', 'food name', 'adjective', 'thing name',
            'place', 'verb', 'adverb', 'food name', 'thing name'
        ]

    for index, prompt in enumerate(prompts):
        Label(entry_frame, text=f'{prompt.capitalize()}:', bg='white', font='arial 10').grid(row=index, column=0, padx=10, pady=5, sticky='w')
        entry = Entry(entry_frame, width=35, font='arial 10')
        entry.grid(row=index, column=1, padx=10, pady=5)
        entry_fields.append(entry)


# this step helps us to generate the story
def generate_story():
    if not entry_fields:
        messagebox.showwarning('No Story Selected', 'Please choose a story first.') # Messagebox is shown in the GUI so that user can input an 
        return

    values = [field.get().strip() for field in entry_fields]
    if any(value == '' for value in values):
        messagebox.showwarning('Missing Input', 'Please fill in all fields before generating the story.')
        return

    if selected_story.get() == 'story_1':
        story = (
            f"say {values[7]}, the photographer said as the camera flashed! "
            f"{values[4]} and I had gone to {values[5]} to get our photos taken on my birthday. "
            f"The first photo we really wanted was a picture of us dressed as {values[0]} "
            f"pretending to be a {values[1]}. When we saw the second photo, it was exactly what I wanted. "
            f"We both looked like {values[3]} wearing {values[2]} and {values[6]} -- exactly what I had in mind."
        )
    elif selected_story.get() == 'story_2':
        story = (
            f"Last night I dreamed I was a {values[0]} butterfly with {values[1]} splashes that looked like {values[2]}. "
            f"I flew to {values[3]} with my best friend and {values[4]} who was a {values[5]} {values[6]}. "
            f"We ate some {values[7]} when we got there and then decided to {values[8]} and the dream ended when I said -- let's {values[8]}."
        )
    else:
        story = (
            f"Today we picked apples from {values[0]}'s orchard. I had no idea there were so many different varieties of apples. "
            f"I ate {values[1]} apples straight off the tree that tasted like {values[2]}. Then there was a {values[3]} apple "
            f"that looked like a {values[4]}. When our bag was full, we went on a free hay ride to {values[5]} and back. "
            f"It ended at a hay pile where we got to {values[6]} {values[7]}. I can hardly wait to get home and cook with the apples. "
            f"We are going to make apple {values[8]} and {values[9]} pies!"
        )

    output_text.delete('1.0', END)
    output_text.insert(END, story)


Button(root, text='The Photographer', font='arial 15', command=lambda: show_story_fields('story_1'), bg='ghost white').pack(pady=5)
Button(root, text='The Butterfly', font='arial 15', command=lambda: show_story_fields('story_2'), bg='ghost white').pack(pady=5)
Button(root, text='Apple Orchard', font='arial 15', command=lambda: show_story_fields('story_3'), bg='ghost white').pack(pady=5)
Button(root, text='Generate Story', font='arial 15 bold', command=generate_story, bg='light blue').pack(pady=10)

show_story_fields('story_1')
root.mainloop()