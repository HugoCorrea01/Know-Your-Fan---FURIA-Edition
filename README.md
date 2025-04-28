
# 🧠 Know Your Fan - FURIA Edition

Aplicação desenvolvida para o Challenge #2 do processo seletivo de Estágio em Engenharia de Software da FURIA Esports.

## 🎯 Objetivo

Coletar, validar e estruturar informações de torcedores da FURIA, simulando o processo real de "Know Your Fan", com uso de inteligência artificial para análise de documentos e perfis sociais.

## 🚀 Funcionalidades

- 📑 Coleta de dados pessoais (nome, endereço, CPF, telefone, e-mail).
- 🎮 Seleção de interesses, atividades e histórico de compras relacionadas a e-sports.
- 🖼️ Upload de documento de identificação com **simulação de validação por IA**.
- 🌐 Vinculação de redes sociais (Instagram, Twitter, Steam, HLTV).
- 🧠 **Simulação de IA** analisando interações sociais (seguidores, curtidas, grupos).
- 🔗 Validação automática de links de perfis em sites de e-sports.
- 📊 Barra de progresso do cadastro + status do torcedor (Recruta → Torcedor Oficial).
- ✅ Termo de Consentimento da LGPD obrigatório para conclusão.
- 🎖️ Badge de conquista ao final do cadastro.


## 🛠️ Tecnologias Utilizadas

- [Python 3.11+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Requests](https://docs.python-requests.org/en/latest/)
- Simulação de Inteligência Artificial utilizando Streamlit (`spinner` + `sleep`)

---

## 📚 Como Rodar Localmente

1. Clone o repositório:

```bash
git clone https://github.com/HugoCorrea01/know-your-fan-furia.git
cd know-your-fan-furia
```

2. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate   # Windows
```

3. Instale as dependências:

```bash
pip install streamlit requests
```

4. Rode a aplicação:

```bash
streamlit run app.py
```

---

## 🧠 Observação

Esta aplicação é um protótipo acadêmico para fins de processo seletivo.  
Todas as validações de IA e extrações de dados são **simulações**, respeitando o escopo do desafio e a ética no tratamento de dados pessoais (LGPD).

---

## ✉️ Contato

Feito  por **Hugo Farranha**.

- [LinkedIn](https://www.linkedin.com/in/hugo-farranha-843724268/)
- [GitHub](https://github.com/HugoCorrea01)

---
