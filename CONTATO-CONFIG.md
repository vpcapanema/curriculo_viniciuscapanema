# 📧 Configuração do Formulário de Contato

## 🎯 Visão Geral

O formulário de contato usa **Formspree** para permitir que visitantes enviem mensagens por **E-mail de forma 100% privada**, sem expor nenhum dado pessoal (nem no código-fonte da página).

---

## ⚙️ Como Configurar (Passo a Passo)

### 1️⃣ **Criar Conta no Formspree (Grátis)**

1. Acesse: **https://formspree.io**
2. Clique em **"Get Started"** ou **"Sign Up"**
3. Crie conta com seu email (ou use Google/GitHub)
4. Confirme seu email

### 2️⃣ **Criar um Formulário**

1. No dashboard, clique em **"+ New Form"**
2. Dê um nome (ex: "Contato Currículo")
3. Clique em **"Create Form"**
4. **Copie o Form ID** (aparece assim: `xyzabc123` ou similar)

### 3️⃣ **Configurar no Código**

1. Abra: `public/index.html`
2. Procure por esta linha (próximo ao final do arquivo):

```javascript
const FORMSPREE_ID = 'YOUR_FORMSPREE_ID'; // ← ALTERE AQUI
```

3. Substitua `YOUR_FORMSPREE_ID` pelo ID que você copiou:

```javascript
const FORMSPREE_ID = 'xyzabc123'; // ← Cole seu ID aqui
```

4. Salve o arquivo (`Ctrl + S`)

---

## ✅ Pronto! Está Funcionando

Agora quando alguém enviar uma mensagem:
1. ✅ A mensagem é enviada para o Formspree
2. ✅ Formspree encaminha para seu email
3. ✅ Você recebe notificação
4. ✅ Pode ver mensagens no dashboard do Formspree
5. ✅ **Nenhum dado seu fica exposto** (nem no código)

---

## 🧪 Como Testar

1. Abra `public/index.html` no navegador
2. Role até a seção "Entre em Contato"
3. Preencha:
   - **Mensagem**: "Teste de formulário"
   - **E-mail (opcional)**: seu email para receber resposta
4. Clique em **"Enviar Mensagem"**
5. Deve aparecer: ✅ "Mensagem enviada com sucesso!"
6. Verifique seu email (pode demorar 1-2 minutos)

---

## ⚠️ Solução de Problemas

### ❌ Erro: "Configure o Formspree primeiro!"
**Causa:** Você não substituiu `YOUR_FORMSPREE_ID` pelo ID real  
**Solução:** Siga os passos 2️⃣ e 3️⃣ acima

### ❌ Erro: "Erro ao enviar mensagem"
**Causa 1:** ID do Formspree inválido  
**Solução:** Verifique se copiou corretamente (sem espaços ou aspas extras)

**Causa 2:** Sem conexão com internet  
**Solução:** Verifique sua conexão e tente novamente

### ❌ Não recebeu email
**Causa:** Email pode ter ido para Spam  
**Solução:** Verifique caixa de Spam/Lixo Eletrônico

---

## 📊 Plano Gratuito do Formspree

| Recurso | Limite Grátis |
|---------|---------------|
| Mensagens/mês | 50 |
| Formulários | Ilimitados |
| Arquivos anexos | 10 MB |
| Anti-spam | ✅ Incluído |
| HTTPS | ✅ Incluído |
| Dashboard | ✅ Incluído |

**Nota:** 50 mensagens/mês é mais que suficiente para currículos pessoais. Se precisar mais, há planos pagos.

---

## 🔒 Segurança e Privacidade

✅ **Seu email NÃO aparece em lugar nenhum** (nem no código-fonte da página)  
✅ **Seu WhatsApp NÃO está mais na página** (foi removido para manter privacidade)  
✅ **Apenas Formspree sabe seu email** (é uma empresa confiável usada por milhões)  
✅ **Você controla quem recebe as mensagens** (só você tem acesso ao dashboard)  

---

## 📚 Documentação Oficial

- Site: https://formspree.io
- Documentação: https://help.formspree.io
- Suporte: https://formspree.io/support

---

## 🧪 Como Testar

### **Teste WhatsApp:**
1. Abra `public/index.html` no navegador
2. Digite uma mensagem de teste
3. Clique em **📱 Enviar por WhatsApp**
4. WhatsApp Web deve abrir com a mensagem pré-preenchida

### **Teste E-mail (Mailto):**
1. Digite uma mensagem
2. Clique em **✉️ Enviar por E-mail**
3. Seu cliente de email padrão deve abrir

### **Teste E-mail (Formspree):**
1. Configure o Formspree conforme acima
2. Digite uma mensagem
3. Clique em **✉️ Enviar por E-mail**
4. Aguarde confirmação
5. Verifique o painel do Formspree ou seu email

---

## 🔒 Segurança e Privacidade

### **WhatsApp:**
- ✅ Número fica no código JavaScript
- ⚠️ Pode ser visto se alguém abrir o código-fonte (`Ctrl+U`)
- ⚠️ Bots podem coletar (menos comum que emails em HTML)
- ✅ Usuários técnicos teriam que procurar ativamente

### **E-mail com Mailto:**
- ⚠️ Email visível no código-fonte
- ⚠️ Bots podem coletar facilmente
- ❌ Não recomendado para evitar spam

### **E-mail com Formspree:**
- ✅ Email **100% oculto**
- ✅ Proteção anti-spam
- ✅ Solução profissional
- ✅ **RECOMENDADO**

---

## 🎨 Personalização

### **Alterar Textos**

Edite em `public/index.html`:

```html
<h2>Entre em Contato</h2> <!-- Título da seção -->
<p>Tem um projeto em mente...</p> <!-- Descrição -->

<textarea placeholder="Digite sua mensagem aqui..."></textarea> <!-- Placeholder -->

<button>📱 Enviar por WhatsApp</button> <!-- Texto do botão -->
<button>✉️ Enviar por E-mail</button> <!-- Texto do botão -->

<p class="contact-hint">💡 Sua mensagem será...</p> <!-- Dica -->
```

### **Alterar Cores**

Os botões usam as variáveis CSS do tema. Para cores personalizadas:

```css
/* Adicione ao <style> */
.contact-form .btn {
  background: #25D366; /* Verde WhatsApp */
}

.contact-form .btn:nth-child(2) {
  background: #EA4335; /* Vermelho Gmail */
}
```

---

## 🚀 Alternativas Avançadas

### **Web3Forms** (Alternativa ao Formspree)
- Gratuito ilimitado
- https://web3forms.com
- Similar ao Formspree

### **Netlify Forms** (Se hospedar no Netlify)
- Incluso no plano gratuito
- 100 submissões/mês
- Configuração por atributos HTML

### **EmailJS**
- JavaScript puro
- Até 200 emails/mês grátis
- https://emailjs.com

---

## 📝 Exemplo Completo de Configuração

```javascript
// Para usar WhatsApp + Formspree (RECOMENDADO):
const WHATSAPP_NUMBER = '5511971190509';
const EMAIL_ADDRESS = 'viniciuscapanema@hotmail.com';
const USE_FORMSPREE = true;
const FORMSPREE_ID = 'xyzabc123'; // ← Obtenha em formspree.io

// Para usar WhatsApp + Mailto (não recomendado):
const WHATSAPP_NUMBER = '5511971190509';
const EMAIL_ADDRESS = 'viniciuscapanema@hotmail.com';
const USE_FORMSPREE = false;
const FORMSPREE_ID = 'YOUR_FORMSPREE_ID';
```

---

## ❓ Solução de Problemas

### **WhatsApp não abre:**
- Verifique o formato do número (sem espaços ou caracteres especiais)
- Teste manualmente: `https://wa.me/5511971190509?text=teste`

### **E-mail não envia (Formspree):**
- Confirme que `USE_FORMSPREE = true`
- Verifique o `FORMSPREE_ID` (deve ter ~10 caracteres)
- Veja console do navegador (F12) para erros

### **Botão de tema quebrou:**
- Certifique-se de não ter apagado o código do tema por acidente
- O código do contato foi adicionado, não substituído

---

## 📚 Recursos

- **Formspree:** https://formspree.io
- **Web3Forms:** https://web3forms.com
- **EmailJS:** https://emailjs.com
- **WhatsApp API:** https://faq.whatsapp.com/general/chats/how-to-use-click-to-chat

---

**Versão:** 1.0  
**Data:** 3 de novembro de 2025  
**Status:** ✅ Implementado e testado
