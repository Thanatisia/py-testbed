TestBench/Practice Ground master project for Python
===================================================

*Description*
-------------
- A full repository of projects and scripts of various concepts, libraries, frameworks and implementation ideas
    - Every project is separated into its own directories and subdirectories with the aim of accomplishing the following goals
        1. Understand how it works
        2. Visualize the operational workflow when using said library
        3. Understand its purpose
        4. Able to modify/manipulate the program after visualizing its general workflow for further understanding

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
    pip install git+https://github.com/Thanatisia/py-testbed#subdirectories=/path/to/[concepts|libraries]/project/root
    ```

- Install from requirements.txt
    - Include the project repository url mapped to the package name in 'requirements.txt'
        ```
        package-name @ git+https://github.com/Thanatisia/py-testbed#subdirectories=/path/to/[concepts|libraries]/project/root
        ```
    - Install python package dependencies
        ```bash
        python3 -m pip install -Ur requirements.txt
        ```

- Install locally in development mode
    - Clone repository
        ```bash
        git clone https://github.com/Thanatisia/py-testbed
        ```
    - Change directory into repository
        ```bash
        cd path/to/[concepts|libraries]/project/root
        ```
    - Install python package dependencies
        ```bash
        python3 -m pip install -Ur requirements.txt
        ```
    - (Optional) Uninstall package
        ```bash
        pip uninstall package-name
        ```
    - Install locally in development mode
        ```bash
        pip install .
        ```

*Documentations*
----------------
> Project Structure/Layout

```
root/
    + README.md
    - concepts/  : Place all concepts-based projects and source files here
        + README.md
        - [concept-title]/ : Create a directory for this concept and store all files related here
            - projects/
                - [project-idea-title]/ : Create a directory for this project idea and source files
                    + README.md
                    + requirements.txt : Contains your project's python dependencies and packages
                    + pyproject.toml : This project's python packaging configuration file
                    - src/
                        - [package-name]/ : Your root package's name
                            + [modules] : Your package modules here
                            - [submodules]/ : Your package submodules and the nested libraries here
                                + ...
    - libraries/ : Place all your python libraries-related projects and source files here
        + README.md
        - [library-name]/ : Create a directory for this library and store all files related to that library here
            - projects/
                - [project-idea-title]/ : Create a directory for this project idea and source files
                    + README.md
                    + requirements.txt : Contains your project's python dependencies and packages
                    + pyproject.toml : This project's python packaging configuration file
                    - src/
                        - [package-name]/ : Your root package's name
                            + [modules] : Your package modules here
                            - [submodules]/ : Your package submodules and the nested libraries here
                                + ...
```

## Resources

## References

## Remarks

