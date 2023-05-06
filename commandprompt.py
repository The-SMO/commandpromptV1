import tkinter as tk
import os
import subprocess
events = []

line = 1
window = tk.Tk()
window.title("ConsolePanel")
text = tk.Text(window, height=40, width=80)
scroll = tk.Scrollbar(window)
text.configure(yscrollcommand=scroll.set,background="black",foreground="white")
text.pack(side=tk.LEFT)

scroll.config(command=text.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
def startline():
    #text.insert(0, tk.END, "yo")
    #text.delete("1.0",tk.END)
    text.insert(tk.END," \n>>> ")
    global line
    line += 1
    print(line)
def enter():
    lineget1 = str(line) + ".04"
    lineget2 = str(line) + ".20"
    input1 = text.get(lineget1,lineget2)
    #if input1 == "help":
        #list help from commandhelp.py
    os.system("cmd /k" + input1)
    returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
    print(returned_text)
    #text.delete("1.0","1.20")
    startline()
    print(input1)
    #print(lineget1)
    #print(lineget2)

enter=tk.Button(window,text="Enter", command = enter)
enter.pack()
text.insert(tk.END,">>> ")
tk.mainloop()


"""
import tkinter as tk
text_box = tk.Text()
window = tk.Tk(window, height=8, width=40)
window.title("Simple Text Editor")
def handle_keypress(event):
    if event.char == "U+23CE":
        print("Enter")
    #Print the character associated to the key pressed
    print(event.char)
key = window.bind("<Key>", handle_keypress)


def enter():
    print("yes")
    input1= text_box.get("1.0","1.20")
    print (input1)
    
enter=tk.Button(window,text="Enter", command = enter)
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)

#text = tk.Text(window, height=8, width=40)
scroll = tk.Scrollbar(window)
text_box.configure(yscrollcommand=scroll.set)
#text.pack(side=tk.LEFT)
  
scroll.config(command=text_box.yview)


text_box.pack()
scroll.pack(side=tk.RIGHT, fill=tk.Y)
#scroll.pack(side=tk.RIGHT, fill=tk.Y)
enter.pack()
#text_box.delete("1.0", "1.4")
#text_box.insert(tk.END, "Put me at the end!")
"""


