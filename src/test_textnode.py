import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq_without_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a test node with url", TextType.LINK, "http://www.unittest.com")
        node2 = TextNode("This is a test node with url", TextType.LINK, "http://www.unittest.com")
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text", TextType.TEXT)
        node2 = TextNode("This is a text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_neq_text(self):
        node = TextNode("This is a text", TextType.TEXT)
        node2 = TextNode("This is a another text", TextType.TEXT)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
