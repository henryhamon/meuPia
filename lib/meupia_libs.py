# lib/meupia_libs.py
import sys

# --- Wrappers ML ---
def ia_treinar(x, y):
    print(f"[IA] Treinando com {x} e {y}...")
    # Código scikit-learn real aqui

# --- Wrappers KSP ---
def ksp_conectar():
    print("[KSP] Conectando ao KSP...")

def ksp_altitude():
    return 1000 # Mock