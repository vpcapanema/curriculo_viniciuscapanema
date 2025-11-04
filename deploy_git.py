#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Deploy para GitHub Pages (usando git via subprocess)
"""

import subprocess
from pathlib import Path

REPO_PATH = Path.cwd()
REPO_URL = "https://github.com/vpcapanema/curriculo_viniciuscapanema.git"
GIT_USER_EMAIL = "vpcapanema@outlook.com"
GIT_USER_NAME = "Vinicius Capanema"


def run_git_command(cmd):
    """Executa comando git"""
    try:
        result = subprocess.run(
            cmd,
            cwd=str(REPO_PATH),
            capture_output=True,
            text=True,
            shell=True
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)


print("🚀 Iniciando Deploy para GitHub Pages...\n")

# Verificar se é um repo git
is_git = (REPO_PATH / ".git").exists()
if is_git:
    print("✅ Repositório git já existe\n")
else:
    print("📝 Inicializando novo repositório git...")
    success, stdout, stderr = run_git_command("git init")
    if success:
        print("✅ Repositório git inicializado\n")
    else:
        print(f"❌ Erro: {stderr}\n")

# Configurar git user
print("👤 Configurando git user...")
run_git_command(f'git config user.email "{GIT_USER_EMAIL}"')
run_git_command(f'git config user.name "{GIT_USER_NAME}"')
print(f"✅ Git user configurado: {GIT_USER_NAME}\n")

# Verificar remote
print("🔗 Configurando remote origin...")
is_remote_set = run_git_command(
    "git remote get-url origin"
)[0]

if is_remote_set:
    run_git_command(f"git remote set-url origin {REPO_URL}")
    print("✅ Remote origin atualizado")
else:
    run_git_command(f"git remote add origin {REPO_URL}")
    print("✅ Remote origin criado")

print()

# Adicionar arquivos
print("📦 Adicionando arquivos...")
success, stdout, stderr = run_git_command("git add --all")
if success:
    print("✅ Arquivos adicionados\n")
else:
    print(f"⚠️  {stderr}\n")

# Status
print("📊 Status git:")
_, stdout, _ = run_git_command("git status")
print(stdout)

# Commit
print("💾 Fazendo commit...")
msg = "🎉 Deploy v07 com melhorias e GitHub Pages"
success, stdout, stderr = run_git_command(f'git commit -m "{msg}"')
if "nothing to commit" in stdout or "nothing to commit" in stderr:
    print("⚠️  Nenhuma mudança para fazer commit")
elif success:
    print(f"✅ Commit realizado: {msg}")
else:
    print(f"⚠️  {stderr}")

print()

# Push
print("📤 Fazendo push para GitHub...")
print("⏳ Aguarde um momento...\n")
success, stdout, stderr = run_git_command("git push -u origin main")

if success:
    print("✅ Push realizado com sucesso!")
    print("\n" + "="*60)
    print("🎉 DEPLOY CONCLUÍDO COM SUCESSO!")
    print("="*60)
    print("\n📍 URLs Disponíveis:")
    print("   Repositório: https://github.com/vpcapanema/" +
          "curriculo_viniciuscapanema")
    print("   Currículo:   https://vpcapanema.github.io/" +
          "curriculo_viniciuscapanema/")
    print("\n💡 Configurações GitHub Pages:")
    print("   1. Acesse Settings > Pages no GitHub")
    print("   2. Selecione Branch: main")
    print("   3. Pasta: / (root)")
    print("   4. Salve e aguarde a publicação\n")
else:
    print(f"❌ Erro ao fazer push:\n{stderr}")
    print("\n💡 Possíveis soluções:")
    print("   1. Verifique sua conexão de internet")
    print("   2. Confirme que tem acesso ao repositório")
    print("   3. Configure credenciais do GitHub (token)")
    print("   4. Use: git push -u origin main\n")
