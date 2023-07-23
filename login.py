import tkinter as tk
import subprocess
from tkinter import *
process = None
def login():
    global process
    # Get the entered username and password

    username = username_entry.get()
    password = password_entry.get()
    
    # Check if the username and password are correct
    if username == "admin" and password == "password":
        # Create a pop-up message to show the user login was successful
        popup = tk.Tk()
        popup.wm_title("Login successful!")
        label = tk.Label(popup, text="Login successful!")
        label.pack(side="top", fill="x", pady=10)
        B1 = tk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        popup.mainloop()

        #print("Login successful!")
        # Execute app.py or perform any other actions upon successful login
        subprocess.run(["python", "menudisplay1.2.pyw"],creationflags=subprocess.DETACHED_PROCESS)  # Replace "app.py" with the actual filename
        process.wait()
        print("External program terminated.")
    else:
        print("Invalid username or password")
    

def signup():
    # Get the entered username and password
    username = username_entry.get()
    password = password_entry.get()

    # Perform the signup logic here (e.g., store the username and password in a database)
    print(f"New user registered: Username - {username}, Password - {password}")
#create a pop message to show that the user has been registered
    popup = tk.Tk()
    popup.wm_title("New user Register!")
    #display the username and password      
    label = tk.Label(popup, text="New user registered: Username - {username}, Password - {password}")
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

#check if the user has already been registered
    


    

# Create the main window
window = tk.Tk()
window.title("ABC British International School Login Form")

# Create the heading label
heading_label = tk.Label(window, text="Welcome to the Examination System",fg='green', font=('Microsoft YaHei UI Light', 20,'bold'))
heading_label.pack()

# Create a frame to hold the form elements
form_frame = tk.Frame(window)
form_frame.pack(pady=20)



# Create a label and entry for the username
username_label = tk.Label(form_frame, text="Please Sign in:",fg='#57a1f8',font=('Microsoft YaHei UI Light',15,'bold'))
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(form_frame)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a label and entry for the password
password_label = tk.Label(form_frame, text="Enter Password:",fg='#57a1f8',font=('Microsoft YaHei UI Light',15,'bold'))
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(form_frame, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create the login and signup buttons
login_button = tk.Button(form_frame, text="Login",bg='#57a1f8',fg='white',font=('Calibri',12,'bold'), command=login)
login_button.grid(row=2, column=0, padx=10, pady=10)
signup_button = tk.Button(form_frame, text="Sign Up",bg='#57a1f8',fg='white',font=('Calibri',12,'bold'), command=signup)
signup_button.grid(row=2, column=1, padx=10, pady=10)

# Create a logo image
logo_image = tk.PhotoImage(file="login.png")

# Create a label to display the logo image
logo_label = tk.Label(window, image=logo_image)
logo_label.pack()

# Start the Tkinter event loop
window.mainloop()
