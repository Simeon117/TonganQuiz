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
        
        self.exit_button = tk.Button(self, text="Back", font=("Arial", 15), bg="red", command=lambda: app.destroy())
        self.exit_button.place(x=100, y=450)
        


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
        
        self.configure(bg='smoke white')
        
        self.app_label = tk.Label(self, text="Test your language Knowldege. \n Happy Tongan language week!!", bg = "smoke white", font=("Arial Bold", 25))
        self.app_label.place(x=40, y=150)

        


      
        
        self.home_button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(Open))
        self.home_button.place(x=650, y=450)
        
        self.back_button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(Welcome))
        self.back_button.place(x=100, y=450)
        
        

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
