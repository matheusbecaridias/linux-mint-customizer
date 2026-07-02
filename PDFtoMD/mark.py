#!/usr/bin/env python3
import sys
import json
import argparse
from pathlib import Path
from markitdown import MarkItDown

def converter_arquivo(caminho_arquivo, diretorio_raiz, md_converter):
    """Converte um arquivo para Markdown e salva no mesmo diretório com o mesmo nome."""
    try:
        print(f"Convertendo: {caminho_arquivo.relative_to(diretorio_raiz)}...")
        
        # Realiza a conversão
        resultado = md_converter.convert(str(caminho_arquivo))
        
        # Parâmetro garantido: mesmo diretório, mesmo nome, extensão .md
        caminho_saida = caminho_arquivo.with_suffix(".md")
        
        with open(caminho_saida, "w", encoding="utf-8") as f:
            f.write(resultado.text_content)
            
        print(f"  -> Salvo em: {caminho_saida.name}")
        return True
    except Exception as e:
        print(f"  ❌ ERRO ao converter {caminho_arquivo.name}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Processa pasta com MarkItDown via JSON.")
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
    extensoes = tuple(ext.lower() for ext in config.get("extensoes", [".pdf", ".epub"]))
    
    if not diretorio_raiz.exists() or not diretorio_raiz.is_dir():
        print(f"❌ Diretório raiz inválido ou inexistente: {diretorio_raiz}")
        sys.exit(1)
        
    md = MarkItDown()
    print(f"Varrendo o diretório com MarkItDown: {diretorio_raiz}")
    arquivos_encontrados = 0
    
    for caminho in diretorio_raiz.rglob("*"):
        if caminho.is_file() and caminho.suffix.lower() in extensoes:
            # Pula arquivos se o .md correspondente já existir
            if caminho.with_suffix(".md").exists():
                continue
            
            sucesso = converter_arquivo(caminho, diretorio_raiz, md)
            if sucesso:
                arquivos_encontrados += 1

    print(f"\n🎉 Conclusão! {arquivos_encontrados} novo(s) arquivo(s) processado(s) pelo MarkItDown.")

if __name__ == "__main__":
    main()