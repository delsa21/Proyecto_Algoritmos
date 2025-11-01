import re
import unicodedata
import nltk
from nltk.corpus import stopwords

# Descargar lista de stopwords (solo la primera vez)
nltk.download('stopwords')

# --- FUNCIONES DE PREPROCESAMIENTO ---
def limpiar_y_normalizar(texto):
    """
    Convierte el texto a minúsculas, elimina acentos, caracteres especiales y espacios extra.
    """
    # Convertir a minúsculas
    texto = texto.lower()
    # Quitar acentos
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    # Eliminar caracteres especiales, números y signos
    texto = re.sub(r'[^a-zñáéíóúü\s]', ' ', texto)
    # Quitar espacios extra
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

def eliminar_stopwords(texto):
    """
    Elimina las palabras vacías (stopwords) del idioma español.
    """
    stop_words = set(stopwords.words('spanish'))
    palabras = texto.split()
    filtradas = [p for p in palabras if p not in stop_words]
    return ' '.join(filtradas)

def contar_palabras(texto):
    """
    Devuelve la cantidad de palabras de un texto.
    """
    return len(texto.split())

# --- LEER ARCHIVOS ---
with open("prideandprejudice.txt", "r", encoding="utf-8") as f:
    texto1 = f.read()
with open("senseandsensibility.txt", "r", encoding="utf-8") as f:
    texto2 = f.read()

# --- PREPROCESAMIENTO ---
print("🔧 Iniciando preprocesamiento de textos...")

# Limpieza y normalización
texto1 = limpiar_y_normalizar(texto1)
texto2 = limpiar_y_normalizar(texto2)

# Eliminación de stopwords
texto1 = eliminar_stopwords(texto1)
texto2 = eliminar_stopwords(texto2)

# --- GUARDAR RESULTADOS ---
with open("prideandprejudice_preprocesado.txt", "w", encoding="utf-8") as f:
    f.write(texto1)
with open("senseandsensibility_preprocesado.txt", "w", encoding="utf-8") as f:
    f.write(texto2)

# --- MOSTRAR RESULTADOS ---
print("\n✅ Archivos preprocesados guardados correctamente como:")
print("- prideandprejudice_preprocesado.txt")
print("- senseandsensibility_preprocesado.txt")

print("\n📊 Resultados del preprocesamiento:")
print(f"- Pride and Prejudice: {contar_palabras(texto1)} palabras finales")
print(f"- Sense and Sensibility: {contar_palabras(texto2)} palabras finales")
print("\n🚀 Preprocesamiento completado exitosamente.")
