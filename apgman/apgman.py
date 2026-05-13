import subprocess
import os
from importlib import resources
from typing import Optional

def _get_script_path(name: str) -> str:
    return str(resources.files("apgman.scripts").joinpath(name))

def _run_command(command_parts: list[str]) -> str:
    executable_path: str = command_parts[0]
    if os.path.isfile(executable_path):
        os.chmod(executable_path, 0o755)
    
    result: subprocess.CompletedProcess = subprocess.run(
        command_parts, 
        capture_output=True, 
        text=True,
        check=False
    )
    return result.stdout

def init(path: Optional[str] = None) -> str:
    return _run_command([_get_script_path("apgman-init"), path or ""])

def build(rule: str = "b3s23", symmetry: str = "C1") -> str:
    return _run_command([_get_script_path("apgman-build"), rule, symmetry])

def run(rule: str = "b3s23", symmetry: str = "C1", *args: str) -> str:
    return _run_command([_get_script_path("apgman-run"), rule, symmetry, *args])

def add_rule(rule_file: str) -> str:
    return _run_command([_get_script_path("apgman-add-rule"), rule_file])