import asyncio

from collections import namedtuple
from concurrent.futures import ThreadPoolExecutor
from functools import partial

StreamInfo = namedtuple('StreamInfo', ['input', 'output'])


async def set_stream(stream_info, quiet=True):
    # cmd = f'ffmpeg -i {stream_info.input} -f ffm {stream_info.output}'
    cmd = 'ffmpeg -i /data/10\\ Bem\\ Escuro\\ \\(Part.\\ Sonianke\\ e\\ Mano\\ Moreles\\).mp3 -f ffm http://ffserver:8090/f1-48'
    await asyncio.create_subprocess_shell(cmd)
