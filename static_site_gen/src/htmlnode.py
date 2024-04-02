class HTMLNode:
    def __init__(self, tag: str | None, value:str | None, children:list | None=None, props:dict[str,str] | None=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self) -> str:
        if self.props is not None:
            html = []
            for key, value in self.props.items():
                html.append(f' {key}="{value}"')
            return "".join(html)
        return ''

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict[str,str] | None=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("Invalid LeafNode: Missing value")
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props:dict[str,str] | None=None):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Invalid ParentNode: Missing tag")
        if self.children is None:
            raise ValueError("Invalid ParentNode: Missing children")
        leafs = ""
        for leaf in self.children:
            leafs += leaf.to_html()
        return f'<{self.tag}{self.props_to_html()}>{leafs}</{self.tag}>'
            
