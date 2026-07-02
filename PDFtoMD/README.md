# 📊 Docling vs MarkItDown: Qual escolher?

Este documento apresenta um comparativo técnico e prático entre os dois motores de conversão configurados neste ambiente (`doc.py` e `mark.py`), ajudando a decidir qual é a melhor escolha para o processamento de seus arquivos.

---

## 🧭 Resumo Rápido (TL;DR)
* **Use o Docling (`doc.py`) se:** Seu foco for PDFs complexos, artigos acadêmicos estruturados em duas colunas, relatórios com tabelas densas ou imagens que necessitem de OCR de layout.
* **Use o MarkItDown (`mark.py`) se:** Você tiver uma grande quantidade de arquivos simples (PDFs puramente textuais), arquivos do Microsoft Office (`.docx`, `.pptx`, `.xlsx`) e precisar de uma conversão extremamente rápida que não sobrecarregue o hardware.

---

## 🔄 Comparativo Direto

| Critério | 🐳 Docling (IBM) | ⚡ MarkItDown (Microsoft) |
| :--- | :--- | :--- |
| **Foco Principal** | Ingestão de dados rica e análise de layout baseada em IA | Versatilidade, agilidade e interoperação com formatos Office |
| **Velocidade** | **Moderada a Lenta** (Exige processamento de CPU para modelos) | **Muito Rápida** (Processamento textual leve) |
| **Consumo de Recursos** | **Alto** (Puxa bastante uso dos núcleos da CPU) | **Baixo** (Muito leve, ideal para rodar em segundo plano) |
| **PDFs Acadêmicos (Duas colunas)** | ⭐ **Excelente** (Lê na ordem correta sem misturar os lados) | 😐 **Regular** (Pode juntar linhas de colunas diferentes) |
| **Tabelas Complexas** | ⭐ **Excelente** (Gera tabelas Markdown estruturadas e limpas) | 🛠️ **Bom** (Extrai o conteúdo, mas pode perder alinhamentos complexos) |
| **Formatos do Office (`.docx`, `.xlsx`)** | 🛠️ **Bom** (Foco menor nestes formatos) | ⭐ **Excelente** (Suporte nativo impecável) |

---

## 🛠️ Análise Técnica Orientada ao Hardware (ThinkPad T420)

### 1. Docling (IBM)
O Docling funciona baixando e executando pequenos modelos de visão computacional e detecção de objetos localmente. 
* **Otimização para CPU:** Como o T420 não possui placa de vídeo dedicada (GPU), o Docling ativa automaticamente o modo *CPU Fallback* usando a biblioteca `PyTorch`. 
* **Impacto no Sistema:** O script `doc.py` está travado em `max_workers=4` para balancear a carga. Durante a execução, a temperatura do processador pode subir e o cooler vai acelerar, pois ele simula o processamento de uma IA diretamente nos núcleos físicos do seu Intel Core de 2ª geração.

### 2. MarkItDown (Microsoft)
O MarkItDown adota uma abordagem de engenharia de software tradicional baseada em extração direta de metadados e streams de texto.
* **Otimização para CPU:** É nativamente feito para rodar na CPU, sem o overhead de carregar tensores ou pesos de modelos neurais complexos.
* **Impacto no Sistema:** O script `mark.py` roda de forma suave, consome pouquíssima memória RAM e processa arquivos em sequência com velocidade notável, sendo a melhor escolha para rotinas diárias massivas de arquivos textuais comuns.

---

## 💡 Recomendações de Fluxo de Trabalho

1. **Abordagem Híbrida (Recomendada):** Mantenha seus arquivos organizados em subpastas no seu `diretorio_raiz` (configurado no `config.json`). Separe os livros escaneados ou artigos com tabelas e rode o `doc.py` especificamente para eles. Para o restante dos documentos comuns, use o `mark.py`.
2. **Checagem de Duplicados:** Ambos os scripts foram programados para **pular** arquivos que já possuem um equivalente `.md` gerado na mesma pasta. Isso permite que você mude de conversor no mesmo diretório sem retrabalho ou perda de tempo.

```markdown
# 📄 PDF & Docs to Markdown Converters (JSON Configured)

Este diretório contém ferramentas otimizadas para converter livros, artigos e documentos de texto (como `.pdf` e `.epub`) para o formato Markdown (`.md`). 

Ambos os conversores foram modificados para ler as configurações de uma mesma origem (**`config.json`**) e seguem rigidamente a regra de **salvar o arquivo `.md` com o mesmo nome e na mesma pasta do arquivo original**.

---

## 📂 Estrutura Atual do Diretório

```text
PdftoMD/
├── config.json          # Arquivo único de configuração (Diretório e Extensões)
├── doc.py     # Conversor em lote utilizando a biblioteca Docling (IBM)
├── mark.py    # Conversor em lote utilizando a biblioteca MarkItDown (Microsoft)
├── input/               # Pasta local para testes de entrada (opcional)
├── README.MD            # Este arquivo de instruções
├── requirements.txt     # Dependências do projeto para o pip
└── venv/                # Seu ambiente virtual Python 3.12

```

---

## ⚙️ 1. Configuração Única (`config.json`)

Antes de rodar qualquer um dos scripts, abra o arquivo `config.json` na raiz do projeto e defina a pasta que deseja varrer e as extensões que deseja converter:

```json
{
  "diretorio_raiz": "/home/matheus/Documentos/PDFOrganizer",
  "extensoes": [".pdf", ".epub"]
}

```

> **Nota:** Ambos os scripts realizam uma busca **recursiva**, ou seja, vão varrer a pasta principal e todas as subpastas dentro dela. Arquivos que já possuem um `.md` correspondente na mesma pasta serão ignorados automaticamente para poupar processamento.

---

## 🚀 2. Como Ativar o Ambiente Virtual

Sempre ative o seu ambiente virtual `venv` antes de executar os conversores:

```bash
source venv/bin/activate

```

*(Se precisar instalar ou atualizar as dependências após as modificações, execute: `pip install -r requirements.txt`)*

---

## 🛠️ 3. Executando os Conversores

Você pode escolher qual motor de conversão utilizar dependendo da sua preferência ou do tipo de documento.

### Opção A: Conversão via Docling (IBM)

Ideal para documentos complexos, tabelas e PDFs acadêmicos de estrutura densa. Ele utiliza processamento paralelo nativo (4 workers).

```bash
python3 doc.py

```

### Opção B: Conversão via MarkItDown (Microsoft)

Excelente para conversões rápidas de texto e compatibilidade geral da Microsoft.

```bash
python3 mark.py

```

### Usando um JSON alternativo

Se quiser apontar para outro arquivo de configuração sem alterar o padrão, ambos os scripts aceitam o parâmetro `--config` ou `-c`:

```bash
python3 doc.py --config /caminho/de/outro_arquivo.json

```

---


* **Gerenciamento de CPU:** O `doc.py` está configurado estritamente com `max_workers=4` para casar perfeitamente com os 4 núcleos (threads) do processador do seu T420, evitando travamentos no sistema.
* **Evite concorrência:** Não execute o `doc.py` e o `mark.py` ao mesmo tempo na mesma pasta para não gerar conflitos de escrita nos arquivos.
* **Saída Garantida:** Os arquivos gerados sempre respeitarão o formato `nome_original.md` exatamente no mesmo diretório do arquivo de origem (ex: `123.pdf` gerará `123.md` no mesmo lugar), facilitando a indexação posterior no Google Drive.

```

```
