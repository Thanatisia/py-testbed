USAGE
=====

## Documentations

*Tools*
-------
+ htmlparser : Test HTML parser using html.parser

## CLI utilities

> htmlparser

*Synopsis/Syntax*
-----------------
- Standard
    ```bash
    htmlparser [urls ...]
    ```

- By Streaming Standard Input
    ```bash
    htmlparser - < file
    ```

- By Piping the standard output of a command into htmlparser's standard input
    ```bash
    [command-output] | htmlparser -
    ```

*Parameters*
------------
- Positionals
    - urls : Specify the target URLs you wish to parse and return the title of
        + Type: String
- Optionals
    - With Arguments
    - Flags

*Usage*
-------
- Obtain the title of a specified URL link
    - Notes
        - Parse a youtube URL string into the CLI utility argument and
            + the application will output the URL mapped to the title in a text file
    - Standard
        ```bash
        htmlparser [urls ...]
        ```
    - By Streaming Standard Input
        ```bash
        htmlparser - < file-name
        ```
    - By Piping the standard output of a command into htmlparser's standard input
        ```bash
        [command-output] | htmlparser -
        ```

## Importing/Embedding as a library/module

*Library*
---------

### Package
- htmlparser : A TestBench HTML Parser created using 'html.parser' to visualize how the library works as an HTML parser

### Modules
- htmlparser
    - main

### Classes
- htmlparser.main
    - `.HTML(HTMLParser)`: Inherit the functions and attributes from 'html.parser.HTMLParser' to override
        - Inheritance
            + html.parser.HTMLParser

### Functions
- htmlparser.main.HTML()
    - `.handle_starttag(tag, attrs)`: Overriding the function found in HTMLParser of the same name; Set start/opening tag to temporary object map
        - Parameter/Argument Signature
            - tag: Specify the opening tag
                + Type: String
            - attrs: Specify the attribute of that tag
                + Type: String
    - `.handle_endtag(tag)`         : Overriding the function found in HTMLParser of the same name; Set end tag to temporary object map, Append the current temporary object map and Reset temporary object map
        - Parameter/Argument Signature
            - tag: Specify the closing tag
                + Type: String
            - attrs: Specify the attribute of that tag
                + Type: String
    - `.handle_data(data)`          : Overriding the function found in HTMLParser of the same name; Set the data to the temporary object map
        - Parameter/Argument Signature
            - data: The data contained between HTML tags
                + Type: String
    - `.handle_comment(data)`       : Overriding the function found in HTMLParser of the same name; Set the comment to the temporary object map
        - Parameter/Argument Signature
            - data: The comments found in HTML code
                + Type: String
    - `.handle_entityref(name)`     : Overriding the function found in HTMLParser of the same name; Set the named entity to the temporary object map
        - Parameter/Argument Signature
            - name: Handle the callback named character reference
                + Type: String
    - `.handle_charref(name)`       : Overriding the function found in HTMLParser of the same name; Set the numerical entity to the temporary object map
        - Parameter/Argument Signature
            - name: Handle the callback decimal/hexadecimal equivalent of the general character reference
                + Type: String

### Data Classes/Types

### Attributes/Variables Objects
- htmlparser.main.HTML(HTMLParser)
    - `.objects`: List of all objects
        + Type: List
        + Default: [] (Empty List)
    - `.tmp_obj_map` : Temporary dictionary for mapping the starting tag to the ending tag, data etc
        + Type: Dictionary
        + Default: {"start-tag" : "", "end-tag" : "", "attrs" : [], "data" : "", "comment" : "", "named-entity" : "", "numerical-entity" : ""} # 

*Usage*
-------
- Import python package
    - General utilities
    - htmlparser source
        ```python
        from htmlparser.main import HTML, parse_html, search_title
        ```

- Initialize Variables
    ```python
    # Initialize Variables
    ```

- Initialize Module Classes
    ```python
    html = HTML()
    ```

- Initialize User Input Pipeline
    ```python
    # Initialize Variables
    urls = []

    # Use the standard input stream if it is full/populated
    if not sys.stdin.isatty():
        # Obtain Standard Input Stream/Pipe
        input_stream = sys.stdin

        # Iterate through the stream and receive all texts
        for line in input_stream:
            # Sanitize current line
            line = line.strip()

            # Append into a results list
            urls.append(line)
    else:
        # Obtain received CLI arguments from Argument parser
        exec = sys.argv[0]
        argv = sys.argv[1:]
        argc = len(argv)

        # Copy the CLI argument list into the urls list
        urls = argv.copy()

    # Validate that there are URLs provided
    if len(urls) > 0:
        # There are URLs provided
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
    ```

## Wiki

## Resources

## References

## Remarks

