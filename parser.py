from tkinter import *
from tkinter import filedialog
import webbrowser
import xml.etree.ElementTree as ET

# Files.
from xml_load import xml_root_load
from utilities import xml_load_error, window_center
from parse_tags_keys import parse_file_to_json

# Root.
root = Tk()
app_title = "XML file parser "
root.title(app_title)

xml_loaded_root_file = None


#################################################################################################### Import file (xml).
def open_file_dialog():
    global xml_loaded_root_file

    root.filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select xml file",
        filetypes=[("xml files (*.xml)", "*.xml")],
    )

    # Window name change.
    root.title(app_title + "(" + root.filename + ")")

    try:
        # Import file.
        xml_tree = ET.parse(root.filename)
        xml_root = xml_tree.getroot()
        # Load to gui.
        xml_root_load(xml_root, root)

        with open(root.filename, "r", encoding="utf-8") as f:
            xml_data = f.read()
        xml_loaded_root_file = ET.fromstring(xml_data)
    except FileNotFoundError:
        xml_load_error(root)
    except ET.ParseError:
        xml_load_error(root)


#################################################################################################### Parse file (xml).
def open_parse_file_to_json():
    global xml_loaded_root_file

    if xml_loaded_root_file is not None:
        parse_file_to_json(root, xml_loaded_root_file)
    else:
        xml_load_error(root)


#################################################################################################### Open GitHub url.
def open_gh_url():
    webbrowser.open("https://github.com/Noarifumirimota/xml-parser")


#################################################################################################### Create menu.
menuBar = Menu(root)

# Opener list.
fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open xml file", command=open_file_dialog)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)
# Parser list.
parserList = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="JSON", menu=parserList)
parserList.add_command(label="Simple (Tags as keys)", command=open_parse_file_to_json)
# Adding help menu.
helpMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="GitHub (open in browser)", command=open_gh_url)

#################################################################################################### Root.
root.config(menu=menuBar)
window_center(root)

root.mainloop()
