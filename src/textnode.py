from enum import Enum
from typing import Self
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text: str, text_type: TextType, url: str | None = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node: Self) -> bool:
        return (
            self.text == node.text
            and self.text_type == node.text_type
            and self.url == node.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(node: TextNode) -> LeafNode:
    match node.text_type:
        case TextType.BOLD:
            return LeafNode(tag="b", value=node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=node.text)
        case TextType.IMAGE:
            return LeafNode(
                tag="img", value="", props={"src": node.url, "alt": node.text}
            )
        case TextType.ITALIC:
            return LeafNode(tag="i", value=node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=node.text, props={"href": node.url})
        case TextType.TEXT:
            return LeafNode(tag=None, value=node.text)
        case _:
            raise Exception("Unknown TextType")
