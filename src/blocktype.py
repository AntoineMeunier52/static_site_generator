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

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH


