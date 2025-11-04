# ⚡ Comandos Rápidos

Este arquivo contém comandos úteis para gerenciar o projeto.

## 🌐 Visualização Local

```powershell
# Opção 1: Abrir diretamente no navegador
Start-Process "D:\CV_ONLINE_VINICIUS\public\index.html"
Start-Process "D:\CV_ONLINE_VINICIUS\public\portfolio.html"

# Opção 2: Servidor HTTP local (Python)
cd D:\CV_ONLINE_VINICIUS\public
python -m http.server 8000
# Acesse: http://localhost:8000

# Opção 3: VS Code Live Server
# Clique com botão direito em index.html → "Open with Live Server"
```

## 🔄 Git — Comandos Essenciais

### Inicialização (primeira vez)
```powershell
cd D:\CV_ONLINE_VINICIUS
git init
git add .
git commit -m "feat: estrutura inicial v2.0.0"
git remote add origin https://github.com/seu-usuario/nome-repo.git
git branch -M main
git push -u origin main
```

### Fluxo Normal de Trabalho
```powershell
# Ver status
git status

# Adicionar mudanças
git add .
# ou adicionar arquivo específico:
git add public/index.html

# Commit
git commit -m "feat: descrição da mudança"

# Enviar para GitHub
git push

# Ver histórico
git log --oneline

# Desfazer último commit (mantém mudanças)
git reset --soft HEAD~1
```

### Mensagens de Commit Convencionais
```
feat: adiciona nova seção
fix: corrige link quebrado
docs: atualiza README
style: ajusta cores do tema
refactor: reorganiza estrutura CSS
```

## 📝 Edição Rápida

```powershell
# Abrir projeto no VS Code
cd D:\CV_ONLINE_VINICIUS
code .

# Editar currículo
code public\index.html

# Editar portfólio
code public\portfolio.html

# Editar README
code README.md
```

## 🧹 Limpeza

```powershell
# Remover arquivos temporários (se necessário)
Remove-Item -Path "D:\CV_ONLINE_VINICIUS\*.tmp" -ErrorAction SilentlyContinue

# Limpar cache do Git (se repositório ficar muito grande)
git gc --aggressive --prune=now
```

## 📊 Verificações

```powershell
# Contar linhas de código
Get-ChildItem -Path D:\CV_ONLINE_VINICIUS\public -Filter *.html -Recurse | Get-Content | Measure-Object -Line

# Tamanho dos arquivos
Get-ChildItem -Path D:\CV_ONLINE_VINICIUS\public -Recurse | Measure-Object -Property Length -Sum

# Listar todos os links externos (requer PowerShell avançado)
Select-String -Path "D:\CV_ONLINE_VINICIUS\public\*.html" -Pattern 'href="http' -AllMatches
```

## 🚀 Deploy Rápido

### GitHub Pages
```powershell
# Após configurar repositório remoto
git add .
git commit -m "deploy: atualiza conteúdo"
git push

# GitHub Pages atualiza automaticamente em ~1-2 minutos
```

### Netlify (CLI)
```powershell
# Instalar (primeira vez)
npm install -g netlify-cli

# Deploy
cd D:\CV_ONLINE_VINICIUS
netlify deploy --dir=public --prod
```

### Vercel (CLI)
```powershell
# Instalar (primeira vez)
npm install -g vercel

# Deploy
cd D:\CV_ONLINE_VINICIUS\public
vercel --prod
```

## 🔍 Validação

```powershell
# Verificar HTML (requer HTML Tidy - opcional)
tidy -q -errors public\index.html

# Verificar links quebrados (requer link checker - opcional)
# npm install -g broken-link-checker
# blc http://localhost:8000 -ro
```

## 🎨 Personalização Rápida

### Alterar cor do tema
```powershell
# Editar variáveis CSS em public/index.html e public/portfolio.html
# Procure por: :root { --brand: #7aa2ff; }
code public\index.html
```

### Adicionar novo projeto ao portfólio
```powershell
# Editar public/portfolio.html
# Procure por: <div class="grid">
# Adicione novo <div class="project-card">
code public\portfolio.html
```

## 📦 Backup

```powershell
# Criar backup local
$date = Get-Date -Format "yyyy-MM-dd"
Compress-Archive -Path D:\CV_ONLINE_VINICIUS\* -DestinationPath "D:\Backups\CV_ONLINE_$date.zip"

# Listar backups
Get-ChildItem D:\Backups\CV_ONLINE_*.zip
```

## 🔧 Troubleshooting

### Problema: Git não reconhecido
```powershell
# Instalar Git: https://git-scm.com/download/win
# Reiniciar PowerShell após instalação
```

### Problema: Links quebrados entre páginas
```powershell
# Verificar que está usando caminhos relativos:
# ✅ ./portfolio.html
# ❌ /portfolio.html ou portfolio.html (sem ./)
```

### Problema: Tema não persiste
```powershell
# Verificar localStorage no navegador (F12 → Application → Local Storage)
# Limpar cache se necessário: Ctrl+Shift+Delete
```

## 📱 Teste Mobile

```powershell
# Abrir DevTools no Chrome
# F12 → Toggle Device Toolbar (Ctrl+Shift+M)
# Testar em diferentes resoluções:
# - iPhone SE: 375x667
# - iPad: 768x1024
# - Desktop: 1920x1080
```

## 🎯 Atalhos do VS Code

```
Ctrl+P          → Buscar arquivo
Ctrl+Shift+F    → Buscar em todos os arquivos
Ctrl+/          → Comentar/descomentar
Alt+Shift+F     → Formatar documento
F2              → Renomear símbolo
Ctrl+D          → Selecionar próxima ocorrência
```

## 📚 Recursos Úteis

```powershell
# Abrir documentação no navegador
Start-Process "https://pages.github.com"           # GitHub Pages
Start-Process "https://docs.netlify.com"           # Netlify
Start-Process "https://vercel.com/docs"            # Vercel
Start-Process "https://developer.mozilla.org"      # MDN (referência HTML/CSS/JS)
```

---

**Dica:** Salve este arquivo como favorito para acesso rápido aos comandos!
