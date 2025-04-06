import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is the first text node", TextType.ITALIC)
        node2 = TextNode("This is the second text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, url="www.google.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, url="www.yahoo.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_url_is_none(self):
        node = TextNode("This is a text node", TextType.ITALIC, url=None)
        node2 = TextNode("This is a text node", TextType.ITALIC, url="www.yahoo.com")
        self.assertNotEqual(node, node2)

    def test_not_eq_everything(self):
        node = TextNode("This is the first text node", TextType.ITALIC, url=None)
        node2 = TextNode(
            "This is the second text node", TextType.BOLD, url="www.google.com"
        )
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
