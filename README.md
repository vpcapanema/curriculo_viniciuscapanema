# Currículo Online — Vinicius Capanema (Modelo A • v2)

## 📋 Visão Geral

Currículo online em HTML estático com tema claro/escuro, conteúdo expandido baseado no PDF original, seção institucional da empresa VPC-GEOSER e integração com página de portfólio.

## 📁 Estrutura do Projeto

```
CV_ONLINE_VINICIUS/
├── public/                    # Arquivos públicos prontos para deploy
│   ├── index.html            # Currículo principal (cv_modelo_a_v2.html)
│   └── portfolio.html        # Página de portfólio
├── assets/                    # Recursos e arquivos de apoio
│   └── docs/                 # Documentos
│       └── Curriculo_Vinicius_Capanema_2025.pdf
├── src/                      # Código-fonte (reservado para futuras extensões)
├── .gitignore                # Arquivos ignorados pelo Git
├── CHANGELOG.md              # Histórico de versões
├── LICENSE                   # Licença MIT
└── README.md                 # Este arquivo
```

### 📂 Descrição dos Diretórios

- **`public/`** — Contém os arquivos HTML prontos para serem servidos. Este é o diretório que deve ser configurado como source no GitHub Pages ou em qualquer serviço de hospedagem estática.

- **`assets/`** — Armazena recursos estáticos como documentos, imagens (futuro), fontes (futuro), etc. Organizado em subdiretórios por tipo.

- **`src/`** — Reservado para código-fonte modular caso o projeto evolua para incluir build steps, preprocessadores CSS, ou módulos JavaScript separados.

### 🎯 Organização dos Arquivos

- **`index.html`** — Renomeado de `cv_modelo_a_v2.html` para facilitar o acesso como página principal (convenção web padrão)
- **`portfolio.html`** — Página complementar acessível via navegação interna
- **PDF original** — Mantido em `assets/docs/` com nome sanitizado (sem espaços ou caracteres especiais)

## 📄 Arquivos Principais

- **`public/index.html`** — Currículo principal (autocontido, renomeado para facilitar deploy)
- **`public/portfolio.html`** — Página de portfólio com projetos em destaque
- **`assets/docs/Curriculo_Vinicius_Capanema_2025.pdf`** — Documento fonte original

## ✨ Recursos Implementados

### 1. Tema Duplo (Light/Dark)
- ✅ Botão de alternância (🌓) com persistência via `localStorage`
- ✅ Variáveis CSS em `:root` e `:root.light`
- ✅ Metas `color-scheme` e `theme-color` configuradas

### 2. Estrutura de Conteúdo
- ✅ **Síntese:** 2 parágrafos expandidos sobre experiência e atuação
- ✅ **Competências-chave:** 6 bullets detalhados (ação → resultado)
- ✅ **Formação Acadêmica:** Doutorado, MBA, Mestrado, Especialização, Graduação
- ✅ **Experiência Profissional:** 6 cargos com 3-6 bullets cada (DER/SP, VEGA, GeoBrasilis, FUNCATE, Mognos)
- ✅ **Tecnologias & Ferramentas:** 8 categorias expandidas
- ✅ **Idiomas:** Inglês (avançado), Espanhol (inicial)

### 3. Seção da Empresa (VPC-GEOSER)
- ✅ Descrição de proposta de valor (geoprocessamento/SR/data science)
- ✅ Blockquote com mensagem de impacto
- ✅ CTA principal para `./portfolio.html`
- ✅ CTA secundário para LinkedIn

### 4. Privacidade
- ✅ Não exibe telefone, e-mail ou CREA
- ✅ Informações públicas: cidade, LinkedIn, Lattes

### 5. Acessibilidade
- ✅ Semântica correta (`header`, `main`, `section`, `footer`)
- ✅ Hierarquia de headings (h1 → h2 → h3)
- ✅ `aria-label` no botão de tema
- ✅ Links com `rel="noopener noreferrer"`
- ✅ Tipografia ≥16px

### 6. Performance
- ✅ Arquivo único autocontido
- ✅ CSS/JS inline minimalistas
- ✅ Sem dependências externas
- ✅ Sem bloqueios de render

### 7. Responsividade
- ✅ Grid 2 colunas ≥900px, 1 coluna em telas menores
- ✅ Testado em 360-1440px
- ✅ `clamp()` para tipografia fluida

### 8. SEO
- ✅ `<title>` descritivo
- ✅ Meta `description` com palavras-chave
- ✅ Estrutura semântica para indexação

## 🚀 Como Usar

### Deploy em GitHub Pages

1. Crie um repositório no GitHub
2. Faça upload de todo o diretório do projeto
3. Vá em **Settings → Pages**
4. Selecione a branch `main` e a pasta `/public` como source
5. Acesse em `https://<seu-usuario>.github.io/<nome-repo>/`
   - O arquivo `index.html` será carregado automaticamente

**Ou configure para a raiz:**
- Se preferir servir da raiz, mova os arquivos de `public/` para a raiz do repositório
- Configure Pages para servir da pasta `/` (root)

### Visualização Local

Navegue até a pasta `public/` e abra `index.html` no navegador, ou use um servidor local:

```bash
# Navegue até o diretório public
cd public

# Python
python -m http.server 8000

# Node.js (npx)
npx serve .

# VS Code Live Server
# Clique com botão direito em index.html > Open with Live Server
```

Acesse: `http://localhost:8000`

## 🎨 Personalização

### Alterar Cores do Tema

Edite as variáveis CSS em `:root` (tema escuro) e `:root.light` (tema claro):

```css
:root {
  --bg: #0b0c0f;        /* Fundo escuro */
  --fg: #e7e7ea;        /* Texto escuro */
  --brand: #7aa2ff;     /* Cor de destaque */
  /* ... */
}

:root.light {
  --bg: #f7f8fa;        /* Fundo claro */
  --fg: #0e1116;        /* Texto claro */
  --brand: #2563eb;     /* Cor de destaque */
  /* ... */
}
```

### Adicionar Projetos ao Portfólio

Edite `public/portfolio.html` e adicione novos cards no grid:

```html
<div class="project-card">
  <h3>🎯 Nome do Projeto</h3>
  <p>Descrição do projeto...</p>
  <div class="pills">
    <span class="pill">Tech 1</span>
    <span class="pill">Tech 2</span>
  </div>
</div>
```

### Atualizar Conteúdo do Currículo

Edite `public/index.html` diretamente. Todas as seções estão claramente marcadas com comentários ou classes CSS.

## 📊 Checklist de Aceite

- [x] Alternância de tema funciona e persiste
- [x] Todas as seções presentes com texto expandido
- [x] Seção da empresa com CTA funcional para `portfolio.html`
- [x] Nenhum dado sensível no DOM (sem telefone/e-mail/CREA)
- [x] Acessibilidade básica (hierarquia, foco, contraste)
- [x] Layout responsivo 360–1440px sem quebras
- [x] Meta description e title descritivos
- [x] Arquivo único autocontido

## 🔧 Tecnologias

- **HTML5** semântico
- **CSS3** com variáveis, `clamp()`, `color-mix()`
- **JavaScript** vanilla (~30 linhas, IIFE)
- **Nenhuma** dependência externa

## 📝 Notas

- Os avisos de lint sobre `style` inline são para pequenos ajustes de espaçamento e não afetam a performance
- O aviso sobre `meta[name=theme-color]` em Firefox/Opera é esperado (progressive enhancement)
- Para adicionar formulário de contato, use serviços serverless como Formspree/Netlify Forms

## 🔄 Controle de Versão

### Primeira Configuração do Git

```bash
# Navegue até o diretório do projeto
cd D:\CV_ONLINE_VINICIUS

# Inicialize o repositório Git
git init

# Adicione todos os arquivos
git add .

# Faça o primeiro commit
git commit -m "feat: estrutura inicial do currículo online v2.0.0"

# Conecte ao repositório remoto do GitHub
git remote add origin https://github.com/seu-usuario/seu-repositorio.git

# Envie para o GitHub
git branch -M main
git push -u origin main
```

### Fluxo de Trabalho

```bash
# Após fazer alterações
git add .
git commit -m "feat: descrição da mudança"
git push

# Exemplos de mensagens de commit:
# feat: adiciona nova seção de certificações
# fix: corrige link quebrado no portfólio
# docs: atualiza README com novas instruções
# style: ajusta cores do tema claro
```

### Versionamento

Este projeto segue [Semantic Versioning](https://semver.org/):
- **MAJOR** (2.x.x): Mudanças incompatíveis na estrutura
- **MINOR** (x.1.x): Novas funcionalidades compatíveis
- **PATCH** (x.x.1): Correções de bugs

Veja o arquivo `CHANGELOG.md` para histórico completo.

## 📄 Licença

© 2025 Vinicius Capanema — Todos os direitos reservados.

---

**Versão:** Modelo A • v2  
**Data de atualização:** 3 de novembro de 2025  
**Status:** ✅ Pronto para produção
