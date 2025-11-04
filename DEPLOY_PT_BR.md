# 🎓 VINICIUS CAPANEMA - DEPLOY PARA GITHUB (PORTUGUÊS)

## 📌 RESUMO EXECUTIVO

Vamos enviar seu currículo v07 para ficar online em:
```
https://vpcapanema.github.io/curriculo_viniciuscapanema/
```

**Tempo necessário**: 5-10 minutos
**Dificuldade**: Fácil (apenas copiar e colar comandos)

---

## ✅ PRÉ-REQUISITOS

### 1. Git Instalado?
Abra PowerShell e digite:
```
git --version
```

Se aparecer uma versão (ex: `git version 2.42.0`) = OK ✅

Se NÃO aparecer:
- Baixe: https://git-scm.com/download/win
- Instale (siga as instruções padrão)
- Reinicie PowerShell

### 2. Conta GitHub?
- Crie em: https://github.com/signup
- Use email: vpcapanema@outlook.com

---

## 🚀 PASSO A PASSO (Copiar e Colar)

### PASSO 1: Abra o PowerShell

Na pasta `D:\CV_ONLINE_VINICIUS`, abra PowerShell clicando:
- Clique com botão direito na pasta vazia
- "Abrir no Windows Terminal" ou "Abrir PowerShell aqui"

Ou digite no terminal:
```
cd D:\CV_ONLINE_VINICIUS
```

### PASSO 2: Execute este comando:

**COPIE TUDO ISTO DE UMA VEZ:**

```
git init && git config user.name "Vinicius Capanema" && git config user.email "vpcapanema@outlook.com" && git add --all && git commit -m "🎉 Deploy v07" && git branch -M main && git remote add origin https://github.com/vpcapanema/curriculo_viniciuscapanema.git && git push -u origin main
```

Depois **COLE** no PowerShell com:
- Botão direito > Colar
- Ou Ctrl+V

E pressione **ENTER**

### PASSO 3: Se Pedir Autenticação

O PowerShell pedirá:

```
Username: 
```
Digite seu **usuário do GitHub** e pressione ENTER

```
Password:
```

**AQUI NÃO É A SENHA DA CONTA!**

Vá em: https://github.com/settings/tokens

1. Clique "Generate new token (classic)"
2. Em "Scopes", marque: ✅ **repo** (full control)
3. Clique "Generate token"
4. **COPIE o token que aparecer**
5. Volte ao PowerShell
6. **COLE o token** (Ctrl+V)
7. Pressione ENTER

---

## ✅ VALIDAR QUE FUNCIONOU

Se viu isto no final:
```
 * [new branch]      main -> main
Branch 'main' set up to track remote tracking branch 'main' from 'origin'.
```

**ÓTIMO!** ✅ Funcionou!

---

## 📋 APÓS O PUSH (Configurar GitHub Pages)

1. Vá em: https://github.com/vpcapanema/curriculo_viniciuscapanema

2. Clique em **Settings** (⚙️)

3. No menu esquerdo, clique em **Pages**

4. Em "Source", selecione:
   - Branch: **main**
   - Folder: **/ (root)**

5. Clique **Save**

6. Aguarde 2-5 minutos

7. A página aparecerá em azul no topo com seu link:
   ```
   https://vpcapanema.github.io/curriculo_viniciuscapanema/
   ```

---

## 🌐 ACESSAR SEU CURRÍCULO ONLINE

Após 2-5 minutos:

```
https://vpcapanema.github.io/curriculo_viniciuscapanema/
```

---

## 🐛 PROBLEMAS COMUNS

### ❌ "git command not found"
**Solução**: Git não está instalado
- Baixe: https://git-scm.com/download/win
- Instale
- Reinicie PowerShell

### ❌ "fatal: not a git repository"
**Solução**: Você não está na pasta correta
- Execute: `cd D:\CV_ONLINE_VINICIUS`
- Depois repita o comando

### ❌ "fatal: remote origin already exists"
**Solução**: Remote já foi adicionado
- Execute: `git remote remove origin`
- Depois repita o comando de push

### ❌ Erro de autenticação
**Solução**: Use Token em vez de Senha
- Token: https://github.com/settings/tokens
- Scope: **repo** (full control)
- Cole como password

### ❌ "refused to merge unrelated histories"
**Solução**: Execute isto:
```
git pull origin main --allow-unrelated-histories
git push -u origin main
```

---

## 📊 O QUE ESTÁ SENDO ENVIADO

```
✅ index.html (raiz)
✅ .nojekyll (configuração Pages)
✅ assets/docs/v07/public/ (PÁGINA PRINCIPAL)
   - index.html (v07)
   - portfolio.html
   - CSS inline
   - Imagens
✅ Todos os PDFs
✅ Scripts Python
✅ Documentação
```

---

## ✨ APÓS TUDO PRONTO

Seu currículo:
- ✅ Online e acessível de qualquer lugar
- ✅ Dark mode automático
- ✅ Responsivo (celular, tablet, desktop)
- ✅ Atualiza automaticamente com cada push
- ✅ Gratuito (GitHub Pages)
- ✅ Domínio personalizado (depois, se quiser)

---

## 📧 DÚVIDAS?

Email: vpcapanema@outlook.com

---

## 🎯 RESUMO DOS COMANDOS

| O que fazer | Comando |
|---|---|
| Iniciar Git | `git init` |
| Configurar nome | `git config user.name "Vinicius Capanema"` |
| Configurar email | `git config user.email "vpcapanema@outlook.com"` |
| Adicionar tudo | `git add --all` |
| Fazer commit | `git commit -m "Deploy v07"` |
| Ir para main | `git branch -M main` |
| Adicionar repositório | `git remote add origin https://github.com/vpcapanema/curriculo_viniciuscapanema.git` |
| **Enviar** ⭐ | `git push -u origin main` |

---

**Pronto? Então COMECE AGORA!** 🚀

Execute o comando do PASSO 2 e deixa a mágica acontecer!
