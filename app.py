import streamlit as st
import re
import requests
import time


st.set_page_config(page_title="Know Your Fan", page_icon="🧠", layout="centered")
st.title("🧠 Know Your Fan - FURIA Edition")
st.write("Preencha as informações para criarmos seu perfil de torcedor!")

# Funções
def buscar_endereco(cep):
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        data = response.json()
        if "erro" in data:
            return None
        return data
    except:
        return None

def mascarar_cpf(cpf):
    return f"{cpf[:3]}.***.***-{cpf[-2:]}"

def mascarar_telefone(telefone):
    return f"({telefone[:2]}) *****-{telefone[-4:]}"

def mascarar_email(email):
    partes = email.split("@")
    return partes[0][0] + "***@" + partes[1]

# Formulário de dados
with st.form("formulario_dados_basicos"):
    st.subheader("📑 Dados Pessoais")

    nome = st.text_input("Nome completo")
    cpf = st.text_input("CPF (somente números)")
    data_nascimento = st.date_input("Data de nascimento")
    email = st.text_input("E-mail")
    telefone = st.text_input("Telefone (com DDD)")

    st.subheader("📍 Endereço")
    cep = st.text_input("CEP (somente números)")
    endereco = ""
    bairro = ""
    cidade = ""
    estado = ""

    if cep and len(cep) == 8:
        endereco_info = buscar_endereco(cep)
        if endereco_info:
            endereco = endereco_info['logradouro']
            bairro = endereco_info['bairro']
            cidade = endereco_info['localidade']
            estado = endereco_info['uf']
            st.success(f"Endereço encontrado: {endereco}, {bairro}, {cidade}-{estado}")
        else:
            st.error("❌ CEP inválido ou não encontrado.")

    st.subheader("🎮 Interesses e Atividades")

    interesses = st.multiselect(
        "Quais temas te interessam mais?",
        ["CS:GO", "Valorant", "League of Legends", "Fortnite", "E-sports em geral", "Moda gamer", "Streaming", "Outros"]
    )

    eventos_participados = st.text_area(
        "Conte se participou de algum evento, campeonato ou encontro relacionado a e-sports no último ano:"
    )

    compras_realizadas = st.multiselect(
        "Você comprou algum produto relacionado à FURIA ou e-sports no último ano?",
        ["Camisa oficial", "Boné", "Mousepad", "Item digital", "Não comprei nada"]
    )

    jogo_favorito = st.selectbox(
        "🎮 Qual seu jogo favorito atualmente?",
        ["CS:GO", "Valorant", "League of Legends", "Fortnite", "PUBG", "Outro"]
    )

    enviado = st.form_submit_button("Enviar informações")

    if enviado:
        if not re.fullmatch(r'\d{11}', cpf):
            st.error("❌ CPF inválido. Digite apenas os números.")
        elif not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            st.error("❌ E-mail inválido. Confira o formato.")
        elif not re.fullmatch(r'\d{10,11}', telefone):
            st.error("❌ Telefone inválido. Deve conter DDD + número.")
        elif len(cep) != 8 or not endereco_info:
            st.error("❌ CEP inválido. Digite corretamente.")
        else:
            st.success("✅ Informações enviadas com sucesso! Avance para o próximo passo.")

# Upload de Documento
st.subheader("🖼️ Upload de Documento")

documento = st.file_uploader("Envie uma foto do seu documento (RG, CNH, CPF)", type=["jpg", "jpeg", "png"])

if documento:
    st.image(documento, width=300, caption="📄 Documento enviado")
    with st.spinner('🤖 Analisando documento com Inteligência Artificial...'):
        time.sleep(3)  # Simula o tempo de análise
    st.success("✅ Documento analisado!")

    # Simulação de IA extraindo dados
    st.info("🔍 Detecção automática:")
    st.write("**Nome detectado:** Hugo Farranha")
    st.write("**CPF detectado:** 123.456.789-00")
    st.success("🎯 Documento validado com sucesso!")
else:
    st.warning("⚠️ Faça o upload do seu documento para prosseguir.")

# Redes sociais
st.subheader("🌐 Vincular Redes Sociais")

instagram = st.text_input("🔗 Instagram (ex: https://www.instagram.com/seuperfil)")
twitter = st.text_input("🔗 Twitter (ex: https://twitter.com/seuperfil)")
steam = st.text_input("🔗 Steam (ex: https://steamcommunity.com/id/seuperfil)")
hltv = st.text_input("🔗 HLTV Profile (ex: https://www.hltv.org/player/)")

if st.button("Validar Redes Sociais"):
    redes_validas = True

    if instagram and not instagram.startswith("https://www.instagram.com"):
        st.error("❌ Link de Instagram inválido.")
        redes_validas = False
    if twitter and not twitter.startswith("https://twitter.com"):
        st.error("❌ Link de Twitter inválido.")
        redes_validas = False
    if steam and not steam.startswith("https://steamcommunity.com"):
        st.error("❌ Link de Steam inválido.")
        redes_validas = False
    if hltv and not hltv.startswith("https://www.hltv.org/player/") and hltv != "":
        st.error("❌ Link de HLTV inválido.")
        redes_validas = False

    if redes_validas:
        with st.spinner("🤖 Analisando perfis sociais com Inteligência Artificial..."):
            time.sleep(2)  # Simula análise de IA
        
        st.success("✅ Todas as redes sociais foram vinculadas corretamente!")

        if steam:
            st.info("🎮 Steam: Perfil relevante detectado - associado a grupos de e-sports!")
        if hltv:
            st.info("🔗 HLTV: Perfil relevante detectado - acompanha times de CS:GO!")

        st.markdown("### 🧠 Análise de Interações Sociais")

if instagram:
    st.success("📸 Detectado: Seguidor da FURIA no Instagram e interação em publicações recentes!")
if twitter:
    st.success("🐦 Detectado: Curtidas e RTs em tweets sobre e-sports!")
if steam:
    st.success("🎮 Detectado: Pertencente a grupos de e-sports na Steam!")
if hltv:
    st.success("🔗 Detectado: Perfil ativo no HLTV, seguindo campeonatos de CS:GO!")


# Cálculo do Progresso
progresso = 0
if nome:
    progresso += 20
if endereco:
    progresso += 20
if documento:
    progresso += 20
if instagram or twitter or steam or hltv:
    progresso += 20
if st.session_state.get("finalizado", False):
    progresso += 20

# Barra de Progresso
st.subheader("🚀 Progresso do Cadastro:")
st.progress(progresso)

if progresso < 40:
    st.info("🚶‍♂️ Status: Recruta FURIOSO (Continue preenchendo!)")
elif progresso < 80:
    st.info("🏃‍♂️ Status: Fã Leal (Falta pouco!)")
elif progresso < 100:
    st.info("🔥 Status: Quase lá! Complete seu cadastro!")
else:
    st.success("🏆 Status: Torcedor Oficial FURIA! Obrigado! 🦁🔥")

# Termo de Consentimento
aceita_termos = st.checkbox("✅ Eu li e aceito os Termos de Uso e a Política de Privacidade da FURIA.")

# Resumo do Cadastro
st.subheader("📋 Resumo do Seu Perfil de Fã")

if st.button("Finalizar Cadastro e Ver Resumo"):
    if not aceita_termos:
        st.error("❌ Você precisa aceitar os Termos de Uso para finalizar o cadastro.")
    else:
        st.session_state["finalizado"] = True

        with st.container():
            st.markdown("### 👤 Dados Pessoais")
            st.write(f"**Nome:** {nome}")
            st.write(f"**CPF:** {mascarar_cpf(cpf)}")
            st.write(f"**Data de Nascimento:** {data_nascimento.strftime('%d/%m/%Y')}")
            st.write(f"**E-mail:** {mascarar_email(email)}")
            st.write(f"**Telefone:** {mascarar_telefone(telefone)}")

            st.markdown("---")

            st.markdown("### 🏡 Endereço")
            if endereco:
                st.write(f"**Rua:** {endereco}")
                st.write(f"**Bairro:** {bairro}")
                st.write(f"**Cidade:** {cidade}")
                st.write(f"**Estado:** {estado}")
            else:
                st.warning("⚠️ Endereço não preenchido.")

            st.markdown("---")

            st.markdown("### 🎮 Interesses e Atividades")
            if interesses:
                st.write(f"**Interesses:** {', '.join(interesses)}")
            if eventos_participados:
                st.write(f"**Eventos participados:** {eventos_participados}")
            if compras_realizadas:
                st.write(f"**Compras realizadas:** {', '.join(compras_realizadas)}")
            if jogo_favorito:
                st.write(f"**Jogo favorito:** {jogo_favorito}")

            st.markdown("---")

            st.markdown("### 📎 Documento Enviado e Validado")
            if documento:
                st.image(documento, width=300, caption="📄 Documento enviado")
                st.success("✅ Documento analisado e validado com Inteligência Artificial!")
            else:
                st.warning("⚠️ Documento não enviado.")

            st.markdown("---")

            st.markdown("### 🌐 Redes Sociais Vinculadas")
            if instagram:
                st.write(f"🔗 [Instagram]({instagram})")
            if twitter:
                st.write(f"🔗 [Twitter]({twitter})")
            if steam:
                st.write(f"🔗 [Steam]({steam})")
            if hltv:
                st.write(f"🔗 [HLTV Profile]({hltv})")

            st.markdown("---")

            st.markdown("### 🧠 Análise de Interações Sociais")
            if instagram:
                st.success("📸 Detectado: Seguidor da FURIA no Instagram e interação em publicações recentes!")
            if twitter:
                st.success("🐦 Detectado: Curtidas e RTs em tweets sobre e-sports!")
            if steam:
                st.success("🎮 Detectado: Participação em grupos de e-sports na Steam!")
            if hltv:
                st.success("🔗 Detectado: Perfil ativo no HLTV acompanhando campeonatos de CS:GO!")

            st.success("✅ Cadastro concluído com sucesso! Obrigado por fazer parte da FURIA! 🦁🔥")
