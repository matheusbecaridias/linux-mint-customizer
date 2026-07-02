#!/usr/bin/env python3
import os
import sys
import json
from pathlib import Path
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from docling.document_converter import DocumentConverter

def converter_arquivo(caminho_entrada):
    """Converte um documento para markdown salvando no mesmo diretório do original."""
    entrada = Path(caminho_entrada)
    if not entrada.exists():
        print(f"❌ Arquivo não encontrado: {caminho_entrada}")
        return None
    
    # Parâmetro garantido: salva na mesma pasta, com o mesmo nome e extensão .md
    caminho_saida = entrada.with_suffix(".md")
    
    try:
        converter = DocumentConverter()
        result = converter.convert(str(entrada))
        conteudo = result.document.export_to_markdown()
        
        with open(caminho_saida, "w", encoding="utf-8") as f:
            f.write(conteudo)
        
        return str(caminho_saida)
    except Exception as e:
        print(f"❌ Erro ao processar {entrada.name}: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Processa pasta com Docling via JSON.")
    parser.add_argument("--config", "-c", default="config.json", help="Caminho para o arquivo JSON de configuração.")
    args = parser.parse_args()
    
    # Carrega o arquivo JSON
    try:
        with open(args.config, "r", encoding="utf-8") as f:
            config = json.load(f)
    except Exception as e:
        print(f"❌ Erro ao ler o arquivo de configuração JSON: {e}")
        sys.exit(1)
        
    diretorio_raiz = Path(config.get("diretorio_raiz"))
    extensoes = set(ext.lower() for ext in config.get("extensoes", [".pdf", ".epub"]))
    
    if not diretorio_raiz.exists() or not diretorio_raiz.is_dir():
        print(f"❌ Diretório raiz inválido ou inexistente: {diretorio_raiz}")
        sys.exit(1)
        
    # Coleta todos os arquivos recursivamente
    arquivos = []
    for root, _, files in os.walk(diretorio_raiz):
        for file in files:
            caminho = Path(root) / file
            if caminho.suffix.lower() in extensoes and caminho.is_file():
                # Verifica se o arquivo .md correspondente já existe para não reprocessar à toa
                if not caminho.with_suffix(".md").exists():
                    arquivos.append(caminho)
                    
    if not arquivos:
        print("✅ Nenhum arquivo pendente encontrado para conversão no Docling.")
        return

    print(f"📂 Docling: Encontrados {len(arquivos)} arquivos para processar em {diretorio_raiz}.")
    
    # Processamento paralelo (Default: 4 workers)
    total = len(arquivos)
    concluidos = 0
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(converter_arquivo, arq): arq for arq in arquivos}
        for future in as_completed(futures):
            origem = futures[future]
            resultado = future.result()
            concluidos += 1
            if resultado:
                print(f"✅ ({concluidos}/{total}) {origem.name} → Convertido com sucesso.")
            else:
                print(f"❌ ({concluidos}/{total}) Falha ao converter {origem.name}")

if __name__ == "__main__":
    main()