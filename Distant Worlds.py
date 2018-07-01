###-------------------------------------------### Distant Worlds ###--------------------------------------------###
###-------------------------------------------###  By Ryan Lau   ###--------------------------------------------###

#imports tkinter module used for the GUI Interface
from tkinter import *
#imports the random function to allow randomly generated numbers to be made
import random

###---------------------------------------------### start setup ###---------------------------------------------###
###---------------------------------------------### start setup ###---------------------------------------------###
###---------------------------------------------### start setup ###---------------------------------------------###

#the main function of the program
def main():
    global window, tkinter, canvas, gamestate, clickbox, modedifficulty, highscore, score, hsname, play, errorname, DOCUMENT_PATH #setup of variables used in multiple parts of the program
    window = Tk() #initial setup of tkinter and the game window
    window.iconbitmap("Images/dwicon.ico") #custom icon on window banner to give a more independent feel
    window.title("Distant Worlds") #gives a title to the window banner
    window.resizable(height=False, width=False) #disables window resizing
    canvas = Canvas(window, width=500, height=500, bg="#0A0A0A") #creates the canvas
    clickbox = 0 #used to find out if the user can print numbers
    DOCUMENT_PATH = "data.txt" #document path of the high score file
    modedifficulty = -1 #variable used to find difficulty
    gamestate = -1 #sets the variable eventset to -1
    highscore = []
    score = 0
    hsname = None
    play = 0

    DOCUMENTR = open(DOCUMENT_PATH, 'r')
    with open('data.txt') as inputfile:
       for line in inputfile:
           highscore.append(line)
    inputfile.close()
    hslistlen = int(len(highscore) / 2)
    for i in range(hslistlen):
        highscore[2*i] = highscore[2*i].replace('\n', '')
    for i in range(hslistlen):
        highscore[1+2*i] = highscore[1+2*i].replace('\n', '')
        
    
    ### gamestate -1 = readyplayerone screen     >>>
    ### gamestate +0 = clicktostart screen       >>>
    ### gamestate +1 = main menu screen          >>>
    ### gamestate +2 = difficulty screen         >>>
    ### gamestate +3 = instructions screen       >>>
    ### gamestate +4 = credits screen            >>>
    ### gamestate +5 = high score view screen    >>>
    
    ### gamestate +7 = high score input screen   >>>
    ### gamestate +8 = gameplay screen           >>>
    ### gamestate +9 = level complete screen     >>>
    
    readyplayer() #runs function
    canvas.bind("<Button-1>", click) #allows user to use left mouse
    for i in range(10):
        canvas.bind(str(i), numpad) #allows user to use numpad
    canvas.pack() #packs the canvas and puts the window into a mainloop
    window.mainloop()

#function that when run deletes everything from the canvas
def clearcanvas():
    canvas.delete(ALL)
#function that deletes all objects with the tag "clickstart" from the canvas
def deleteclickstart():
    canvas.delete("clickstart")
    
#click function that reads where the user clicks and what to do next
def click(event):
    global gamestate, clickbox, modedifficulty, clicker, hsname
    if gamestate == 0: #runs only when the title screen is up
        clicker = "off"
        window.after(400, clearcanvas)
        window.after(800, clearcanvas)
        window.after(1200, clearcanvas)
        window.after(600, clearcanvas)
        window.after(1000, clearcanvas)
        window.after(1400, clearcanvas)
        window.after(1600, deleteclickstart)
        window.after(1600, mainmenu)
        
    if gamestate == 1: #runs only when the main menu is up
        if event.x > 155 and event.y > 178 and event.x < 345 and event.y < 205:
            window.after(1, gamestate2) #difficulty screen
            window.after(200, clearcanvas)
            window.after(400, difficultyscreen)
        if event.x > 218 and event.y > 228 and event.x < 284 and event.y < 255:
            gamestate = 3 #instructions screen
            window.after(200, clearcanvas)
            window.after(400, instructions)
        if event.x > 200 and event.y > 280 and event.x < 300 and event.y < 300:
            gamestate = 4 #credits screen
            window.after(200, clearcanvas)
            window.after(400, credits)
        if event.x > 175 and event.y > 330 and event.x < 320 and event.y < 352:
            gamestate = 5 #high score view screen
            window.after(200, clearcanvas)
            window.after(400, hsview)
            
    if gamestate == 2: #runs only when the difficulty screen is up
        gamestate = 2
        mode = 1
        for i in range(3): 
            if event.x > 275 and event.y > (115+i*81) and event.x < 355 and event.y < (140+i*81):
                modedifficulty = mode
                gamestate = 8 #gameplay screen
                window.after(100, clearcanvas)
                window.after(400, gameplay)
            if i == 0 or i == 2:  
                if event.x > 145 and event.y > (115+i*81) and event.x < 225 and event.y < (140+i*81):
                    modedifficulty = mode
                    gamestate = 8 #gameplay screen
                    window.after(100, clearcanvas)
                    window.after(400, gameplay)
            elif i == 1:
                if event.x > 145 and event.y > (115+i*81) and event.x < 250 and event.y < (140+i*81):
                    modedifficulty = mode
                    gamestate = 8 #gameplay screen
                    window.after(100, clearcanvas)
                    window.after(400, gameplay)
            mode += 1
        if event.x > 215 and event.y > 360 and event.x < 285 and event.y < 380:
            gamestate = 1 #mainmenu screen
            window.after(200, clearcanvas)
            window.after(400, mainmenu)
            
    if gamestate == 3: #runs only when the instructions screen is up
        if event.x > 215 and event.y > 360 and event.x < 285 and event.y < 380:
            gamestate = 1 #mainmenu screen
            window.after(200, clearcanvas)
            window.after(400, mainmenu)
            
    if gamestate == 4: #runs only when the credits screen is up
        if event.x > 215 and event.y > 360 and event.x < 285 and event.y < 380:
            gamestate = 1 #mainmenu screen
            window.after(200, clearcanvas)
            window.after(400, mainmenu)
            
    if gamestate == 5: #runs only when the high score view screen is up
        if event.x > 215 and event.y > 360 and event.x < 285 and event.y < 380:
            gamestate = 1 #mainmenu screen
            window.after(200, clearcanvas)
            window.after(400, mainmenu)
            
    if gamestate == 6: #runs only when the high score submit screen is up
        if event.x > 215 and event.y > 360 and event.x < 285 and event.y < 380:
            hsname = nameentry.get().upper().strip()
            if hsname.isalpha() and len(hsname) == 3:
                gamestate = 5 #high score view screen
                addhighscore()
                window.after(200, clearcanvas)
                window.after(400, hsview)
                 
    if gamestate == 8: #runs only when the gameplay screen is up
        if event.x > 60 and event.y > 90 and event.x < 100 and event.y < 110:
            gamestate = 1 #mainmenu screen
            window.after(200, clearcanvas)
            window.after(400, mainmenu)
        if event.x > 215 and event.y > 340 and event.x < 285 and event.y < 360:
            checknum()
            if numcheck == True:
                gamestate = 9 #level complete screen
                window.after(200, clearcanvas)
                window.after(400, checkanswer)
            
    if gamestate == 9: #runs only when the level complete screen is up
        if event.x > 215 and event.y > 360 and event.x < 285 and event.y < 380:
            gamestate = 6 #high score submit screen
            window.after(200, clearcanvas)
            window.after(400, hsenter)

#function generator for questions
def numgenerate():
    global answerlist, questionlist
    dividelist = []
    operatorlist = ["+", "-", "*", "*", "*", "/", "/", "/"]
    questionlist = []
    answerlist = []
    operator = -1
    divtimeslist = [2, 3, 2, 3, 4, 5]
    #makes the question up
    for i in range(3):
        dividelist = []
        operator = -1
        if modedifficulty == 1:
            operator = random.randint(0, 1)
        elif modedifficulty == 2: 
            operator = random.randint(0, 4)
        elif modedifficulty == 3: 
            operator = random.randint(0, 7)
        operator = operatorlist[operator]
        if operator == "/":
            d = random.choice(divtimeslist)
            f = 62 - 8 * d
            randnum1 = random.randint(10, f) * d
            questionlist.append(randnum1)
            questionlist.append(operator)
            for i in range(2, 50):
                a = randnum1 / i
                b = False
                b = float(a).is_integer()
                if b == True:
                    dividelist.append(i)
            randnum2 = random.choice(dividelist)
            questionlist.append(randnum2)
        elif operator == "*":
            randnum1 = random.randint(5, 15)
            questionlist.append(randnum1)
            questionlist.append(operator)
            randnum2 = random.randint(6, 15)
            questionlist.append(randnum2)
        elif operator == "-":
            randnum1 = random.randint(modedifficulty * 4, modedifficulty * 37)
            questionlist.append(randnum1)
            questionlist.append(operator)
            randnum2 = random.randint(modedifficulty * 4, modedifficulty * 37)
            while randnum2 >= randnum1:
                randnum2 = random.randint(modedifficulty * 4, modedifficulty * 37)
            questionlist.append(randnum2)
        else:
            randnum1 = random.randint(modedifficulty * 4, modedifficulty * 37)
            questionlist.append(randnum1)
            questionlist.append(operator)
            randnum2 = random.randint(modedifficulty * 4, modedifficulty * 37)
            questionlist.append(randnum2)
        #makes the answer to the question
        if operator == "/": 
            answernum = randnum1 / randnum2
        elif operator == "+": 
            answernum = questionlist[0 + 3 * i] + questionlist[2 + 3 * i]
        elif operator == "-": 
            answernum = questionlist[0 + 3 * i] - questionlist[2 + 3 * i]
        elif operator == "*": 
            answernum = questionlist[0 + 3 * i] * questionlist[2 + 3 * i]
        answernum2 = int(answernum)
        answerlist.append(answernum2)

#checks if number input is a number
def checknum():
    global numcheck
    numcheck = False
    num1 = num1entry.get()
    num2 = num2entry.get()
    num3 = num3entry.get()
    n1 = num1.isnumeric()
    n2 = num2.isnumeric()
    n3 = num3.isnumeric()
    if n1 == True and n2 == True and n3 == True:
        numcheck = True

#function that checks answer
def checkanswer():
    global score, hsname, lcscore, num1, num2, num3
    lcscore = 0
    if modedifficulty == 1:
        addscore = 1100
    if modedifficulty == 2:
        addscore = 2200
    if modedifficulty == 3:
        addscore = 3300
    num1 = num1entry.get()
    num2 = num2entry.get()
    num3 = num3entry.get()
    #checks entries for numbers
    if int(num1) == int(answerlist[0]):
        score += addscore
        lcscore += addscore
    if int(num2) == int(answerlist[1]):
        score += addscore
        lcscore += addscore
    if int(num3) == int(answerlist[2]):
        score += addscore
        lcscore += addscore
        
    levelcomplete()

#calculates where in the high score list the new score should be put
def hsnamefind(): 
    global hsname, hsreplacelist, score
    hsreplacelist = []
    #writes name in list
    hslistlen = int(len(highscore) / 2)
    for i in range(hslistlen):
        if score > int(highscore[1+i*2]):
            v = 1+i*2
            hsreplacelist.append(v)

#function used to calculate score
def scorestr():
    global score
    #writes score in list
    if len(str(score)) > 4:
        score = str(score)
    elif len(str(score)) == 4:
        score = '0' + str(score)
    elif score == 0:
        score = '00000'

#function that adds high score
def addhighscore():
    global score, hsname, x, hsreplacelist
    a = score
    if play != 1: 
        highscore.pop(x)
        highscore.pop(x)
    hsnamefind()
    if hsreplacelist != []:   
        x = hsreplacelist[0] - 1
        highscore.insert(x, hsname)
    else:
        highscore.append(hsname)
        x = int(len(highscore)) - 1
    scorestr()
    if hsreplacelist != []: 
        highscore.insert(x+1, score)
    else:
        highscore.append(score)
    #Write data to text file
    DOCUMENT = open(DOCUMENT_PATH, 'w')    
    DOCUMENT.truncate()
    for lines in highscore: 
        DOCUMENT.write(lines + '\n')
    DOCUMENT.close()
    score = a

#used to confirm that the numpad can be used
def numpad(event):
    a = 1

#used to make the gamestate 2
def gamestate2():
    global gamestate
    gamestate = 2

###---------------------------------------------###  end setup  ###---------------------------------------------###
###---------------------------------------------###  end setup  ###---------------------------------------------###
###---------------------------------------------###  end setup  ###---------------------------------------------###

###---------------------------------------------### all screens ###---------------------------------------------###
###---------------------------------------------### all screens ###---------------------------------------------###
###---------------------------------------------### all screens ###---------------------------------------------###
### ready player one code ###
#the main function of the readyplayerone screen
def readyplayer():
    global eventset
#draws the first "ready player one" text
    readyplayerone("#FFFFFF").draw(canvas)
#orders the fadeout functions and seperates them by 0.2 seconds each
    window.after(2000, clearcanvas)
    window.after(2200, clearcanvas)
    window.after(2400, clearcanvas)
    window.after(2600, clearcanvas)
    window.after(2800, clearcanvas)
    window.after(3000, clearcanvas)
    window.after(3200, clearcanvas)
    window.after(3400, clearcanvas)
    window.after(2000, fadeready1)
    window.after(2200, fadeready2)
    window.after(2400, fadeready3)
    window.after(2600, fadeready4)
    window.after(2800, fadeready5)
    window.after(3000, fadeready6)
    window.after(3200, fadeready7)
    window.after(3400, fadeready8)
    window.after(3600, clearcanvas)
    window.after(4000, afterreadyplayer)
#functions for fade "Ready Player One"
#used as different functions to control the timing between each change
def fadeready1():
    readyplayerone("#DFDFEA").draw(canvas)
def fadeready2():
    readyplayerone("#BFBFCA").draw(canvas)
def fadeready3():
    readyplayerone("#9F9FAA").draw(canvas)
def fadeready4():
    readyplayerone("#7F7F8A").draw(canvas)
def fadeready5():
    readyplayerone("#5F5F6A").draw(canvas)   
def fadeready6():
    readyplayerone("#3F3F4A").draw(canvas)
def fadeready7():
    readyplayerone("#1F1F2A").draw(canvas)
def fadeready8():
    readyplayerone("#0F0F1A").draw(canvas)
### end ###

### title screen code ###
# function waits 0.2 seconds before running the next function
def afterreadyplayer():
    window.after(200, titlescreen)
#the title screen function
def titlescreen():
    global title1, gamestate, clicker
    title1 = PhotoImage(file="Images/title2.gif") #variable storing location of image
    title(1, title1).draw(canvas) #class draws the title on screen
    gamestate = 0
    clicker = "on"
    blinkclick()
#runs blinkclick function until user clicks 
def blinkclick():
    if gamestate == 0 and clicker == "on": #this loop will continue to run itself until the user clicks
        window.after(200, clicktostart)
        window.after(1400, deleteclickstart)
        window.after(1600, blinkclick)
#loop function until gamestate == 1  
def clicktostart():
    if gamestate == 0: 
        clickstartblink("#F0F0F0").draw(canvas)
### end ###

### main menu code ###
#function for the main menu screen
def mainmenu():
    global title2, gamestate
    gamestate = 1
    title2 = PhotoImage(file="Images/title2.gif")
    title(2, title2).draw(canvas)
    text24(250, 190, "Start Game").draw(canvas)
    text20(250, 240, "Help").draw(canvas)
    text18(250, 290, "Credits").draw(canvas)
    text18(250, 340, "High Scores").draw(canvas)
    fourlines(4).draw(canvas)  
### end ###

### difficulty screen code ###
def difficultyscreen():
    header("Difficulty", 125).draw(canvas)
    text20(250, 130, "Easy      >>>").draw(canvas)
    text20(250, 210, "Normal    >>>").draw(canvas)
    text20(250, 290, "Hard      >>>").draw(canvas)
    text18(250, 370, "Back").draw(canvas)
    fourlines(4).draw(canvas)
### end ###

### instructions screen ###
def instructions():
    header("Help", 85).draw(canvas)
    text15(250, 225, " Add numbers in squares to \n make the number at the end \n \n Complete all questions  \n to progress").draw(canvas)
    text18(250, 370, "Back").draw(canvas)
    fourlines(4).draw(canvas)
### end ###

### credits screen ###
def credits():
    header("Credits", 100).draw(canvas)
    text15(250, 215, " Code and Graphics \n Ryan Lau \n \n ©COPYRIGHT 2018 \n ALL RIGHTS RESERVED").draw(canvas)
    text18(250, 370, "Back").draw(canvas)
    fourlines(4).draw(canvas)
### end ###

### gameplay screen ###
def gameplay():
    global md, num1entry, num2entry, num3entry
    if modedifficulty == 1:
        md = "Easy"
    elif modedifficulty == 2:
        md = "Normal"
    elif modedifficulty == 3:
        md = "Hard"
    titleheader = "Play - " + md
    header(titleheader, 200).draw(canvas)
    fourlines(4).draw(canvas)
    numgenerate()
    line1 = str(questionlist[0]) + "  " + str(questionlist[1]) + "  "  + str(questionlist[2])
    line2 = str(questionlist[3]) + "  " + str(questionlist[4]) + "  "  + str(questionlist[5])
    line3 = str(questionlist[6]) + "  " + str(questionlist[7]) + "  "  + str(questionlist[8])
    text15(200, 130, line1).draw(canvas)
    text15(200, 210, line2).draw(canvas)
    text15(200, 290, line3).draw(canvas)
    text18(250, 350, "Check").draw(canvas)
    num1entry = Entry(window, width=3, font='courier 16 bold', highlightthickness=0, borderwidth=0)
    canvas.create_window(330, 130, window=num1entry)
    num2entry = Entry(window, width=3, font='courier 16 bold', highlightthickness=0, borderwidth=0)
    canvas.create_window(330, 210, window=num2entry)
    num3entry = Entry(window, width=3, font='courier 16 bold', highlightthickness=0, borderwidth=0)
    canvas.create_window(330, 290, window=num3entry)
    text15(85, 100, "Back").draw(canvas)
### end ###

### high score view screen ###
def hsview():
    header("HIGH SCORES", 200).draw(canvas)
    fourlines(4).draw(canvas)
    text20(200, 105, "Name").draw(canvas)
    text20(300, 105, "Score").draw(canvas)
    for i in range(3):
        text15(195, 165+(60*i), highscore[i * 2]).draw(canvas)
        text15(295, 165+(60*i), highscore[1 + i * 2]).draw(canvas)
    text18(250, 370, "Back").draw(canvas)
### end ###

### high score enter screen ###
def hsenter(): 
    global nameentry
    header("ENTER NAME SCORE", 220).draw(canvas)
    text18(250, 195, "Enter Your Name: ").draw(canvas)
    fourlines(4).draw(canvas)
    nameentry = Entry(window, width=5, font='courier 20 bold', highlightthickness=0, borderwidth=0)
    canvas.create_window(250, 250, window=nameentry)
    text18(250, 370, "Submit").draw(canvas)
    text18(250, 170, "Input should be 3 characters").draw(canvas)
    text12(250, 320, "Note: If you have already entered \n a name this is your chance to change it").draw(canvas)
### end ###

### level complete screen ###
def levelcomplete():
    global play
    play += 1
    header("Level Complete", 210).draw(canvas)
    textlc = "Score = " + str(score)
    if lcscore > 1000: 
        text18(250, 170, "Well Done!").draw(canvas)
    else:
        text18(250, 170, "Unlucky!").draw(canvas)
    text18(250, 215, textlc).draw(canvas)
    text18(250, 370, "Continue").draw(canvas)
    fourlines(4).draw(canvas)
    text12(170, 265, "Correct Answer").draw(canvas)
    text12(170, 295, "Your Answer").draw(canvas)
    for i in range(3):
        text12(270+50*i, 265, answerlist[i]).draw(canvas)
    text12(270, 295, num1).draw(canvas)
    text12(320, 295, num2).draw(canvas)
    text12(370, 295, num3).draw(canvas)
    
### end ###

###---------------------------------------------### end screens ###---------------------------------------------###
###---------------------------------------------### end screens ###---------------------------------------------###
###---------------------------------------------### end screens ###---------------------------------------------###

###---------------------------------------------### all classes ###---------------------------------------------###
###---------------------------------------------### all classes ###---------------------------------------------###
###---------------------------------------------### all classes ###---------------------------------------------###
#class "Ready Player One" fade
class readyplayerone():
    def __init__(self, fillcolor): 
        self.fillcolor = fillcolor
    def draw(self, canvas): 
        canvas.create_text(250, 200, text="Ready Player One", font="courier 30 bold", fill=self.fillcolor)
#class  "click to start" blink
class clickstartblink():
    def __init__(self, fillcolor): 
        self.fillcolor = fillcolor
    def draw(self, canvas): 
        canvas.create_text(250, 365, text="click to start", font="courier 15 bold", fill=self.fillcolor, tag="clickstart")
        canvas.create_line(125, 365, 150, 365, fill="#F0F0F0", width=2, tag="clickstart")
        canvas.create_line(375, 365, 350, 365, fill="#F0F0F0", width=2, tag="clickstart")
#class images
class image():
    def __init__(self, x, y, photo): 
        self.x = x
        self.y = y
        self.photo = photo
    def draw(self, canvas): 
        canvas.create_image(self.x, self.y, image=self.photo)
#class text size 24
class text24():
    def __init__(self, x, y, text): 
        self.x = x
        self.y = y
        self.text = text
    def draw(self, canvas): 
        canvas.create_text(self.x, self.y, text=self.text, font="courier 24 bold", fill="#F0F0F0", tag="text")
#class text size 20
class text20():
    def __init__(self, x, y, text): 
        self.x = x
        self.y = y
        self.text = text
    def draw(self, canvas): 
        canvas.create_text(self.x, self.y, text=self.text, font="courier 20 bold", fill="#F0F0F0", tag="text")
#class  text size 18
class text18():
    def __init__(self, x, y, text): 
        self.x = x
        self.y = y
        self.text = text
    def draw(self, canvas): 
        canvas.create_text(self.x, self.y, text=self.text, font="courier 18 bold", fill="#F0F0F0", tag="text")
#class text size 15
class text15():
    def __init__(self, x, y, text): 
        self.x = x
        self.y = y
        self.text = text
    def draw(self, canvas): 
        canvas.create_text(self.x, self.y, text=self.text, font="courier 15 bold", justify="center", fill="#F0F0F0", tag="text")
#class text size 12
class text12():
    def __init__(self, x, y, text): 
        self.x = x
        self.y = y
        self.text = text
    def draw(self, canvas): 
        canvas.create_text(self.x, self.y, text=self.text, font="courier 12 bold", justify="center", fill="#F0F0F0", tag="text")
#class draw lines
class fourlines():
    def __init__(self, a):
        self.a = a
    def draw(self, canvas): 
        canvas.create_line(0, 460, 250, 460, fill="#F0F0F0", width=4, tag="fourlines")
        canvas.create_line(260, 460, 510, 460, fill="#F0F0F0", width=4, tag="fourlines")
        canvas.create_line(0, 450, 240, 450, fill="#F0F0F0", width=4, tag="fourlines")
        canvas.create_line(260, 440, 510, 440, fill="#F0F0F0", width=4, tag="fourlines")
        canvas.create_line(0, 440, 250, 440, fill="#F0F0F0", width=4, tag="fourlines")
        canvas.create_line(250, 450, 510, 450, fill="#F0F0F0", width=4, tag="fourlines")
        canvas.create_line(0, 430, 240, 430, fill="#F0F0F0", width=4, tag="fourlines")
        canvas.create_line(250, 430, 510, 430, fill="#F0F0F0", width=4, tag="fourlines")
        canvas.create_line(0, 420, 250, 420, fill="#F0F0F0", width=4, tag="fourlines")
        canvas.create_line(260, 420, 510, 420, fill="#F0F0F0", width=4, tag="fourlines")
        canvas.create_line(0, 470, 240, 470, fill="#F0F0F0", width=4, tag="fourlines")
        canvas.create_line(250, 470, 510, 470, fill="#F0F0F0", width=4, tag="fourlines")
#class used to draw the title, mode 1 is for the start screen, mode 2 is for the menu screen
class title():
    def __init__(self, mode, picture):
        self.mode = mode
        self.picture = picture
    def draw(self, canvas):
        if self.mode == 1:
            canvas.create_image(250, 147, image=self.picture)
            canvas.create_line(40, 90, 460, 90, fill="#F0F0F0", width=4)
            canvas.create_line(20, 105, 480, 105, fill="#F0F0F0", width=4.5)
            canvas.create_line(20, 185, 480, 185, fill="#F0F0F0", width=4.5)
            canvas.create_line(50, 205, 450, 205, fill="#F0F0F0", width=4)
        if self.mode == 2:
            canvas.create_image(250, 87, image=self.picture)
            canvas.create_line(40, 30, 460, 30, fill="#F0F0F0", width=4)
            canvas.create_line(20, 45, 480, 45, fill="#F0F0F0", width=4.5)
            canvas.create_line(20, 125, 480, 125, fill="#F0F0F0", width=4.5)
            canvas.create_line(50, 145, 450, 145, fill="#F0F0F0", width=4)
#class
class header():
    def __init__(self, text, length):
        self.text = text
        self.length = length
    def draw(self, canvas):
        canvas.create_text(250, 60, text=self.text, font="courier 24 bold", fill="#F0F0F0")
        canvas.create_line(250-self.length, 38, 250+self.length, 38, fill="#F0F0F0", width=3.5)
        canvas.create_line(250-self.length, 82, 250+self.length, 82, fill="#F0F0F0", width=3.5)
###---------------------------------------------### end classes ###---------------------------------------------###
###---------------------------------------------### end classes ###---------------------------------------------###
###---------------------------------------------### end classes ###---------------------------------------------###

#run main function
main()
