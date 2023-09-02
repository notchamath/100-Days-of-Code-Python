# from tkinter import *
#
#
# def btn_clicked():
#     my_label["text"] = f"{user_input.get()}"
#
#
# window = Tk()
# window.title("Hello GUI")
# window.minsize(width=500, height=500)
# window.config(padx=20, pady=20)
#
# # Label
# my_label = Label(text="This is a label", font=("Arial", 24, "bold"))
# my_label.config(text="Text 3")
# my_label.grid(column=0, row=0)
# my_label.config(padx=30, pady=30)
#
#
# # Buttons
# button = Button(text=f"Click me", command=btn_clicked)
# button.grid(column=1, row=1)
#
# # Input
# user_input = Entry(width=50)
# print(user_input.get())
# user_input.grid(column=4, row=4)
#
# new_btn = Button(text="new button")
# new_btn.grid(column=2, row=0)
#
# window.mainloop()


from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(pady=20, padx=20)

user_input = Entry(width=5)
user_input.grid(column=1, row=0)
user_input.insert(END, string="0")

equal_label = Label(text="is Equal to")
equal_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

answer_label = Label(text="0")
answer_label.grid(column=1, row=1)


def convert():
    answer = 1.609 * float(user_input.get())
    answer_label.config(text=answer)


btn = Button(text="Calculate", command=convert)
btn.grid(column=1, row=2)


window.mainloop()
