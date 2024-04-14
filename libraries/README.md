Python Libraries
================

*Description*
-------------
- This directory is designed to hold testbench/practice ground project ideas for every library
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
    - [library-name]/ : Create a directory for this library and store all files related to that library here
        - projects/
            - [project-idea-title]/ : Create a directory for this project idea and source files
                + README.md
                + pyproject.toml : This project's python packaging configuration file
                - src/
                    - [package-name]/ : Your root package's name
                        + [modules] : Your package modules here
                        - [submodules]/ : Your package submodules and the nested libraries here
                            + ...
```

