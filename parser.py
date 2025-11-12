from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import scrolledtext
import webbrowser
import xml.etree.ElementTree as ET
from tkinter import ttk

# Files.
from xml_load import xml_root_load
from utilities import xml_load_error, xml_save_error, window_center
from parse_tags_keys import parse_file_to_json

# Root.
root = Tk()
app_title = "XML file parser "
root.title(app_title)

xml_loaded_root_file = None
xml_json_to_save = None

xml_tree_view = ttk.Treeview(root, columns=("text",), show="tree headings")
text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD)


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
        # Clear elements.
        xml_tree_view.delete(*xml_tree_view.get_children())
        text_box.config(state=tk.NORMAL)
        text_box.delete("1.0", tk.END)
        # Import file.
        xml_tree = ET.parse(root.filename)
        xml_root = xml_tree.getroot()
        # Load to gui.
        xml_root_load(xml_root, root, xml_tree_view)

        # JSON parse.
        with open(root.filename, "r", encoding="utf-8") as f:
            xml_data = f.read()
        xml_loaded_root_file = ET.fromstring(xml_data)
    except FileNotFoundError:
        xml_load_error(root)
    except ET.ParseError:
        xml_load_error(root)


#################################################################################################### Parse file xml.
def open_parse_file_to_json():
    global xml_loaded_root_file
    global xml_json_to_save

    xml_json_to_save = None

    if xml_loaded_root_file is not None:
        xml_json_to_save = parse_file_to_json(xml_loaded_root_file, text_box)
    else:
        xml_load_error(root)


#######################################################################################3############ Save file
def save_as_json():
    global xml_json_to_save

    if xml_json_to_save is not None:
        file_to_save = filedialog.asksaveasfilename(
            defaultextension=".json", filetypes=[("xml files (*.xml)", "*.xml")]
        )

        if file_to_save:
            try:
                with open(file_to_save, "w", encoding="utf-8") as f:
                    f.write(xml_json_to_save)
            except Exception as e:
                xml_save_error(root)
    else:
        xml_save_error(root)


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
# File save.
fileSave = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Save", menu=fileSave)
fileSave.add_command(label="As JSON file", command=save_as_json)
# Adding help menu.
helpMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="GitHub (open in browser)", command=open_gh_url)

root.config(menu=menuBar)

#################################################################################################### Elements.
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

# Tree gui view by ttk.
xml_tree_view.heading("#0", text="Tag")
xml_tree_view.heading("text", text="Text value")
xml_tree_view.grid(column=0, row=0, padx=2, pady=2, sticky="nsew")

# Text field.
text_box.grid(column=0, row=1, padx=2, pady=2, sticky="nsew")

#################################################################################################### Root.
window_center(root)
root.mainloop()
