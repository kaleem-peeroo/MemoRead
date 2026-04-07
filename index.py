import requests
import os
import json

from rich.pretty import pprint
from pathlib import Path


def get_latest_file(files: list[str] | None = None) -> Path:
    if files is None:
        raise ValueError("No files.")

    if len(files) == 0:
        raise ValueError("No files.")

    filepaths = [Path(file) for file in files]

    return max(filepaths, key=lambda file: file.stat().st_mtime)


def fetch_cached_highlights(cache_dir: str = "./cache/") -> dict:
    if not os.path.exists(cache_dir):
        raise ValueError(f"{cache_dir} does NOT exist.")

    cache_files = [os.path.join(cache_dir, file) for file in os.listdir(cache_dir)]

    latest_cache_file = get_latest_file(cache_files)

    return json.loads(latest_cache_file.read_text())


def is_file_empty(file: str = "") -> bool:
    if file == "":
        raise ValueError("No file passed.")

    if not os.path.exists(file):
        raise ValueError(f"File does not exist: {file}")

    return os.path.getsize(file) == 0


def cache_files_exist(cache_dir_path: str = "./cache/") -> bool:
    if not os.path.exists(cache_dir_path):
        raise ValueError(f"{cache_dir_path} does not exist.")

    if len(os.listdir(cache_dir_path)) == 0:
        return False

    files = [os.path.join(cache_dir_path, file) for file in os.listdir(cache_dir_path)]

    return all(not is_file_empty(file) for file in files)


def fetch_highlights(cache_dir: str = "./cache/") -> dict:
    os.makedirs(cache_dir, exist_ok=True)

    if cache_files_exist():
        return fetch_cached_highlights()
    else:
        return fetch_highlights_via_api()


def main():
    highlights = fetch_highlights()


if __name__ == "__main__":
    main()
