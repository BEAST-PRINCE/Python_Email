import tkinter as tk
import smtplib


root = tk.Tk()
root.title("Mail Application")
root.geometry("630x680")
root.resizable(width=False, height=False)



# Send E-Mail
def send_mail():
    try:
        temp_username = username.get()
        temp_password = password.get()
        temp_to_id = to_id.get()
        temp_subject = subject.get()
        temp_body = body_entry.get("1.0", tk.END)

        if temp_password == '' or temp_username == '' or temp_to_id == '' or temp_subject == '' or temp_body == '':
            notification_label.config(text="All fields are required!", fg="red")
            return
        else:
            final_message = "Subject: {}\n\n{}".format(temp_subject, temp_body)

            # Connect to the SMTP server
            smtp_server = "smtp.gmail.com"
            smtp_port = 587
            smtp_username = temp_username
            smtp_password = temp_password

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)

            server.sendmail(temp_username, temp_to_id, final_message)

            server.quit()

            notification_label.config(text="Email sent successfully!", fg="green")

    except Exception as e:
        notification_label.config(text=f"Error sending email: {str(e)}", fg="red")
        print(e)


# Reset Window
def reset():
    username_entry.delete(0,'end')
    password_entry.delete(0,'end')
    to_entry.delete(0,'end')
    subject_entry.delete(0,'end')
    body_entry.delete(0,'end')

    notification_label.config(text='')



# Head Label
heading_label = tk.Label(root, text="Application to send Email.", font=("Helvetica",24))
heading_label.pack(pady=15)


# Main Frame
mainFrame = tk.Frame(root, borderwidth=5)
mainFrame.pack(fill='x')


# Labels for Input
email_label = tk.Label(mainFrame, text="Email: ", font=("Calibri",18))
email_label.grid(row=1, column=0, sticky=tk.W, padx=10)

password_label = tk.Label(mainFrame, text="Password: ", font=("Calibri",18))
password_label.grid(row=2, column=0, sticky=tk.W, padx=10)

to_label = tk.Label(mainFrame, text="To: ", font=("Calibri",18))
to_label.grid(row=3, column=0, sticky=tk.W, padx=10)

subject_label = tk.Label(mainFrame, text="Subject: ", font=("Calibri",18))
subject_label.grid(row=4, column=0, sticky=tk.W, padx=10)

body_label = tk.Label(mainFrame, text="Body: ", font=("Calibri",18))
body_label.grid(row=5, column=0, sticky=tk.W, padx=10)


# Notification LAbel
notification_label = tk.Label(mainFrame, text='', font=("Calibri",18))
notification_label.grid(row=8, column=0, sticky=tk.W, padx=15, pady=30)

# Storage Variables
username = tk.StringVar()
password = tk.StringVar()
to_id = tk.StringVar()
subject = tk.StringVar()

username_entry = tk.Entry(mainFrame, textvariable=username, width=50)
username_entry.grid(row=1, column=1, padx=15)

password_entry = tk.Entry(mainFrame, textvariable=password, show='*', width=50)
password_entry.grid(row=2, column=1, padx=15)

to_entry = tk.Entry(mainFrame, textvariable=to_id, width=50)
to_entry.grid(row=3, column=1, padx=15)

subject_entry = tk.Entry(mainFrame, textvariable=subject, width=50)
subject_entry.grid(row=4, column=1, padx=15)

# body_entry = tk.Entry(mainFrame, textvariable=body, width=30)
body_entry = tk.Text(mainFrame, font=("Arial",14), height=15, width=40)
body_entry.grid(row=5, column=1, padx=15, pady=10)


# Reset Button
reset_button = tk.Button(mainFrame, text="Reset", command = reset, borderwidth=3, height=2, width=10)
reset_button.grid(row=7, pady=20, sticky=tk.W, padx=10)


# Send Button
send_button = tk.Button(mainFrame, text="Send", command=send_mail, borderwidth=3, height=2, width=10)
send_button.grid(row=7, column=1, pady=10, sticky=tk.E)



root.mainloop()