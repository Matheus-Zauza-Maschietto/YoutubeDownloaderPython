import PySimpleGUIQt as sg


def VisualLayoutInicial():
    return [[sg.Text('Youtube Downloader', font=['calibri', 48], justification='center', background_color='red')],
            [sg.Frame('Seleciono qual o tipo de Arquivo',
                            [[sg.Radio('MP4', 'filetype', default=True, font=['calibri', 30], key='mp4'),
                              sg.Radio('MP3', 'filetype', font=['calibri', 30])]], font=['calibri', 30], key='mp3')],
            [sg.T('Link do Video', font=['calibri', 30]), sg.I('', font=['calibri', 20], key='videoLink')],
            [sg.B(' ', size=(1, 330), disabled=True)],
            [sg.B('Sair', size=(140, 80), font=('calibri', 30)), sg.B('Carregar', size=(160, 80), font=('calibri', 30))]]


def VisualLayoutMP4(imagePath, titulo, views, duracao, resolucoes):
    return [[sg.Image(filename=imagePath), sg.Frame('', layout=[[sg.T(text=titulo, font=['calibri', 25])],
                                                                [sg.T(text=views+' Visualiazações', font=['calibri', 25])],
                                                                [sg.T(text='Duração: '+duracao+' Min', font=['calibri', 25])]])],
            [sg.T('Resolução: ', font=['calibri', 30], size=(22, 1)), sg.Combo(resolucoes, font=['calibri', 30], size=(34, 3), key='resolucao')],
            [sg.B(' ', size=(1, 300), disabled=True)],
            [sg.B('Voltar', font=['calibri', 30], size=(160, 80)), sg.B('Baixar', font=['calibri', 30], size=(160, 80))]]


def VisualLayoutMP3(imagePath, titulo, views, duracao, audioQualities):
    return [[sg.Image(filename=imagePath), sg.Frame('', layout=[[sg.T(text=titulo, font=['calibri', 25])],
                                                                [sg.T(text=views + ' Visualiazações',
                                                                      font=['calibri', 25])],
                                                                [sg.T(text='Duração: ' + duracao + ' Min',
                                                                      font=['calibri', 25])]])],
            [sg.T('Qualidade do audio: ', font=['calibri', 30], size=(22, 2)),
             sg.Combo(audioQualities, font=['calibri', 30], size=(34, 3), key='qualidade')],
            [sg.B(' ', size=(1, 300), disabled=True)],
            [sg.B('Voltar', font=['calibri', 30], size=(160, 80)),
             sg.B('Baixar', font=['calibri', 30], size=(160, 80))]]


def VisualWaitScreen():
    return 'a'


def FilePath():
    return sg.PopupGetFolder(message='Selecione a pasta que será usada para o download do video', no_window=True)



