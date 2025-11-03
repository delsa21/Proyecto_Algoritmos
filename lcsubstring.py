# longest common substring (versión optimizada)
import time
from typing import Tuple, List

def longest_common_substring(s1: str, s2: str) -> Tuple[int, str]:
    """
    Encuentra el Substring Común Más Largo (LCSstr) entre dos cadenas.
    Optimizado para usar menos memoria.
    """
    n, m = len(s1), len(s2)
    prev = [0] * (m + 1)
    max_len = 0
    end_index_s1 = 0

    for i in range(1, n + 1):
        curr = [0] * (m + 1)
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1] + 1
                if curr[j] > max_len:
                    max_len = curr[j]
                    end_index_s1 = i
        prev = curr

    fragmento = s1[end_index_s1 - max_len : end_index_s1]
    return max_len, fragmento


def dividirBloques(texto: str, tamaño: int = 1000) -> List[str]:
    """
    Divide el texto en fragmentos de un tamaño específico.
    """
    return [texto[i : i + tamaño] for i in range(0, len(texto), tamaño)]


def main():

    # lee los textos ya limpios (asegúrate de cambiar los nombres si tus archivos se llaman distinto)
    try:
        with open("prideandprejudice_clean.txt", "r", encoding="utf-8") as f:
            texto1 = f.read()
        with open("senseandsensibility_clean.txt", "r", encoding="utf-8") as f:
            texto2 = f.read()
    except FileNotFoundError:
        print("Error: No se encontraron los archivos de texto limpio.")
        print("Asegúrate de que los archivos existan en la misma carpeta.")
        return

    # divide los textos en bloques (bloques más pequeños = más rápido)
    tamaño_bloque = 1000
    bloques1 = dividirBloques(texto1, tamaño=tamaño_bloque)
    bloques2 = dividirBloques(texto2, tamaño=tamaño_bloque)

    print(f"Textos divididos en bloques de {tamaño_bloque} caracteres.")
    print(f"Comparando bloque por bloque ({len(bloques1)} pares aprox)...")

    mejor_fragmento = ""
    mejor_longitud = 0
    inicio = time.time()

    # compara solo bloque i con bloque i (en lugar de todos contra todos)
    for i in range(min(len(bloques1), len(bloques2))):
        longitud, fragmento = longest_common_substring(bloques1[i], bloques2[i])
        if longitud > mejor_longitud:
            mejor_longitud = longitud
            mejor_fragmento = fragmento

    duracion = time.time() - inicio
    porcentaje = (
        (mejor_longitud / min(len(texto1), len(texto2))) * 100
        if min(len(texto1), len(texto2)) > 0
        else 0
    )

    # mostrar resultados
    print(f"Longitud del substring común más largo: {mejor_longitud}")
    print(f"Porcentaje de similitud: {porcentaje:.4f}%")
    print(f"Tiempo de ejecución: {duracion:.2f} s")
    print(
        f"Fragmento encontrado: {mejor_fragmento[:300]}"
        + ("..." if len(mejor_fragmento) > 300 else "")
    )
main()
