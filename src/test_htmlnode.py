import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_empty_props(self):
        print("test empty props")
        node = HTMLNode("a", "link", [], "")
        self.assertEqual(node.props_to_html(), "")

    def test_props(self):
        print("test props")
        node = HTMLNode("a", "link", [], {"test": "je suis un test", "href": "je suis un lien"})
        self.assertEqual(node.props_to_html(), ' test="je suis un test" href="je suis un lien"')

if __name__ == "__main__":
    unittest.main()
