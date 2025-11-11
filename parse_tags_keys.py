import json
import tkinter as tk
from tkinter import scrolledtext


def remove_namespaces(xml_root):
    for xml_element in xml_root.iter():
        if "}" in xml_element.tag:
            xml_element.tag = xml_element.tag.split("}", 1)[-1]
    return xml_root


def xml_dict(xml_root):
    js = {}

    nested = list(xml_root)
    if nested:
        nested_dict = {}

        for n in nested:
            name = n.tag
            value = xml_dict(n)

            if name in nested_dict:
                if isinstance(nested_dict[name], list):
                    nested_dict[name].append(value)
                else:
                    nested_dict[name] = [nested_dict[name], value]
            else:
                nested_dict[name] = value
        js.update(nested_dict)
    else:
        text = xml_root.text.strip() if xml_root.text else ""
        if text:
            js["value"] = text
    return js


def parse_file_to_json(root, xml_root):
    xml_root.tag = xml_root.tag.split("}", 1)[-1]
    # XML convertion into dict.
    dict_data = {xml_root.tag: xml_dict(remove_namespaces(xml_root))}

    # Dict into JSON string.
    json_str = json.dumps(dict_data, indent=4, ensure_ascii=False)

    # Create text field.
    text_box = scrolledtext.ScrolledText(root, wrap=tk.WORD)
    text_box.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    # Fill text field.
    text_box.insert(tk.END, json_str)
    text_box.config(state=tk.DISABLED)
