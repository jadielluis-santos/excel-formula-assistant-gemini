# Excel Formula Assistant (V5.0 - Gemini AI)

## Aplicação de IA Generativa para Solução de Fórmulas em Planilhas

**Projeto em Produção:** [**Acesse e Teste a IA Aqui**](https://excel-formula-assistant-gemini-e6e2gzzeber3k6uhwmucvz.streamlit.app/)

Este projeto é um **Assistente de Fórmulas de Excel e Google Sheets** construído 100% em Python, utilizando a IA Generativa do Google Gemini.

Ele resolve um problema comum no ambiente de BI e Análise de Dados: a dificuldade em lembrar ou construir fórmulas complexas (como `PROCX`, `MÉDIA.SE`, ou `UNIRTEXTO`) em tempo real. O usuário apenas insere a intenção em linguagem natural (Português), e a IA retorna a fórmula mais moderna e uma descrição detalhada.

### Destaques Técnicos e Conquistas

* **IA Generativa (Gemini API):** O "cérebro" do assistente, responsável por interpretar a intenção do usuário e gerar a fórmula mais moderna e eficiente.
* **Prompt Engineering:** Implementação de técnicas para forçar a saída do Gemini em um formato estruturado (JSON), garantindo confiabilidade no retorno da fórmula.
* **Pipeline Completo (End-to-End):** O projeto foi desenvolvido, depurado e lançado em produção, cobrindo o ciclo completo de desenvolvimento de software (Python, Streamlit, Deploy em Cloud).

### Tecnologias Utilizadas

| Categoria | Tecnologia | Uso |
| :--- | :--- | :--- |
| **IA Generativa** | Google Gemini | Geração de fórmulas e descrições. |
| **Linguagem** | Python 3.11+ | Backend e lógica de integração. |
| **Web Framework** | Streamlit | Interface de usuário interativa e *low-code*. |
| **Hosting** | Streamlit Cloud | Plataforma de lançamento e produção. |

### Exemplos de Interação com a IA

| Pedido do Usuário | Resultado Esperado da IA |
| :--- | :--- |
| "Quero buscar um valor em outra planilha." | `=PROCX(valor; Planilha2!A:A; Planilha2!B:B; ...)` |
| "Preciso somar valores, mas apenas para a região Sul." | `=SOMASE(Região:Região; "Sul"; Vendas:Vendas)` |
| "Qual a fórmula para juntar o nome e sobrenome?" | `=CONCAT(Nome; " "; Sobrenome)` |

***




