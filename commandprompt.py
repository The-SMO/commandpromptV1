"""
======================= START OF LICENSE NOTICE =======================
  Copyright (C) 2023 Olivers Sokolovs Kazaks. All Rights Reserved

  NO WARRANTY. THE PRODUCT IS PROVIDED BY DEVELOPER "AS IS" AND ANY
  EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL DEVELOPER BE LIABLE FOR
  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
  GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
  IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
  OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THE PRODUCT, EVEN
  IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
======================== END OF LICENSE NOTICE ========================
  Primary Author: Olivers Sokolovs Kazaks

"""

import tkinter as tk
import os
import subprocess
events = []
addextra = 0
line = 1
window = tk.Tk()
window.title("ConsolePanel")
text = tk.Text(window, height=40, width=80)
scroll = tk.Scrollbar(window)
text.configure(yscrollcommand=scroll.set,background="black",foreground="white",insertbackground='white')
text.pack(side=tk.LEFT)

scroll.config(command=text.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
def startline():
    #text.insert(0, tk.END, "yo")
    #text.delete("1.0",tk.END)
    text.insert(tk.END," \n>>> ")
    global line
    global addextra
    line = line + addextra
    line += 1
    #print(line)
def enter():
    lineget1 = str(line) + ".04"
    lineget2 = str(line) + ".90"
    input1 = text.get(lineget1,lineget2)
    #if input1 == "help":
        #list help from commandhelp.py
    command = "cmd /c" +"\""+ input1+"\""
    os.system("cmd /c" +"\""+ input1+"\"")
    #returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
    #print(returned_text)
    retext = subprocess.check_output(command,errors=None,shell=None)
    print(retext)
    text.insert(tk.END,retext)
    global addextra
    addextra = 0
    addextra = len(retext.splitlines())
    #text.delete("1.0","1.20")
    startline()
    #print(input1)
    #print(lineget1)
    #print(lineget2)

enter=tk.Button(window,text="Enter", command = enter)
enter.pack()
text.insert(tk.END,"======================= START OF LICENSE NOTICE =======================\n  Copyright (C) 2023 Olivers Sokolovs Kazaks. All Rights Reserved\n\n  NO WARRANTY. THE PRODUCT IS PROVIDED BY DEVELOPER \"AS IS\" AND ANY\n  EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE\n  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR\n  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL DEVELOPER BE LIABLE FOR\n  ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL\n  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE\n  GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS\n  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER\n  IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR\n  OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THE PRODUCT, EVEN\n  IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.\n======================== END OF LICENSE NOTICE ========================\n  Primary Author: Olivers Sokolovs Kazaks\n")
text.insert(tk.END,">>> ")
line += 16
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


