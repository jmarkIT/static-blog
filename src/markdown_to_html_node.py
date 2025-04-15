from block_markdown import block_to_block_type, BlockType, markdown_to_blocks
from htmlnode import HTMLNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, LeafNode, TextNode, TextType


def markdown_to_html_node(markdown: str):
    parent_node = HTMLNode(tag="div", children=[])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.PARAGRAPH:
                children = text_to_children(block)
                node = HTMLNode(tag="p", children=children)
                parent_node.children.append(node)
            case BlockType.CODE:
                block_text = block.lstrip("```")
                block_text = block_text.rstrip("```")
                block_text = block_text.strip()
                text_node = TextNode(text=block_text, text_type=TextType.CODE)
                node = text_node_to_html_node(text_node)
                pre_node = HTMLNode(tag="pre", children=node)
                parent_node.children.append(pre_node)
            case BlockType.HEADING:
                level = block.count("#", 0, 5)
                block_text = block[level + 1 :]
                children = text_to_children(block_text)
                node = HTMLNode(tag=f"h{level}", children=children)
                parent_node.children.append(node)
            case BlockType.ORDERED_LIST:
                children = text_to_children(block)
                node = HTMLNode(tag="ol", children=children)
                parent_node.children.append(node)
            case BlockType.UNORDERED_LIST:
                children = text_to_children(block)
                node = HTMLNode(tag="ul", children=children)
                parent_node.children.append(node)
            case BlockType.QUOTE:
                children = text_to_children(block)
                node = HTMLNode(tag="blockquote", children=children)
                parent_node.children.append(node)

    return parent_node


def text_to_children(text: str) -> [LeafNode]:
    text_nodes = text_to_textnodes(text)
    leaf_nodes = []
    for text_node in text_nodes:
        leaf_node = text_node_to_html_node(text_node)
        leaf_nodes.append(leaf_node)
    return leaf_nodes
