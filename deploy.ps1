#!/usr/bin/env pwsh
# Deploy Script para GitHub Pages - Vinicius Capanema
# Uso: .\deploy.ps1

param(
    [switch]$Push = $false,
    [string]$Message = "🎉 Update: Melhorias no currículo"
)

$ErrorActionPreference = "Stop"

# Cores para output
$colors = @{
    Success = "Green"
    Error = "Red"
    Warning = "Yellow"
    Info = "Cyan"
    Header = "Magenta"
}

function Write-Title {
    param([string]$Text)
    Write-Host "`n" -ForegroundColor $colors.Header
    Write-Host ("="*70) -ForegroundColor $colors.Header
    Write-Host $Text -ForegroundColor $colors.Header
    Write-Host ("="*70) -ForegroundColor $colors.Header
}

function Write-Success {
    param([string]$Text)
    Write-Host "✅ $Text" -ForegroundColor $colors.Success
}

function Write-Error-Custom {
    param([string]$Text)
    Write-Host "❌ $Text" -ForegroundColor $colors.Error
}

function Write-Info {
    param([string]$Text)
    Write-Host "ℹ️  $Text" -ForegroundColor $colors.Info
}

Write-Title "🚀 GitHub Pages Deploy - Vinicius Capanema"

# Verificar Git
try {
    $gitVersion = git --version
    Write-Success "Git encontrado: $gitVersion"
} catch {
    Write-Error-Custom "Git não está instalado"
    Write-Host "`n📥 Baixe em: https://git-scm.com/download/win`n"
    exit 1
}

# Verificar se está no diretório correto
if (-not (Test-Path "./assets/docs/v07/public/index.html")) {
    Write-Error-Custom "Arquivo v07 index.html não encontrado"
    Write-Info "Execute o script dentro de: D:\CV_ONLINE_VINICIUS"
    exit 1
}
Write-Success "Diretório correto verificado"

# Inicializar repo se necessário
if (-not (Test-Path "./.git")) {
    Write-Info "Inicializando repositório git..."
    git init
    Write-Success "Repositório inicializado"
} else {
    Write-Success "Repositório git já existe"
}

Write-Info "Configurando identidade..."
git config user.name "Vinicius Capanema"
git config user.email "vpcapanema@outlook.com"
Write-Success "Identidade configurada"

# Adicionar remote
if (git remote get-url origin 2>$null) {
    Write-Info "Atualizando remote origin..."
    git remote set-url origin `
        "https://github.com/vpcapanema/curriculo_viniciuscapanema.git"
} else {
    Write-Info "Adicionando remote origin..."
    git remote add origin `
        "https://github.com/vpcapanema/curriculo_viniciuscapanema.git"
}
Write-Success "Remote origin configurado"

# Adicionar arquivos
Write-Info "Adicionando arquivos..."
git add --all
Write-Success "Arquivos adicionados"

# Status
Write-Host "`n📊 Status git:"
git status

# Verificar se há mudanças para commit
$status = git status --porcelain
if (-not $status) {
    Write-Host "`n⚠️  Nenhuma mudança para fazer commit" `
        -ForegroundColor $colors.Warning
    if (-not $Push) {
        exit 0
    }
} else {
    # Commit
    Write-Info "Fazendo commit..."
    git commit -m $Message
    Write-Success "Commit realizado: $Message"
}

# Branch
Write-Info "Verificando branch..."
$currentBranch = git rev-parse --abbrev-ref HEAD
if ($currentBranch -ne "main") {
    Write-Info "Renomeando branch para 'main'..."
    git branch -M main
    Write-Success "Branch renomeado para 'main'"
} else {
    Write-Success "Branch: main"
}

# Push (se solicitado)
if ($Push) {
    Write-Info "Fazendo push para GitHub..."
    Write-Host ""
    git push -u origin main
    Write-Success "Push concluído!"
    
    Write-Title "✨ DEPLOY COMPLETO!"
    Write-Host @"

📍 URLs:
   Repositório: https://github.com/vpcapanema/curriculo_viniciuscapanema
   Currículo:   https://vpcapanema.github.io/curriculo_viniciuscapanema/

⏳ Aguarde 1-2 minutos para a publicação estar pronta.

💡 Dica: Configure GitHub Pages em:
   Settings > Pages > Branch main / Pasta /

"@ -ForegroundColor $colors.Success
} else {
    Write-Host @"

📋 Próximas etapas:
   1. Revisar mudanças acima
   2. Execute para fazer push:
      .\deploy.ps1 -Push

   Ou manualmente:
      git push -u origin main

"@ -ForegroundColor $colors.Info
}

Write-Host ""
