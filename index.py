import requests
import os


def is_file_empty(file: str = ""):
    if file == "":
        raise ValueError("No file passed.")

    if not os.path.exists(file):
        raise ValueError(f"File does not exist: {file}")

    return os.path.getsize(file) == 0


def cache_files_exist(cache_dir_path: str = "./cache/"):
    if not os.path.exists(cache_dir_path):
        raise ValueError(f"{cache_dir_path} does not exist.")

    if len(os.listdir(cache_dir_path)) == 0:
        return False

    files = [os.path.join(cache_dir_path, file) for file in os.listdir(cache_dir_path)]

    return all(not is_file_empty(file) for file in files)


def fetch_highlights():
    os.makedirs("./cache/", exist_ok=True)

    if cache_files_exist():
        return fetch_cached_highlights()
    else:
        return fetch_highlights_via_api()


def main():
    highlights = fetch_highlights()


if __name__ == "__main__":
    main()
