YouTube Webscraper CLI utilities and implementations
====================================================

## Information
### Description
- Collection of useful webscraper CLI utilities powered by BeautifulSoup
    + With this being based around YouTube video searches and obtaining information via HTML Parsing

### Scripts
+ yt-obtain-url : Simple YouTube URL title finder CLI utility

## Setup
### Dependencies
+ python
+ python-pip
+ python-venv

### Pre-Requisites
- Create Python Virtual Environment
    - Generate Virtual Environment
        ```bash
        python3 -m venv [virtual-environment-name]
        ```
    - Chroot into Virtual Environment
        - Linux-based
            ```bash
            . [virtual-environment-name]/bin/activate
            ```
        - Windows-based
            ```bash
            .\[virtual-environment-name]\Scripts\activate
            ```

- Optionals
    - Append the Virtual Environment directories into system path
        - 'bin' (binaries) directory
            ```bash
            export PATH+="/path/to/[virtual-environment-name]/bin:"
            ```

### Installation
- Install using pip
    ```bash
    pip install git+https://github.com/Thanatisia/py-webscraping#subdirectory=frameworks/beautifulsoup4/apps/youtube
    ```

- Install locally in development mode
    - Clone repository
        ```bash
        git clone https://github.com/Thanatisia/py-webscraping
        ```
    - Change directory into repository
        ```bash
        cd frameworks/beautifulsoup4/apps/youtube
        ```
    - Install python package dependencies
        ```bash
        python3 -m pip install -Ur requirements.txt
        ```
    - (Optional) Uninstall package
        ```bash
        pip uninstall yt-scripts
        ```
    - Install locally in development mode
        ```bash
        pip install .
        ```

## Documentations

> yt-obtain-url

### Synopsis/Syntax

### Parameters
- Positionals
- Optionals
    - With Arguments
    - Flags

### Usage

## Resources

## References

## Remarks

