
# 🧠 Know Your Fan - FURIA Edition

🔗 [Acesse a Aplicação Online](https://furiayourfan.streamlit.app/)

Projeto desenvolvido para o **Challenge #2 - Know Your Fan** do processo seletivo de Estágio em Engenharia de Software da **FURIA Esports**.

---

## 🎯 Objetivo

Desenvolver uma aplicação capaz de:

- Coletar, validar e estruturar informações de torcedores da FURIA.
- Simular o processo de "Know Your Fan" adotado por clubes profissionais.
- Utilizar Inteligência Artificial para análise de documentos e perfis sociais.

---

## 🚀 Funcionalidades Implementadas

- 📑 **Coleta de Dados Pessoais**: Nome, endereço, CPF, telefone, e-mail.
- 🎮 **Interesses e Atividades**: Histórico de participação e compras no universo e-sports.
- 🖼️ **Upload e Validação de Documentos**: Simulação de análise de RG, CNH ou CPF via IA.
- 🌐 **Vinculação de Redes Sociais**: Instagram, Twitter, Steam e HLTV.
- 🧠 **Análise de Interações Sociais**: Identificação de curtidas, grupos e atividade no mundo dos e-sports.
- 🔗 **Validação de Links**: Checagem automática de perfis em sites externos.
- 📊 **Barra de Progresso**: Acompanhamento do status de cadastro (Recruta → Torcedor Oficial).
- ✅ **Termo de Consentimento LGPD**: Obrigatório para finalização.
- 🎖️ **Badge de Conquista**: Ao completar o cadastro.

---

## 🛠️ Tecnologias Utilizadas

- [Python 3.11+](https://www.python.org/)
- [Streamlit](https://streamlit.io/) – Desenvolvimento rápido de aplicações web
- [Requests](https://docs.python-requests.org/en/latest/) – Integração com API pública (ViaCEP)
- **Simulação de IA** usando recursos nativos do Streamlit (`spinner`, `sleep`, `mensagens condicionais`)

---

## 📚 Como Rodar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/HugoCorrea01/know-your-fan-furia.git
cd know-your-fan-furia
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install streamlit requests
```

### 4. Rode a aplicação

```bash
streamlit run app.py
```

Acesse o app em: `http://localhost:8501/`

---

## 🔒 Observação Importante

Esta aplicação é um protótipo acadêmico para fins de processo seletivo.  
Todas as análises de documentos, validações de perfis sociais e simulações de IA são fictícias, respeitando o escopo ético da Lei Geral de Proteção de Dados (LGPD).

---

## 👨‍💻 Autor

**Hugo Farranha**  
[LinkedIn](https://www.linkedin.com/in/hugo-farranha-843724268/) • [GitHub](https://github.com/HugoCorrea01)

---

# 🦁 GL HF!

Esta solução foi desenvolvida com técnica e paixão, buscando representar o DNA inovador da FURIA.  
**Obrigado pela oportunidade de fazer parte deste desafio!** 🦁🔥
