# Building the docs

To build the documentation for current package follow bellow steps from the root dir:

- install the package and docs requirements

    `pip install . -r docs/requirements.txt`

- generate .rst files for modules

    `sphinx-apidoc -f -o docs/modules src/<package-name>`

- generate docs

    `sphinx-build -b html -WEa docs docs/_build`


`sphinx` automatically generates documentation based on dynamically created `.rst` files from docstrings found in the package and static `.rst` files kept in docs directory (such as `index.rst` or `installation.rst`).


