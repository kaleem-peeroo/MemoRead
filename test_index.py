import os
from pathlib import Path


class TestIndex:
    def test_cache_files_exist(self):
        from index import cache_files_exist

        assert cache_files_exist("./tests/cache/")
        assert not cache_files_exist("./tests/empty_cache/")
        assert not cache_files_exist("./tests/cache_with_empty_files/")

    def test_is_file_empty(self):
        from index import is_file_empty

        assert is_file_empty(
            "/Users/kaleem/Projects/MemoRead/tests/cache_with_empty_files/20260407.json"
        )

        assert not is_file_empty(
            "/Users/kaleem/Projects/MemoRead/tests/cache_with_empty_files/20260408.json"
        )

    def test_fetch_cached_higlights(self):
        from index import fetch_cached_highlights

        highlights = fetch_cached_highlights("./tests/cache/")
        assert highlights is not None, "Highlights are None"
        assert len(highlights) > 0

    def test_get_latest_file(self):
        from index import get_latest_file

        files = [
            os.path.join("./tests/cache/", file)
            for file in os.listdir("./tests/cache/")
        ]

        latest_file = get_latest_file(files)
        assert latest_file is not None
        assert latest_file == Path("./tests/cache/20260405.json")
