import PySimpleGUIQt as sg
import PySimpleGUImy as sgmy
import pytubeMy as pymy
import verify_and_sys as verify


class grafico:
    def __init__(self):
        sg.theme('Dark')
        janelaEscolha = sg.Window('Downloader', sgmy.VisualLayoutInicial(), size=(900, 700))
        while True:
            key, value = janelaEscolha.read()

            if key == sg.WINDOW_CLOSED or key == 'Sair':
                janelaEscolha.close()
                break

            elif key == 'Carregar':
                videoLink = value['videoLink']
                if not verify.VerificaConexao():
                    sg.PopupOK('Você Não Possui Conexão Com a Internet')
                else:
                    if not verify.VerificaLink(videoLink):
                        sg.PopupOK('O Link Digitado é invalido !', font=['calibri', 20])
                    else:
                        if not verify.VerificaVideo(videoLink):
                            sg.PopupOK('O Video Está Indisponivel Para Download !', font=['calibri', 20])
                        else:
                            janelaEscolha.hide()
                            if value['mp4']:
                                janelaMP4 = sg.Window('MP4 Downloader',
                                                      sgmy.VisualLayoutMP4(pymy.ThumbnailDownload(videoLink),
                                                                           pymy.VideoTitulo(videoLink),
                                                                           pymy.VideoViews(videoLink),
                                                                           pymy.Videoduracao(videoLink),
                                                                           pymy.Resolucoes(videoLink)))
                                while True:
                                    key, value = janelaMP4.read()
                                    if key == sg.WINDOW_CLOSED or key == 'Voltar':
                                        janelaMP4.close()
                                        janelaEscolha.un_hide()
                                        break
                                    elif key == 'Baixar':
                                        while True:
                                            filePath = sgmy.FilePath()
                                            if filePath is not None:
                                                if verify.VerificaPath(filePath):
                                                    try:
                                                        janelaMP4.hide()
                                                        sg.popup_timed('Seu download está sendo executado, aguarde.',
                                                                       keep_on_top=True, auto_close_duration=5,
                                                                       font=['calibri', 20])
                                                        pymy.VideoDownload(videoLink, filePath, pymy.resolutionGetter(value['resolucao']))
                                                        # Usar multitranding para mostrar barra de download
                                                    except Exception as erro:
                                                        sg.PopupOK('Ocorreu um Erro no Download', font=['calibri', 20])
                                                        janelaMP4.close()
                                                        janelaEscolha.un_hide()
                                                        break
                                                    else:
                                                        sg.PopupOK('Download feito com sucesso', font=['calibri', 20], keep_on_top=True)
                                                        janelaMP4.close()
                                                        janelaEscolha.un_hide()
                                                        break
                                                else:
                                                    tentarNovamente = sg.PopupYesNo('Pasta Invalida, Deseja Tentar novamente ?')
                                                    if tentarNovamente == 'No':
                                                        break
                                            else:
                                                break
                            elif not value['mp4']:
                                janelaMP3 = sg.Window('MP3 Downloader',
                                                      sgmy.VisualLayoutMP3(pymy.ThumbnailDownload(videoLink),
                                                                           pymy.VideoTitulo(videoLink),
                                                                           pymy.VideoViews(videoLink),
                                                                           pymy.Videoduracao(videoLink),
                                                                           pymy.AudioQualities(videoLink)))
                                while True:
                                    key, value = janelaMP3.read()
                                    if key == sg.WINDOW_CLOSED or key == 'Voltar':
                                        janelaMP3.close()
                                        janelaEscolha.un_hide()
                                        break
                                    if key == 'Baixar':
                                        filePath = sgmy.FilePath()
                                        if filePath is not None:
                                            if verify.VerificaPath(filePath):
                                                try:
                                                    janelaMP3.hide()
                                                    sg.popup_timed('Seu download está sendo executado, aguarde.',
                                                                   keep_on_top=True, auto_close_duration=5,
                                                                   font=['calibri', 20])
                                                    pymy.AudioDownload(videoLink, filePath, pymy.audioGetter(value['qualidade']))
                                                except Exception as erro:
                                                    sg.PopupOK('Ocorreu um erro no download', font=['calibri', 20])
                                                    janelaMP3.close()
                                                    janelaEscolha.un_hide()
                                                    break
                                                else:
                                                    sg.PopupOK('Download feito com sucesso', font=['Calibri', 20], keep_on_top=True)
                                                    janelaMP3.close()
                                                    janelaEscolha.un_hide()
                                                    break


iniciar = grafico()
