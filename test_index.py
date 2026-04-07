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
