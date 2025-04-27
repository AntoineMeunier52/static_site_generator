from textnode import TextType
from textnode import TextNode
from markdown_to_html import markdown_to_html

def main():
    print(TextType)
    textlink = TextNode("This is some anchor", TextType.LINK, "http://www.anchor.test")
    print(textlink)
    test = """
# **test**

## _test_

### test

no a heading

>testquote
>retest
>ahah tjrs test

>test a nouveau

- 1test
- 2test
- 3test

1. order
2. ordertest
3. teste

```testcode alsdhpoifh**bodl**
ldkjf
alsdkfjlj
lsadkjf';;
```

#### test
##### test
###### test
####### no head
######## no head2
"""
    markdown_to_html(test)

main()
