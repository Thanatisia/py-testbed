"""
HTML Parser in Python using the built-in 'html.parser' package library/module
"""
import os
import sys
import requests
from html.parser import HTMLParser
from html.entities import name2codepoint

class HTML(HTMLParser):
    """
    Inherit the functions and attributes from 'html.parser.HTMLParser' to override
    """
    objects = [] # List of all objects
    tmp_obj_map = {"start-tag" : "", "end-tag" : "", "attrs" : [], "data" : "", "comment" : "", "named-entity" : "", "numerical-entity" : ""} # Temporary dictionary for mapping the starting tag to the ending tag, data etc

    def handle_starttag(self, tag, attrs):
        """
        print("Start Tag:", tag)
        for attr in attrs:
            print("\tattr: {}".format(attr))
        """

        # Set start/opening tag to temporary object map
        self.tmp_obj_map["start-tag"] = tag 
        self.tmp_obj_map["attrs"] = attrs

    def handle_endtag(self, tag):
        # Set end tag to temporary object map
        self.tmp_obj_map["end-tag"] = tag

        # Append the current temporary object map
        self.objects.append(self.tmp_obj_map)

        # Reset temporary object map
        self.tmp_obj_map = {"start-tag" : "", "end-tag" : "", "attrs" : [], "data" : "", "comment" : "", "named-entity" : "", "numerical-entity" : ""}

        # print("End Tag:", tag)
    def handle_data(self, data):
        # Set the data to the temporary object map
        self.tmp_obj_map["data"] = data

        # print("Data: {}".format(data))
    def handle_comment(self, data):
        # Set the comment to the temporary object map
        self.tmp_obj_map["comment"] = data

        # print("Comment: {}".format(data))
    def handle_entityref(self, name):
        c = chr(name2codepoint[name])

        # Set the named entity to the temporary object map
        self.tmp_obj_map["named-entity"] = c

        # print("Named Entity: {}".format(c))
    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))

        # Set the numerical entity to the temporary object map
        self.tmp_obj_map["numerical-entity"] = c

        # print("Numerical Entity: {}".format(c))

def parse_html(url):
    # Initialize Variables

    # Initialize HTML Parser object
    parser = HTML()

    # Send a HTTP REST API GET request
    response = requests.get(url)

    # Obtain HTML code of the send URL
    response_text = response.text

    # Feed the HTML code into the parser
    parser.feed(response_text)

    # Return/Output
    return parser

def search_tag_data(tag):
    """
    Search for the data within a specified tag
    """

def search_title(html_objects):
    """
    Search for the title of a particular url

    :: Params
    - html_objects : List containing dictionaries with the mapping of each line's components (data, starting tag, closing tag, comments etc)
        + Type: List
        - Values
            - object-dictionaries : Key-Value mappings of each line's components returned from the overriden HTML parser
                + Type: Dictionary
                - Key-Value Mappings
                    + start-tag : The Opening/Starting Tag; String
                    + end-tag"  : The Closing/Ending Tag; String
                    + attrs     : The Attributes; List
                    + data      : The content string wrapped between the tags; String
                    + comment   : Comments written in the tag; String
                    + named-entity : The Named entities; String
                    + numerical-entity : The Numerical entities
    """
    # Initialize Variables
    title = ""

    # Iterate through the object dictionaries and search for the title
    for i in range(len(html_objects)):
        # Get current object
        obj = html_objects[i]

        # List out the 'title'
        start_tag = obj["start-tag"]
        data = obj["data"]
        closing_tag = obj["end-tag"]

        # If start tag is 'title'
        if start_tag == "title":
            # print("Title: {}".format(data))
            title = data
            break

    # Output
    return title

def main():
    # Initialize Variables
    url = ""
    urls = []

    # Use the standard input stream if it is full/populated
    if not sys.stdin.isatty():
        input_stream = sys.stdin

        for line in input_stream:
            # Sanitize current line
            line = line.strip()

            # Append into a results list
            urls.append(line)
    else:
        exec = sys.argv[0]
        argv = sys.argv[1:]
        argc = len(argv)
        urls = argv.copy()

    if len(urls) > 0:
        for url in urls:
            # Parse the URL's HTML code into the HTML Parser and return the parser object
            parser = parse_html(url)

            # Obtain all stored html tags and data
            objs = parser.objects

            # Search for a data in a particular tag
            title = search_title(objs)
            print("URL: {}".format(url))
            print("Title: {}".format(title))
    else:
        print("No URLs provided.")

if __name__ == "__main__":
    main()

