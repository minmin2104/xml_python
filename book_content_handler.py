from xml import sax


class BookContentHandler(sax.handler.ContentHandler):
    def __init__(self):
        self.current_data = ""

    def startElement(self, name, attr):
        if name == "book":
            print("ID:", attr.getValue("id"))
        self.current_data = ""

    def endElement(self, name):
        if name == "book" or name == "catalog":
            return
        print(f"{name}: {self.current_data}")

    def characters(self, content):
        self.current_data += content
