# logic.py (Cérebro Generativo com Gemini API)

import os
from google import genai
from google.genai.errors import APIError
import json # Adicionar json aqui para garantir

# Tenta carregar a chave de API do ambiente (segurança)
API_KEY = os.getenv("GEMINI_API_KEY")

try:
    if not API_KEY:
        # Se a chave não for encontrada, o cliente falhará.
        raise ValueError("GEMINI_API_KEY não configurada.")
        
    client = genai.Client(api_key=API_KEY)
    # Não vamos printar sucesso aqui para não sujar a saída do teste
except ValueError as e:
    # Se a chave não estiver na variável de ambiente, tratamos aqui
    client = None
    # print(f"❌ Erro de Configuração: {e}") # Descomentar para debug
except Exception as e:
    client = None
    # print(f"❌ Erro ao inicializar o cliente Gemini: {e}") # Descomentar para debug


def gerar_formula(pedido: str) -> dict:
    """
    Gera a fórmula de Excel correta usando a IA Generativa (Gemini).
    """
    if client is None:
        return {
            "erro": "API Gemini indisponível.",
            "sugestao": "Verifique se a variável GEMINI_API_KEY está configurada corretamente no terminal."
        }

    prompt_sistema = """
    Você é um assistente especialista em Microsoft Excel e Google Sheets.
    Sua única tarefa é receber um pedido em português e retornar A FÓRMULA DE PLANILHA MAIS ADEQUADA, junto com uma breve descrição.

    Regras de Resposta:
    1. A fórmula deve ser sempre a melhor e mais moderna (use PROCX em vez de PROCV, se aplicável).
    2. A resposta DEVE estar estritamente no formato JSON, sem NENHUM texto adicional antes ou depois.
    3. Use ponto-e-vírgula (;) como separador de argumentos, como é comum em versões do Excel em português.

    Exemplo de formato JSON de saída:
    {
      "formula": "=PROCX(valor_a_procurar; coluna_de_busca; coluna_de_retorno)",
      "descricao": "Procura o valor em uma coluna e retorna o correspondente em outra."
    }
    """

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[prompt_sistema, f"Pedido do Usuário: {pedido}"],
            config={"response_mime_type": "application/json"} 
        )
        
        # Analisa o JSON retornado pela IA
        resultado_json = json.loads(response.text)
        
        return {
            "formula": resultado_json.get("formula", "Fórmula não encontrada"),
            "descricao": resultado_json.get("descricao", "Descrição não encontrada"),
            "tipo": "Generative AI"
        }

    except APIError as e:
        return {"erro": f"Erro na API do Google: {e.message}", "sugestao": "Verifique sua chave de API e o limite de uso."}
    except json.JSONDecodeError:
        # Muitas vezes o modelo gera texto explicativo ANTES do JSON, o que quebra o parse
        return {"erro": f"A IA retornou JSON inválido ou texto extra. Raw Output: {response.text[:50]}...", "sugestao": "Tente refinar o prompt do sistema."}
    except Exception as e:
        return {"erro": f"Ocorreu um erro inesperado: {e}", "sugestao": "Verifique a conexão de rede."}


# Se você for rodar o teste de terminal, adicione esta linha no final do logic.py:
if __name__ == '__main__':
    from run import rodar_teste_terminal
    rodar_teste_terminal()