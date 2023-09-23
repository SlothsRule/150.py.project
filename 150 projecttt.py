from tkinter import *

import random

root=Tk()
root.geometry("500x500")
root.title("country capitals")

enter_name = Entry(root)
enter_name.place(relx= 0.5, rely= 0.2, anchor = CENTER)

friend_list = Label(root)
random_number_label = Label(root)
lucky_friend = Label(root)

list1 = []
def addfriend():
    friend_name = enter_name.get()
    list1.append(friend_name)
    friend_list["text"] = "Your friendlist : " +  str(list1)

def random_number():
    length = len(list1)
    r=random.randint(0, length-1)
    random_number_label["text"] = str(r)
    genR = list1[r]
    lucky_friend["text"] = "your lucky friend is: " + str(genR)
        

btn = Button(root, text="Add to the friendlist", command= addfriend)
btn.place(relx= 0.5, rely= 0.3, anchor= CENTER)

friend_list.place(relx= 0.5, rely= 0.4, anchor= CENTER)

btn1 = Button(root, text="Who is your lucky friend?", command= random_number)
btn1.place(relx= 0.5, rely= 0.5, anchor= CENTER)
   
random_number_label.place(relx= 0.5, rely= 0.6, anchor= CENTER)
lucky_friend.place(relx= 0.5, rely= 0.7, anchor= CENTER)

        

root.mainloop()