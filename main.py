import sys
import requests
import subprocess
from threading import Thread
import os
import pathlib
from functools import partial
import logging
os.chdir('C:\\python_projects\\protocol\\dist')
logging.basicConfig(filename="logger.log",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
logger = logging.getLogger('urbanGUI')

const = '''
#EXTINF:-1 , {f} {seria}
{url}
'''


def setData(f, elem):
    return const.format(**{
        "f": f[0],
        "seria": elem["name"],
        "url": elem["std"]
    })


def SSort(setData, response, id):
    return list(map(partial(setData, (get_info(id), setData)), sorted(list(response), key=lambda d: int(d['name'].split()[0]))))


def get_info(id):
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Origin': 'https://reansn0w.github.io',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://reansn0w.github.io/',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
    }

    data = {
        'id': f'{id}'
    }

    response = requests.post('https://api.animevost.org/v1/info',
                             headers=headers, data=data).json()["data"][0]["title"].split("/ ")[0]
    return response


def getepisodes(epId):
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Origin': 'https://reansn0w.github.io',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://reansn0w.github.io/',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
    }

    data = {
        'id': f'{epId}'
    }

    response = requests.post(
        'https://api.animevost.org/v1/playlist', headers=headers, data=data).json()

    with open(f"{pathlib.Path(__file__).parent.resolve()}/{epId}.m3u8", "wb") as f:
        f.write(bytes("".join(SSort(setData, response, epId)), encoding="utf-8"))
    Thread(target=subprocess.run, args=(
        ['mpv', f'{pathlib.Path(__file__).parent.resolve()}\\{epId}.m3u8'],)).start()


getepisodes(sys.argv[-1].split("id=")[-1].rstrip('/'))
