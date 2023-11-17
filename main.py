import PyPDF2
import csv
from tqdm import tqdm


def extrair_dados_pdf(pdf_file):
    final = []

    # Crie um objeto de leitura PDF
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Use tqdm para criar uma barra de progresso
    for page_num in tqdm(range(len(pdf_reader.pages)), desc="Extraindo dados do PDF"):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()

        # Remova os itens indesejados
        items_to_ignore = ["Observações", "Mobile", "Other", "E-mail", "Disp. móvel", "Celular", "OUTRO", "Home"]
        texto = [item for item in text.split('\n') if not any(ignore_item in item for ignore_item in items_to_ignore)]

        final.extend(texto)

    return final

def criar_arquivo_csv(dados, nome_arquivo):
    # Usando list comprehension para criar pares
    nova_lista = [dados[i:i+2] for i in range(0, len(dados), 2)]

    # Use tqdm para criar uma barra de progresso
    with tqdm(total=len(nova_lista), desc="Criando arquivo CSV") as pbar:
        # Escrever os dados no arquivo CSV
        with open(nome_arquivo, 'w', newline='\n', encoding='utf-8') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            for linha in nova_lista:
                escritor_csv.writerow(linha)
                pbar.update(1)  # Atualiza a barra de progresso

    print(f'O arquivo {nome_arquivo} foi criado com sucesso!')

def main():
    # Nome do arquivo PDF a ser processado
    nome_arquivo_pdf = 'contatos.pdf'

    # Nome do arquivo CSV a ser criado
    nome_arquivo_csv = 'dados.csv'

    # Extrair dados do PDF
    dados_extrair = extrair_dados_pdf(nome_arquivo_pdf)

    # Criar arquivo CSV
    criar_arquivo_csv(dados_extrair, nome_arquivo_csv)

if __name__ == "__main__":
    main()
