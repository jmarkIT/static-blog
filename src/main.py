from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    extract_markdown_images,
    extract_markdown_links,
    text_to_textnodes,
)
from block_markdown import markdown_to_blocks, block_to_block_type
from markdown_to_html_node import markdown_to_html_node


def main():
    md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

### a level 3 header

some more text

1. cat
2. dog

- parrot
- donkey

> some quote text
> more quotes

```
some code _italics_ nope
more code
```
    """

    node = markdown_to_html_node(md)
    print(node)


if __name__ == "__main__":
    main()
