from os import path, listdir, getenv as env
from dotenv import load_dotenv
from shutil import move

load_dotenv()

target = env('NAS_TARGET')
source = env('LOCAL_SOURCE')
allowed_extensions = tuple(['.' + i.lower() for i in env('ALLOWED_EXTENSIONS').split(' ')])

local_media = listdir(source)

for file in local_media:
    if file.endswith(allowed_extensions):
        move(path.join(source, file), target)
