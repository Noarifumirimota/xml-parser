from tkinter import *
from tkinter import filedialog

# Root.
root = Tk()
appTitle = 'XML file parser '
root.title(appTitle)

# Open file (xml).
def openFileDialog():
    root.filename = filedialog.askopenfilename(
        initialdir='/',
        title='Select xml file',
        filetypes=[
            ("xml files (*.xml)", "*.xml")
        ]
    )
    root.title(appTitle + "(" + root.filename + ")")

    # Open.
    openedFile = open(root.filename, 'r')
    testFirstLine = str(openedFile.readlines())
    Label(root, text=testFirstLine).pack()
    openedFile.close()

# Create menu.
menuBar = Menu(root)

# Adding file menu.
fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='Open xml file', command=openFileDialog)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=root.quit)
# Adding help menu.
helpMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_command(label='GitHub')

# Root.
root.config(menu=menuBar)
root.geometry(
    '1024x768'
)

root.mainloop()
