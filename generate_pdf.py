#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de PDF do Currículo V07
Converte index.html para PDF e salva em disco
"""

import os
import sys
from pathlib import Path

# Tentar importar as bibliotecas necessárias
try:
    from weasyprint import HTML
except ImportError:
    print("❌ WeasyPrint não instalado.")
    print("📦 Instalando: pip install weasyprint")
    os.system("pip install weasyprint")
    from weasyprint import HTML

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("❌ BeautifulSoup não instalado.")
    print("📦 Instalando: pip install beautifulsoup4")
    os.system("pip install beautifulsoup4")
    from bs4 import BeautifulSoup


def clean_html_for_pdf(html_path):
    """
    Limpa o HTML para melhor renderização em PDF
    Remove scripts, estilos desnecessários, etc
    """
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Remover scripts
    for script in soup.find_all('script'):
        script.decompose()

    # Remover elementos desnecessários para PDF
    for elem in soup.find_all(['nav', 'footer']):
        elem.decompose()

    # Remover botões de ação (tema, voltar ao topo)
    for btn in soup.find_all('button', {'id': 'themeToggle'}):
        btn.decompose()

    for link in soup.find_all('a', {'onclick': True}):
        if 'scrollTo' in link.get('onclick', ''):
            link.decompose()

    return str(soup)


def generate_pdf():
    """
    Gera o PDF do currículo
    """
    # Caminhos
    html_file = Path(
        r"D:\CV_ONLINE_VINICIUS\assets\docs\v07\public\index.html"
    )
    pdf_output = Path(
        r"D:\CV_ONLINE_VINICIUS\assets\docs"
        r"\Curriculo_Vinicius_Capanema_2025.pdf"
    )

    # Verificar se arquivo HTML existe
    if not html_file.exists():
        print(f"❌ Arquivo não encontrado: {html_file}")
        return False

    try:
        print(f"📄 Processando: {html_file}")
        print(f"💾 Saída: {pdf_output}")

        # Converter HTML para PDF usando WeasyPrint
        HTML(str(html_file)).write_pdf(
            str(pdf_output),
            optimized_size=['images', 'fonts']
        )

        # Verificar tamanho do arquivo
        size_mb = pdf_output.stat().st_size / (1024 * 1024)

        print("✅ PDF gerado com sucesso!")
        print(f"📦 Tamanho: {size_mb:.2f} MB")
        print(f"📍 Localização: {pdf_output}")

        return True

    except Exception as e:
        print(f"❌ Erro ao gerar PDF: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("🎯 Gerador de PDF - Currículo Vinicius Capanema")
    print("=" * 60)

    success = generate_pdf()

    print("=" * 60)
    sys.exit(0 if success else 1)
