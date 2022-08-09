import tkinter as tk
names = []
from tkinter import messagebox

# First class is the first Frame to show up when program Opens
class Open(tk.Frame):
    def __init__(self, parent, controller): #the constructor has a controller that is defined in the Program class and is what controls which frame to show in this program
        tk.Frame.__init__(self, parent, bg='white smoke')
        
        self.border = tk.LabelFrame(self, text='Login', bg='white smoke', fg='#f85f6a', bd = 10, font=("Arial", 20))
        self.border.pack(fill="both", expand="yes", padx = 150, pady=150)
        
        self.user_label = tk.Label(self.border, text="Username", font=("Arial Bold", 15), bg='white smoke', fg='#f85f6a')
        self.user_label.place(x=50, y=20)
        self.user_entry = tk.Entry(self.border, width = 30, bd = 5, bg='white smoke')
        self.user_entry.place(x=180, y=20)
        
        self.password_label = tk.Label(self.border, text="Password", font=("Arial Bold", 15), bg='white smoke', fg='#f85f6a')
        self.password_label.place(x=50, y=80)
        self.password_entry = tk.Entry(self.border, width = 30, show='*', bd = 5, bg='white smoke')
        self.password_entry.place(x=180, y=80)
        #this method opens the text file, checks the users and their passwords and only proceed if there is a match
        def check_login():
            try:
                with open("users.txt", "r") as f:
                    info = f.readlines()
                    i  = 0
                    for e in info:
                        self.user_name, self.user_password =e.split(",")
                        if self.user_name.strip() == self.user_entry.get() and self.user_password.strip() == self.password_entry.get():
                            controller.show_frame(Welcome)#the controller opens Welcome Frame
                            i = 1
                            break
                    if i==0:
                        messagebox.showinfo("Error", "The Username or Password you have entered are incorrect!")
            except:
                messagebox.showinfo("Error", "Couldnt open file")
     
         
        self.submitbutton = tk.Button(self.border, text="Submit", font=("Arial", 15), bg='#f85f6a', fg='white smoke' , command=check_login)
        self.submitbutton.place(x=320, y=115)

      #this runs when sign up buttons pressed
        def signup():
            signup_window = tk.Tk()#opens a new window
            signup_window.resizable(0,0)
            signup_window.configure(bg="white smoke")
            signup_window.title("signup")
            reg_name_label = tk.Label(signup_window, text="Username:", font=("Arial",15), bg="white smoke", fg="#f85f6a")
            reg_name_label.place(x=10, y=10)
            reg_name_entry = tk.Entry(signup_window, width=30, bd=5)
            reg_name_entry.place(x = 200, y=10)
            
            reg_password_label = tk.Label(signup_window, text="Password:", font=("Arial",15), bg="white smoke", fg="#f85f6a")
            reg_password_label.place(x=10, y=60)
            reg_password_entry = tk.Entry(signup_window, width=30, show="*", bd=5)
            reg_password_entry.place(x = 200, y=60)
            
            confirm_password_label = tk.Label(signup_window, text="Confirm Password:", font=("Arial",15), bg="white smoke", fg="#f85f6a")
            confirm_password_label.place(x=10, y=110)
            confirm_password_entry = tk.Entry(signup_window, width=30, show="*", bd=5)
            confirm_password_entry.place(x = 200, y=110)
            
            def check():
                if reg_name_entry.get()!="" or reg_password_entry.get()!="" or confirm_password_entry.get()!="":
                    if reg_password_entry.get()==confirm_password_entry.get():
                        with open("users.txt", "a") as f:
                            f.write(reg_name_entry.get()+","+reg_password_entry.get()+"\n")
                            messagebox.showinfo("Welcome","You are signuped successfully!!")
                            signup_window.destroy()
                    else:
                        messagebox.showinfo("Error","Your password didn't get match!!")
                else:
                  messagebox.showinfo("Error", "Please fill the complete field!!")
                    
            self.signup_button = tk.Button(signup_window, text="signup", font=("Arial",15), bg="#f85f6a", fg="white smoke", command=check)
            self.signup_button.place(x=170, y=150)
            
            signup_window.geometry("470x220")
            signup_window.mainloop()
            
        self.signup_button = tk.Button(self, text="Sign Up", bg = "#f85f6a", font=("Arial",15), fg="white smoke", command=signup)
        self.signup_button.place(x=650, y=20)
        
class Welcome(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg= "white smoke")
        
        self.title_label = tk.Label(self, text="Welcome to Tongan Knowlege Quiz", bg = "white smoke", font=("Arial Bold", 25))
        self.title_label.place(x=40, y=150)        
        self.next_button = tk.Button(self, text="Next", font=("Arial", 15), bg="green" , command=lambda: controller.show_frame(TonganQuiz))
        self.next_button.place(x=650, y=450)
        
        self.exit_button = tk.Button(self, text="Back", font=("Arial", 15), bg="red", command=lambda: parent.destroy())
        self.exit_button.place(x=100, y=450)
        
global question_number
#question_number = 0
#The Python "KeyError: 0" exception is caused when we try to access a 0 key in a a dictionary that doesn't contain the key. To solve the error, set the key in the dictionary before trying to access it or conditionally set it if it doesn't exist
question_number = 1 #as we are looking at the keys not index positions
class TonganQuiz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.tongan_questions = {
          1: ["What is the name of the hall?", #item 1, index 0 will be the question
          'Watson Hall', # Item 2, index 1 will be the first choice
          'Ball Hall', # Item 3, index 2 will be the second choice
          'Butler Hall', # Item 4, index 3 will be the third choice
          'School Hall', # Item 5, index 4 will be the fourth choice
          'Cathedral Hall'# Item 6, index 5 will be the write statement we need to dsiplay the right stetment if the user enters the wrong choice
          ,3], # Item 7, index 6 will be the postion of the right answer (ubdex where right answer sits), this will be our check if answer is correct or no
          2: ["How many fields are there?",
          '2',
          '4',
          '7',
          '3',
          '6'
          ,1],
          3: ["Where can you find the tuckshop?",
          'B Block',
          'The Quad',
          'Field One',
          'Hockey Turf',
          'T Block'
          ,2],
          4: ["How many Gyms in school?",
          '8',
          '3',
          '2',
          '4',
          '1'
          ,2],
          5: ["What is the street address of Mount Roskill Grammar?",
          '23  Odessa Crescent',
          '22  Garden Road',
          '14  Kesteven Avenue',
          '17  Granada Place',
          '37 Frost Road'
          ,5],
          6: ["Where is the Maths Deparment?",
          'The Library',
          'C Block',
          'A Block',
          'The Hall',
          'E Block'
          ,3],
          7: ["What is the name of the principal?",
          'Leon Kennedy',
          'Gordon Freeman',
          'Marcus Fenix',
          'Greg Watson',
          'Anthony Carmine'
          ,4],
          8: ["How many turfs are there?",
          '2',
          '5',
          '3',
          '1',
          '2'
          ,1],
          9: ["Where is the Commerce department?",
          'T Block',
          'Gym 4',
          'E Block',
          'D Block',
          'The Library'
          ,3],
          10:["Where is the Music deparment block?",
          'E Block',
          'S Block',
          'D Block',
          'G Block',
          'M Block'
          ,5],
        }
        
        self.configure(bg='white smoke')
        
        self.app_label = tk.Label(self, text="Test your language Knowldege. \n Happy Tongan language week!!", bg = "white smoke", font=("Arial Bold", 25))
        self.app_label.place(x=40, y=100)      
        
        self.home_button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(Open))
        self.home_button.place(x=650, y=450)
        
        self.back_button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(Welcome))
        self.back_button.place(x=100, y=450)

        
        
        #widgets for the quiz goes below
        self.question_label = tk.Label (self, text = self.tongan_questions[question_number][0], font = ("Helvetica","18","bold"), bg="white smoke")
        self.question_label.place(x=40, y=200) 
        background_color = "white smoke"

        radiobutton_value = tk.IntVar() #holds value of radio buttons

        #first radio button to hold first choice answer 
        
        #Radiobutton 1
        self.choice1 = tk.Radiobutton (self, text = self.tongan_questions[question_number][1], font = ("Helvetica", "14"), bg = background_color, value = 1, variable = radiobutton_value, padx = 10, pady = 10)
        
        self.choice1.place(x=40, y=250)

        #Radiobutton 2
        
        self.choice2 = tk.Radiobutton (self, text = self.tongan_questions[question_number][2], font = ("Helvetica", "14"), bg = background_color, value = 2, variable = radiobutton_value, padx = 10, pady = 10)

        self.choice2.place(x=40, y=300)

        #Radiobutton 3
        self.choice3 = tk.Radiobutton (self, text = self.tongan_questions[question_number][3], font = ("Helvetica", "14"), bg = background_color, value = 3, variable = radiobutton_value, padx = 10, pady=10)

        self.choice3.place(x=40, y=300)
        #Radiobutton 4
        self.choice4 = tk.Radiobutton (self, text = self.tongan_questions[question_number][4], font = ("Helvetica", "14"), bg = background_color, value = 4, variable = radiobutton_value, padx = 10, pady = 10)

        self.choice4.place(x=40, y=350)

        #Radiobutton 5
        self.choice5 = tk.Radiobutton (self, text = self.tongan_questions[question_number][5], font = ("Helvetica", "14"), bg = background_color, value = 5, variable = radiobutton_value, padx = 10, pady = 10)

        self.choice5.place(x=40, y=400)


        #Confirm button
        self.confirm_button = tk.Button (self, text = "Confirm", font = ("Helvetica", "13", "bold"), bg = background_color, command = self.test_progress)

        self.confirm_button.grid (row = 6, padx = 5, pady = 5)

        #Score label
        self.score_label = tk.Label (self, text = "SCORE", font = ("Helvetica", "15"), bg = background_color,)

        self.score_label.grid (row = 7, padx = 10, pady = 1)

        #Quit Button
        self.quit= tk.Button(self, text="Quit", font=("Helvetica", "13", "bold"), bg="IndianRed1", command=self.end_screen)
        self.quit.place(x=40, y=550)

        
  
          #Method showing the next questions data
    def questions_setup (self):
      radiobutton_value.set(0)
      question_number +=1
      self.question_label.config(text = self.tongan_questions[question_number][0])
      self.choice1.config(text = self.tongan_questions[question_number][1])
      self.choice2.config(text = self.tongan_questions[question_number][2])
      self.choice3.config(text = self.tongan_questions[question_number][3])
      self.choice4.config(text = self.tongan_questions[question_number][4])
      self.choice5.config(text = self.tongan_questions[question_number][5])
  
    #This is the method that would get invoked with confrim answer button is clicked, to take care of test_progress
  
    def test_progress(self):
      global score
      scr_label = self.score_label
      choice = radiobutton_value.get()
      if len(asked)>9: #if the question is last
        if choice == self.tongan_questions[question_number][6]: #if the last question is the correct answer
          score+=1 
          scr_label.configure(text = score)
          self.confirm_button.config(text="Confirm")
          self.end_screen()
        else: #if the last question is the incorrect answer
          print(choice)
          score+=0
          scr_label.configure(text = " The correct answer was " + self.tongan_questions[question_number][5])
          self.confirm_button.config(text="Confirm")
          self.end_screen()
      else: #if it is not the last question
        if choice==0: #checks if the user has made a choice
          self.confirm_button.config(text="Try again please, you didnt select anyhting")
          choice=radiobutton_value.get()
        else: #if a choice was made and its not the last question
          if choice == self.tongan_questions[question_number][6]: #if thier choice is correct
            score+=1
            scr_label.configure(text = score)
            self.confirm_button.config(text="Confirm")
            self.questions_setup() #execute the method to move on to the next question 
          else: #if the choice was wrong
            print(choice)
            score+=0
            scr_label.configure(text="The correct answer was: " + self.tongan_questions[question_number][5])
            self.confirm_button.configure(text="Confirm")
            self.questions_setup() 
  
  
    def end_screen(self):
        app.withdraw() 

 #starting point of the program and the controller of the display of different frames       
class Program(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
      
        self.window = tk.Frame(self)
        self.window.pack()
        
        self.window.grid_rowconfigure(0, minsize = 500)
        self.window.grid_columnconfigure(0, minsize = 800)
        
        self.frames = {}# Frames of this program, controller shows them in other classes
        for F in (Open, Welcome, TonganQuiz):
            frame = F(self.window, self)
            self.frames[F] = frame
            frame.grid(row = 0, column=0, sticky="nsew")
            
        self.show_frame(Open)#initiallly the Start frame shows up
        
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Tongan Knowledge")


#Open of program
if __name__ == '__main__':           
    app = Program()
    app.maxsize(800,500)
    app.mainloop()
