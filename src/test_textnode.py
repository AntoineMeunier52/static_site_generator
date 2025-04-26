import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq_without_url(self):
        print("test eq without url")
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        print("test eq with url")
        node = TextNode("This is a test node with url", TextType.LINK, "http://www.unittest.com")
        node2 = TextNode("This is a test node with url", TextType.LINK, "http://www.unittest.com")
        self.assertEqual(node, node2)

    def test_neq(self):
        print("test no equal type")
        node = TextNode("This is a text", TextType.TEXT)
        node2 = TextNode("This is a text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_neq_text(self):
        print("test not equal test")
        node = TextNode("This is a text", TextType.TEXT)
        node2 = TextNode("This is a another text", TextType.TEXT)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
