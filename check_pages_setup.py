#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub Pages Deploy Status e Configuração
"""

from pathlib import Path

print("\n" + "="*70)
print("🎓 CONFIGURAÇÃO GITHUB PAGES - VINICIUS CAPANEMA")
print("="*70)

# Verificar arquivos configurados
paths = [
    (".nojekyll", "✅ Arquivo .nojekyll configurado"),
    ("index.html", "✅ Redirecionador da raiz"),
    ("assets/docs/v07/public/index.html", "✅ Página principal v07"),
    ("GITHUB_PAGES_SETUP.md", "✅ Guia de setup"),
]

print("\n📁 Verificando arquivos configurados:\n")
for path, desc in paths:
    full_path = Path.cwd() / path
    if full_path.exists():
        print(f"   {desc}")
    else:
        print(f"   ❌ {path} NÃO ENCONTRADO")

print("\n" + "-"*70)
print("🚀 PRÓXIMAS ETAPAS:\n")

steps = [
    ("1", "Instalar Git", "https://git-scm.com/download/win"),
    ("2", "Executar comandos de push", "Ver GITHUB_PAGES_SETUP.md"),
    ("3", "Configurar Pages no GitHub", "Settings > Pages > Branch main"),
    ("4", "Validar URL", "https://vpcapanema.github.io/" +
           "curriculo_viniciuscapanema/"),
]

for num, task, detail in steps:
    print(f"   [{num}] {task}")
    print(f"       📌 {detail}\n")

print("-"*70)
print("\n📧 INFORMAÇÕES DE DEPLOY:\n")
info = [
    ("Repositório", "https://github.com/vpcapanema/" +
                    "curriculo_viniciuscapanema.git"),
    ("Email Git", "vpcapanema@outlook.com"),
    ("Nome Git", "Vinicius Capanema"),
    ("Branch", "main"),
    ("Pasta Raiz", "/"),
    ("URL Final", "https://vpcapanema.github.io/" +
                  "curriculo_viniciuscapanema/"),
]

for key, value in info:
    print(f"   {key:.<20} {value}")

print("\n" + "="*70)
print("✨ TUDO PRONTO! Agora execute os comandos Git no terminal.")
print("="*70 + "\n")
