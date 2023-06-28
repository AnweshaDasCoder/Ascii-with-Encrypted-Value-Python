from tkinter import *

root=Tk()
root.title("Ascii and Encrypted Value")

root.geometry("400x400")
root.configure(background = 'light blue')
entry_word = Entry(root)
entry_word.place(relx=0.5, rely=0.4, anchor=CENTER)

label = Label(root, text = "Name in Ascii: ", bg="light yellow", fg="black")
label1 = Label(root, text= "Name in Encrypted Value: ", bg="light yellow", fg="black")

def asciiConverter():
    input_word = entry_word.get()
    
    for letter in input_word :
        label["text"] += str(ord(letter)) + " "
        ascii = int(ord(letter))
        encrypted = ascii - 1
        label1["text"] += (chr(encrypted))

btn=Button(root, text="Show name Ascii and in Encypted Value", command=asciiConverter, bg='gold', fg="black")
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

label.place(relx=0.5, rely=0.9, anchor=CENTER)
label1.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()


