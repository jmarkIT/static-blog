import unittest
from block_markdown import markdown_to_blocks, block_to_block_type, BlockType


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_extra_lines(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_list(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

```this is a code block
it has
code in it```

> Here is a quote
> This is still a quote

- This is a list
- with items

1. Something
2. Something else

# Dogs
    """
        blocks = markdown_to_blocks(md)
        block_types = []
        for block in blocks:
            block_types.append(block_to_block_type(block))
        self.assertListEqual(
            block_types,
            [
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
                BlockType.CODE,
                BlockType.QUOTE,
                BlockType.UNORDERED_LIST,
                BlockType.ORDERED_LIST,
                BlockType.HEADING,
            ],
        )

    def test_block_to_block_type_paragraph(self):
        md = "This is just some text. this part is **bold**, but it doesn't matter"
        self.assertEqual(
            block_to_block_type(md),
            BlockType.PARAGRAPH,
        )

    def test_block_to_block_type_heading(self):
        md = "### Heading level 3"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_block_to_block_type_code(self):
        md = "```Code in a block\nthis is another line```"
        self.assertEqual(block_to_block_type(md), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        md = "> a quote\n> line 2\n> more quotes"
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        md = "- bullet\n- bullet\n- bullet"
        self.assertEqual(block_to_block_type(md), BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered_list(self):
        md = "1. first item\n2. second item"
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)
