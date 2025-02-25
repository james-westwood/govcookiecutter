# `hooks` API reference

This page gives an overview of all public `hooks` objects, functions, and methods. All classes and functions exposed in the `hooks.*` namespace are public.

## Cookiecutter pre-generation hooks

These are functions run after user input, but before project generation. If any pre-generation hooks fail, the project will not be generated.

### Prompt input validation

- check_valid_email_address_format

## Cookiecutter post-generation hooks

These are functions run after initial project generation by the `cookiecutter` package. These include moving the selected organisational frameworks to the correct location, as well as deleting unnecessary files and folders. If any post-generation hooks fail, the generated project will be rolled back and deleted.

### Public sector organisational framework functions

- set_aqa_framework
- set_request_template

### Post-generation clean up

- delete_files_and_folders
- parse_features_json