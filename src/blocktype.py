from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown):
    lst_blocks = []
    split_markdown = markdown.split("\n\n")
    for line in split_markdown:
        if line == "":
            continue
        lst_blocks.append(line.strip())
    return lst_blocks

def check_headings(text):
    return text.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### "))

def check_code(text):
    text_split = text.split("```")
    if len(text_split) != 3:
        return False
    if text_split[0] == "" and text_split[-1] == "":
        return True
    return False

def check_quote(text):
    split_text = text.split("\n")

    for line in split_text:
        if line[0] == ">":
            continue
        else:
            return False
    return True

def check_unordered(text):
    split_text = text.split("\n")

    for line in split_text:
        if line[:2] == "- ":
            continue
        else:
            return False
    return True

def check_ordered(text):
    count_line = 1
    split_text = text.split("\n")

    for line in split_text:
        if not line.startswith(f"{count_line}. "):
            return False
        count_line += 1
    return True

def block_to_block_type(text):
    if check_headings(text):
        return BlockType.HEADING
    if check_code(text):
        return BlockType.CODE
    if check_quote(text):
        return BlockType.QUOTE
    if check_unordered(text):
        return BlockType.ULIST
    if check_ordered(text):
        return BlockType.OLIST
    return BlockType.PARAGRAPH


