from typing import Self


class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list[Self] | None = None,
        props: dict[str, str] | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        html = ""
        for key, value in self.props.items():
            html += f' {key}="{value}"'
        return html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str, str] | None = None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value

        html = ""
        open_tag = f"<{self.tag}"
        if self.props is not None:
            for key, value in self.props.items():
                open_tag += f' {key}="{value}"'
        open_tag += ">"
        close_tag = f"</{self.tag}>"
        html += open_tag + self.value + close_tag
        return html


class ParentNode(HTMLNode):
    def __init__(
        self, tag: str, children: list[Self], props: dict[str, str] | None = None
    ):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Missing tag")
        if self.children is None:
            raise ValueError("Missing children")

        html = ""
        open_tag = f"<{self.tag}"
        if self.props is not None:
            for key, value in self.props.items():
                open_tag += f' {key}="{value}"'
        open_tag += ">"
        html += open_tag
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html
