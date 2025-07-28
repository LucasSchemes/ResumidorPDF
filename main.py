from pdf_resumidor import pdf_para_texto, resumir_texto, extrair_metadados

def main():
    pasta_pdf = input("Digite o caminho do arquivo PDF: ")
    print("Lendo metadados do PDF...")
    
    metadados = extrair_metadados(pasta_pdf)
    for chave, valor in metadados.items():
        print(f"{chave}: {valor}")

    print("\nProcessando o conteúdo do PDF...")
    texto = pdf_para_texto(pasta_pdf)

    if not texto.strip():
        print("Nenhum texto encontrado no PDF.")
        return

    print("Texto extraído com sucesso. Resumindo...")
    resumo = resumir_texto(texto)

    with open("resumo.txt", "w", encoding="utf-8") as f:
        f.write(resumo)

    print("Resumo salvo em resumo.txt")
