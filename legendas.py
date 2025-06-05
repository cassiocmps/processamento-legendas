import os
import sys

def processar_legendas(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.read().splitlines()

    resultado = []
    fala_atual = None
    texto_atual = []

    def salvar_fala():
        if fala_atual and texto_atual:
            resultado.append(f"{fala_atual}: {' '.join(texto_atual)}")

    i = 0
    while i < len(linhas):
        linha = linhas[i].strip()

        if linha.isdigit():
            i += 1
            continue

        if '-->' in linha:
            i += 1
            continue

        if ':' in linha:
            nome, fala = linha.split(':', 1)
            nome = nome.strip()
            fala = fala.strip()

            if fala_atual == nome:
                texto_atual.append(fala)
            else:
                salvar_fala()
                fala_atual = nome
                texto_atual = [fala]
        else:
            if texto_atual is not None:
                texto_atual.append(linha)

        i += 1

    salvar_fala()

    return '\n\n'.join(resultado)

def processar_arquivo(caminho_arquivo):
    print(f"Processando: {caminho_arquivo}")
    texto_processado = processar_legendas(caminho_arquivo)
    diretorio = os.path.dirname(caminho_arquivo)
    nome_arquivo = os.path.basename(caminho_arquivo)
    arquivo_saida = os.path.join(diretorio, f"RESULTADO_{nome_arquivo}")
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        f.write(texto_processado)
    print(f"✅ Salvo: {arquivo_saida}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python legendas.py <caminho_arquivo_ou_pasta>")
        sys.exit(1)

    caminho = sys.argv[1]

    if not os.path.exists(caminho):
        print(f"Erro: Caminho '{caminho}' não encontrado.")
        sys.exit(1)

    if os.path.isfile(caminho):
        if not caminho.lower().endswith('.vtt'):
            print("Erro: O arquivo deve ter extensão .vtt")
            sys.exit(1)
        processar_arquivo(caminho)

    elif os.path.isdir(caminho):
        arquivos_vtt = [
            os.path.join(caminho, nome)
            for nome in os.listdir(caminho)
            if nome.lower().endswith('.vtt')
        ]

        if not arquivos_vtt:
            print(f"Nenhum arquivo .vtt encontrado em '{caminho}'.")
            sys.exit(0)

        for arquivo in arquivos_vtt:
            processar_arquivo(arquivo)
    else:
        print(f"Erro: '{caminho}' não é um arquivo nem uma pasta válida.")
        sys.exit(1)
