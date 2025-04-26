class HTMLNode ():
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
