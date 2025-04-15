from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        images = extract_markdown_images(old_node.text)
        original_text = old_node.text

        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        for image in images:
            image_alt = image[0]
            image_link = image[1]
            sections = original_text.split(f"![{image_alt}]({image_link})", 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown")

            if sections[0] != "":
                new_nodes.append(TextNode(text=sections[0], text_type=TextType.TEXT))

            new_nodes.append(
                TextNode(text=image_alt, text_type=TextType.IMAGE, url=image_link)
            )
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(text=original_text, text_type=TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        links = extract_markdown_links(old_node.text)
        original_text = old_node.text

        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        for link in links:
            link_text = link[0]
            url = link[1]
            sections = original_text.split(f"[{link_text}]({url})", 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown")

            if sections[0] != "":
                new_nodes.append(TextNode(text=sections[0], text_type=TextType.TEXT))

            new_nodes.append(TextNode(text=link_text, text_type=TextType.LINK, url=url))
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(text=original_text, text_type=TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    node = TextNode(text=text, text_type=TextType.TEXT)
    nodes = split_nodes_image([node])
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes
