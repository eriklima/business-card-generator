import os
import time
import shutil
import csv
from PIL import Image, ImageDraw, ImageFont

CAMINHO_CSV_CONTATOS = u'../contatos.csv'
PASTA_FUNDOS = u'../imagens/fundos'
PASTA_FOTOS = u'../imagens/fotos'
PASTA_QRCODES = u'../imagens/qrcodes'
PASTA_CARTOES_GERADOS = u'../imagens/cartoes_gerados'

FONTE_PADRAO = u'../fontes/louis_george_cafe/Louis George Cafe.ttf'
FONTE_NEGRITO = u'../fontes/louis_george_cafe/Louis George Cafe Bold.ttf'


def main():
    pasta_cartoes_gerados = os.path.join(os.path.dirname(__file__), PASTA_CARTOES_GERADOS)
    limpar_pasta(pasta_cartoes_gerados)

    contatos = obter_lista_de_contatos()

    criar_cartoes_de_visita(contatos)


def limpar_pasta(nome_pasta):
    shutil.rmtree(nome_pasta)
    os.makedirs(nome_pasta)


def obter_lista_de_contatos():
    caminho_csv_contatos = os.path.join(os.path.dirname(__file__), CAMINHO_CSV_CONTATOS)
    contatos = ler_csv(caminho_csv_contatos)
    del contatos[0] #deletar a primeira linha do csv, com os nomes das colunas
    return contatos


def ler_csv(caminho_arquivo_csv):   
    with open(caminho_arquivo_csv, newline='') as arquivo_csv:
        linhas = csv.reader(arquivo_csv, delimiter=';') 
        linhas = list(linhas) # Coloca as linhas numa lista
        
    return linhas


def criar_cartoes_de_visita(contatos):
    for contato in contatos:
        empresa = contato[0]
        nome_completo = contato[1]
        cargo = contato[3]

        print(f"Gerando cartão para: {nome_completo}")

        try:
            criar_cartao(nome_completo, cargo, empresa)
        except Exception as e:
            # print(f"ERRO ::::: {e}")
            print(e)

        print('------------------------------------------')


def criar_cartao(nome, cargo, empresa):
    imagem_base = criar_imagem_base(empresa)
    
    adicionar_foto(imagem_base, nome)

    escrever_textos(imagem_base, nome, cargo)    
    
    adicionar_qrcode(imagem_base, nome)

    salvar_cartao(imagem_base, empresa, nome)


def criar_imagem_base(empresa):
    imagem_base = os.path.join(os.path.dirname(__file__), PASTA_FUNDOS, f"{empresa.lower()}.jpg")
    imagem_base = Image.open(imagem_base)
    return imagem_base


def adicionar_foto(imagem_base, nome):
    caminho_foto = os.path.join(os.path.dirname(__file__), PASTA_FOTOS, f'{nome}.png')
    posicao = (150, 300)
    tamanho = (500, 500)
    adicionar_imagem(imagem_base, caminho_foto, posicao, tamanho)


def adicionar_imagem(imagem_base, caminho_imagem, posicao, tamanho=None):
    imagem = Image.open(caminho_imagem)

    if tamanho:
        imagem = imagem.resize(tamanho)

    imagem_base.paste(imagem, posicao)


def escrever_textos(imagem_base, nome, cargo):
    cartao_visita = ImageDraw.Draw(imagem_base)

    # Escreve o nome
    caminho_fonte_padrao = os.path.join(os.path.dirname(__file__), FONTE_PADRAO)
    fonte = ImageFont.truetype(caminho_fonte_padrao, 45)
    cartao_visita.text((150, 820), nome, fill=(0, 0, 0), font=fonte) #começando do superior esquerdo /1 é a horizontal e o 2 vertical

    # Escreve o cargo
    caminho_fonte_negrito = os.path.join(os.path.dirname(__file__), FONTE_NEGRITO)
    fonte = ImageFont.truetype(caminho_fonte_negrito, 32)
    cartao_visita.text((150, 870), cargo, fill=(0, 0, 0), font=fonte)


def adicionar_qrcode(imagem_base, nome):
    caminho_foto = os.path.join(os.path.dirname(__file__), PASTA_QRCODES, f'{nome}.png')
    posicao = (150, 950)
    tamanho = (500, 500)
    adicionar_imagem(imagem_base, caminho_foto, posicao, tamanho)    


def salvar_cartao(imagem_base, empresa, nome):
    imagem_base.save(os.path.join(os.path.dirname(__file__), PASTA_CARTOES_GERADOS, f"{empresa}-{nome}.png"))


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"Concluído em: {(time.time() - start_time):.2f} segundos")
