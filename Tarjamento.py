import fitz  # PyMuPDF para manipulação de PDF
import re

def tarjar_cpf_em_pdf ('C:\Nome Camila Amaral de Paula Melo''\Nova pasta')
    """
    Identifica e tarja CPFs em um documento PDF.
    """
    # Expressão regular para CPF
    regex_cpf = re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}')

    doc = fitz.open()

    for page in doc:
        # Extrai o texto com as coordenadas
        text_instances = page.search_for(regex_cpf)

        # Adiciona uma anotação de tarja sobre cada CPF encontrado
        for inst in text_instances:
            highlight = page.add_redact_annot(inst, fill=(0, 0, 0))

        # Aplica as tarjas
        page.apply_redactions('C:\Nome Camila Amaral de Paula Melo')

    doc.save('C:\Nova pasta')
    doc.close()

# Exemplo de uso
# tarjar_cpf_em_pdf("documento_original.pdf", "documento_tarjado.pdf")