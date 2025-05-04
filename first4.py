import tkinter as tk
from tkinter import ttk, messagebox
import pymysql

# Create main window
win = tk.Tk()
win.geometry("1500x790+0+0")
win.title("Student Management System")

# Title Label
title_label = tk.Label(win, text="Student Management System", font=("Arial", 30, "bold"), border=12, relief=tk.GROOVE, bg="sky blue", foreground="green")
title_label.pack(side=tk.TOP, fill=tk.X)

# Detail Frame (for input fields)
detail_frame = tk.LabelFrame(win, text="Enter Details", font=("Arial", 20, "bold"), bd=12, relief=tk.GROOVE)
detail_frame.place(x=10, y=80, width=500, height=710)

# Data Frame (for displaying records)
data_frame = tk.Frame(win, bd=12, bg="lightgrey", relief=tk.GROOVE)
data_frame.place(x=560, y=100, width=900, height=680)

# Variables
rollno = tk.StringVar()
name = tk.StringVar()
class_var = tk.StringVar()
section = tk.StringVar()
contact = tk.StringVar()
fathersnm = tk.StringVar()
address = tk.StringVar()
gender = tk.StringVar()
dob = tk.StringVar()
search_by = tk.StringVar()

# Entry Fields
# Roll Number
rollno_lbl = tk.Label(detail_frame, text="Roll No", font=("Arial", 17), bg="lightgrey")
rollno_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="w")
rollno_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 17), textvariable=rollno)
rollno_ent.grid(row=0, column=1, padx=10, pady=10)

# Name
name_lbl = tk.Label(detail_frame, text="Name", font=("Arial", 17), bg="lightgrey")
name_lbl.grid(row=1, column=0, padx=10, pady=10, sticky="w")
name_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 17), textvariable=name)
name_ent.grid(row=1, column=1, padx=10, pady=10)

# Class
class_lbl = tk.Label(detail_frame, text="Class", font=("Arial", 17), bg="lightgrey")
class_lbl.grid(row=2, column=0, padx=10, pady=10, sticky="w")
class_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 17), textvariable=class_var)
class_ent.grid(row=2, column=1, padx=10, pady=10)

# Section
section_lbl = tk.Label(detail_frame, text="Section", font=("Arial", 17), bg="lightgrey")
section_lbl.grid(row=3, column=0, padx=10, pady=10, sticky="w")
section_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 17), textvariable=section)
section_ent.grid(row=3, column=1, padx=10, pady=10)

# Contact
contact_lbl = tk.Label(detail_frame, text="Contact", font=("Arial", 17), bg="lightgrey")
contact_lbl.grid(row=4, column=0, padx=10, pady=10, sticky="w")
contact_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 17), textvariable=contact)
contact_ent.grid(row=4, column=1, padx=10, pady=10)

# Father's Name
fathersnm_lbl = tk.Label(detail_frame, text="Father's Name", font=("Arial", 17), bg="lightgrey")
fathersnm_lbl.grid(row=5, column=0, padx=10, pady=10, sticky="w")
fathersnm_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 17), textvariable=fathersnm)
fathersnm_ent.grid(row=5, column=1, padx=10, pady=10)

# Address
address_lbl = tk.Label(detail_frame, text="Address", font=("Arial", 17), bg="lightgrey")
address_lbl.grid(row=6, column=0, padx=10, pady=10, sticky="w")
address_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 17), textvariable=address)
address_ent.grid(row=6, column=1, padx=10, pady=10)

# Gender
gender_lbl = tk.Label(detail_frame, text="Gender", font=("Arial", 17), bg="lightgrey")
gender_lbl.grid(row=7, column=0, padx=10, pady=10, sticky="w")
gender_ent = ttk.Combobox(detail_frame, font=('Arial', 17), textvariable=gender)
gender_ent['values'] = ("Male", "Female", "Others")
gender_ent.grid(row=7, column=1, padx=2, pady=2)

# Date of Birth
dob_lbl = tk.Label(detail_frame, text="D.O.B", font=("Arial", 17), bg="lightgrey")
dob_lbl.grid(row=8, column=0, padx=10, pady=10, sticky="w")
dob_ent = tk.Entry(detail_frame, bd=7, font=("Arial", 17), textvariable=dob)
dob_ent.grid(row=8, column=1, padx=10, pady=10)

# Functions
def fetch_data():
    try:
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        curr = conn.cursor()
        curr.execute("SELECT * FROM data")
        rows = curr.fetchall()
        if len(rows) != 0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert('', tk.END, values=row)
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching data: {e}")
    finally:
        if conn:
            conn.close()

def add_func():
    if rollno.get() == "" or name.get() == "" or class_var.get() == "":
        messagebox.showerror("Error!", "Please fill all the fields!")
    else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
            curr = conn.cursor()
            curr.execute("INSERT INTO data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                          (rollno.get(), name.get(), class_var.get(), section.get(), contact.get(), fathersnm.get(), address.get(), gender.get(), dob.get()))
            conn.commit()
            messagebox.showinfo("Success", "Record added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error adding data: {e}")
        finally:
            if conn:
                conn.close()
            fetch_data()
            clear()

def get_cursor(event):
    cursor_row = student_table.focus()
    content = student_table.item(cursor_row)
    row = content['values']
    rollno.set(row[0])
    name.set(row[1])
    class_var.set(row[2])
    section.set(row[3])
    contact.set(row[4])
    fathersnm.set(row[5])
    address.set(row[6])
    gender.set(row[7])
    dob.set(row[8])

def clear():
    rollno.set("")
    name.set("")
    class_var.set("")
    section.set("")
    contact.set("")
    fathersnm.set("")
    address.set("")
    gender.set("")
    dob.set("")

def update_func():
    if rollno.get() == "":
        messagebox.showerror("Error", "Please select a record to update!")
    else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
            curr = conn.cursor()
            curr.execute("UPDATE data SET name=%s, class=%s, section=%s, contact=%s, fathersnm=%s, address=%s, gender=%s, dob=%s WHERE rollno=%s",
                          (name.get(), class_var.get(), section.get(), contact.get(), fathersnm.get(), address.get(), gender.get(), dob.get(), rollno.get()))
            conn.commit()
            messagebox.showinfo("Success", "Record updated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error updating data: {e}")
        finally:
            if conn:
                conn.close()
            fetch_data()
            clear()

def delete_func():
    if rollno.get() == "":
        messagebox.showerror("Error", "Please select a record to delete!")
    else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
            curr = conn.cursor()
            curr.execute("DELETE FROM data WHERE rollno=%s", (rollno.get(),))
            conn.commit()
            messagebox.showinfo("Success", "Record deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting data: {e}")
        finally:
            if conn:
                conn.close()
            fetch_data()
            clear()

def search_func():
    try:
        conn = pymysql.connect(host="127.0.0.1", port="3306", user="root", password="", database="sms1")
        curr = conn.cursor()
        if search_by.get() == "Roll No":
            curr.execute("SELECT * FROM data WHERE rollno=%s", (search_in.get(),))
        elif search_by.get() == "Name":
            curr.execute("SELECT * FROM data WHERE name LIKE %s", ("%" + search_in.get() + "%",))
        elif search_by.get() == "Contact":
            curr.execute("SELECT * FROM data WHERE contact=%s", (search_in.get(),))
        elif search_by.get() == "Father's Name":
            curr.execute("SELECT * FROM data WHERE fathersnm LIKE %s", ("%" + search_in.get() + "%",))
        elif search_by.get() == "Class":
            curr.execute("SELECT * FROM data WHERE class=%s", (search_in.get(),))
        elif search_by.get() == "Section":
            curr.execute("SELECT * FROM data WHERE section=%s", (search_in.get(),))
        elif search_by.get() == "D.O.B":
            curr.execute("SELECT * FROM data WHERE dob=%s", (search_in.get(),))

        rows = curr.fetchall()
        if len(rows) != 0:
            student_table.delete(*student_table.get_children())
            for row in rows:
                student_table.insert('', tk.END, values=row)
        else:
            messagebox.showinfo("Info", "No matching records found!")
    except Exception as e:
        messagebox.showerror("Error", f"Error searching data: {e}")
    finally:
        if conn:
            conn.close()

# Buttons Frame
btn_frame = tk.Frame(detail_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
btn_frame.place(x=40, y=544, width=370, height=120)

# Buttons
add_btn = tk.Button(btn_frame, text="Add", bg="lightgrey", bd=7, font=("Arial", 13), width=15, command=add_func)
add_btn.grid(row=0, column=0, padx=5, pady=5)

update_btn = tk.Button(btn_frame, text="Update", bg="lightgrey", bd=7, font=("Arial", 13), width=15, command=update_func)
update_btn.grid(row=0, column=1, padx=5, pady=5)

delete_btn = tk.Button(btn_frame, text="Delete", bg="lightgrey", bd=7, font=("Arial", 13), width=15, command=delete_func)
delete_btn.grid(row=1, column=0, padx=5, pady=5)

clear_btn = tk.Button(btn_frame, text="Clear", bg="lightgrey", bd=7, font=("Arial", 13), width=15, command=clear)
clear_btn.grid(row=1, column=1, padx=5, pady=5)

# Search Frame
search_frame = tk.Frame(data_frame, bg="lightgrey", bd=10, relief=tk.GROOVE)
search_frame.pack(side=tk.TOP, fill=tk.X)

search_lbl = tk.Label(search_frame, text="Search", bg="lightgrey", font=("Arial", 14))
search_lbl.grid(row=0, column=0, padx=12, pady=2)

search_in = ttk.Combobox(search_frame, font=("Arial", 14), state="readonly", textvariable=search_by)
search_in['values'] = ("Roll No", "Name", "Contact", "Father's Name", "Class", "Section", "D.O.B")
search_in.grid(row=0, column=1, padx=12, pady=2)

search_btn = tk.Button(search_frame, text="Search", font=("Arial", 13), bd=9, width=14, bg="lightgrey", command=search_func)
search_btn.grid(row=0, column=2, padx=12, pady=2)

showall_btn = tk.Button(search_frame, text="Show All", font=("Arial", 13), bd=9, width=14, bg="lightgrey", command=fetch_data)
showall_btn.grid(row=0, column=3, padx=12, pady=2)

# Database Frame
main_frame = tk.Frame(data_frame, bg="lightgrey", bd=11, relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

student_table = ttk.Treeview(main_frame, columns=("Roll No.", "Name", "Class", "Section", "Contact", "Father's Name", "Address", "Gender", "D.O.B"), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

student_table.heading("Roll No.", text="Roll No.")
student_table.heading("Name", text="Name")
student_table.heading("Class", text="Class")
student_table.heading("Section", text="Section")
student_table.heading("Contact", text="Contact")
student_table.heading("Father's Name", text="Father's Name")
student_table.heading("Address", text="Address")
student_table.heading("Gender", text="Gender")
student_table.heading("D.O.B", text="D.O.B")

student_table['show'] = 'headings'

student_table.column("Roll No.", width=100)
student_table.column("Name", width=100)
student_table.column("Class", width=100)
student_table.column("Section", width=100)
student_table.column("Contact", width=100)
student_table.column("Father's Name", width=100)
student_table.column("Address", width=150)
student_table.column("Gender", width=100)
student_table.column("D.O.B", width=100)

student_table.pack(fill=tk.BOTH, expand=True)

fetch_data()

student_table.bind("<ButtonRelease-1>", get_cursor)

# Run Tkinter main loop
win.mainloop()