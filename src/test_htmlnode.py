import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode(props=props)
        html = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), html)

    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
        node = HTMLNode("p", "Here is some text", None, {"class": "bridge"})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, Here is some text, children: None, {'class': 'bridge'})",
        )

    def test_leaf_to_html_a(self):
        tag = "a"
        value = "Click Me!"
        props = {
            "href": "https://www.google.com",
        }
        node = LeafNode(tag=tag, value=value, props=props)
        html = '<a href="https://www.google.com">Click Me!</a>'
        self.assertEqual(node.to_html(), html)

    def test_leaf_to_html_a_two_props(self):
        tag = "a"
        value = "Click Me!"
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = LeafNode(tag=tag, value=value, props=props)
        html = '<a href="https://www.google.com" target="_blank">Click Me!</a>'
        self.assertEqual(node.to_html(), html)

    def test_leaf_to_html_p(self):
        tag = "p"
        value = "This is just some text!"
        node = LeafNode(tag=tag, value=value)
        html = "<p>This is just some text!</p>"
        self.assertEqual(node.to_html(), html)

    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), html)

    def test_parent_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_to_html_with_props(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode(
            "span", [grandchild_node], props={"class": "the-best-span"}
        )
        parent_node = ParentNode("div", [child_node], {"class": "something"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="something"><span class="the-best-span"><b>grandchild</b></span></div>',
        )
