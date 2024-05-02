## Retry

### Pytest-Retry
> Installation

```shell
pip install pytest-retry
```

> usage

```shell
python -m pytest --retries 2 --retry-delay 5
```

> set a flaky test

```python
@pytest.mark.flaky(retries=2, only_on=[ValueError, IndexError])
```

## adding retries in code

> add retry on API call in requests

```python
session.mount(url, HTTPAdapter(max_retries=5))
```

> add timeout in request call

```python
response = self.select_method(method_name.lower(), self.session)(
                url=url,
                data=body,
                allow_redirects=True,
                timeout=3
            )
```
### behave rerun

> add rerun to ini file

```ini
[behave]
format   = rerun
outfiles = rerun_failing.features
```
> Rerun the files

```shell
behave -f rerun -o failed_features.feature
```

## pre-commit

> installation

```shell
pip install pre-commit
```

> pre-commit file configuration example

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
        args: [
          '--unsafe'
        ]
      - id: requirements-txt-fixer
      - id: check-toml
  - repo: https://github.com/asottile/reorder-python-imports
    rev: v3.12.0
    hooks:
      - id: reorder-python-imports
        exclude: ^(pre_commit/resources/|testing/resources/python3_hooks_repo/)
        args: [ --py39-plus, --add-import, 'from __future__ import annotations' ]
  - repo: https://github.com/asottile/add-trailing-comma
    rev: v3.1.0
    hooks:
      - id: add-trailing-comma
  - repo: https://github.com/asottile/pyupgrade
    rev: v3.15.0
    hooks:
      - id: pyupgrade
        args: [ --py312-plus ]
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.7
    hooks:
      # linter
      - id: ruff
        args: [ --fix ]
      # formatter.
      - id: ruff-format
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.7.1
    hooks:
      - id: mypy
        additional_dependencies: [ types-all ]
        exclude: ^todo_api/input_data/

```
> run command:

```shell
pre-commit run --all-files
```

## References


https://pypi.org/project/pytest-retry/

https://pre-commit.com/
