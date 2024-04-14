Python Libraries
================

*Description*
-------------
- This directory is designed to hold testbench/practice ground project ideas for various concepts and understandings, including Proof-of-Concepts for the purpose of education, learning and understanding
    - essentially to accomplish the following goals
        1. Understand how it works
        2. Visualize the operational workflow when using said library
        3. Understand its purpose
        4. Able to modify/manipulate the program after visualizing its general workflow for further understanding

*Documentations*
----------------
> Project Structure/Layout

```
root/
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
```

