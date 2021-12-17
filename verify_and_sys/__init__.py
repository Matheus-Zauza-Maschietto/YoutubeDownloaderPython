import os
from pytube import YouTube
import validators
import urllib.request


def VerificaLink(link):
    return validators.url(link)


def VerificaVideo(link):
    try:
        YouTube(link)
    except:
        return False
    else:
        return True


def VerificaConexao():
    try:
        urllib.request.urlopen('https://www.google.com/')
    except:
        return False
    else:
        return True


def VerificaPath(path):
    return os.path.exists(path)
