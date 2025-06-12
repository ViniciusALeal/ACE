from openai import OpenAI

def resposta_llm(pergunta):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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",
    )

    try:
        completion = client.chat.completions.create(
            model="google/gemini-2.5-pro-exp-03-25:free",
            messages=[{"role": "user", "content": pergunta}]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Erro ao gerar resposta: {e}"

