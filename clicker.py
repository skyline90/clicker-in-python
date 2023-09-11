import tkinter
import tkinter.messagebox
import random

clicks = 0


def randomize():
    global clicks, letters, letter
    btn_click.place(x=random.randint(70, 1000), y=random.randint(70, 650))
    close_button.place(x=random.randint(70, 1000), y=random.randint(70, 650))
    clicks += 1
    label_click['text'] = str(clicks)
    label_click.pack()



window = tkinter.Tk()
window.title('Clicker')
# window.geometry('1280x720')
window.state('zoomed')
window.overrideredirect(1) # развернутая на весь экран
# window.resizable(width=False, height=False)
window.configure(bg='black')

label_click = tkinter.Label(window, text=clicks, font=(
    'Comic Sans MS', 30, 'bold'), bg='black', fg='white')
label_click.pack()

btn_click = tkinter.Button(window, text='Click', bg='lime', fg='black',
                           padx='20', pady='8', font=('Comic Sans MS', 13, 'bold'), command=randomize, activebackground='Green')
btn_click.place(x=random.randint(70, 1000), y=random.randint(70, 650))

close_button = tkinter.Button(window, text="Close", command=lambda: window.destroy(), bg='lime', fg='black',
                           padx='20', pady='8', font=('Comic Sans MS', 13, 'bold'), activebackground='Green')
close_button.place(x=random.randint(70, 1000), y=random.randint(70, 650))


window.mainloop()
