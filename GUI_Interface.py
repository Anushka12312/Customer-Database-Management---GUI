from tkinter import *
from tkinter import messagebox
from Customer_Database import Database # type: ignore


db = Database('store.db')

## Functions

def execute_sql():
    sql_command = sql_text.get("1.0", "end-1c")  # Get the SQL command from the Text widget
    try:
        # Execute the SQL command and fetch the results
        results = db.execute_query(sql_command)
        # Clear the output Text widget
        output_text.delete("1.0", END)
        # Display the results in the output Text widget
        for result in results:
            output_text.insert(END, result)
            output_text.insert(END, "\n")
    except Exception as e:
        messagebox.showerror("Error", f"Error executing SQL: {str(e)}")

def populate_table():
    table.delete(0, END)
    for row in db.fetch():
        table.insert(END, row)

def add_record():
    if c_name_text.get() == '' or c_email_text.get() == '' or c_city_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(c_name_text.get(), c_email_text.get(), c_city_text.get())
    table.insert(END, (c_name_text.get(), c_email_text.get(), c_city_text.get()))
    clear_text()
    populate_table()

def select_item(event):
    try:
        global selected_item
        index = table.curselection()[0]
        selected_item = table.get(index)

        c_id_entry.delete(0, END)
        c_id_entry.insert(END, selected_item[0])
        c_name_entry.delete(0, END)
        c_name_entry.insert(END, selected_item[1])
        c_email_entry.delete(0, END)
        c_email_entry.insert(END, selected_item[2])
        c_city_entry.delete(0, END)
        c_city_entry.insert(END, selected_item[3])

    except IndexError:
        pass

def delete_record():
    db.remove(selected_item[0])
    clear_text()
    populate_table()

def update_record():
    db.update(selected_item[0], c_name_text.get(), c_email_text.get(), c_city_text.get())
    populate_table()

def clear_text():
    c_id_entry.delete(0, END)
    c_name_entry.delete(0, END)
    c_email_entry.delete(0, END)
    c_city_entry.delete(0, END)

## Function to open a new window ##
def open_new_window():
    sql_window = Toplevel(app_window)
    sql_window.title('SQL Commands')
    sql_window.geometry('600x400') # resize the window (widthxheight)

    #Message BOX for column names
    c_sql_label = Label(sql_window,text='Customer (Customer_ID, Customer_Name, Customer_Email_ID, Customer_City)' \
          ,font=('Times New Roman',12,'bold'),pady=20,padx=20) ## creates a label for Customer ID
    
    c_sql_label.grid(row=0,column=1,sticky=W) ## place the label in a grid,sticky : aligns label to the left

    #Textbox for SQL commands
    global sql_text 
    sql_text = Text(sql_window, height=5, width=40)
    sql_text.grid(row=1, column=1, columnspan=3, padx=20, pady=10)

    #Button to execute SQL
    execute_btn = Button(sql_window, text="Execute SQL", font=('Times New Roman', 11, 'bold'), width=12, command=execute_sql, fg="black", bg="coral")
    execute_btn.grid(row=2, column=1, pady=10)

    #Text widget to display SQL output
    global output_text 
    output_text = Text(sql_window, height=10, width=60)
    output_text.grid(row=3, column=1, columnspan=3, padx=20, pady=10)


## Creates a window
app_window=Tk()


## Widgets
## Customer ID
c_id_text=StringVar()
c_id_label=Label(app_window,text='Customer ID',font=('Times New Roman',12,'bold'),pady=20,padx=20) ## creates a label for Customer ID
# pady : padding/space along the Y-axis
c_id_label.grid(row=0,column=0,sticky=W) ## place the label in a grid,sticky : aligns label to the left
c_id_entry=Entry(app_window,textvariable=c_id_text,width=40)
c_id_entry.grid(row=0,column=1)

## Customer's Name
c_name_text=StringVar()
c_name_label=Label(app_window,text='Customer Name',font=('Times New Roman',12,'bold'),pady=20,padx=20) ## creates a label for Customer name
c_name_label.grid(row=1,column=0,sticky=W) ## place the label in a grid
c_name_entry=Entry(app_window,textvariable=c_name_text,width=40)
c_name_entry.grid(row=1,column=1)

## Customer's Email
c_email_text=StringVar()
c_email_label=Label(app_window,text='Customer Email-ID',font=('Times New Roman',12,'bold'),pady=20,padx=20) ## creates a label for Customer email
c_email_label.grid(row=2,column=0,sticky=W) ## place the label in a grid
c_email_entry=Entry(app_window,textvariable=c_email_text,width=40)
c_email_entry.grid(row=2,column=1)

## Customer's City
c_city_text=StringVar()
c_city_label=Label(app_window,text='Customer City',font=('Times New Roman',12,'bold'),pady=20,padx=20) ## creates a label for Customer email
c_city_label.grid(row=3,column=0,sticky=W) ## place the label in a grid
c_city_entry=Entry(app_window,textvariable=c_city_text,width=40)
c_city_entry.grid(row=3,column=1)

## Table display
table=Listbox(app_window,height=10,width=60)
table.grid(row=5,column=0,columnspan=3,rowspan=6,pady=20,padx=20)

## Scrollbar for table
scrollbar=Scrollbar(app_window)
scrollbar.grid(row=6,column=3)

## Connect scrollbar to listbox
table.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=table.yview) # yview: scroll along y axis

# Bind select
table.bind('<<ListboxSelect>>', select_item)


## Buttons
## Add Record button
add_btn=Button(app_window,text='Insert Record',font=('Times New Roman',11,'bold'),width=12,command=add_record,fg="black",bg="coral") # add record is a user defined function
add_btn.grid(row=0,column=4,pady=20)

## Delete Record button
delete_btn=Button(app_window,text='Delete Record',font=('Times New Roman',11,'bold'),width=12,command=delete_record,fg="black",bg="coral")
delete_btn.grid(row=1,column=4)

## Update Record button
update_btn=Button(app_window,text='Update Record',font=('Times New Roman',11,'bold'),width=12,command=update_record,fg="black",bg="coral")
update_btn.grid(row=2,column=4)

## Clear Input button
clear_btn=Button(app_window,text='Clear Input',font=('Times New Roman',11,'bold'),width=12,command=clear_text,fg="black",bg="coral")
clear_btn.grid(row=3,column=4)

## SQL Input button
sql_btn=Button(app_window,text='Execute SQL',font=('Times New Roman',11,'bold'),width=12,command=open_new_window,fg="black",bg="coral")
sql_btn.grid(row=12,column=1)

app_window.title('Customer')
app_window.geometry('600x600') # resize the window (widthxheight)


# Populate database
populate_table()

## Starts the program 
app_window.mainloop()
