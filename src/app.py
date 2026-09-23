import json

# Simulação de carregamento da Base de Conhecimento
def carregar_base():
    with open("data/base_conhecimento.json", "r", encoding="utf-8") as f:
        return json.load(f)

# Simulação do comportamento do agente "Junior"
def responder_usuario(pergunta, base):
    pergunta_lc = pergunta.lower()
    
    # Busca por palavras-chave na base
    for topico in base.get("topicos", []):
        for palavra in topico.get("palavras_chave", []):
            if palavra in pergunta_lc:
                return f"🤖 Junior: {topico['conceito']}\n💡 Exemplo: {topico['exemplo_ludico']}"
    
    # Resposta padrão caso não encontre na base (evitar alucinação)
    return f"🤖 Junior: {base['regras_de_resposta']['fora_do_escopo']}"

if __name__ == "__main__":
    print("=== Assistente Virtual Junior Iniciado ===")
    base = carregar_base()
    
    # Exemplo de teste
    duvida = "Para que serve o cofrinho?"
    print(f"Usuário: {duvida}")
    print(responder_usuario(duvida, base))
