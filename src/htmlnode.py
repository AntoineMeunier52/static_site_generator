class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented for the moment")

    def props_to_html(self):
        if self.props is None:
            return ""
        res_str = ""
        for attribute in self.props:
            res_str += f' {attribute}="{self.props[attribute]}"'
        return res_str

    def __repr__(self):
        return f"HTMLNODE/n/ttag = {self.tag}/n/tvalue = {self.value}/n/tchildren = {self.children}/n/tprops = {self.props_to_html}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf node must have a value")
        if self.tag is None:
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent node must have a tag")
        if self.children is None:
            raise ValueError("All parent node must have a children")

        res_html = ""
        for node in self.children:
            res_html += node.to_html()
        return f"<{self.tag}>{res_html}</{self.tag}>"

