# `govcookiecutter` structure

This page provides information on the repository's structure. The repository's folder structure is explained here:

## Top-level files

Each subsection here contains a brief description about the files at the top-level of this Git repository.

### `.flake8`

A configuration file for the `flake8` Python package that provides linting. This file is based on the [common configuration described in the GDS Way][gds-way-flake8].

### `.gitignore`

A `.gitignore` file to ignore certain files and folders from this Git repository. [See the contributor guide to modify the `.gitignore` file][docs-updating-gitignore].

### `.pre-commit-config.yaml`

[A pre-commit hook configuration file][docs-pre-commit-hooks].

### `.secrets.baseline`

[Baseline file for the `detect-secrets` to detect secrets][detect-secrets]. In conjunction with `pre-commit`, `detect-secrets` prevents secrets from being committed to the repository. The baseline file flags secret-like data that the user deliberately wishes to commit to the repository.

### `CODE_OF_CONDUCT.md`

[The Code of Conduct for contributors to this project][code-of-conduct], including maintainers and `best-practice-and-impact` organisation owners.

### `conftest.py`

File to contain shared fixture functions for the `pytest` tests in the `tests` folder.

### `CONTRIBUTING.md`

The contributing guidelines for this project.

### `cookiecutter.json`

A JSON file containing the prompts and default values during template generation. Note any keys beginning with an underscore are not shown to users.

The first block of JSON refers to cookiecutter extensions. The next block relates to organisation-specific information, such as your HM Government department, and its organisation handle on GitHub or GitLab. The last block relates to project-specific information.

[For further information in the `cookiecutter.json` file, see the `cookiecutter` package documentation][cookiecutter].

### `pyproject.toml`

A configuration file for managing the project dependencies and settings using Poetry. This file includes information about the project, dependencies, and build system requirements.

### `mkdocs.yml`

A configuration file for MkDocs, a static site generator that's geared towards project documentation. This file includes settings for the documentation site, such as the site name, theme, and navigation structure.

### `docs/`

A directory containing the documentation files for the project. These files are written in Markdown and are used by MkDocs to generate the static site.

### `tests/`

A directory containing the test files for the project. These tests are written using `pytest` and help ensure the code's functionality and reliability.

### `README.md`

A Markdown file providing an overview of the project, including installation instructions, usage examples, and other relevant information.


[black]: https://black.readthedocs.io/en/stable/
[code-of-conduct]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/docs/CODE_OF_CONDUCT.md
[cookiecutter]: https://cookiecutter.readthedocs.io/
[detect-secrets]: https://github.com/Yelp/detect-secrets
[docs-pre-commit-hooks]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/docs/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/pre_commit_hooks.md
[docs-updating-gitignore]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/docs/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/updating_gitignore.md
[gds-way-flake8]: https://gds-way.cloudapps.digital/manuals/programming-languages/python/python.html#common-configuration
