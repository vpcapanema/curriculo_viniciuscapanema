# ⚡ COMANDOS PRONTOS PARA COPIAR E COLAR

## 🎯 OPÇÃO 1: Comando Único (Recomendado)

Copie e cole TUDO isto no PowerShell/Git Bash:

```
cd D:\CV_ONLINE_VINICIUS && git init && git config user.name "Vinicius Capanema" && git config user.email "vpcapanema@outlook.com" && git add --all && git commit -m "🎉 Deploy v07 com GitHub Pages" && git branch -M main && git remote add origin https://github.com/vpcapanema/curriculo_viniciuscapanema.git && git push -u origin main
```

---

## 🎯 OPÇÃO 2: Passo a Passo (Se Opção 1 falhar)

Copie E COLE CADA LINHA (uma por vez):

### Linha 1:
```
cd D:\CV_ONLINE_VINICIUS
```

### Linha 2:
```
git init
```

### Linha 3:
```
git config user.name "Vinicius Capanema"
```

### Linha 4:
```
git config user.email "vpcapanema@outlook.com"
```

### Linha 5:
```
git add --all
```

### Linha 6:
```
git commit -m "🎉 Deploy v07 com GitHub Pages"
```

### Linha 7:
```
git branch -M main
```

### Linha 8:
```
git remote add origin https://github.com/vpcapanema/curriculo_viniciuscapanema.git
```

### Linha 9: ⭐ A MAIS IMPORTANTE
```
git push -u origin main
```

---

## 🔑 SE PEDIR PASSWORD/TOKEN

1. Vá em: https://github.com/settings/tokens
2. Clique: "Generate new token (classic)"
3. Em Scopes, selecione: ✅ repo (full control)
4. Clique: "Generate token"
5. COPIE o token que apareceu
6. Volte ao PowerShell
7. Na hora que pedir "password", **COLE O TOKEN** (Ctrl+V)
8. Pressione Enter

---

## ✅ RESULTADO

Se tudo der certo, verá:
```
 * [new branch]      main -> main
Branch 'main' set up to track remote tracking branch 'main' from 'origin'.
```

---

## 📍 PRÓXIMOS PASSOS

1. Acesse: https://github.com/vpcapanema/curriculo_viniciuscapanema
2. Vá em: Settings > Pages
3. Source: Branch main / Pasta /
4. Clique Save
5. Aguarde 2-5 minutos
6. Acesse: https://vpcapanema.github.io/curriculo_viniciuscapanema/

---

## 🐛 SE NÃO FUNCIONAR

### "command not found: git"
→ Git não está instalado
→ Baixe: https://git-scm.com/download/win

### "fatal: not a git repository"
→ Certifique que está no diretório certo
→ Execute: `cd D:\CV_ONLINE_VINICIUS`

### "fatal: remote origin already exists"
→ Execute: `git remote remove origin`
→ Depois tente novamente

### "Permission denied"
→ Gere Personal Access Token (token)
→ https://github.com/settings/tokens

---

📧 Dúvidas: vpcapanema@outlook.com
