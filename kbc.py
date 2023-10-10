from tkinter import *
from tkinter.ttk import Progressbar
import pyttsx3

tts = pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice',voices[1].id)

def select(event):
    callButton.place_forget()
    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()

    progressbarLabelA.place_forget()
    progressbarLabelB.place_forget()
    progressbarLabelC.place_forget()
    progressbarLabelD.place_forget()
    b=event.widget
    value=b['text']

    for i in range(15):
        if value==correct_answers[i]:
            if value==correct_answers[14]:
                def close():
                    root2.destroy()
                    root.destroy()

                
                


                root2=Toplevel()
                root2.overrideredirect(True)
                root2.config(bg='black')
                root2.geometry('500x400+140+30')
                
                imgLabel=Label(root2,image=centerImage,bd=0)
                imgLabel.pack(pady=30)

                winLabel=Label(root2,text='You Win', font=('ariel',40,'bold'),bg='black',fg='white')
                winLabel.pack()

                
                closeButton=Button(root2,text='Close',font=('ariel',20,'bold'),bg='black',fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2',command=close)
                closeButton.pack()

                happyimage=PhotoImage(file='happy.png')
                happyLabel=Label(root2,image=happyimage,bg='black')
                happyLabel.place(x=30,y=280)

                happyLabel1=Label(root2,image=happyimage,bg='black')
                happyLabel1.place(x=400,y=280)
                

                root2.mainloop()
                break

            questionArea.delete(1.0,END)
            questionArea.insert(END,questions[i+1])

            optionButton1.config(text=first_option[i+1])
            optionButton2.config(text=second_option[i+1])
            optionButton3.config(text=third_option[i+1])
            optionButton4.config(text=fourth_option[i+1])
            amountLabel.config(image=amountImages[i])
        
        if value not in correct_answers:
            def close():
              root1.destroy()
              root.destroy()
 
            


            root1=Toplevel()
            root1.overrideredirect(True)
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            
            imgLabel=Label(root1,image=centerImage,bd=0)
            imgLabel.pack(pady=30)

            loseLabel=Label(root1,text='You Lose', font=('ariel',40,'bold'),bg='black',fg='white')
            loseLabel.pack()

            

            closeButton=Button(root1,text='Close',font=('ariel',20,'bold'),bg='black',fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2',command=close)
            closeButton.pack()

            sadimage=PhotoImage(file='sad.png')
            sadLabel=Label(root1,image=sadimage,bg='black')
            sadLabel.place(x=30,y=280)

            sadLabel1=Label(root1,image=sadimage,bg='black')
            sadLabel1.place(x=400,y=280)
            

            root1.mainloop()
            break

def lifeline50():
    lifeline50Button.config(image=image50X,state=DISABLED)
    if questionArea.get(1.0,'end-1c')==questions[0]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[1]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[2]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[3]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[4]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[5]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[6]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[7]:
        optionButton1.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[8]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[9]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[10]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[11]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[12]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[13]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0,'end-1c')==questions[14]:
        optionButton2.config(text='')
        optionButton4.config(text='')

   

def audiencePolllifeline():
    audiencePollButton.config(image=audiencePollX,state=DISABLED)
    progressbarA.place(x=580,y=190)
    progressbarB.place(x=620,y=190)
    progressbarC.place(x=660,y=190)
    progressbarD.place(x=700,y=190)

    progressbarLabelA.place(x=580,y=320)
    progressbarLabelB.place(x=620,y=320)
    progressbarLabelC.place(x=660,y=320)
    progressbarLabelD.place(x=700,y=320)
    

    if questionArea.get(1.0,'end-1c')==questions[0]:
        progressbarA.config(value=40)
        progressbarB.config(value=80)
        progressbarC.config(value=60)
        progressbarD.config(value=10)
    
    if questionArea.get(1.0,'end-1c')==questions[1]:
        progressbarA.config(value=45)
        progressbarB.config(value=5)
        progressbarC.config(value=40)
        progressbarD.config(value=75)

    if questionArea.get(1.0,'end-1c')==questions[2]:
        progressbarA.config(value=90)
        progressbarB.config(value=30)
        progressbarC.config(value=20)
        progressbarD.config(value=10)

    if questionArea.get(1.0,'end-1c')==questions[3]:
        progressbarA.config(value=50)
        progressbarB.config(value=20)
        progressbarC.config(value=70)
        progressbarD.config(value=40)

    if questionArea.get(1.0,'end-1c')==questions[4]:
        progressbarA.config(value=90)
        progressbarB.config(value=10)
        progressbarC.config(value=30)
        progressbarD.config(value=20)

    if questionArea.get(1.0,'end-1c')==questions[5]:
        progressbarA.config(value=20)
        progressbarB.config(value=50)
        progressbarC.config(value=80)
        progressbarD.config(value=30)

    if questionArea.get(1.0,'end-1c')==questions[6]:
        progressbarA.config(value=30)
        progressbarB.config(value=10)
        progressbarC.config(value=90)
        progressbarD.config(value=50)

    if questionArea.get(1.0,'end-1c')==questions[7]:
        progressbarA.config(value=10)
        progressbarB.config(value=10)
        progressbarC.config(value=50)
        progressbarD.config(value=90)

    if questionArea.get(1.0,'end-1c')==questions[8]:
        progressbarA.config(value=30)
        progressbarB.config(value=80)
        progressbarC.config(value=60)
        progressbarD.config(value=10)

    if questionArea.get(1.0,'end-1c')==questions[9]:
        progressbarA.config(value=80)
        progressbarB.config(value=30)
        progressbarC.config(value=40)
        progressbarD.config(value=30)

    if questionArea.get(1.0,'end-1c')==questions[10]:
        progressbarA.config(value=50)
        progressbarB.config(value=40)
        progressbarC.config(value=10)
        progressbarD.config(value=80)

    if questionArea.get(1.0,'end-1c')==questions[11]:
        progressbarA.config(value=50)
        progressbarB.config(value=10)
        progressbarC.config(value=90)
        progressbarD.config(value=50)

    if questionArea.get(1.0,'end-1c')==questions[12]:
        progressbarA.config(value=20)
        progressbarB.config(value=70)
        progressbarC.config(value=50)
        progressbarD.config(value=40)

    if questionArea.get(1.0,'end-1c')==questions[13]:
        progressbarA.config(value=90)
        progressbarB.config(value=25)
        progressbarC.config(value=10)
        progressbarD.config(value=40)

    if questionArea.get(1.0,'end-1c')==questions[14]:
        progressbarA.config(value=80)
        progressbarB.config(value=25)
        progressbarC.config(value=40)
        progressbarD.config(value=10)

    

def phoneLifeline():
    callButton.place(x=70,y=260)
    phoneButton.config(image=phoneimageX,state=DISABLED)

def phoneclick():
    for i in range(15):
        if questionArea.get(1.0,'end-1c')==questions[i]:
            tts.say(f'The answer is {correct_answers[i]}')
            tts.runAndWait()

        

    

  
    
    
correct_answers = ["Coca-Cola","Octagonal","Russia","Oslo","April 22","0","Moon",
                   "AB negative","Damascus","France","Chile","Viking-1","Giraffe","Tulips","Ethiopia"]


questions = ["What was the first soft drink in space?",
             "Which geometric shape is generally used in stop signs?",
             "Which country borders 14 countries and crosses 8 time zones?",
             "The Nobel Peace Prize is awarded in which city?",
             "When is Earth Day celebrated?",
             "How many bones do sharks have?",
             "Where is the sea of tranquility found?",
             "Which is the rarest blood type?",
             "What is the world's oldest and currently inhabited city?",
             "Which European country shares a border with Brazil?",
             "Which country is the largest producer of copper?",
             "What is the name of the first spacecraft to reach Mars?",
             "Which mammal does not have vocal cords?",
             "Which flower was used as currency previously?",
             "Which African country was previously known as Abyssinia?"]
             

first_option = ["Pepsi","Circular",
                "Russia","Paris",
                "April 22","206",
                "Earth","B negative",
                "Athens","France",
                "China","Apollo 11",
                "Rhino","Tulips",
                "Ethiopia"]

second_option = ["Coca-Cola","Pentagonal",
                 "Brazil","Berlin",
                 "September 19","188",
                 "Saturn","A negative",
                 "Damascus","Spain",
                 "Uruguay","Sputnik",
                 "Giraffe","Roses",
                 "Egypt"]
                

third_option = ["Fanta","Hexagonal",
                "Kazakhstan","Oslo",
                "January 28","0",
                "Moon","O negative",
                "Varanasi","Germany",
                "USA","Viking-1",
                "Platypus","Jasmine",
                "Nigeria"]
            

fourth_option = ["Sprite","Octagonal",
                 "Sudan","Geneva",
                 "May 16","5",
                 "Neptune","AB negative",
                 "Sidon","Belgium",
                 "Chile","GSLV-5",
                 "Camel","Lotus",
                 "Somalia"]





root=Tk()
root.geometry('1270x652+0+0')
root.title("KBC")
root.config(bg='black')

leftframe=Frame(root,bg='black',padx=100)
leftframe.grid(row=0,column=1)

topFrame=Frame(leftframe,bg='black')
topFrame.grid()

centerFrame=Frame(leftframe,bg='black')
centerFrame.grid(row=1,column=0)

bottomFrame=Frame(leftframe)
bottomFrame.grid(row=2,column=0)

rightframe=Frame(root,bg='black',padx=50,pady=25)
rightframe.grid(row=0,column=2)

image50=PhotoImage(file ='50-50.png')
image50X=PhotoImage(file ='50-50-X.png')

lifeline50Button=Button(topFrame,image=image50,bg='black',bd=0,activebackground='dark blue',width=180,height=80,cursor='hand2',command=lifeline50)
lifeline50Button.grid(row=0, column=0)

audiencePoll=PhotoImage(file ='audiencePoll.png')
audiencePollX=PhotoImage(file ='audiencePollX.png')

audiencePollButton=Button(topFrame,image=audiencePoll,bg='black',bd=0,activebackground='dark blue',width=180,height=80,cursor='hand2',command=audiencePolllifeline)
audiencePollButton.grid(row=0, column=1)

phoneimage=PhotoImage(file='phoneAFriend.png')
phoneimageX=PhotoImage(file='phoneAFriendX.png')

phoneButton=Button(topFrame,image=phoneimage,bg='black',bd=0,activebackground='dark blue',width=180,height=80,cursor='hand2',command=phoneLifeline)
phoneButton.grid(row=0, column=2)

callimage=PhotoImage(file='phone.png')
callButton=Button(root,image=callimage,bd=0,bg='black',activebackground='dark blue',cursor='hand2',command=phoneclick)

centerImage=PhotoImage(file='unnamed101.png')
logolabel=Label(centerFrame,image=centerImage,bg='black',width=500,height=220)
logolabel.grid(row=0,column=0)

amountimage1=PhotoImage(file='1.png')
amountimage2=PhotoImage(file='2.png')
amountimage3=PhotoImage(file='3.png')
amountimage4=PhotoImage(file='4.png')
amountimage5=PhotoImage(file='5.png')
amountimage6=PhotoImage(file='6.png')
amountimage7=PhotoImage(file='7.png')
amountimage8=PhotoImage(file='8.png')
amountimage9=PhotoImage(file='9.png')
amountimage10=PhotoImage(file='10.png')
amountimage11=PhotoImage(file='11.png')
amountimage12=PhotoImage(file='12.png')
amountimage13=PhotoImage(file='13.png')
amountimage14=PhotoImage(file='14.png')
amountimage15=PhotoImage(file='15.png')

amountImages=[amountimage2,amountimage3,amountimage4,amountimage5,amountimage6,
              amountimage7,amountimage8,amountimage9,amountimage10,amountimage11,amountimage12,
              amountimage13,amountimage14,amountimage15]

amountLabel=Label(rightframe,image=amountimage1,bg='black')
amountLabel.grid(row=0,column=0)

layoutimage=PhotoImage(file='lay.png')

layoutLabel=Label(bottomFrame,image=layoutimage,bg='black')
layoutLabel.grid(row=0,column=0)

questionArea=Text(bottomFrame,font=('arial',18,'bold'),width=34,height=2,wrap='word',bg='black',fg='white',bd=0)
questionArea.place(x=70,y=10)

questionArea.insert(END,questions[0])


labelA=Label(bottomFrame,text='A:',bg='black',fg='white',font=('ariel',16,'bold'))
labelA.place(x=60,y=110)

optionButton1=Button(bottomFrame,text=first_option[0],bg='black',fg='white',font=('ariel',18,'bold'),bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionButton1.place(x=100,y=100)

labelB=Label(bottomFrame,text='B:',bg='black',fg='white',font=('ariel',16,'bold'))
labelB.place(x=330,y=110)

optionButton2=Button(bottomFrame,text=second_option[0],bg='black',fg='white',font=('ariel',18,'bold'),bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionButton2.place(x=370,y=100)

labelC=Label(bottomFrame,text='C:',bg='black',fg='white',font=('ariel',16,'bold'))
labelC.place(x=60,y=190)

optionButton3=Button(bottomFrame,text=third_option[0],bg='black',fg='white',font=('ariel',18,'bold'),bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionButton3.place(x=100,y=180)

labelD=Label(bottomFrame,text='D:',bg='black',fg='white',font=('ariel',16,'bold'))
labelD.place(x=330,y=190)

optionButton4=Button(bottomFrame,text=fourth_option[0],bg='black',fg='white',font=('ariel',18,'bold'),bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionButton4.place(x=370,y=180)

progressbarA=Progressbar(root,orient=VERTICAL,length=120)
progressbarB=Progressbar(root,orient=VERTICAL,length=120)
progressbarC=Progressbar(root,orient=VERTICAL,length=120)
progressbarD=Progressbar(root,orient=VERTICAL,length=120)

progressbarLabelA=Label(root,text='A',font=('ariel',20,'bold'),bg='black',fg='white')
progressbarLabelB=Label(root,text='B',font=('ariel',20,'bold'),bg='black',fg='white')
progressbarLabelC=Label(root,text='C',font=('ariel',20,'bold'),bg='black',fg='white')
progressbarLabelD=Label(root,text='D',font=('ariel',20,'bold'),bg='black',fg='white')


optionButton1.bind('<Button-1>',select)
optionButton2.bind('<Button-1>',select)
optionButton3.bind('<Button-1>',select)
optionButton4.bind('<Button-1>',select)

root.mainloop()
