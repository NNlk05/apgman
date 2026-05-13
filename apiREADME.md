# APGman Python API README

> FOR THE MAIN README PLEASE SEE [README.md](https://github.com/NNlk05/apgman/blob/main/README.md)

## To use

### Install

```bash
pip install apgman
```

## Import

```python
import apgman
```

## Functions

`add_rule(rule_file: str) -> str`

Adds a `.rule` file to APGman.

`build(rule: str = 'b3s23', symmetry: str = 'C1') -> str`

Builds a new instance of APGman

`init(path: Optional[str] = None) -> str`

Installs APGman on your system.

`run(rule: str = 'b3s23', symmetry: str = 'C1', *args: str) -> str`

Runs a search using apgman

## Example

```python
# Can be also found in /example.py
import apgman

apgman.build("b3s23", "C1")
apgman.run("b3s23", "C1", "-t", "1", "-n", "1000000", "-p", "4")
```
