# app.py (Interface Web Streamlit)
import streamlit as st
from logic import gerar_formula
 # Importa a função do nosso outro arquivo

# --- Configuração da Página ---
st.set_page_config(
    page_title="Excel Formula Assistant - V1",
    layout="centered"
)

# --- Título e Instrução ---
st.title("🤖 Excel Formula Assistant (V1)")
st.markdown("""
Bem-vindo ao seu assistente de fórmulas! Nesta primeira versão, usamos regras simples para mapear sua intenção.
""")

# --- Campo de Entrada do Usuário ---
pedido_usuario = st.text_area(
    "Descreva a função do Excel que você precisa:",
    placeholder="Ex: 'Quero buscar um valor em uma lista usando PROCX' ou 'Como somar se a condição for atendida?'"
)

# --- Botão de Ação ---
if st.button("Gerar Fórmula"):
    if pedido_usuario:
        # Chamamos a função que está no formulas.py
        resultado = gerar_formula(pedido_usuario)
        
        # Lógica de exibição de resultado
        if "erro" in resultado:
            st.error(f"❌ {resultado['erro']}")
            st.info(f"💡 Sugestão: {resultado['sugestao']}")
        else:
            st.success("✅ Fórmula Recomendada Encontrada!")
            st.code(resultado["formula"], language="excel")
            st.subheader("Descrição:")
            st.write(resultado["descricao"])
            
    else:
        st.warning("⚠️ Por favor, digite o que você deseja fazer antes de clicar no botão.")
# Fim do arquivo app.py
