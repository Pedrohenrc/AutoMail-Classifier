# app/infrastructure/ai/prompts/gemini_prompts.py

PRODUCTIVE_RESPONSE_PROMPT = """
        Você recebeu um email PRODUTIVO de um cliente de uma instituição financeira.

        Tarefa:
        Escreva uma resposta profissional confirmando o recebimento do email e informando que a solicitação será analisada pela área responsável.

        Diretrizes:
        - Tom profissional, cordial e natural
        - Demonstre que compreendeu o assunto do email
        - Faça referência direta ao tema mencionado pelo cliente
        - Informe encaminhamento ou análise interna
        - Cite prazo apenas se fizer sentido, sem promessas rígidas
        - Seja conciso (até 3 parágrafos curtos)

        Restrições:
        - Não prometa soluções ou ações específicas
        - Não use linguagem excessivamente institucional
        - Não use listas, markdown ou emojis
        - Gere apenas o texto final da resposta

        # EXEMPLO DE BOA RESPOSTA
            Email cliente: "Não consigo acessar minha conta"
            Resposta: "Prezado(a), obrigado por entrar em contato. Recebemos sua solicitação referente ao problema de acesso à sua conta e entendemos a urgência da situação. Nossa equipe técnica já foi acionada e está analisando o caso. Você deve receber um retorno com a solução em até 24 horas úteis. Caso precise de assistência imediata, Estamos à disposição."

        Email recebido:
        "{email_content}"

        Resposta:"""

UNPRODUCTIVE_RESPONSE_PROMPT = """"
            Você recebeu um email IMPRODUTIVO que não exige ação da equipe.

            Seu papel:
            Responder de forma breve, educada e profissional, encerrando a interação sem criar expectativa de retorno.

            Diretrizes:
            - Resposta curta e cordial
            - Linguagem natural e adequada ao setor financeiro
            - Encerrar a interação educadamente

            Restrições:
            - Não mencionar análise, equipe ou prazos
            - Não criar expectativa de contato futuro
            - Gerar apenas o texto final

            Exemplos:

            Email: "Feliz Natal! Desejo sucesso a todos."
            Resposta: "Obrigado pelas mensagens e votos. Desejamos também ótimas festas."

            Email: "PROMOÇÃO IMPERDÍVEL! CLIQUE AQUI!"
            Resposta: "Agradecemos o contato. Atenciosamente."

            Agora gere a resposta para o email abaixo:

            Email:
            "{email_content}"

            Resposta:
            """
