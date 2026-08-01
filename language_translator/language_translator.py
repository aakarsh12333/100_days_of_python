from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

# Language mapping for the dropdowns
language = LANGUAGES
lang_value = list(language.values())
lang_code = {value: key for key, value in language.items()}

# Create main window
window = Tk()
window.title('Language Translator')
window.minsize(600, 500)
window.maxsize(600, 500)

# Source language dropdown
combo1 = ttk.Combobox(window, values=lang_value, state='readonly')
combo1.place(x=100, y=20, width=150)
combo1.set('choose a language')

# Input text area
f1 = Frame(window, bg='black', bd=4)
f1.place(x=100, y=100, width=150, height=150)
text1 = Text(f1, font='Roboto 14', bg='white', relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=140, height=140)

# Target language dropdown
combo2 = ttk.Combobox(window, values=lang_value, state='readonly')
combo2.place(x=300, y=20, width=150)
combo2.set('choose a language')

# Output text area
f2 = Frame(window, bg='black', bd=4)
f2.place(x=300, y=100, width=150, height=150)
text2 = Text(f2, font='Roboto 14', bg='white', relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=140, height=140)

# Translate button
button = Button(window, text='Translate', font=('normal', 15), bg='yellow')
button.place(x=220, y=300)


def translate():
    try:
        source_text = text1.get('1.0', END).strip()
        source_lang = combo1.get().strip()
        target_lang = combo2.get().strip()

        if not source_text:
            messagebox.showwarning('Empty text', 'Please enter text to translate.')
            return

        if source_lang == 'choose a language':
            source_code = None
        else:
            source_code = lang_code.get(source_lang)

        if target_lang == 'choose a language':
            messagebox.showwarning('Select language', 'Please choose a target language.')
            return

        target_code = lang_code.get(target_lang)
        translator = Translator()
        result = translator.translate(source_text, src=source_code, dest=target_code)

        text2.delete('1.0', END)
        text2.insert(END, result.text)

    except Exception as e:
        messagebox.showerror('Translation error', f'Try again.\n{e}')


button.config(command=translate)
window.mainloop()