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
        

class TonganQuiz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.tongan_questions = {
          1: ["What is the capital of Tonga?", #item 1, index 0 will be the question
          'Papeete', # Item 2, index 1 will be the first choice
          'Avarua', # Item 3, index 2 will be the second choice
          'Nuku`alofa', # Item 4, index 3 will be the third choice
          'Alofi', # Item 5, index 4 will be the fourth choice
          'Funafuti'# Item 6, index 5 will be the write statement we need to dsiplay the right stetment if the user enters the wrong choice
          ,3], # Item 7, index 6 will be the postion of the right answer (ubdex where right answer sits), this will be our check if answer is correct or no
          2: ["What is Hello in Tongan?",
          'Mālō e lelei',
          'Talofa',
          'Fakalofa Atu',
          'Kia Ora',
          'Aloha'
          ,1],
          3: ["Which term do you use to ask how someone is in Tongan?",
          'Vacava tiko',
          'Fefe hake',
          'kei te pehea koe',
          'O ā mai oe',
          'Pehea ʻoe'
          ,2],
          4: ["How do you say teacher in Tongan?",
          'Kaiako',
          'Faiako',
          'Tija',
          'Faiaoga',
          'Kumu'
          ,2],
          5: ["What is sorry in Tongan?",
          '23  O',
          'Malie,
          'E kala mai',
          'Vosota',
          'Fakamolemole'
          ,5],
          6: ["How do you announce name in Tongan?",
          'The Library',
          '`O (name) wau',
          'Ko (name) au',
          'O (name) a`u',
          'Ko (name) ahau'
          ,3],
          7: ["What is thank you in Tongan?",
          'Fa`afetai',
          'Whakawhetai koe',
          'Vinaka',
          'malo ʻaupito',
          'Mahalo iā ʻoe'
          ,4],
          8: ["What is the Tongan name for New Zealand?",
          'Nuʻu Sila',
          'Niu Sila',
          'Aotearoa',
          'Ni`u Siladi',
          'Niu Silani'
          ,1],
          9: ["What is yes and no in tongan",
          'Io and Sega',
          'E and To',
          '`Io and `Ikai',
          'Ioe and Leai',
          'Ae and Kao'
          ,3],
          10:["What is the word Friend in Tongan",
          'Kapitiga',
          'Uo',
          'E hoa',
          'I tokani',
          'Kaungameʻa'
          ,5],
        }
        
        self.configure(bg='white smoke')
        
              
        
        self.home_button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(Open))
        self.home_button.place(x=650, y=220)
        
        

        self.question_number = 1

        
        
        #widgets for the quiz goes below
        self.question_label = tk.Label (self, text = self.tongan_questions[self.question_number][0], font = ("Helvetica","18","bold"), bg="white smoke")
        self.question_label.place(x=40, y=200) 
        background_color = "white smoke"

        self.radiobutton_value = tk.IntVar() #holds value of radio buttons

        #first radio button to hold first choice answer 
        
        #Radiobutton 1
        self.choice1 = tk.Radiobutton (self, text = self.tongan_questions[self.question_number][1], font = ("Helvetica", "14"), bg = background_color, value = 1, variable = self.radiobutton_value, padx = 10, pady = 10)
        
        self.choice1.place(x=40, y=250)

        #Radiobutton 2
        
        self.choice2 = tk.Radiobutton (self, text = self.tongan_questions[self.question_number][2], font = ("Helvetica", "14"), bg = background_color, value = 2, variable = self.radiobutton_value, padx = 10, pady = 10)

        self.choice2.place(x=40, y=300)

        #Radiobutton 3
        self.choice3 = tk.Radiobutton (self, text = self.tongan_questions[self.question_number][3], font = ("Helvetica", "14"), bg = background_color, value = 3, variable = self.radiobutton_value, padx = 10, pady=10)

        self.choice3.place(x=40, y=300)
        #Radiobutton 4
        self.choice4 = tk.Radiobutton (self, text = self.tongan_questions[self.question_number][4], font = ("Helvetica", "14"), bg = background_color, value = 4, variable = self.radiobutton_value, padx = 10, pady = 10)

        self.choice4.place(x=40, y=350)

        #Radiobutton 5
        self.choice5 = tk.Radiobutton (self, text = self.tongan_questions[self.question_number][5], font = ("Helvetica", "14"), bg = background_color, value = 5, variable = self.radiobutton_value, padx = 10, pady = 10)

        self.choice5.place(x=40, y=400)


        #Confirm button
        self.confirm_button = tk.Button (self, text = "Confirm", font = ("Helvetica", "13", "bold"), bg = background_color, command = self.test_progress)

        self.confirm_button.place (x = 650, y = 450)

        #Score label
        self.score_label = tk.Label (self, text = "SCORE", font = ("Helvetica", "15"), bg = background_color,)

        self.score_label.place (x = 100, y = 460)

        #Quit Button
        self.quit= tk.Button(self, text="Quit", font=("Helvetica", "13", "bold"), bg="IndianRed1", command=self.end_screen)
        self.quit.place(x=40, y=550)

        
  
          #Method showing the next questions data
    def questions_setup (self):
      self.radiobutton_value.set(0)
      self.question_number +=1
      self.question_label.config(text = self.tongan_questions[self.question_number][0])
      self.choice1.config(text = self.tongan_questions[self.question_number][1])
      self.choice2.config(text = self.tongan_questions[self.question_number][2])
      self.choice3.config(text = self.tongan_questions[self.question_number][3])
      self.choice4.config(text = self.tongan_questions[self.question_number][4])
      self.choice5.config(text = self.tongan_questions[self.question_number][5])
  
    #This is the method that would get invoked with confrim answer button is clicked, to take care of test_progress
  
    def test_progress(self):
      global score
      score = 0
      
      scr_label = self.score_label
      choice = self.radiobutton_value.get()
      if self.question_number ==10: #if the question is last
        if choice == self.tongan_questions[self.question_number][6]: #if the last question is the correct answer
          score+=1 
          scr_label.configure(text = score)
          self.confirm_button.config(text="Confirm")
          self.end_screen()
        else: #if the last question is the incorrect answer
          print(choice)
          score+=0
          scr_label.configure(text = " The correct answer was " + self.tongan_questions[self.question_number][5])
          self.confirm_button.config(text="Confirm")
          self.end_screen()
      else: #if it is not the last question
        if choice==0: #checks if the user has made a choice
          self.confirm_button.config(text="Try again please, you didnt select anyhting")
          choice=self.radiobutton_value.get()
        else: #if a choice was made and its not the last question
          if choice == self.tongan_questions[self.question_number][6]: #if thier choice is correct
            score+=1
            scr_label.configure(text = score)
            self.confirm_button.config(text="Confirm")
            self.questions_setup() #execute the method to move on to the next question 
          else: #if the choice was wrong
            print(choice)
            score+=0
            scr_label.configure(text="The correct answer was: " + self.tongan_questions[self.question_number][5])
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
