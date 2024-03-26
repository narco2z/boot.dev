from textnode import TextNode

def main():
    a = TextNode("This is a text textnote", "bold", "boot.dev")
    b = TextNode("This is a text textnote", "bold", "boot.dev")
    c = TextNode("this is a text textnote", "italic")
    print(a)
    print(b)
    print(c)
    print(a.__eq__(b))
    
main()

