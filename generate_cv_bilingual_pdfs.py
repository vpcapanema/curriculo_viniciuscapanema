#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de PDF Bilíngue do Currículo V07 - Usando Playwright
Converte index.html (PT-BR) e index-en.html (EN) para PDF e salva em disco
"""

import os
import sys
import asyncio
from pathlib import Path
import traceback

# Tentar importar as bibliotecas necessárias
try:
    from playwright.async_api import async_playwright
except ImportError:
    print("❌ Playwright não instalado.")
    print("📦 Instalando: pip install playwright")
    os.system("pip install playwright")
    from playwright.async_api import async_playwright


async def generate_pdf_for_language(html_file, pdf_output, language_name):
    """
    Gera o PDF para um arquivo HTML específico usando Playwright
    """
    # Verificar se arquivo HTML existe
    if not html_file.exists():
        print(f"❌ Arquivo não encontrado: {html_file}")
        return False

    try:
        print("📄 Processando ({0}): {1}".format(language_name, html_file))
        print("💾 Saída: {0}".format(pdf_output))

        async with async_playwright() as p:
            # Usar Chromium para renderizar o PDF
            browser = await p.chromium.launch()
            page = await browser.new_page()

            # Carregar o arquivo HTML com file:// protocol
            await page.goto(
                f"file://{html_file.resolve()}", wait_until="networkidle"
            )

            # Gerar PDF
            await page.pdf(path=str(pdf_output), print_background=True)

            await browser.close()

        # Verificar tamanho do arquivo
        if pdf_output.exists():
            size_mb = pdf_output.stat().st_size / (1024 * 1024)
            print("✅ PDF ({0}) gerado com sucesso!".format(language_name))
            print("📦 Tamanho: {0:.2f} MB".format(size_mb))
            print("📍 Localização: {0}\n".format(pdf_output))
            return True

        print("❌ PDF ({0}) não foi criado\n".format(language_name))
        return False

    except (OSError, RuntimeError) as err:
        print("❌ Erro ao gerar PDF ({0}): {1}\n".format(language_name, err))
        traceback.print_exc()
        return False


async def generate_bilingual_pdfs():
    """
    Gera os PDFs em português e inglês
    """
    # Caminhos
    html_pt = Path(
        r"d:\REPOSITORIOS\CV_ONLINE_VINICIUS\assets\docs\v07"
        r"\public\index.html"
    )
    html_en = Path(
        r"d:\REPOSITORIOS\CV_ONLINE_VINICIUS\assets\docs\v07"
        r"\public\index-en.html"
    )
    
    pdf_pt = Path(
        r"d:\REPOSITORIOS\CV_ONLINE_VINICIUS\assets\docs"
        r"\Curriculo_Vinicius_Capanema_2025.pdf"
    )
    pdf_en = Path(
        r"d:\REPOSITORIOS\CV_ONLINE_VINICIUS\assets\docs"
        r"\Curriculo_Vinicius_Capanema_EN_2025.pdf"
    )

    success_pt = await generate_pdf_for_language(
        html_pt, pdf_pt, "Português-BR"
    )
    success_en = await generate_pdf_for_language(
        html_en, pdf_en, "English"
    )

    return success_pt and success_en


if __name__ == "__main__":
    print("=" * 60)
    print("🎯 Gerador de PDF Bilíngue - Currículo Vinicius Capanema")
    print("=" * 60 + "\n")

    success = asyncio.run(generate_bilingual_pdfs())

    print("=" * 60)
    if success:
        print("✅ Ambos os PDFs foram gerados com sucesso!")
    else:
        print("⚠️  Um ou mais PDFs falharam na geração")
    print("=" * 60)

    sys.exit(0 if success else 1)
