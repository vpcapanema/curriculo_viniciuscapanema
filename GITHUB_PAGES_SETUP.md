# Guia de Deploy - GitHub Pages

## ⚙️ Pré-requisitos
1. Git instalado: https://git-scm.com/download/win
2. Repositório criado: https://github.com/vpcapanema/curriculo_viniciuscapanema

## 🚀 Executar Deploy

Execute um destes comandos no terminal (PowerShell/Git Bash):

### Opção 1: Via PowerShell (com Git instalado)
```powershell
cd D:\CV_ONLINE_VINICIUS
git init
git config user.name "Vinicius Capanema"
git config user.email "vpcapanema@outlook.com"
git add --all
git commit -m "🎉 Deploy v07 com melhorias e GitHub Pages"
git branch -M main
git remote add origin https://github.com/vpcapanema/curriculo_viniciuscapanema.git
git push -u origin main
```

### Opção 2: Via Git Bash
```bash
cd /d/CV_ONLINE_VINICIUS
git init
git config user.name "Vinicius Capanema"
git config user.email "vpcapanema@outlook.com"
git add --all
git commit -m "🎉 Deploy v07 com melhorias e GitHub Pages"
git branch -M main
git remote add origin https://github.com/vpcapanema/curriculo_viniciuscapanema.git
git push -u origin main
```

## 📋 Checklist após o Deploy

- [ ] Arquivos foram para o GitHub
- [ ] Vá em: https://github.com/vpcapanema/curriculo_viniciuscapanema/settings/pages
- [ ] Selecione: Branch `main`, pasta `/` (root)
- [ ] Salve a configuração
- [ ] Aguarde 1-2 minutos pela publicação
- [ ] Acesse: https://vpcapanema.github.io/curriculo_viniciuscapanema/

## 📄 Arquivos Estrutura

```
/
├── index.html (redireciona para v07)
├── .nojekyll (desativa Jekyll)
├── assets/docs/v07/public/
│   ├── index.html ⭐ (página principal)
│   ├── portfolio.html
│   └── (css, imagens, etc)
└── ... (outros arquivos de configuração)
```

## 🔐 Se pedir autenticação no push

Use: **GitHub Personal Access Token**

1. Vá em: https://github.com/settings/tokens
2. Gere um novo token (Classic)
3. Escopo: `repo` (full control)
4. Copie o token
5. Na hora de pedir password, cole o token em vez de senha

## 📧 Suporte

Email: vpcapanema@outlook.com
Repositório: https://github.com/vpcapanema/curriculo_viniciuscapanema
