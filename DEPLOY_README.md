# 🎓 Currículo Online - Vinicius Capanema (V07)

> Versão assimétrica e minimalista com design profissional

## 🌐 Links

- **Repositório**: https://github.com/vpcapanema/curriculo_viniciuscapanema
- **Currículo (v07)**: https://vpcapanema.github.io/curriculo_viniciuscapanema/
- **Email**: vpcapanema@outlook.com

## 📋 Status de Configuração

✅ **GitHub Pages Configurado**

- ✅ Arquivo `.nojekyll` - Desativa Jekyll processador
- ✅ `index.html` (raiz) - Redireciona para v07
- ✅ Página principal: `assets/docs/v07/public/index.html`
- ✅ Suporte a light/dark mode
- ✅ Design responsivo (mobile/tablet/desktop)

## 🚀 Como Fazer Deploy

### Pré-requisito
Ter Git instalado: https://git-scm.com/download/win

### Comandos (execute no PowerShell ou Git Bash)

```bash
cd D:\CV_ONLINE_VINICIUS

# Inicializar repositório (primeira vez)
git init

# Configurar identidade
git config user.name "Vinicius Capanema"
git config user.email "vpcapanema@outlook.com"

# Adicionar todos os arquivos
git add --all

# Fazer commit
git commit -m "🎉 Deploy v07 com melhorias de formatação"

# Renomear branch para main (se necessário)
git branch -M main

# Adicionar remote (primeira vez)
git remote add origin https://github.com/vpcapanema/curriculo_viniciuscapanema.git

# Fazer push
git push -u origin main

# Atualizações futuras (apenas estes comandos)
git add --all
git commit -m "Update: [descrição das alterações]"
git push origin main
```

## ⚙️ Configurar GitHub Pages (no GitHub)

1. Vá em: https://github.com/vpcapanema/curriculo_viniciuscapanema/settings/pages
2. Source: `Deploy from a branch`
3. Branch: `main` | Pasta: `/` (root)
4. Clique em Save
5. Aguarde 1-2 minutos
6. Acesse: https://vpcapanema.github.io/curriculo_viniciuscapanema/

## 📁 Estrutura de Arquivos

```
/
├── index.html                          (raiz - redireciona v07)
├── .nojekyll                          (config GitHub Pages)
├── GITHUB_PAGES_SETUP.md              (instruções de setup)
├── README.md                          (este arquivo)
│
├── assets/docs/
│   ├── v07/public/
│   │   ├── index.html                ⭐ (página principal)
│   │   ├── portfolio.html            (portfólio - opcional)
│   │   └── (estilos CSS, assets, etc)
│   ├── v01-v06/                      (versões anteriores)
│   └── Curriculos_PDFs/              (PDFs)
│
├── generate_cv_pdf.py                 (gerador PDF)
├── gerar_curriculo_otimizado.py      (PDF otimizado)
├── deploy.py                         (deploy automation)
└── ... (outros scripts)
```

## 🎨 Versões Disponíveis

- **v07** (Atual) - Assimétrico, minimalista, responsivo ⭐
- v06 - Anterior
- v05, v04, v03, v02, v01 - Históricas

## 🔧 Tecnologias

- **Frontend**: HTML5, CSS3, JavaScript (vanilla)
- **PDF**: ReportLab (Python)
- **Deploy**: GitHub Pages
- **Hosting**: GitHub (gratuito)

## 💡 Dicas

### Atualizar conteúdo
```bash
# Editar arquivos localmente
# Depois fazer commit e push
git add --all
git commit -m "Update: descrição"
git push origin main
```

### Ver histórico
```bash
git log --oneline
```

### Revertir mudança
```bash
git revert <commit-hash>
git push origin main
```

## 🐛 Troubleshooting

### "Git não está instalado"
- Baixe em: https://git-scm.com/download/win
- Instale com opções default

### "Erro de autenticação"
- Use GitHub Personal Access Token
- https://github.com/settings/tokens
- Gere token com escopo `repo`
- Use como password no prompt

### "Página não aparece"
- Aguarde 2-5 minutos após push
- Verifique Settings > Pages
- Limpe cache do navegador (Ctrl+Shift+Delete)
- Verificar HTTPS: https://vpcapanema.github.io/curriculo_viniciuscapanema/

## 📧 Contato

**Vinicius Capanema**
- Email: vpcapanema@outlook.com
- GitHub: https://github.com/vpcapanema
- LinkedIn: [seu-link]

---

**Última atualização**: 4 de novembro de 2025
**Status**: ✅ Online
