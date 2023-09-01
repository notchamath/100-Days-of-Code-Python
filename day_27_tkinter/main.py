from tkinter import *

window = Tk()
window.title("Hello GUI")
window.minsize(width=500, height=500)

# Label
my_label = Label(text="This is a label", font=("Arial", 24, "bold"))
# pack displays created element
my_label.pack()

# Changing properties
my_label["text"] = "Text 2"
my_label.config(text="Text 3")


# Input
user_input = Entry(width=50)
user_input.pack()
print(user_input.get())


# Buttons
def btn_clicked():
    my_label["text"] = f"{user_input.get()}"


button = Button(text=f"Click me", command=btn_clicked)
button.pack()



window.mainloop()
