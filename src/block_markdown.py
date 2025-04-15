import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    blocks = [x for x in blocks if x != ""]
    blocks = [x.strip() for x in blocks]
    blocks = [x.strip("\n") for x in blocks]
    return blocks


def block_to_block_type(block: str) -> BlockType:
    lines = block.split("\n")
    # test for heading block
    if re.match(r"^(#{1,6})\s+(.+)$", block):
        return BlockType.HEADING

    # test for code block
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE

    # test for quote block
    is_quote_block = True
    for line in lines:
        if not line.startswith(">"):
            is_quote_block = False
    if is_quote_block:
        return BlockType.QUOTE

    # TODO: unordered list
    is_unordered_list_block = True
    for line in lines:
        if not line.startswith("- "):
            is_unordered_list_block = False
    if is_unordered_list_block:
        return BlockType.UNORDERED_LIST

    # TODO: test for ordered list
    is_ordered_list_block = True
    for i, line in enumerate(lines):
        if not line.startswith(f"{i + 1}. "):
            is_ordered_list_block = False
    if is_ordered_list_block:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
