# Sphinx Installation

Sphinx is a Python application, but it can be in multiple ways. For this guide, we will be focussing on how to instal Sphinx through [PyPI](https://pypi.org).

You can choose to either make a new GitHub Repo and store your Documentation there, or install Sphinx in an already existing Project. We will be covering both.

```{contents} Table Of Contents
:depth: 2
:local:
:backlinks: none
```

## Creating A New Project:

If you wish to create a new GitHub Repo for your Project Documentation, first navigate to GitHub.

### Creating a Repo

Log into GitHub, and create a new Repository. When creating, be sure you check the following options:

- Initiate Project with a README
- Choose a Project LICENSE
- Choose to include a python `.gitignore` template.

Next, copy the repositories HTTPS or SSH Key. We will be cloning the Project Repo to our local machine throught the use of `git clone`.

### Terminal Commands

Open a new terminal/command prompt, and type the following:

``` console
git clone (Paste HTTPS or SSH Key here.)
cd (GitHub Repo name)
```

Then, we need to set up a Python Virtual Enviroment to install our packages. Do so with either:

``` console
python -m venv venv
source venv/bin/activate
```

```{admonition} For windows users!
:class: danger
The command to activate a Python Virtual Enviroment is a bit different for windows than on MacOS. You will need to replace `source venv/bin/activate`, with `.\venv\Scripts\activate`
```

## For Existing Projects:

WIP