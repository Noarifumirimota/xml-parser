import tkinter as tk
from tkinter import ttk


# Error loader draw.
def xml_load_error(root):
    tk.Label(
        root,
        text="File not found or invalid XML file.",
        background="#ff6666",
        font=("Helvetica", 8, "bold"),
    ).pack()


# Get all tags without namespaces.
# def xml_get_tags(xml_root):
#     print(
#         {xml_element.tag.split('}', 1)[-1] for xml_element in xml_root.iter()}
#     )


#################################################################################################### Load tree.
def xml_insert_element(xml_tree_view, xml_parent_element, xml_element):
    # Get tag text.
    xml_text_value = (xml_element.text or "").strip()

    # Remove namespace.
    new_tag_name = xml_element.tag.split("}", 1)[-1]

    # Insert element into tree.
    node_id = xml_tree_view.insert(
        xml_parent_element, "end", text=new_tag_name, values=[xml_text_value]
    )

    # Open (tag expansion).
    xml_tree_view.item(node_id, open=True)

    """
        Recursion.
    """
    for xml_element_child in xml_element:
        xml_insert_element(xml_tree_view, node_id, xml_element_child)


def xml_root_load(xml_root, root):
    # xml_get_tags(xml_root)

    # Get all tags and text.
    # for xml_element in xml_root.iter():
    #     print(xml_element.tag.split('}', 1)[-1])
    #     # print(xml_element.attrib)
    #     print(xml_element.text)

    # Generate tree gui view by ttk.
    xml_tree_view = ttk.Treeview(root, columns=("text",), show="tree headings")
    xml_tree_view.heading("#0", text="Tag")
    xml_tree_view.heading("text", text="Text value")
    xml_tree_view.pack(fill="both", expand=True, padx=5, pady=5)

    # Add the main tree root.
    tree_root_id = xml_tree_view.insert(
        "",
        "end",
        text=xml_root.tag.split("}", 1)[-1],
        values=[(xml_root.text or "").strip()],
    )

    # Fill tree with childs.
    for xml_element in xml_root:
        xml_insert_element(xml_tree_view, tree_root_id, xml_element)
