import os
import tempfile

from neurality.storage import store, cache


class TestStore:
    def test(self):
        storage_dir = tempfile.gettempdir()
        function_called = False

        @store(storage_directory=storage_dir)
        def func(x):
            nonlocal function_called
            assert not function_called
            function_called = True
            return x

        assert func(1) == 1
        assert os.path.isfile(os.path.join(storage_dir, 'test_storage.func', 'x=1.pkl'))
        # second call returns same thing and doesn't actually call function again
        assert func(1) == 1


class TestCache:
    def test(self):
        function_called = False

        @cache()
        def func(x):
            nonlocal function_called
            assert not function_called
            function_called = True
            return x

        assert func(1) == 1
        # second call returns same thing and doesn't actually call function again
        assert func(1) == 1
