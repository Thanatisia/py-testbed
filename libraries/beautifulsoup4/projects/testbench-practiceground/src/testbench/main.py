"""
Testbed: Get the YouTube video title by its url using python
"""
import os
import sys
import requests
from bs4 import BeautifulSoup

def remove_tags(text, tags=None):
    """
    Cleanup and Sanitize result output by removing tags

    :: Params
    - text : Your text to remove tags
        Type: String

    - tags : List containing your opening tag and closing tag to remove from the text
        + Type: List
        - Notes
            + Ensure that there are only 2 elements in the list - the opening tag and the closing tag
    """
    if tags != None and len(tags) == 2:
        for tag in tags:
            text = text.replace(tag, "")

    return text

def remove_tag_title(title):
    # Cleanup and Sanitize result output
    title = title.replace("<title>","")
    title = title.replace("</title>","")

    return title

def get_cli_arguments():
    """
    Get CLI arguments
    """
    exec = sys.argv[0]
    argv = sys.argv[1:]
    argc = len(argv)

    return [argv, argc]

def process_cli_arguments(argv, argc):
    """
    Process the obtained CLI arguments
    """
    # Initialize variables
    url = ""

    # Check if required arguments exists
    if argc >= 1:
        # Parse in required configuration files
        url = argv[0]

    # Output
    return url

def main():
    # Obtain CLI arguments
    argv, argc = get_cli_arguments()

    # Process CLI arguments
    url = process_cli_arguments(argv, argc)

    # Null Value check
    if url == "":
        # Obtain URL from user input
        url = input("Please enter a URL to scrape: ")

    # Send a HTTP REST API GET request to the youtube URL and return the response stream
    response = requests.get(url)

    # Initialize BeautifulSoup to crawl the response text HTML5 code
    soup = BeautifulSoup(response.text, features="html.parser")

    # DEBUG: View soup
    print("Soup: {}".format(soup))

    # Find all occurences of the title which is the link
    result = soup.find_all(name="title")

    # DEBUG: View result
    print("Result: {}".format(result))

    # Find link
    link = result[0]

    # Obtain the text returned (the title)
    title = link.text

    # Sanitize title
    title = remove_tags(title, ["<title>", "</title>"])

    # Output
    print("Title: {}".format(title))


if __name__ == "__main__":
    main()

