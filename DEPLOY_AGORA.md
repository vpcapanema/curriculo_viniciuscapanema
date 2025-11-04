# ⚡ DEPLOY INSTANTÂNEO - SIGA EXATAMENTE ISSO

## 🎯 OBJETIVO
Enviar o currículo v07 para: https://github.com/vpcapanema/curriculo_viniciuscapanema

---

## 📋 PRÉ-REQUISITO (1 MINUTO)

### Se Git NÃO estiver instalado:
1. Baixe: https://git-scm.com/download/win
2. Instale (próximo, próximo, próximo...)
3. Reinicie o PowerShell/CMD

### Verificar Git:
```powershell
git --version
```
Se aparecer versão = OK ✅

---

## 🚀 EXECUTE ESTES COMANDOS (3 MINUTOS)

Abra PowerShell ou Git Bash e execute **linha por linha**:

### PASSO 1: Ir para o diretório
```bash
cd D:\CV_ONLINE_VINICIUS
```

### PASSO 2: Inicializar repositório
```bash
git init
git config user.name "Vinicius Capanema"
git config user.email "vpcapanema@outlook.com"
```

### PASSO 3: Adicionar arquivos
```bash
git add --all
git status
```
(Deve listar arquivos em verde)

### PASSO 4: Fazer commit
```bash
git commit -m "🎉 Deploy v07 com GitHub Pages"
```

### PASSO 5: Renomear branch
```bash
git branch -M main
```

### PASSO 6: Adicionar remote
```bash
git remote add origin https://github.com/vpcapanema/curriculo_viniciuscapanema.git
```

### PASSO 7: ⭐ FAZER PUSH (O IMPORTANTE!)
```bash
git push -u origin main
```

**SERÁ PEDIDO:**
- Username (ou Personal Access Token)
- Password (ou Token)

**Para password:**
- Gere token em: https://github.com/settings/tokens
- Clique: "Generate new token (classic)"
- Escopo: selecione `repo` (full control)
- Copy o token
- Na hora do push, onde pede "password", cole o token

---

## ✅ APÓS FAZER PUSH

1. Aguarde 2-5 minutos
2. Acesse: https://github.com/vpcapanema/curriculo_viniciuscapanema
3. Vá em: **Settings > Pages**
4. Selecione:
   - Source: **Deploy from a branch**
   - Branch: **main** 
   - Folder: **/ (root)**
5. Clique **Save**

---

## 🌐 ACESSAR CURRÍCULO ONLINE

Após ~2 minutos:
```
https://vpcapanema.github.io/curriculo_viniciuscapanema/
```

---

## 🐛 SE DER ERRO

### "Erro de autenticação"
```bash
git credential reject
git config --global credential.helper store
git push -u origin main
```

### "Remote já existe"
```bash
git remote remove origin
git remote add origin https://github.com/vpcapanema/curriculo_viniciuscapanema.git
git push -u origin main
```

### "Branch mismatch"
```bash
git branch -M main
git push -u origin main
```

### Verificar o que vai enviar:
```bash
git status
git log --oneline
```

---

## 📊 CHECKLIST

- [ ] Git instalado (verificar com `git --version`)
- [ ] No diretório D:\CV_ONLINE_VINICIUS
- [ ] Executou `git init`
- [ ] Configurou user.name e user.email
- [ ] Executou `git add --all`
- [ ] Fez commit (`git commit`)
- [ ] Renomeou branch para main (`git branch -M main`)
- [ ] Adicionou remote origin (`git remote add origin ...`)
- [ ] **Fez PUSH** (`git push -u origin main`) ⭐
- [ ] Configurou GitHub Pages em Settings > Pages
- [ ] Acessou https://vpcapanema.github.io/curriculo_viniciuscapanema/

---

## 📧 SUPORTE

**Email**: vpcapanema@outlook.com
**GitHub**: https://github.com/vpcapanema

---

**Tempo total**: ~5 minutos (primeira vez)
**Atualizações futuras**: ~1 minuto
