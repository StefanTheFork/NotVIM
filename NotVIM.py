from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess

window = Tk()
window.title('NotVIM')
window.iconbitmap("NotVIM.ico")
window.geometry('800x850')
gpath = ''


def runMyCode():
    global gpath
    if gpath == '':
        saveMsg = Toplevel()
        msg = Label(saveMsg, text="Save Before You Run")
        msg.pack()
        return
    command = f'python {gpath}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    outputResult, error = process.communicate()
    output.insert('1.0', outputResult)
    output.insert('1.0', error)


def openMyFile():
    path = askopenfilename(filetypes=[('Python Stuff', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        textEditor.delete('1.0', END)
        textEditor.insert('1.0', code)
        global gpath
        gpath = path


def saveMyFileAs():
    global gpath
    if gpath == '':
        path = asksaveasfilename(filetypes=[('Python Stuff', '*.py')])
    else:
        path = gpath
    with open(path, 'w') as file:
        code = textEditor.get('1.0', END)
        file.write(code)


textEditor = Text(height=50,width=9090)
textEditor.config(bg='#362f2e', fg='#d2ded1', insertbackground='black')
textEditor.pack()

output = Text(height=30,width=9090)
output.config(bg='#362f2e', fg='#1dd604')
output.pack()

menuBar = Menu(window)

fileBar = Menu(menuBar, tearoff=0)
fileBar.add_command(label='Open', command=openMyFile)
fileBar.add_command(label='Save', command=saveMyFileAs)
menuBar.add_cascade(label='File', menu=fileBar)

runBar = Menu(menuBar, tearoff=0)
runBar.add_command(label='Run', command=runMyCode)
menuBar.add_cascade(label='Run', menu=runBar)

window.config(menu=menuBar)
window.mainloop()