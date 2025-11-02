import re  # para trabajar con regex
import unicodedata  # para normalización de texto

# lista de palabras y términos comunes en inglés que se eliminarán del texto
stop_words = {
    "a",
    "about",
    "above",
    "after",
    "again",
    "against",
    "all",
    "am",
    "an",
    "and",
    "any",
    "are",
    "as",
    "at",
    "be",
    "because",
    "been",
    "before",
    "being",
    "below",
    "between",
    "both",
    "but",
    "by",
    "can",
    "could",
    "did",
    "do",
    "does",
    "doing",
    "down",
    "during",
    "each",
    "few",
    "for",
    "from",
    "further",
    "had",
    "has",
    "have",
    "having",
    "he",
    "her",
    "here",
    "hers",
    "herself",
    "him",
    "himself",
    "his",
    "how",
    "i",
    "if",
    "in",
    "into",
    "is",
    "it",
    "its",
    "itself",
    "just",
    "me",
    "more",
    "most",
    "my",
    "myself",
    "no",
    "nor",
    "not",
    "now",
    "of",
    "off",
    "on",
    "once",
    "only",
    "or",
    "other",
    "our",
    "ours",
    "ourselves",
    "out",
    "over",
    "own",
    "same",
    "she",
    "should",
    "so",
    "some",
    "such",
    "than",
    "that",
    "the",
    "their",
    "theirs",
    "them",
    "themselves",
    "then",
    "there",
    "these",
    "they",
    "this",
    "those",
    "through",
    "to",
    "too",
    "under",
    "until",
    "up",
    "very",
    "was",
    "we",
    "were",
    "what",
    "when",
    "where",
    "which",
    "while",
    "who",
    "whom",
    "why",
    "with",
    "would",
    "you",
    "your",
    "yours",
    "yourself",
    "yourselves",
}


# función para limpiar el texto
def clean_text(text):
    text = text.lower()  # convierte el texto a minúsculas

    text = (
        unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")
    )  # elimina los acentos

    text = re.sub(
        r"[^a-z\s]", " ", text
    )  # quita la puntuación, números y caracteres especiales

    text = re.sub(r"\s+", " ", text).strip()  # quita los espacios extra
    words = text.split()  # divide el texto en palabras individuales

    filtered = [w for w in words if w not in stop_words]  # elimina las palabras comunes

    return " ".join(filtered)  # vuelve a unir las palabras en un solo string


# se definen los archivos originales y los de salida
input_files = {
    "prideandprejudice.txt": "prideandprejudice_clean.txt",
    "senseandsensibility.txt": "senseandsensibility_clean.txt",
}

# se procesa cada archivo
for infile, outfile in input_files.items():
    with open(infile, "r", encoding="utf-8") as f:
        raw_text = f.read()

    cleaned = clean_text(raw_text)  # limpia el texto

    # se reduce el texto a las primeras 15,000 palabras para mejor análisis
    words = cleaned.split()
    reduced = " ".join(words[:15000])

    # se guarda el texto limpio y reducido en un nuevo archivo
    with open(outfile, "w", encoding="utf-8") as f:
        f.write(reduced)
