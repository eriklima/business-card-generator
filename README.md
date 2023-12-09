# Gerador de Cartão Visita

Cria cartões de visita para vários contados.

# Como Configurar

1. Colocar todos os contatos no arquivo _contatos.csv_, seguindo este padrão:
    > **EMPRESA;NOME;EMAIL;CARGO;TELEFONE;SITE**
2. Colocar as fotos de todos os contatos na pasta _"imagens/fotos_":
    - As fotos devem ser do tipo PNG;
    - Os nomes dos arquivos das fotos devem ser o mesmo informado na coluna **NOME** do arquivo _contatos.csv_;
3. Colocar as imagens de fundo dos cartões de cada empresa na pasta _"imagens/fundos_:
    - As imagens de fundo devem ser do tipo JPG;
    - Os nomes dos arquivos das imagens de fundo devem ser o mesmo informado na coluna **EMPRESA** do arquivo _contatos.csv_;
4. Colocar os QRCodes de todos os contados na pasta _"imagens/qrcodes"_:
    - Os QRCodes devem ser to tipo PNG;
    - Os nomes dos arquivos QRCodes devem ser o mesmo informado na coluna **NOME** do arquivo _contatos.csv_;

# Como Executar

Entrar na pasta _"src"_ e executar o comando:

> python main.py

As imagens dos cartões de visita serão gerados na pasta _"imagens/cartoes_gerados"_

# Referências

-   Pillow:
    -   https://pillow.readthedocs.io/en/stable/index.html
    -   https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
-   Exemplos:
    -   https://code-maven.com/create-images-with-python-pil-pillow
    -   https://www.geeksforgeeks.org/adding-text-on-image-using-python-pil/
-   Fontes:
    -   https://www.dafont.com/pt/
    -   https://www.netfontes.com.br/
