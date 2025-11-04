# Prompt para Finalização da V07 (Avant)

## Contexto
Estou trabalhando na versão 7 (V07 - Avant) do meu currículo online. Esta versão já possui:
- Layout assimétrico com hero grid 1.2:1
- Tipografia unificada Montserrat
- Esquema de cores dark (azul escuro/cinza): `--bg:#0a0e14`, `--surface:#141b24`, `--accent:#60a5fa`
- Sistema de timeline vertical com expand/collapse funcional
- Portfolio em masonry grid com filtros
- Estrutura de tema claro/escuro com localStorage

## Localização dos Arquivos
- **V07 (Avant) atual**: `D:\CV_ONLINE_VINICIUS\assets\docs\v07\public\index.html`
- **V07 Portfolio**: `D:\CV_ONLINE_VINICIUS\assets\docs\v07\public\portfolio.html`
- **V01 (fonte de conteúdo completo)**: `D:\CV_ONLINE_VINICIUS\public\index.html`

## O Que Precisa Ser Feito

### 1. EXPANDIR TODO O CONTEÚDO COM EXPAND/COLLAPSE

**Seções que precisam ser expandidas com conteúdo completo da V01:**

#### A) **Competências-chave** (8 itens com descrições detalhadas)
Copiar da V01 e adicionar sistema expand/collapse igual ao timeline:
1. Pesquisa & Desenvolvimento
2. Gestão de Projetos & Equipes
3. Governança Ambiental & Sustentabilidade
4. Geoprocessamento & Sensoriamento Remoto
5. Engenharia de Dados Geoespaciais
6. WebGIS & Desenvolvimento de Aplicações
7. Análise Multicritério & Tomada de Decisão
8. (verificar se há mais na V01)

Cada item deve ter:
```html
<li class="competency-item">
  <div class="competency-header" onclick="toggleCompetency(this)">
    <span class="expand-icon">▶</span>
    <span>TÍTULO DA COMPETÊNCIA</span>
  </div>
  <div class="competency-content">
    CONTEÚDO DETALHADO COMPLETO DA V01
  </div>
</li>
```

#### B) **Idiomas**
- Inglês — Avançado
- Espanhol — Intermediário

#### C) **Cursos** (5 categorias com expand/collapse)
1. Georreferenciamento & Topografia
2. Geoprocessamento & SIG
3. Programação & Dados
4. Meio Ambiente & Licenciamento
5. Gestão & Negócios

Cada categoria com lista completa de cursos da V01.

#### D) **Projetos** (2 projetos com expand/collapse)
1. Monitoramento Ambiental por Satélite no Bioma Amazônia (INPE)
2. e-Sensing: Big Earth Observation Data Analytics

Cada projeto com descrição completa, período, objetivos e resultados da V01.

#### E) **Formação Acadêmica** (5 itens com expand/collapse)
Manter os 5 mini-cards mas adicionar expand/collapse com descrições completas:
1. Doutorado em Sensoriamento Remoto (INPE - 2022)
2. MBA em Gestão de Projetos (Unopar - 2020)
3. Mestrado em Sensoriamento Remoto (INPE - 2017)
4. Especialização em Georreferenciamento (Faculdades Vale Juruena - 2010)
5. Graduação em Engenharia Florestal (UNEMAT - 2009)

Cada item deve ter descrição detalhada da tese/dissertação, orientador, etc (verificar V01).

#### F) **Experiência Profissional** 
**JÁ ESTÁ COMPLETO** com 8 posições expandidas:
- SEMIL/SP (Julho/2025 – Atual)
- DER/SP Coordenador (Setembro/2024 – Janeiro/2025)
- DER/SP Especialista (Agosto/2023 – Setembro/2024)
- Stantec (Janeiro/2024 – Março/2024)
- VEGA (Março/2022 – Agosto/2023)
- GeoBrasilis (Setembro/2021 – Março/2022)
- FUNCATE (Maio/2017 – Março/2018)
- Mognos (Janeiro/2010 – Janeiro/2015)

#### G) **Tecnologias & Ferramentas** (9 categorias com expand/collapse)
Copiar da V01 com descrições técnicas completas:
1. Geoprocessamento & Sensoriamento Remoto
2. Programação & Análise de Dados
3. Banco de Dados Espaciais
4. WebGIS & Publicação de Serviços
5. APIs & Backend Geoespacial
6. DevOps & Infraestrutura
7. IA & Machine Learning Aplicado
8. Governança & Qualidade de Dados
9. Office & Produtividade

#### H) **Publicações** (6 artigos com expand/collapse)
Copiar da V01 com citações completas, autores, DOI, URLs:
1. IUFRO 2019 (2 artigos)
2. SBSR 2019
3. Revista Brasileira de Cartografia 2018
4. SBSR 2017 (2 artigos)

#### I) **VPC-GEOSER**
Seção especial com descrição do sistema (copiar da V01).

---

### 2. IMPLEMENTAR MODO CLARO/ESCURO FUNCIONAL

**O toggle já existe**, mas precisa ajustar as cores do modo claro:

```css
/* Modo Escuro (ATUAL - JÁ FUNCIONA) */
:root {
  --bg:#0a0e14; --fg:#e8eaed; --muted:#9ba3ae;
  --surface:#141b24; --surface-2:#0f1520; --line:#1f2937;
  --accent:#60a5fa; --accent-dark:#3b82f6; --accent-light:#dbeafe;
}

/* Modo Claro (ADICIONAR) */
:root.light {
  --bg:#f8f9fa; --fg:#1a1d28; --muted:#6b7280;
  --surface:#ffffff; --surface-2:#f1f3f5; --line:#e5e7eb;
  --accent:#3b82f6; --accent-dark:#2563eb; --accent-light:#93c5fd;
  --shadow: 0 2px 8px rgba(0,0,0,.08), 0 1px 2px rgba(0,0,0,.05);
  --shadow-lg: 0 10px 30px rgba(0,0,0,.12), 0 2px 8px rgba(0,0,0,.08);
}
```

**JavaScript do toggle:**
- Já existe no arquivo
- Deve alternar classe `dark` ou `light` no `:root`
- Deve salvar preferência em `localStorage('v07-theme')`
- Deve carregar tema salvo ao abrir página

---

### 3. APLICAR DEGRADÊS DE 90° E 135° EM TODOS OS CARDS

Adicionar gradientes sutis em todos os elementos card/mini-card:

```css
/* Exemplo de aplicação */
.card, .mini-card {
  background: 
    linear-gradient(90deg, color-mix(in oklab, var(--accent) 15%, transparent), transparent),
    linear-gradient(135deg, color-mix(in oklab, var(--accent) 12%, transparent), transparent),
    var(--surface);
}
```

**Cards que precisam de gradiente:**
- `.card` (todos os cards principais)
- `.mini-card` (cards de formação acadêmica)
- `.timeline-item` (itens de experiência profissional)
- `.competency-item` (quando expandido)
- `.tech-item` (tecnologias, cursos, projetos, publicações)
- Cards de contato/VPC-GEOSER

---

### 4. CSS PARA EXPAND/COLLAPSE

Garantir que este CSS esteja presente para todas as seções:

```css
/* Competências */
.competency-item .competency-header {
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 0;
  -webkit-user-select: none;
  user-select: none;
}
.competency-item .expand-icon {
  font-size: 12px;
  transition: transform .2s;
}
.competency-item .expand-icon.expanded {
  transform: rotate(90deg);
}
.competency-content {
  overflow: hidden;
  max-height: 0;
  opacity: 0;
  transition: max-height .4s ease, opacity .4s ease;
}
.competency-content.expanded {
  max-height: 3000px;
  opacity: 1;
  margin-top: 8px;
}
```

**Replicar para:**
- `.tech-item` (já existe parcialmente)
- `.formation-item` (formação acadêmica)
- `.project-item`
- `.publication-item`

---

### 5. JAVASCRIPT NECESSÁRIO

Adicionar funções toggle para cada tipo de seção:

```javascript
function toggleCompetency(header) {
  const icon = header.querySelector('.expand-icon');
  const content = header.nextElementSibling;
  icon.classList.toggle('expanded');
  content.classList.toggle('expanded');
}

function toggleTech(header) {
  const icon = header.querySelector('.expand-icon');
  const content = header.nextElementSibling;
  icon.classList.toggle('expanded');
  content.classList.toggle('expanded');
}

function toggleFormation(header) {
  const icon = header.querySelector('.expand-icon');
  const content = header.nextElementSibling;
  icon.classList.toggle('expanded');
  content.classList.toggle('expanded');
}

// Tema
const themeToggle = document.getElementById('theme-toggle');
const root = document.documentElement;
const savedTheme = localStorage.getItem('v07-theme') || 'dark';

if (savedTheme === 'light') {
  root.classList.remove('dark');
  root.classList.add('light');
}

themeToggle?.addEventListener('click', () => {
  if (root.classList.contains('dark')) {
    root.classList.remove('dark');
    root.classList.add('light');
    localStorage.setItem('v07-theme', 'light');
  } else {
    root.classList.remove('light');
    root.classList.add('dark');
    localStorage.setItem('v07-theme', 'dark');
  }
});
```

---

### 6. BOTÃO DE TOGGLE TEMA NO NAV

Adicionar no `.nav-actions`:

```html
<button id="theme-toggle" class="btn" aria-label="Alternar tema claro/escuro">
  <i class="bi bi-moon-stars-fill"></i>
</button>
```

---

## Estrutura Completa Esperada

### SEÇÕES NO INDEX.HTML (ordem):

1. **Hero** (já existe)
2. **Síntese** (card full-width)
3. **Grid lateral (aside):**
   - Competências-chave (8 itens expand/collapse)
   - Idiomas (2 itens)
   - Cursos (5 categorias expand/collapse)
   - Projetos (2 projetos expand/collapse)
4. **Grid principal (main):**
   - Formação Acadêmica (5 mini-cards com expand/collapse)
   - Experiência Profissional (8 posições expand/collapse) ✅ JÁ FEITO
   - Tecnologias & Ferramentas (9 categorias expand/collapse)
   - Publicações (6 artigos expand/collapse)
   - VPC-GEOSER (card especial)
5. **Contato** (formulário com Formspree)
6. **Footer**

---

## Checklist Final

- [ ] Todas as seções com conteúdo completo da V01
- [ ] Sistema expand/collapse funcionando em todas as seções
- [ ] Modo claro com cores definidas (`:root.light`)
- [ ] Toggle tema funcional com localStorage
- [ ] Gradientes 90° e 135° em todos os cards
- [ ] Ícones rotacionam ao expandir (▶ → ▼)
- [ ] Transições suaves (400ms)
- [ ] Responsivo (mobile-first)
- [ ] Sem erros no console
- [ ] Acessibilidade (aria-labels, user-select)

---

## Estilo de Código Esperado

- **HTML semântico** com `<section>`, `<article>`, `<aside>`
- **CSS moderno** com custom properties, color-mix, backdrop-filter
- **JavaScript vanilla** (sem frameworks)
- **Mobile-first** com media queries
- **Performance** (fontes preconnect, transições GPU-accelerated)

---

## Observações Importantes

1. **NÃO resumir conteúdo** - copiar TUDO da V01 palavra por palavra
2. **Manter consistência visual** com o design Avant já estabelecido
3. **Testar gradientes** para não ficarem muito chamativos (opacidade 12-18%)
4. **Validar contraste** do modo claro para acessibilidade (WCAG AA mínimo)
5. **Preservar** a experiência de usuário do expand/collapse (smooth, intuitivo)

---

## Referências

- Arquivo V01 original: `D:\CV_ONLINE_VINICIUS\public\index.html`
- Arquivo V07 atual: `D:\CV_ONLINE_VINICIUS\assets\docs\v07\public\index.html`
- Portfolio V07: `D:\CV_ONLINE_VINICIUS\assets\docs\v07\public\portfolio.html`

---

**Sistema Operacional:** Windows  
**Shell:** PowerShell  
**Editor:** VS Code  
**Data:** 04 de novembro de 2025
