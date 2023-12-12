# rapid
resto python API

## Build

Install virtual environnment :

    python3 -m venv venv
    source venv/bin/activate
    pip install wheel
    pip install setuptools
    pip install build
    pip install twine

    # Build
    python -m build

    # Install library from local build
    pip install ./dist/rapid-1.0.0-py3-none-any.whl --force-reinstall
