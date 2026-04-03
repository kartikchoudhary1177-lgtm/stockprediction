from google import genai
from django.conf import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)


def stock_chatbot(stock, question):

    prompt = f"""
    {stock['symbol']} P:{stock['price']} H:{stock['high']} L:{stock['low']} V:{stock['volume']}
Q:{question}
1 line: Good buy / Risky / Avoid + reason.

"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text