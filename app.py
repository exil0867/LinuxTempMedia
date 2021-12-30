from os import unlink, isfile, path, listdir, getenv as env
from dotenv import load_dotenv
from shutil import copy2 as copy

load_dotenv()

target = env('NAS_TARGET')
source = env('LOCAL_SOURCE')
allowed_extensions = tuple(['.' + i.lower() for i in env('ALLOWED_EXTENSIONS').split(' ')])

local_media = listdir(source)

def copy_to_target():
    for item in local_media:
        try:
            if item.endswith(allowed_extensions):
                copy(path.join(source, item), target)
        except Exception as e:
            print(f'Failed to copy {item}. Reason: {e}.')

def purge_source():
    for i in local_media:
        item = path.join(source, file)
        try:
            if path.isfile(item) and file.endswith(allowed_extensions):
                os.unlink(item)
        except Exception as e:
            print(f'Failed to delete {item}. Reason: {e}.')
