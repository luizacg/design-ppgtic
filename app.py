from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Guia Visual · Instagram PPGTIC",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

HTML_FILE = Path(__file__).with_name("preview.html")

st.html("""
<style>
  .block-container { max-width: 100% !important; padding: 0 !important; }
  [data-testid="stHeader"] {
    height: 0 !important;
    min-height: 0 !important;
    background: transparent !important;
  }
  [data-testid="stToolbar"],
  [data-testid="stDecoration"],
  #MainMenu,
  footer { display: none !important; }
</style>
""")

if not HTML_FILE.is_file():
    st.error("Arquivo preview.html não encontrado. Coloque-o na mesma pasta que app.py.")
    st.stop()

st.html(HTML_FILE, width="stretch")
