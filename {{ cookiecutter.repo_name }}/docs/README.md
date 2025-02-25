# `docs` folder overview

All documentation for the project should be included in this folder in Markdown files, with acceptable formatting for MkDocs. [Guidance on how to write MkDocs documentation is supplied in the contributor guide][writing-mkdocs-documentation].

To build the documentation, first ensure you have Poetry installed and the project's dependencies set up:

```shell
poetry install
```

Then try to build
```shell
poetry run mkdocs build
```

The HTML-version of this documentation can then be viewed at `docs/_build/index.html`,
relative to the top-level of this repository.

## Analytical quality assurance (AQA)

All analytical quality assurance (AQA) documents can be found in the `docs/aqa` folder.
These files document how this project meets organisational [guidance on producing
quality analysis for HM Government projects][aqua-book].

[aqua-book]: https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government
[docs-makefile]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/Makefile
[writing-mkdocs-documentation]: https://github.com/best-practice-and-impact/govcookiecutter/blob/main/%7B%7B%20cookiecutter.repo_name%20%7D%7D/docs/contributor_guide/writing_mkdocs_documentation.md
