from textnode import TextType
from textnode import TextNode

def main():
    print(TextType)
    textlink = TextNode("This is some anchor", TextType.LINK, "http://www.anchor.test")
    print(textlink)

main()
