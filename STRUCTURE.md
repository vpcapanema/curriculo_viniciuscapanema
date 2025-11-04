# Estrutura de Diretórios — CV Online Vinicius Capanema

```
📁 CV_ONLINE_VINICIUS/
│
├── 📁 public/                          ← Arquivos prontos para deploy
│   ├── 📄 index.html                   ← Currículo principal (página inicial)
│   └── 📄 portfolio.html               ← Portfólio de projetos
│
├── 📁 assets/                          ← Recursos e arquivos de apoio
│   └── 📁 docs/
│       └── 📄 Curriculo_Vinicius_Capanema_2025.pdf  ← PDF original
│
├── 📁 src/                             ← Código-fonte (futuras extensões)
│   └── (vazio - reservado)
│
├── 📄 .gitignore                       ← Arquivos ignorados pelo Git
├── 📄 CHANGELOG.md                     ← Histórico de versões
├── 📄 LICENSE                          ← Licença MIT
└── 📄 README.md                        ← Documentação principal

```

## 🎯 Propósito de Cada Arquivo

### Arquivos Principais (public/)

| Arquivo | Propósito | Acesso |
|---------|-----------|--------|
| `index.html` | Currículo completo com todas as seções expandidas | `/` ou `/index.html` |
| `portfolio.html` | Portfólio de projetos e demos | `/portfolio.html` |

### Documentação

| Arquivo | Propósito |
|---------|-----------|
| `README.md` | Documentação completa do projeto, instruções de uso e deploy |
| `CHANGELOG.md` | Histórico detalhado de versões e mudanças |
| `LICENSE` | Licença MIT do projeto |
| `.gitignore` | Configuração de arquivos a serem ignorados pelo Git |

### Assets

| Diretório | Conteúdo |
|-----------|----------|
| `assets/docs/` | Documentos (PDF do currículo original) |
| `assets/` (raiz) | Futuramente: imagens, fontes, ícones |

### Source (src/)

Reservado para desenvolvimento futuro:
- Componentes modulares
- Preprocessadores CSS (SASS/LESS)
- Scripts TypeScript/JavaScript modulares
- Ferramentas de build (se necessário)

## 🚀 URLs de Acesso (após deploy)

```
https://seu-usuario.github.io/nome-repo/           → index.html (currículo)
https://seu-usuario.github.io/nome-repo/portfolio  → portfolio.html
```

## 📊 Fluxo de Navegação

```
┌─────────────┐
│ index.html  │  (Currículo)
│             │
│ ┌─────────┐ │
│ │ Botão:  │ │
│ │Portfolio│─┼─────┐
│ └─────────┘ │     │
└─────────────┘     │
                    ▼
            ┌─────────────────┐
            │ portfolio.html  │
            │                 │
            │  ┌───────────┐  │
            │  │  Botão:   │  │
            │  │ Currículo │──┼────┐
            │  └───────────┘  │    │
            └─────────────────┘    │
                    ▲              │
                    └──────────────┘
```

## 💡 Convenções Adotadas

1. **Nomenclatura de Arquivos**
   - Snake_case para PDFs e documentos: `Curriculo_Vinicius_Capanema_2025.pdf`
   - Kebab-case ou camelCase para código futuro
   - index.html como página principal (convenção web)

2. **Organização**
   - Separação clara entre público (`public/`) e recursos (`assets/`)
   - Diretório `src/` preparado para evolução do projeto
   - Documentação na raiz para fácil acesso

3. **Versionamento**
   - Semantic Versioning (MAJOR.MINOR.PATCH)
   - Changelog mantido atualizado
   - Commits descritivos seguindo convenção

## 🔐 Segurança e Privacidade

- ✅ Nenhum dado sensível nos arquivos HTML (sem telefone, e-mail, CREA)
- ✅ Links externos com `rel="noopener noreferrer"`
- ✅ `.gitignore` configurado para evitar commits acidentais de arquivos sensíveis
- ✅ PDF original preservado em `assets/docs/` (não linkado publicamente)

---

**Versão da Estrutura:** 2.0.0  
**Data:** 3 de novembro de 2025
