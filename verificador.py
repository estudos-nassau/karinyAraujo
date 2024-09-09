import json

# Função para carregar o arquivo JSON a partir do caminho fornecido
def carregar_arquivo_json(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
        return dados
    except FileNotFoundError:
        # Se o arquivo não for encontrado, exibe uma mensagem de erro
        print(f"Erro: O arquivo {caminho_arquivo} não foi encontrado.")
        return None
    except json.JSONDecodeError:
        # Se ocorrer um erro ao decodificar o JSON, exibe uma mensagem de erro
        print("Erro: O arquivo não está em um formato JSON válido.")
        return None

# Função auxiliar para procurar a palavra em uma estrutura JSON
def procurar_palavra(dados, palavra):
    if isinstance(dados, dict):
        # Se o dado for um dicionário, verifica as chaves e valores
        for chave, valor in dados.items():
            if isinstance(valor, (dict, list)):
                if procurar_palavra(valor, palavra):
                    return True
            elif palavra.lower() in str(valor).lower():
                return True
    elif isinstance(dados, list):
        # Se o dado for uma lista, verifica todos os elementos
        for item in dados:
            if procurar_palavra(item, palavra):
                return True
    return False

# Função principal para verificar a existência de uma palavra no arquivo JSON
def palavra_existe_em_json(caminho_arquivo, palavra):
    dados = carregar_arquivo_json(caminho_arquivo)
    if dados is None:
        return False
    return procurar_palavra(dados, palavra)

# Especifica o caminho local do arquivo JSON
caminho_arquivo = "palavras.json"

# Lista de palavras para procurar
palavras = ["Python", "Dados", "Inteligência", "Artificial", "Go", "engineer", "Carro", "Moto"]

# Verifica se cada palavra existe no arquivo JSON e imprime o resultado
for palavra in palavras:
    existe = palavra_existe_em_json(caminho_arquivo, palavra)
    print(f"A palavra '{palavra}' existe no arquivo JSON? {existe}")
