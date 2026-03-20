import subprocess
from pathlib import Path

script_dir = Path(__file__).resolve().parent

def _run_command(command: str):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def init(apgman_path: str = None):
    if apgman_path == None:
        apgman_path = ""
    _run_command(f"{script_dir}/apgman-init {apgman_path}")

def build(rule: str = "", symm: str = ""):
    _run_command(f"{script_dir}/apgman-build {rule} {symm}")

def run(rule: str = "", symm: str = ""):
    _run_command(f"{script_dir}/apgman-run {rule} {symm}")