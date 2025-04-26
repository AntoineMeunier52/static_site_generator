import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_props(self):
        print("test empty props")
        node = HTMLNode("a", "link", [], "")
        self.assertEqual(node.props_to_html(), "")

    def test_props(self):
        print("test props")
        node = HTMLNode("a", "link", [], {"test": "je suis un test", "href": "je suis un lien"})
        self.assertEqual(node.props_to_html(), ' test="je suis un test" href="je suis un lien"')

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_lesf_to_html_a(self):
        node = LeafNode("a", "this is a link!!!", {"href": "https://www.boot.dev"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.boot.dev\">this is a link!!!</a>")
    
    def test_to_html_with_parent(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
