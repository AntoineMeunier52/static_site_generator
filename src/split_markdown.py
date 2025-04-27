from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node.append(node)
            continue

        split_text = node.text.split(delimiter)
        if len(split_text) % 2 == 0:
            raise ValueError("invalid markdown, delimiter not close")
        for i in range(len(split_text)):
            if split_text[i] == "":
                continue
            if i % 2 == 0:
                new_node.append(TextNode(split_text[i], TextType.TEXT))
            else:
                new_node.append(TextNode(split_text[i], text_type))
    return new_node

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_node = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node.append(node)
            continue
        current_text = node.text
        image_info = extract_markdown_images(current_text)
        if len(image_info) == 0:
            new_node.append(node)
            continue
        for image in image_info:
            split_text = current_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(split_text) != 2:
                raise ValueError("invalid markdown, image not close")
            if split_text[0] != "":
                new_node.append(TextNode(split_text[0], TextType.TEXT))
            new_node.append(TextNode(image[0], TextType.IMAGE, image[1]))
            current_text = split_text[1]
        if current_text != "":
            new_node.append(TextNode(current_text, TextType.TEXT))
    return new_node

def split_nodes_link(old_nodes):
    new_node = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node.append(node)
            continue
        current_text = node.text
        image_info = extract_markdown_links(current_text)
        if len(image_info) == 0:
            new_node.append(node)
            continue
        for image in image_info:
            split_text = current_text.split(f"[{image[0]}]({image[1]})", 1)
            if len(split_text) != 2:
                raise ValueError("invalid markdown, image not close")
            if split_text[0] != "":
                new_node.append(TextNode(split_text[0], TextType.TEXT))
            new_node.append(TextNode(image[0], TextType.LINK, image[1]))
            current_text = split_text[1]
        if current_text != "":
            new_node.append(TextNode(current_text, TextType.TEXT))
    return new_node

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    print(nodes)
    return nodes
