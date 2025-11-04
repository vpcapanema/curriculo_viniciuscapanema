#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Deploy para GitHub Pages
Inicializa git, configura remoto e faz push
"""

from pathlib import Path
from git import Repo

# Configurações
REPO_PATH = Path.cwd()
REPO_URL = "https://github.com/vpcapanema/curriculo_viniciuscapanema.git"
GIT_USER_EMAIL = "vpcapanema@outlook.com"
GIT_USER_NAME = "Vinicius Capanema"

print("🚀 Iniciando Deploy para GitHub Pages...\n")

# Verificar se já é um repositório git
if (REPO_PATH / ".git").exists():
    print("✅ Repositório git já existe")
    repo = Repo(REPO_PATH)
else:
    print("📝 Inicializando novo repositório git...")
    repo = Repo.init(REPO_PATH)
    print("✅ Repositório git inicializado")

# Configurar git user
print(f"👤 Configurando git user: {GIT_USER_NAME} ({GIT_USER_EMAIL})")
git = repo.git
git.config("user.email", GIT_USER_EMAIL)
git.config("user.name", GIT_USER_NAME)
print("✅ Git user configurado")

# Adicionar remote
print(f"🔗 Adicionando remote: {REPO_URL}")
if "origin" in repo.remotes:
    origin = repo.remote("origin")
    origin.set_url(REPO_URL)
    print("✅ Remote origin atualizado")
else:
    repo.create_remote("origin", REPO_URL)
    print("✅ Remote origin criado")

# Adicionar todos os arquivos
print("📦 Adicionando arquivos ao índice...")
repo.git.add("--all")
print("✅ Arquivos adicionados")

# Status
print("\n📊 Status do repositório:")
print(repo.git.status())

# Fazer commit
try:
    commit_msg = (
        "🎉 Deploy v07 com melhorias de formatação e Pages"
    )
    repo.index.commit(commit_msg)
    print(f"\n✅ Commit realizado: {commit_msg}")
except Exception as e:
    print(f"\n⚠️ Nenhuma mudança para fazer commit: {e}")

# Push para GitHub
print("\n📤 Fazendo push para GitHub...")
try:
    origin = repo.remote("origin")
    origin.push(force=False)
    print("✅ Push realizado com sucesso!")
    print("\n🎉 Deploy concluído!")
    print("📍 Seu currículo estará disponível em:")
    print("   https://vpcapanema.github.io/curriculo_viniciuscapanema/")
except Exception as e:
    print(f"❌ Erro ao fazer push: {e}")
    print("\n💡 Dicas:")
    print("   1. Verifique sua conexão de internet")
    print("   2. Confirme que tem acesso ao repositório no GitHub")
    print("   3. Use: git push -u origin main")
