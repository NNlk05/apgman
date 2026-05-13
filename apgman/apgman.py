import subprocess
import os
from importlib import resources
from typing import Optional

def _get_script_path(name: str) -> str:
    return str(resources.files("apgman.scripts").joinpath(name))

def _run_command(command_parts: list[str]) -> str:
    for i, part in enumerate(command_parts):
        if i == 0 and os.path.isfile(part):
            os.chmod(part, 0o755)
    
    result = subprocess.run(
        command_parts, 
        capture_output=True, 
        text=True,
        check=False
    )
    return result.stdout

def init(path: Optional[str] = None) -> str:
    script = _get_script_path("apgman-init")
    return _run_command([script, path or ""])

def build(rule: str = "b3s23", symmetry: str = "C1") -> str:
    script = _get_script_path("apgman-build")
    return _run_command([script, rule, symmetry])

def run(rule: str = "b3s23", symmetry: str = "C1", *args: str) -> str:
    script = _get_script_path("apgman-run")
    return _run_command([script, rule, symmetry, *args])

def add_rule(rule_file: str) -> str:
    script = _get_script_path("apgman-add-rule")
    return _run_command([script, rule_file])