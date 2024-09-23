# Python template project

![CI](https://github.com/JeremyPike/template-python/actions/workflows/ci.yml/badge.svg)


Template project for python projects.

## Developer Instructions

These instructions will get you started on your local machine for development and testing purposes.

### Prerequisites

To run this project, you're required to have the following software installed on your machine:

* Python 3
* git
* pip
* A python environment manager such as virtualenv, conda or mamba.

### Installation

1. Create and activate a python environment.
2. Clone this repository and `cd` into the project directory.
3. Install the template package including the testing and linting dependencies:
    ```bash
    pip install .[test,lint]
    ```

### Running tests and coverage reporting

Run the tests and gather some coverage data:

```bash
coverage run -m --branch --source=template unittest discover
```
Report on the coverage results:

```bash
coverage report -m
```

## License

This project is licensed under the [MIT License](https://opensource.org/license/MIT) - see the [LICENSE.md](LICENSE.md)
file for details.
