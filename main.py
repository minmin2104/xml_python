from book_content_handler import BookContentHandler
from xml import sax
import sys


def main():
    filename = "./books.xml"
    book_ct_handler = BookContentHandler()
    try:
        sax.parse(filename, book_ct_handler)
    except sax.SAXParseException as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
