from sqlite3 import register_converter
from tabnanny import check
from tkinter import *
import pandas as DataFrame
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
# READ DATA FROM CSV 
data = DataFrame.read_csv(r"C:\Users\deger\Downloads\flash-card-project-start\data\french_words.csv")
data1= data.to_dict(orient="records") # TAKE THE VALUES !
current_card = {} # TO CREATE A NEW VALUE WE CREATE A DICTIONARY AND SET GLOBAL

def next_card():###NEXT CARD MISSION
    global current_card,flip_timer# After 3 Seconds... Critical Info
    window.after_cancel(flip_timer)
    current_card=random.choice(data1)#Takes a Random French Word! ONEMLI
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word,text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    window.after(3000, func=next_card2) # After 3 Seconds... Critical Info


def next_card2():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word,text=current_card["English"])
    canvas.itemconfig(card_background, image=new_image)




window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=next_card2) # After 3 Seconds... Critical Info

## CANVAS CREATION
canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file=r"C:\Users\deger\Downloads\flash-card-project-start\images\card_front.png")
card_background  = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400,150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263,text="word", font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2) #Columnspan ile sag kaymis buttonlari duzeltiyor. ONEMLI 
card_back_img = PhotoImage(file=r"C:\Users\deger\Downloads\flash-card-project-start\images\card_back.png")


##SECOND IMAGE MISSION TO CHANGE COLOR
new_image = card_back_img
old_image = card_front_img
#canvas_image = canvas.create_image(300, 300, image=old_image)


# "X" BUTTON CREATION
cross_image=PhotoImage(file=r"C:\Users\deger\Downloads\flash-card-project-start\images\wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0, command=next_card)
unknown_button.grid(row=1,column=0)


# "CHECKIMAGE" BUTTON CREATION
check_image= PhotoImage(file=r"C:\Users\deger\Downloads\flash-card-project-start\images\right.png")
known_button = Button(image=check_image,highlightthickness=0,command=next_card)
known_button.grid(column=1, row=1)






next_card()
window.mainloop()