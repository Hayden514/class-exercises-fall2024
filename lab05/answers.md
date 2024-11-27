# Lab 5: Package Management Tutorial

Please complete the hands-on activities associated with this lab outlined in the <a href="https://csci338.github.io/fall2024/assignments/lab05" target="_blank">Lab 5 Instructions</a> (on the course website). When you're done, answer the following questions. Feel free to use Google / ChatGPT to help you think about these questions (but keep in mind that you'll need to know them for the midterm exam).

## Part 1. Operating System Package Managers

Answer the questions for either Homebrew or apt (depending on whether you're using Linux / WSL or Windows)

1. What is Homebrew / apt, and why is it useful?
   APT is a package manager for Debian-based Linux distributions that simplifies the installation and management of software packages.
2. What does the `update` command do (either `brew update` or `apt-get update`)?
   The apt-get update command updates the local package database with the latest information from the software repositories.
3. Where are the packages that are managed by Homebrew / apt stored on your local computer?
   Packages managed by APT are stored in /var/cache/apt/archives before installation, with installed files distributed across directories like /usr/bin and /etc.

## Part 2.

1. What is a python virtual environment?
   A Python virtual environment is an isolated environment that allows you to install packages and dependencies without affecting the global Python installation.
2. What is Poetry, and how is it different from other Python package managers like pip?
   Poetry is a Python dependency and package manager that simplifies project setup and management, offering features like dependency resolution and packaging, whereas pip mainly installs packages without managing project-level configurations.
3. What happened when you issued the `poetry new poetry-demo` command?
   The poetry new poetry-demo command created a new directory structure for a Python project, including configuration files like pyproject.toml.
4. How do you run a python file using the poetry virtual environment?
   I run a Python file in the Poetry virtual environment using poetry run python <filename>.
5. What is the purpose of the `poetry.lock` file?
   The poetry.lock file locks the specific versions of the project’s dependencies to ensure consistency across environments.

## Part 3.

1. What are some of the things that `package.json` is used for?
   package.json is used to define a project's metadata, dependencies, and scripts to automate tasks like building and running the project.
2. Why wouldn't you want to check in the `node_modules` directory into GitHub?
   I wouldn't want to check in the node_modules directory into GitHub because it contains large files that can be installed through npm and would unnecessarily bloat the repository.
