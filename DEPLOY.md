# Guia de Deploy — Currículo Online

## 🚀 Opções de Deploy

### 1️⃣ GitHub Pages (Recomendado)

#### Método A: Deploy da pasta `public/`

```bash
# 1. Crie um repositório no GitHub (exemplo: cv-online)

# 2. Configure Git localmente
cd D:\CV_ONLINE_VINICIUS
git init
git add .
git commit -m "feat: estrutura inicial v2.0.0"

# 3. Conecte ao GitHub
git remote add origin https://github.com/seu-usuario/cv-online.git
git branch -M main
git push -u origin main

# 4. Configure GitHub Pages
# Vá para: Settings → Pages
# Source: Deploy from a branch
# Branch: main
# Folder: /public
# Save
```

**URL de acesso:** `https://seu-usuario.github.io/cv-online/`

#### Método B: Deploy da raiz (mover arquivos)

```bash
# Se preferir servir da raiz, mova os arquivos:
mv public/* .
rm -rf public/

# Atualize links no HTML se necessário
# Então siga os passos 2-4 acima, mas escolha:
# Folder: / (root)
```

### 2️⃣ Netlify

```bash
# 1. Instale Netlify CLI (opcional)
npm install -g netlify-cli

# 2. Faça login
netlify login

# 3. Deploy da pasta public
netlify deploy --dir=public --prod

# Ou use Drag & Drop no site do Netlify:
# https://app.netlify.com/drop
# Arraste a pasta 'public' para a área de upload
```

**Vantagens:**
- Deploy instantâneo
- HTTPS automático
- Domínio customizável

### 3️⃣ Vercel

```bash
# 1. Instale Vercel CLI
npm install -g vercel

# 2. Faça login
vercel login

# 3. Deploy
cd public
vercel --prod
```

### 4️⃣ Servidor Apache/Nginx (Tradicional)

```bash
# 1. Copie os arquivos para o servidor
scp -r public/* usuario@servidor:/var/www/html/cv/

# 2. Configure permissões
ssh usuario@servidor
chmod -R 755 /var/www/html/cv/
```

**Configuração Nginx:**
```nginx
server {
    listen 80;
    server_name cv.seudominio.com;
    root /var/www/html/cv;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

## ✅ Checklist Pré-Deploy

- [ ] Testar index.html localmente
- [ ] Verificar navegação entre index.html ↔ portfolio.html
- [ ] Testar alternância de tema (🌓)
- [ ] Validar responsividade (360px–1440px)
- [ ] Verificar links externos (LinkedIn, Lattes)
- [ ] Confirmar que não há dados sensíveis no código
- [ ] Revisar ortografia e gramática
- [ ] Testar em navegadores: Chrome, Firefox, Safari, Edge
- [ ] Verificar em mobile (Chrome DevTools)

## 🔧 Configuração de Domínio Personalizado

### GitHub Pages

1. Adicione arquivo `CNAME` na pasta `public/`:
   ```
   cv.seudominio.com
   ```

2. Configure DNS no seu provedor:
   ```
   Type: CNAME
   Name: cv (ou @)
   Value: seu-usuario.github.io
   ```

3. No GitHub: Settings → Pages → Custom domain → Digite `cv.seudominio.com`

### Netlify/Vercel

Interface gráfica:
1. Dashboard → Domain Settings
2. Add custom domain
3. Siga instruções de configuração DNS

## 📊 Monitoramento e Analytics (Opcional)

### Google Analytics

Adicione antes do `</head>` em `index.html` e `portfolio.html`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Plausible Analytics (Privacy-Friendly)

```html
<script defer data-domain="seudominio.com" src="https://plausible.io/js/script.js"></script>
```

## 🔄 Atualização do Conteúdo

```bash
# 1. Edite os arquivos HTML em public/
# 2. Teste localmente
# 3. Commit e push

git add public/
git commit -m "feat: atualiza seção de experiência"
git push

# GitHub Pages atualizará automaticamente em ~1-2 minutos
```

## 🐛 Troubleshooting

### Problema: Página 404 no GitHub Pages
**Solução:** Verifique se a pasta configurada em Settings → Pages corresponde à localização dos arquivos

### Problema: Links quebrados entre páginas
**Solução:** Use caminhos relativos (`./portfolio.html` em vez de `/portfolio.html`)

### Problema: Tema não persiste
**Solução:** Verifique se localStorage está habilitado no navegador

### Problema: Deploy demora muito
**Solução:** GitHub Pages pode levar até 10 minutos na primeira vez. Deployments subsequentes são mais rápidos.

## 📈 SEO Pós-Deploy

1. **Google Search Console**
   - Adicione propriedade
   - Envie sitemap (opcional)
   - Monitore indexação

2. **Sitemap.xml** (Opcional - crie em `public/sitemap.xml`):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://seudominio.com/</loc>
    <lastmod>2025-11-03</lastmod>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://seudominio.com/portfolio.html</loc>
    <lastmod>2025-11-03</lastmod>
    <priority>0.8</priority>
  </url>
</urlset>
```

## 🎯 Próximos Passos Após Deploy

1. ✅ Compartilhar URL no LinkedIn
2. ✅ Adicionar ao e-mail de assinatura
3. ✅ Incluir em perfis profissionais (GitHub, Lattes)
4. ✅ Solicitar feedback de colegas
5. ✅ Monitorar analytics (se configurado)

---

**Dúvidas?** Consulte o `README.md` para mais informações.
