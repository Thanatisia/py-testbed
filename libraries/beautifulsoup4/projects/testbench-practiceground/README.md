# Python Web scraping using BeautifulSoup4

## Information
### Description
- BeautifulSoup is a Python framework/library that performs allows data scraping on the web (aka web scraping)
    + Using this along with the functionality to 'crawl' the web, and you will have a webcrawler

## Setup
### Dependencies
+ python
+ python-pip
+ python-venv
- Python Packages
    + beautifulsoup4
    + requests : For HTTP REST API (GET requests etc)

### Pre-Requisites
- Create Python Virtual Environments
    - Generate Virtual Environment Shell
        ```bash
        python3 -m venv [virtual-environment-name]
        ```
    - Chroot into Virtual Environment
        - Linux
            ```bash
            . [virtual-environment-name]/bin/activate
            ```
        - Windows
            ```bash
            .\[virtual-environment-name]\Scripts\activate
            ```

- Install python dependencies
    ```bash
    python3 -m pip install -Ur requirements.txt
    ```

## Documentation
### Operational Workflow
- Send a HTTP REST API GET request to the youtube URL and return the response stream
    ```bash
    response = requests.get(url)
    ```

- Obtain the HTML file contents from the response
    ```bash
    response_text = response.text
    ```

- Initialize BeautifulSoup to crawl the response text HTML5 code
    ```bash
    soup = BeautifulSoup(response_text, features="html.parser")
    ```

- Find all occurences/existences of the tag (aka parameter 'name') and return in a list object
    ```bash
    result = soup.find_all(name="tag")
    ```

- Obtain the result(s)
    + In the case where the tag/name is 'title', there is only one result due to the search query being '<title></title>' and there is only 1 title tag in any HTML5 markup
    ```bash
    link = result[0]
    ```

- Obtain the text returned from the search
    ```bash
    tag_text = link.text
    ```

- Sanitize title (remove the opening and closing tags)
    - Opening tag
        ```bash
        tag_text = tag_text.replace("<tag>", "")
        ```
    - Closing tag
        ```bash
        tag_text = tag_text.replace("</tag>", "")
        ```

- Output
    ```bash
    print("Result: {}".format(tag))
    ```

## Resources

## References

## Remarks

