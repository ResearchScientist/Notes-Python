# Virtual Environment

It is good practice to set up an isolated virtual environment to run individual projects. This allows for control and sharing of environments.

## Steps


**Install Python**

- at root directory `pip install python`

**Create Environment**

If only making one environment without a name
- at root directory `python -m venv .venv`

If making multiple environments with each having a unique name
- at root directory `python -m venv .venv-some-name`

**Activate Environment**

- `source .venv/bin/activate` (no name)
- `source .venv-some-name/bin/active` (unique name)

**Install Packages**

- at root directory make a file `requirements.txt`
- inside file on a separate line enter names for each package to install
- at root `pip install -r requirements.txt`

If using multiple environments:
name each file to match the environment name `requirements-some-name.txt`

**Deactivate Environment**

- `deactivate`

# Versioning

- put `.venv` in `gitignore`

# Delete Environment

- deactivate environment `deactivate`
- delete entire virtual environment directory `rm -rf .venv-some-name`
