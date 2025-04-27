from blocktype import (
    BlockType,
    block_to_block_type,
    markdown_to_blocks,
)

from split_markdown import (
    text_to_textnodes
)

from htmlnode import (
    LeafNode,
    ParentNode
)

from textnode import (
    TextNode,
    text_node_to_html_node
)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes

def create_heading(block):
    tag = ""
    text_to_child = ""
    if block.startswith("# "):
        tag = "h1"
        text_to_child = block[2:]
    elif block.startswith("## "):
        tag = "h2"
        text_to_child = block[3:]
    elif block.startswith("### "):
        tag = "h3"
        text_to_child = block[4:]
    elif block.startswith("#### "):
        tag = "h4"
        text_to_child = block[5:]
    elif block.startswith("##### "):
        tag = "h5"
        text_to_child = block[6:]
    elif block.startswith("###### "):
        tag = "h6"
        text_to_child = block[7:]
    children = text_to_children(text_to_child)
    return ParentNode(tag, children)

def create_paragraph(block):
    lines = block.split("\n")
    para = " ".join(lines)
    children = text_to_children(para)
    return ParentNode("p", children)

def create_quote(block):
    quote_lst = []
    lines = block.split("\n")

    for line in lines:
        children = text_to_children(line[1:])
        quote_lst.append(ParentNode("blockquote", children))

    return ParentNode("div", quote_lst)

def create_ulist(block):
    lines = block.split("\n")
    li_lst = []

    for line in lines:
        children = text_to_children(line[2:])
        li_lst.append(ParentNode("li", children))
    return ParentNode("ul", li_lst)

def create_olist(block):
    lines = block.split('\n')
    li_lst = []
    count = 1

    for line in lines:
        children = text_to_children(line[2+len(str(count)):])
        li_lst.append(ParentNode("li", children))
        count += 1
    return ParentNode("ol", li_lst)

def create_code(block):
    leaf = LeafNode("code", block[3:-3])
    return ParentNode("pre", [leaf])

def block_to_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.HEADING:
        return create_heading(block)
    if block_type == BlockType.PARAGRAPH:
        return create_paragraph(block)
    if block_type == BlockType.QUOTE:
        return create_quote(block)
    if block_type == BlockType.ULIST:
        return create_ulist(block)
    if block_type == BlockType.OLIST:
        return create_olist(block)
    if block_type == BlockType.CODE:
        return create_code(block)
    raise ValueError("invalid block type")

def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    node_blocks = []
    for block in blocks:
        node_blocks.append(block_to_node(block))
    return ParentNode("div", node_blocks)

