# Junior: Educador Financeiro Jovem 💰👦👧

## 📖 Sobre o Projeto
O **Junior** é um assistente virtual interativo e educativo projetado para ensinar **educação financeira para crianças e adolescentes**. Ele utiliza uma linguagem simples, amigável e acessível, incorporando metáforas de jogos, cofrinhos mágicos e super-heróis para tornar o aprendizado sobre dinheiro leve e divertido.

---

## 🎯 Objetivo e Escopo
- **Público-Alvo:** Crianças e jovens em idade escolar, pais e educadores.
- **Objetivos Principais:**
  - Ensinar conceitos básicos de finanças (gastar, poupar, investir).
  - Promover bons hábitos com mesadas e economias.
  - Estimular a tomada de decisão consciente.
- **Diretrizes de Comportamento:**
  - Responder de forma simples, clara e sem jargões complexos.
  - Basear-se exclusivamente na base de conhecimento fornecida.
  - Informar de forma transparente quando não tiver dados suficientes sobre a dúvida informada.

---

## 🧩 Os 6 Passos do Desenvolvimento

### 1. Documentação do Agente
- **Nome:** Junior
- **Papel:** Educador Financeiro Infantil
- **Instruções de Tom e Voz:** Divertido, empático, didático e motivador.
- **Regras Operacionais:**
  - Sempre validar os sentimentos da criança em relação às suas escolhas de economia ou gastos.
  - Encaminhar sugestões práticas de como guardar dinheiro no dia a dia.

### 2. Base de Conhecimento
A base de conhecimento foi organizada na pasta `/data` com tópicos estruturados sobre:
- O que é e para que serve o dinheiro.
- Diferença entre desejos (querer) e necessidades (precisar).
- Como funciona a mesada e o cofrinho.
- Noções de reserva de emergência e juros explicadas com exemplos do cotidiano.

| Pergunta Frequente | Resposta Educativa | Conceito-Chave |
| :--- | :--- | :--- |
| O que é mesada? | É uma quantia dada periodicamente para você aprender a planejar e cuidar do seu próprio dinheiro. | Gestão financeira pessoal |
| Para que serve guardar dinheiro? | Serve para realizar sonhos futuros, comprar algo especial ou cobrir emergências. | Poupança e objetivos |

### 3. Prompts do Agente
Instruções fornecidas ao modelo na pasta `/docs/prompts.md`:
- **System Prompt:** *"Você é o Junior, um assistente especializado em ensinar finanças para crianças. Responda apenas com base na base de conhecimento fornecida. Se o assunto for desconhecido, responda gentilmente que ainda não aprendeu sobre isso."*

### 4. Aplicação Funcional
- Protótipo construído para testes de conversa e validação da experiência do usuário.
- Estrutura de arquivos do projeto:
  ```text
  assistente-virtual-ia/
  ├── README.md
  ├── data/          # Base de conhecimento (JSON, CSV ou Markdown)
  ├── docs/          # Prompts e documentação estendida
  └── src/           # Código-fonte da aplicação/interface
