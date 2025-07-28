# 📄 Resumo Automático de PDFs com OCR, Metadados e Divisão

Este projeto permite extrair conteúdo de arquivos PDF e gerar resumos automáticos utilizando inteligência artificial. O sistema também realiza OCR em páginas com imagens, extrai metadados, divide PDFs extensos e salva os resumos em um arquivo de texto.

## ✅ Funcionalidades

- 🧠 Resumo automático com IA (modelo BART da HuggingFace)
- 📰 Extração de texto de PDFs via `PyMuPDF`
- 🖼️ Reconhecimento óptico de caracteres (OCR) com `Tesseract`
- 🧾 Extração de metadados do PDF (autor, título, número de páginas, etc.)
- 📚 Divisão de PDFs grandes em blocos resumíveis
- 💾 Salva o resumo final no arquivo `resumo.txt`

---

## 🧰 Bibliotecas Utilizadas

| Biblioteca         | Função Principal                                |
|--------------------|--------------------------------------------------|
| `PyMuPDF` (`fitz`) | Leitura de PDFs, extração de texto e metadados  |
| `pdf2image`        | Conversão de páginas PDF para imagem (OCR)      |
| `pytesseract`      | Reconhecimento óptico de caracteres (OCR)       |
| `transformers`     | Geração de resumo com modelo BART               |
| `torch`            | Backend para uso dos modelos da HuggingFace     |
| `Pillow`           | Manipulação de imagens                          |

---

## 🔧 Instalação

1. Clone o repositório ou baixe os arquivos:

```bash
git clone https://github.com/seuusuario/pdf-resumo.git
cd pdf-resumo


2. (Opcional) Crie um ambiente virtual:
