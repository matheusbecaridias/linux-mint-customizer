Com base na reestruturação dos seus scripts para leitura via arquivo JSON e na nova organização das ferramentas, preparei um **README.md** totalmente atualizado e personalizado para o seu ambiente e diretório atual.

Abaixo está o conteúdo pronto para você salvar no seu arquivo `README.MD`:

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
