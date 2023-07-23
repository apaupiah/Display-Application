from tkinter import *
from tkcalendar import *
from datetime import datetime
import csv
from tkinter import ttk
import subprocess

root = Tk()
root.title("ABC British International School")
root.configure(bg="MistyRose")
root.geometry("900x600")

cal = None  # Global variable to store the calendar widget
cal_button = None  # Global variable to store the button widget
process = None
def run_external_program():
    global process  # Access the global process variable
    process = subprocess.Popen(["python", "examsAppBorder1.2.py"], creationflags=subprocess.DETACHED_PROCESS)
    process.wait()
    print("External program terminated.")


def displaycommand():
    def grab_date():
        selected_date = cal.get_date()
        datetime_obj = datetime.strptime(selected_date, "%m/%d/%y")
        formatted_date = datetime_obj.strftime("%d/%m/%Y")
        my_date.config(text=formatted_date)

        # Call the function to filter exam details based on the selected date
        filter_exam_details(formatted_date)

    global cal, cal_button  # Access the global calendar and button widgets
    if cal:
        cal.destroy()  # Remove existing calendar widget if it exists
    if cal_button:
        cal_button.destroy()  # Remove existing button widget if it exists

    cal = Calendar(root, selectmode="day")
    cal.pack(pady=20)
    cal_button = Button(root, text="Select date", command=grab_date)
    cal_button.pack(pady=20)

my_date = Label(root, text="")
my_date.pack(pady=20)

def externalcommand():
    def grab_date():
        selected_date = cal.get_date()
        datetime_obj = datetime.strptime(selected_date, "%m/%d/%y")
        formatted_date = datetime_obj.strftime("%d/%m/%Y")
        my_date.config(text=formatted_date)

        # Call the function to filter exam details based on the selected date
        filter_exam_details(formatted_date)

    global cal, cal_button  # Access the global calendar and button widgets
    if cal:
        cal.destroy()  # Remove existing calendar widget if it exists
    if cal_button:
        cal_button.destroy()  # Remove existing button widget if it exists

    cal = Calendar(root, selectmode="day")
    cal.pack(pady=20)
    cal_button = Button(root, text="Select date", command=grab_date)
    cal_button.pack(pady=20)

def filter_exam_details(selected_date):
    # Assuming the CSV file has the following format:
    # Date,Start,Subject,Duration

    # Function to retrieve exam details based on the selected date
    def get_exam_details(selected_date):
        exam_details = []

        # Open the CSV file and read the data
        with open('exam_details.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Date'] == selected_date:
                    exam_details.append([
                        row['Date'],
                        row['Subject'],
                        row['Exam'],
                        row['Duration']
                    ])

        return exam_details

    # Example usage to retrieve and display filtered exam details
    exam_details = get_exam_details(selected_date)

    # Clear previous results (if any)
    clear_results()

    # Display the filtered exam details in a table
    tree = ttk.Treeview(root)
    tree["columns"] = ("Date", "Subject", "Exam", "Duration")
    tree.column("#0", width=0, stretch=NO)  # Remove the surplus column
    tree.heading("#0", text="", anchor="w")  # Empty heading for surplus column

    # Configure the style for the table headings
    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Helvetica', 15, 'bold'))

    for i, heading in enumerate(["Date","Subject", "Exam", "Duration"]):
        tree.column(heading, anchor="center", width=200)
        tree.heading(heading, text=heading, anchor="center")

    for detail in exam_details:
        tree.insert("", "end", values=detail)

    tree.pack()

def clear_results():
    # Clear previous results by destroying the treeview widget
    for widget in root.winfo_children():
        if isinstance(widget, ttk.Treeview):
            widget.destroy()

# Create the menu
mymenu = Menu(root)
root.config(menu=mymenu)

# Create the submenu
file_menu = Menu(mymenu, tearoff=0)
display_menu=Menu(mymenu, tearoff=0)
mymenu.add_cascade(label="View Exams", font=('Helvetica', 15, 'bold'), menu=file_menu)
file_menu.add_command(label="Internal", command=displaycommand)
file_menu.add_separator()
file_menu.add_command(label="External", command=externalcommand)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
mymenu.add_cascade(label="Exams Display", font=('Helvetica', 15, 'bold'), menu=display_menu)
display_menu.add_command(label="Internal Display", command=displaycommand)
display_menu.add_separator()
display_menu.add_command(label="External Display", command=run_external_program)
root.mainloop()
