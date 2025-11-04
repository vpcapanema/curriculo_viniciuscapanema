@echo off
REM Deploy para GitHub Pages - Vinicius Capanema
REM Execute este arquivo ou rode os comandos manualmente

cls
echo.
echo ===============================================================================
echo. 🚀 GITHUB PAGES DEPLOY - VINICIUS CAPANEMA
echo ===============================================================================
echo.

REM Verificar Git
where git >nul 2>nul
if errorlevel 1 (
    echo ❌ Git nao esta instalado
    echo.
    echo Baixe em: https://git-scm.com/download/win
    echo.
    pause
    exit /b 1
)

echo ✅ Git encontrado
echo.

REM Inicializar repo
if not exist ".git" (
    echo 📝 Inicializando repositorio git...
    git init
    echo ✅ Repositorio inicializado
    echo.
) else (
    echo ✅ Repositorio git ja existe
    echo.
)

REM Configurar git
echo 👤 Configurando identidade git...
git config user.name "Vinicius Capanema"
git config user.email "vpcapanema@outlook.com"
echo ✅ Identidade configurada
echo.

REM Configurar remote
echo 🔗 Configurando remote origin...
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    git remote add origin https://github.com/vpcapanema/curriculo_viniciuscapanema.git
    echo ✅ Remote origin criado
) else (
    git remote set-url origin https://github.com/vpcapanema/curriculo_viniciuscapanema.git
    echo ✅ Remote origin atualizado
)
echo.

REM Adicionar arquivos
echo 📦 Adicionando arquivos...
git add --all
echo ✅ Arquivos adicionados
echo.

REM Status
echo 📊 Status git:
git status
echo.

REM Commit
echo 💾 Fazendo commit...
git commit -m "🎉 Deploy v07 com melhorias e GitHub Pages"
echo.

REM Branch
echo 🌿 Configurando branch...
git branch -M main
echo ✅ Branch: main
echo.

REM Instruções
echo ===============================================================================
echo. 📋 PROXIMAS ETAPAS
echo ===============================================================================
echo.
echo [1] Fazer PUSH para GitHub:
echo     git push -u origin main
echo.
echo [2] Configurar GitHub Pages:
echo     - Acesse: https://github.com/vpcapanema/curriculo_viniciuscapanema
echo     - Settings ^> Pages
echo     - Source: Branch main / Pasta /
echo     - Salve
echo.
echo [3] Acessar o curriculo:
echo     https://vpcapanema.github.io/curriculo_viniciuscapanema/
echo.
echo ===============================================================================
echo.
pause
