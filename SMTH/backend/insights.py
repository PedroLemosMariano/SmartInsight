import openai
openai.api_key = "SUA_CHAVE_AQUI"

def gerar_insights(df):
    resumo = df.describe().to_string()
    prompt = (
        f"Analise os seguintes dados e produza insights claros:\n\n{resumo}\n\n"
        f"Escreva um resumo profissional sobre tendências e possíveis causas."
    )
    resposta = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=250
    )
    return resposta.choices[0].message["content"]
