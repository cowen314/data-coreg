import subprocess
from pathlib import Path


def generate_ui_files(input_base_path: Path):
    for file in input_base_path.iterdir():
        if not file.is_file() or file.name.split(".")[1] != "ui":
            continue
        name = file.name.split(".")[0]
        subprocess.call(["pyside2-uic", "-o", name+".py", name+".ui"], shell=True)


if __name__ == "__main__":
    generate_ui_files(Path("."))
