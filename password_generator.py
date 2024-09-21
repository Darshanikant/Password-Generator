'''
This is the code of python to generate password with the combination of alphabet like uppercase, lowercase, digits and punctuations.
and also we can copy the password in our clipboard
'''
# library import
from tkinter import *
import random, string
import pyperclip  # this library to copy the password in clipboard

#creat a root variable
root = Tk() #get TK() module in root variable
root.geometry('400x400') # size of the windows
root.resizable(0,0) # disable windos by user
root.title("PYTHON PASSWORD GENERATOR") # titel of the window

Label(root,text='Password',font='arial  15 bold').pack() # we creat one label named as password
Label(root,text='python',font='arial 14 bold').pack() # another label named as python

pass_label = Label(root,text='password length',font = 'arial 10 bold').pack() # its a another lenth named as password length
pass_length= IntVar() # intvar is tikenter variable store integer value , here we use to set the password length
length = Spinbox(root,from_=8,to=32,textvariable=pass_length,width=15).pack() # spinbox allow to set the pass word length
pass_str = StringVar() # tkinter variable hold the string data here for password


def generator():
    password = [] # password variable as list to store the password
    
    if pass_length.get()>=4:
        password.append(random.choice(string.ascii_uppercase)) # random password uppercase 
        password.append(random.choice(string.ascii_lowercase)) # random password lowecase
        password.append(random.choice(string.digits)) # random password digit
        password.append(random.choice(string.punctuation)) # random password punctuations
         # all are append to the password variable
        
        for _ in range(pass_length.get()-4):
            # get combine all the password
            password.append(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation))
            
        random.shuffle(password)
    else:
        # If length is less than 4, just fill the required length with random choices
        for _ in range(pass_length.get()):
            password.append(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation))
    
    # Convert list to string and set it to the variable
    pass_str.set(''.join(password))


# copy the password to clipboard
def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text='GENERATE PASSWORD', command=generator).pack(pady=5) # generate password button
Entry(root, textvariable=pass_str).pack()
Button(root, text='COPY TO CLIPBOARD', command=Copy_password).pack(pady=5) # copy to clipboard button

root.mainloop()
        
        