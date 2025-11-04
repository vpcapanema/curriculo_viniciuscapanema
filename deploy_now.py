#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Deploy Automático para GitHub - Vinicius Capanema
Envia aplicação completa para repositório
"""

import subprocess
import sys
from pathlib import Path

REPO_URL = "https://github.com/vpcapanema/curriculo_viniciuscapanema.git"
GIT_EMAIL = "vpcapanema@outlook.com"
GIT_NAME = "Vinicius Capanema"
REPO_PATH = Path.cwd()


def run_command(cmd, description=""):
    """Executa comando git e exibe resultado"""
    print(f"\n{'='*70}")
    print(f"⏳ {description}")
    print(f"{'='*70}")
    print(f"$ {cmd}\n")

    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=False,
            text=True
        )
        if result.returncode == 0:
            print(f"\n✅ OK: {description}")
            return True
        else:
            print(f"\n❌ ERRO em: {description}")
            return False
    except Exception as e:
        print(f"\n❌ EXCEÇÃO: {e}")
        return False


def main():
    print("\n" + "="*70)
    print("🚀 GITHUB PAGES DEPLOY - VINICIUS CAPANEMA")
    print("="*70)
    print(f"\n📁 Diretório: {REPO_PATH}")
    print(f"🔗 Repositório: {REPO_URL}")
    print(f"📧 Email: {GIT_EMAIL}")

    # 1. Verificar Git
    print("\n[PASSO 1/7] Verificando Git...")
    result = subprocess.run(
        "git --version",
        shell=True,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print("❌ GIT NÃO ESTÁ INSTALADO!")
        print("📥 Baixe em: https://git-scm.com/download/win")
        sys.exit(1)
    print(f"✅ {result.stdout.strip()}")

    # 2. Inicializar repo
    print("\n[PASSO 2/7] Inicializando repositório...")
    if (REPO_PATH / ".git").exists():
        print("✅ Repositório já existe")
    else:
        if not run_command("git init", "Criar novo repositório"):
            sys.exit(1)

    # 3. Configurar Git
    print("\n[PASSO 3/7] Configurando identidade Git...")
    run_command(f'git config user.email "{GIT_EMAIL}"', "Configurar email")
    run_command(f'git config user.name "{GIT_NAME}"', "Configurar nome")

    # 4. Configurar Remote
    print("\n[PASSO 4/7] Configurando remote origin...")
    check_remote = subprocess.run(
        "git remote get-url origin",
        shell=True,
        capture_output=True,
        text=True
    )
    if check_remote.returncode == 0:
        print("✅ Remote já existe, atualizando URL...")
        run_command(
            f"git remote set-url origin {REPO_URL}",
            "Atualizar remote origin"
        )
    else:
        print("Remote não existe, criando...")
        run_command(
            f"git remote add origin {REPO_URL}",
            "Criar remote origin"
        )

    # 5. Adicionar arquivos
    print("\n[PASSO 5/7] Adicionando todos os arquivos...")
    if not run_command("git add --all", "Adicionar arquivos ao índice"):
        sys.exit(1)

    # 6. Verificar Status
    print("\n[PASSO 6/7] Status do repositório:")
    print("="*70)
    subprocess.run("git status", shell=True)

    # 7. Commit
    print("\n[PASSO 7/7] Fazendo commit...")
    msg = "🎉 Deploy v07: Currículo com GitHub Pages, melhorias de formatação"
    if not run_command(f'git commit -m "{msg}"', "Criar commit"):
        print("⚠️  Nenhuma mudança para commitar (não é erro)")

    # Verificar branch
    print("\n[BRANCH] Configurando branch main...")
    run_command("git branch -M main", "Renomear/garantir branch main")

    # PUSH - A PARTE IMPORTANTE
    print("\n" + "="*70)
    print("🚀 FAZENDO PUSH PARA GITHUB...")
    print("="*70)
    print("\n⏳ Conectando ao GitHub...")
    print("💾 Enviando arquivos...\n")

    result = subprocess.run(
        "git push -u origin main",
        shell=True
    )

    print("\n" + "="*70)
    if result.returncode == 0:
        print("🎉 SUCESSO! Deploy concluído!")
        print("="*70)
        print("""
📍 URLs IMPORTANTES:

🔗 Repositório:
   https://github.com/vpcapanema/curriculo_viniciuscapanema

🌐 Currículo Online (v07):
   https://vpcapanema.github.io/curriculo_viniciuscapanema/

⚙️  PRÓXIMA ETAPA (se necessário):

   1. Acesse o repositório no GitHub
   2. Vá em: Settings > Pages
   3. Source: Branch 'main' / Pasta '/'
   4. Clique Save
   5. Aguarde 2-5 minutos
   6. Acesse a URL acima

📧 Email: vpcapanema@outlook.com

""")
    else:
        print("❌ ERRO ao fazer push!")
        print("="*70)
        print("""
💡 POSSÍVEIS SOLUÇÕES:

1. AUTENTICAÇÃO:
   Use GitHub Personal Access Token
   https://github.com/settings/tokens
   - Gere um novo token (Classic)
   - Escopo: 'repo' (full control)
   - Use como password no prompt

2. CONEXÃO:
   Verifique sua conexão de internet

3. REPOSITÓRIO:
   Confirme que o repositório existe:
   https://github.com/vpcapanema/curriculo_viniciuscapanema

4. MANUAL:
   Execute no terminal:
   git push -u origin main

""")
        sys.exit(1)

if __name__ == "__main__":
    main()
