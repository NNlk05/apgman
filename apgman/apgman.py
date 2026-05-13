import subprocess
import os
from pathlib import Path
from typing import Optional

def _get_script_path(name: str) -> str:
    current_dir: Path = Path(__file__).resolve().parent
    script_path: Path = current_dir / "scripts" / name
    if not script_path.exists():
        script_path = current_dir.parent / name
    return str(script_path)

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