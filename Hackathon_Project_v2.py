# Build an app like thing where anyone can report a sick , injured , rabid or unneutered dog to bbmp or nearest vet hospital or ambulance.

import customtkinter
from email.message import EmailMessage
import ssl
import smtplib
import authcheck

subject = "Person has found an injured/sick/rabid/un-neutered dog"
email_receiver = 'dakir41056@artgulin.com' # Example email from https://temp-mail.org/en
email_password = authcheck.idpw()[1]
email_sender = authcheck.idpw()[0]

def report():
    em = EmailMessage()
    
    em['From'] = str(entry1)

    em['To'] = email_receiver

    em['Subject'] = subject
    body = input("Please enter what has happened to the dog you have found :  ")
    body2 = input("Enter your current google location :  ")
    em.set_content(body)
    em.set_content(body2)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


def open_next_gui():
    new_root = customtkinter.CTk()
    new_root.geometry("500x500")
    new_root.title("Animal Rescue")
    
    new_frame = customtkinter.CTkFrame(master=new_root)
    new_frame.pack(pady=20, padx=60, fill="both", expand=True)
    
    new_label = customtkinter.CTkLabel(master=new_frame, text="Welcome to the Animal Rescue App")
    new_label.pack(pady=12, padx=10)
    
    button1 = customtkinter.CTkButton(master=new_frame, text="Report", command=report)
    button1.pack(pady=12, padx=10)
    
    new_root.mainloop()

def login():
    email = str(entry1.get())
    password = str(entry2.get())
    
    if email == email and password == password:
        root.destroy()
        
        open_next_gui()

root = customtkinter.CTk()
root.geometry("500x500")
root.title("Animal Rescue App")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Animal Rescue", font=("Arial", 24, "bold"), text_color= "#ADD8E6")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Email")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)
app_pwd = customtkinter.CTkLabel(master=frame, text="Enter your App Password from Google", font=("Arial", 15), text_color= "#318CE7")
app_pwd.pack(pady=1)
app_pwd = customtkinter.CTkLabel(master=frame, text="https://myaccount.google.com/apppasswords", font=("Arial",13), text_color="#318CE7")
app_pwd.pack(pady=0)

button1 = customtkinter.CTkButton(master=frame, text="Login", command=login)
button1.pack(pady=12, padx=10)

root.mainloop()
