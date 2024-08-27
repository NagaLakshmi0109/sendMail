# Send mail

import tkinter as tk
from tkinter import scrolledtext
import smtplib
from email.mime.text import MIMEText
from tkinter import messagebox

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'gnagalakshmi0109@gmail.com'
smtp_password = 'xsed cmak flcj qwav'

smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
smtp_connection.starttls()

smtp_connection.login(smtp_username, smtp_password)

def sendMail():
	global root
	message = MIMEText(body.get("1.0", "end"))
	message['Subject'] = subject.get()
	message['From'] = smtp_username
	message['To'] = to.get()
	smtp_connection.send_message(message)
	smtp_connection.quit()
	messagebox.showinfo("Notification", "Mail sent!")
	root.destroy()
	smtp_connection.quit()


root = tk.Tk()
root.title("Compose")
root.geometry("400x500")

toLabel = tk.Label(root, text="To: ")
toLabel.grid(row=0, column=0, padx=(10, 5), pady=(10, 5), sticky=tk.W)
to = tk.Entry(root)
to.grid(row=0, column=1, padx=(5, 10), pady=(10, 5), sticky=tk.EW)

subjectLabel = tk.Label(root, text="Subject: ")
subjectLabel.grid(row=1, column=0, padx=(10, 5), pady=(5, 10), sticky=tk.W)
subject = tk.Entry(root)
subject.grid(row=1, column=1, padx=(5, 10), pady=(5, 10), sticky=tk.EW)

body = scrolledtext.ScrolledText(root, wrap=tk.WORD)
body.grid(row=2, column=0, columnspan=2, padx=10, pady=(5, 10), sticky=tk.NSEW)

sendButton = tk.Button(root, text="Send", command=sendMail, bg="blue", fg="white", width="10")
sendButton.grid(row=3, column=0, padx=10, pady=(0, 10))

root.bind('<Return>', lambda event: sendMail())

# Configure grid to make widgets responsive
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

root.mainloop()
