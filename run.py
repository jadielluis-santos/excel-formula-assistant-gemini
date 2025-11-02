# teste_logica.py - Para validar a lógica no Terminal
from logic import gerar_formula
# --- Lista de Testes de Intenção ---
TESTES = [
    "Quero procurar um nome em outra planilha.",
    "Preciso somar as vendas apenas para a região Sul.",
    "Qual a fórmula para contar quantas células não estão vazias?",
    "Como calcular a média de valores se um critério for atendido?",
    "Preciso de ajuda para buscar algo.",
    "Qual a fórmula para concatenar textos?"
]

def rodar_teste_terminal():
    """Roda todos os testes e imprime os resultados da nossa IA no console."""
    print("=" * 50)
    print("🤖 Excel Formula Assistant (V1) - Teste de Lógica")
    print("=" * 50)
    
    for i, pedido in enumerate(TESTES):
        print(f"\n[{i+1}/{len(TESTES)}] Pedido do Usuário: {pedido}")
        
        # Chama a função principal de inteligência (o cérebro)
        resultado = gerar_formula(pedido)
        
        if "erro" in resultado:
            print("❌ Resposta da IA: Não Encontrado")
            print(f"   Sugestão: {resultado['sugestao']}")
        else:
            print("✅ Resposta da IA: Encontrado!")
            print(f"   Fórmula: {resultado['formula']}")
            print(f"   Descrição: {resultado['descricao']}")
            
        print("-" * 20)

# ...
# Inicia a execução do teste
if __name__ == '__main__':
    rodar_teste_terminal()