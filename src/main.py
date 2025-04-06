from textnode import TextNode, TextType


def main():
    node = TextNode("Here is some text", TextType.BOLD, "www.google.com")
    print(node)


if __name__ == "__main__":
    main()
