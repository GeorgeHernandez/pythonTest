# pythonTest

Just a repo for George Hernandez to explore Python.

## Virtual Environments

For a project without a virtual environment:

```text
ps> pip list # The global packages
ps> mkdir myProject
ps> cd myProject
ps> python -m venv venv # Or like: [path to a specific python version] -m venv venv
ps> venv\Scripts\activate
(venv) ps> python -m pip instal myPackage
(venv) ps> pip list # The vevnv packages
(venv) ps> deactivate
ps> pip list # Back to the global package
```
