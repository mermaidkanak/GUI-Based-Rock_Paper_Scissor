from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="#FDD5DF")

rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

user_label = Label(root, image=scissor_img, bg="#FDD5DF")
comp_label = Label(root, image=scissor_img_comp, bg="#FDD5DF")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

playerScore = Label(root, text=0, font=100, bg="#FDD5DF", fg="black")
computerScore = Label(root, text=0, font=100, bg="#FDD5DF", fg="black")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

user_indicator = Label(root, font=50, text="USER", bg="#FDD5DF", fg="black")
comp_indicator = Label(root, font=50, text="COMPUTER",
                       bg="#FDD5DF", fg="black")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

msg = Label(root, font=50, bg="#FDD5DF", fg="black")
msg.grid(row=3, column=2)

def updateMessage(x):
    msg['text'] = x

def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()

    else:
        pass

choices = ["rock", "paper", "scissor"]
def updateChoice(x):

    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkWin(x, compChoice)

rock = Button(root, width=20, height=4, text="ROCK",
              bg="#F7FFDD", fg="black", command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=4, text="PAPER",
               bg="#D2E1E0", fg="black", command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=4, text="SCISSOR",
                 bg="#D0E3CC", fg="black", command=lambda: updateChoice("scissor")).grid(row=2, column=3)

root.mainloop()
