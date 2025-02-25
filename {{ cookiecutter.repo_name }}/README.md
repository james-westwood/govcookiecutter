# {{ cookiecutter.repo_name }}

## Overview
{{ cookiecutter.overview }}

## Requirements
- Python 3.10, 3.11, or 3.12
- Poetry

## Installation

### Using Poetry

1. **Install Poetry**:
   Follow the instructions on the Poetry website to install Poetry.

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/{{ cookiecutter.repo_name }}.git
   cd {{ cookiecutter.repo_name }}
   ```

3. **Install Dependencies**:
   ```bash
   poetry install
   ```

4. **Activate the Virtual Environment**:
   ```bash
   poetry shell
   ```

## Documentation

### Building the Documentation

This project uses MkDocs to build the documentation. To build the documentation locally, follow these steps:

1. **Install MkDocs and MkDocs-Material**:
   These should already be included in your `pyproject.toml` file. If not, you can add them:
   ```bash
   poetry add mkdocs mkdocs-material --dev
   ```

2. **Serve the Documentation Locally**:
   ```bash
   poetry run mkdocs serve
   ```

   This will start a local server, and you can view the documentation in your web browser at `http://127.0.0.1:8000`.

## Running Tests

To run the tests, use the following command:
```bash
poetry run pytest
```

## Contributing

We welcome contributions! Please see the CONTRIBUTING.md file for more information.

## License

This project is licensed under the terms of the LICENSE file.

## Acknowledgements

[This project structure is based on the `govcookiecutter` template
project][govcookiecutter].

[contributing]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/CONTRIBUTING.md
[govcookiecutter]: https://github.com/best-practice-and-impact/govcookiecutter
[docs-loading-environment-variables]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/user_guide/loading_environment_variables.md
[docs-loading-environment-variables-secrets]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/user_guide/loading_environment_variables.md#storing-secrets-and-credentials
