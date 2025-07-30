# Processamento de Legendas (.vtt)

Este repositório contém um script Python para processar arquivos de legendas no formato `.vtt` (WebVTT). O objetivo é extrair e organizar as falas presentes nos arquivos de legenda, gerando um novo arquivo de texto com o conteúdo processado.

## Propósito
O script lê arquivos `.vtt` e transforma as legendas em um formato mais limpo, agrupando as falas por personagem ou locutor. O resultado é salvo em um novo arquivo chamado `RESULTADO_<nome_arquivo>.vtt` na mesma pasta do arquivo original.

## Como usar
1. **Pré-requisitos:**
   - Python 3 instalado.

2. **Execução:**
   - Para processar um único arquivo `.vtt`:
     ```bash
     python legendas.py caminho/para/arquivo.vtt
     ```
   - Para processar todos os arquivos `.vtt` em uma pasta:
     ```bash
     python legendas.py caminho/para/pasta
     ```

3. **Saída:**
   - O resultado será salvo em um novo arquivo chamado `RESULTADO_<nome_arquivo>.vtt` na mesma pasta do arquivo original.

## Observações
- O script aceita apenas arquivos com extensão `.vtt`.
- Se for fornecida uma pasta, todos os arquivos `.vtt` nela serão processados.
- Caso não sejam encontrados arquivos `.vtt`, uma mensagem será exibida.

## Exemplo de uso
```bash
python legendas.py exemplo.vtt
```

## Licença
Este projeto está sob licença MIT.
