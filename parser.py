from tkinter import *
from tkinter import filedialog
import xml.etree.ElementTree as ET
# Files.
from xml_load import xml_root_load, xml_load_error

# Root.
root = Tk()
app_title = 'XML file parser '
root.title(app_title)

#################################################################################################### Import file (xml).
def open_file_dialog():
    root.filename = filedialog.askopenfilename(
        initialdir='/',
        title='Select xml file',
        filetypes=[
            ("xml files (*.xml)", "*.xml")
        ]
    )

    # Window name change.
    root.title(app_title + "(" + root.filename + ")")

    try:
        # Import.
        xml_tree = ET.parse(root.filename)
        xml_root = xml_tree.getroot()
        # Load.
        xml_root_load(xml_root, root)
    except FileNotFoundError:
        xml_load_error(root)
    except ET.ParseError:
        xml_load_error(root)

#################################################################################################### Create menu.
menuBar = Menu(root)

# Adding file menu.
fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='Open xml file', command=open_file_dialog)
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=root.quit)
# Adding help menu.
helpMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Help', menu=helpMenu)
helpMenu.add_command(label='GitHub')

#################################################################################################### Root.
root.config(menu=menuBar)
root.geometry(
    '1024x768+20+20'
)

root.mainloop()
