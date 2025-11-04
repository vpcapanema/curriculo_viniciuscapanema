#!/bin/bash
# Deploy Shell Script para GitHub - Vinicius Capanema
# Use este script se estiver no Linux/Mac ou Git Bash no Windows

REPO_URL="https://github.com/vpcapanema/curriculo_viniciuscapanema.git"
GIT_EMAIL="vpcapanema@outlook.com"
GIT_NAME="Vinicius Capanema"

echo "==============================================================================="
echo "🚀 GITHUB PAGES DEPLOY - VINICIUS CAPANEMA"
echo "==============================================================================="
echo ""

# Verificar Git
if ! command -v git &> /dev/null; then
    echo "❌ Git não está instalado"
    echo "Baixe em: https://git-scm.com/download"
    exit 1
fi

echo "✅ Git encontrado: $(git --version)"
echo ""

# Inicializar repositório
if [ ! -d ".git" ]; then
    echo "📝 Inicializando repositório..."
    git init
    echo "✅ Repositório inicializado"
    echo ""
fi

# Configurar identidade
echo "👤 Configurando identidade Git..."
git config user.email "$GIT_EMAIL"
git config user.name "$GIT_NAME"
echo "✅ Configurado: $GIT_NAME <$GIT_EMAIL>"
echo ""

# Configurar remote
echo "🔗 Configurando remote..."
if git remote get-url origin &> /dev/null; then
    git remote set-url origin "$REPO_URL"
    echo "✅ Remote atualizado"
else
    git remote add origin "$REPO_URL"
    echo "✅ Remote criado"
fi
echo ""

# Adicionar arquivos
echo "📦 Adicionando arquivos..."
git add --all
echo "✅ Arquivos adicionados"
echo ""

# Status
echo "📊 Status:"
git status
echo ""

# Commit
echo "💾 Fazendo commit..."
git commit -m "🎉 Deploy v07: Currículo com GitHub Pages"
echo ""

# Branch
echo "🌿 Configurando branch main..."
git branch -M main
echo "✅ Branch: main"
echo ""

# Push
echo "==============================================================================="
echo "📤 FAZENDO PUSH PARA GITHUB"
echo "==============================================================================="
echo ""
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "==============================================================================="
    echo "🎉 DEPLOY CONCLUÍDO COM SUCESSO!"
    echo "==============================================================================="
    echo ""
    echo "📍 URLs:"
    echo "   Repositório: https://github.com/vpcapanema/curriculo_viniciuscapanema"
    echo "   Currículo:   https://vpcapanema.github.io/curriculo_viniciuscapanema/"
    echo ""
    echo "⚙️  Configurar GitHub Pages:"
    echo "   1. Acesse: https://github.com/vpcapanema/curriculo_viniciuscapanema/settings/pages"
    echo "   2. Source: Branch 'main' / Pasta '/'"
    echo "   3. Salve"
    echo ""
else
    echo ""
    echo "❌ Erro ao fazer push"
    echo ""
fi
