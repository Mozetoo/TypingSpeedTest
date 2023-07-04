'''Access You on your typing skills and Tells you how many you got write and wrong '''

from tkinter import *
from random import choice


def key_press(event):
    entry.config(fg="black")  # once the any key is pressed want it to turn black


def key_release(event):
    if event.keysym == "space":  # once the space key is pressed want it to turn black
        entry.config(fg="green")


def gets_data():
    text = entry.get()  # Get the text from the Entry widget
    recorded_text = text.split(" ")  # Split the text into a list and store it
    for data in recorded_text:
        user_word_count.append(data)  # Add the data to a list


def timer_expired():
    wrong = []
    gets_data()  # gets all the data in the entry box
    user_word = list(filter(lambda item: item != "", user_word_count))  # removes empty list
    print(user_word)
    for correct in user_word:  # checks for the wrong words
        if correct in word_list:
            continue
        else:
            wrong.append(correct)  # and adds it to the list
    text_label.config(
        text=f"60 seconds are up! \n Speed : {len(user_word)} words / per minute\n With {len(wrong)} wrong words") # interuppts the screen once 60 seconds is over
    entry.config(state="disabled")
    timer_label.config(text="Time Up")


def update_timer(seconds): # timer , once 60 seconds it up it goes to the time_expired function
    timer_label.config(text=f"Timer: {seconds} seconds")
    if seconds == 60:
        timer_expired()
    else:
        window.after(1000, update_timer, seconds + 1)  # Call the function again after 1 second


def enter_key(event): # use enter to clear the entry box and save the data
    gets_data()
    entry.delete(0, END)  # Delete the text in the entry
    new_text = f"{choice(word_list)}  {choice(word_list)}  {choice(word_list)}  {choice(word_list)}  {choice(word_list)}"
    text_label.config(text=new_text)


user_word_count = [] # where we will save the user words
word_list = [
    "apple", "banana", "cat", "dog", "elephant", "fish", "giraffe", "horse", "icecream", "jellyfish",
    "kangaroo", "lemon", "monkey", "nest", "orange", "penguin", "quail", "rabbit", "strawberry", "tiger",
    "umbrella", "violet", "whale", "xylophone", "yak", "zebra", "ant", "bee", "carrot", "duck",
    "egg", "fox", "grape", "honey", "island", "juice", "kiwi", "lion", "mango", "nut",
    "ostrich", "pear", "quinoa", "rose", "sunflower", "tomato", "unicorn", "vegetable", "watermelon", "xylophone"
] # words we are going to be using

text_display = f"{choice(word_list)}  {choice(word_list)}  {choice(word_list)}  {choice(word_list)}  {choice(word_list)}" # first text to show

window = Tk()
window.title("Speed Typing Test")

window.config(padx=50, pady=50)

text_label = Label(window, text=text_display, font=("Arial", 15)) # words display settings
text_label.grid(row=0, column=0, pady=10)

entry = Entry(window, width=40, highlightthickness=0) #entty box settings
entry.grid(row=1, column=0, pady=10)
entry.bind("<Return>", enter_key)
entry.bind("<KeyPress>", key_press)
entry.bind("<KeyRelease>", key_release)

timer_label = Label(window, text="Timer: 0 seconds") # timer display
timer_label.grid(row=2, column=0, pady=10)

update_timer(0) # starts the timer

window.mainloop()
