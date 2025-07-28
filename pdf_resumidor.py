import fitz  # PyMuPDF
import pytesseract
from pdf2image import convert_from_path
from transformers import pipeline

# Função para extrair texto de um PDF, usando OCR se necessário
def pdf_para_texto(pasta_pdf):
    documento = fitz.open(pasta_pdf)
    texto_total = ""

    for pagina in documento:
        texto = pagina.get_text()

        if texto.strip():
            texto_total += texto + "\n"
        else:
            imagens = convert_from_path(pasta_pdf, first_page=pagina.number + 1, last_page=pagina.number + 1)
            texto_ocr = pytesseract.image_to_string(imagens[0], lang='por')  # Altere 'por' para 'eng', 'spa' etc.
            texto_total += texto_ocr + "\n"
    
    return texto_total

# Função para dividir texto em blocos menores (para resumir grandes textos)
def dividir_texto(texto, tamanho_bloco=1000):
    blocos = [texto[i:i + tamanho_bloco] for i in range(0, len(texto), tamanho_bloco)]
    return blocos

# Função de resumo usando modelo do HuggingFace
def resumir_texto(texto):
    resumo_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")
    blocos = dividir_texto(texto)
    resumo_final = ""

    for bloco in blocos:
        resultado = resumo_pipeline(bloco, max_length=150, min_length=30, do_sample=False)
        resumo_final += resultado[0]['summary_text'] + "\n"

    return resumo_final

def extrair_metadados(caminho_pdf):
    documento = fitz.open(caminho_pdf)
    metadados = documento.metadata

    info = {
        "Título": metadados.get("title", "Não disponível"),
        "Autor": metadados.get("author", "Não disponível"),
        "Assunto": metadados.get("subject", "Não disponível"),
        "Palavras-chave": metadados.get("keywords", "Não disponível"),
        "Criador": metadados.get("creator", "Não disponível"),
        "Produtor": metadados.get("producer", "Não disponível"),
        "Data de Criação": metadados.get("creationDate", "Não disponível"),
        "Data de Modificação": metadados.get("modDate", "Não disponível"),
        "Número de Páginas": len(documento),
    }

    return info