import os
from pytube import YouTube
from PIL import Image
import requests
import tempfile


def ArquivoTemporario():
    thumbsDir = tempfile.TemporaryFile()
    return thumbsDir.name


def ThumbnailDownload(videoLink):
    # Função usada após a verificação da disponibilidade do video
    videoInfos = YouTube(videoLink)

    filename = ArquivoTemporario()+f'{videoInfos.title}.png'

    # Image Download
    image = requests.get(videoInfos.thumbnail_url)
    file = open(filename, 'wb')
    file.write(image.content)
    file.close()

    # Change Image Size
    MudaTamanho(filename)
    return filename


def MudaTamanho(filePath):
    imagem = Image.open(filePath)
    imagemMudada = imagem.resize((200, 180))
    ExcluiArquivo(filePath)
    imagemMudada.save(filePath)


def ExcluiArquivo(filePath):
    os.remove(filePath)


def VideoTitulo(link):
    return YouTube(link).title


def Videoduracao(link):
    duracao = YouTube(link).length
    duracaomim = duracao//60
    duracaoseg = (duracao % 60)+1
    duracao = str(duracaomim)+':'+str(duracaoseg) if duracaoseg != 0 else str(duracaomim)
    return duracao


def VideoViews(link):
    views = YouTube(link).views
    contador = 0
    viewsPontuada = ''
    for letra in range(1, len(str(views))+1):
        if contador == 3:
            viewsPontuada += '.'
            contador = 0
        viewsPontuada += str(views)[-letra]
        contador += 1
    return viewsPontuada[::-1]


def Resolucoes(link):
    qualidadeVideo = ['144p', '240p', '360p', '480p', '720p', '1080p', '1440p', '2160p']
    listaAmostragem = []
    Stream = YouTube(link).streams
    for item in qualidadeVideo:
        if len(Stream.filter(res=item, progressive=True)) > 0:
            qualidade = item
            fileSize = (Stream.filter(res=item).first().filesize / 1000000)
            listaAmostragem.append(qualidade + f'  --   {fileSize:.2f}mb'.replace('.', ','))
    return listaAmostragem


def VideoDownload(link, filePath, resolution):
    return YouTube(link).streams.filter(res=resolution).first().download(output_path=filePath)


def AudioDownload(link, filePath, audioQualit):
    return YouTube(link).streams.filter(only_audio=True, abr=audioQualit).first().download(output_path=filePath)


def resolutionGetter(string: str):
    return string[0:string.find('p')+1]


def audioGetter(string: str):
    return string[0:string.find('s')+1]


def AudioQualities(link):
    listaExemplos = ['48kbps', '50kbps', '70kbps', '128kbps', '160kbps']
    listaAmostragem = []
    Stream = YouTube(link).streams
    for item in listaExemplos:
        if len(Stream.filter(only_audio=True, abr=item)) > 0:
            fileSize = (Stream.filter(only_audio=True, abr=item).first().filesize / 1000000)
            listaAmostragem.append(item+f' --  {fileSize:.2f}mb')
    return listaAmostragem





