
Resources: https://flask.palletsprojects.com/en/3.0.x/tutorial/layout/

### Installation

`mkdir <project_name>`

`cd <project_name>`

`python3 -m venv .venv` - using the virtual env to manage dependencies.What problem does a virtual environment solve? The more Python projects you have, the more likely it is that you need to work with different versions of Python libraries, or even Python itself. Newer versions of libraries for one project can break compatibility in another project.

Virtual environments are independent groups of Python libraries, one for each project. Packages installed for one project will not affect other projects or the operating system’s packages.

Python comes bundled with the venv module to create virtual environments.

#### Activating the environment
`. .venv/bin/activate`

`pip install Flask` - Installing the Flask