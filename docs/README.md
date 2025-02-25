# `docs` folder overview

All documentation for the project should be included in this folder in Markdown files, with acceptable formatting for MkDocs. [Guidance on how to write MkDocs documentation is supplied in the contributor guide][writing-mkdocs-documentation].

If you want to include any documentation written in the `{{ cookiecutter.repo_name }}` folder without duplicating it, include it in the `docs/{{ cookiecutter.repo_name }}` folder.

To build the documentation, run the following command:

```shell
mkdocs build
```

The HTML version of this documentation can then be viewed by serving the site locally:

```shell
mkdocs serve
```

This will start a local web server at `http://127.0.0.1:8000/`.

[writing-mkdocs-documentation]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/writing_mkdocs_documentation.md
