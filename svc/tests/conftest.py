import shutil

from ..storage import FileStorage

def pytest_funcarg__file_store(request):
    store_dir = "/tmp/storage"
    s = FileStorage(store_dir)
    request.addfinalizer(lambda : shutil.rmtree(store_dir))
    return s

def pytest_funcarg__repository_path(request):
    repository_dir = "D:\\test_svc"
    request.addfinalizer(lambda : shutil.rmtree(repository_dir))
    return repository_dir
    
    
