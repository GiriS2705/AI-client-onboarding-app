from openai import OpenAI
from secret_key import openapi_key 
# Initialize client (make sure OPENAI_API_KEY is set in env)
#client = OpenAI()
client = OpenAI(api_key=openapi_key)

def validate_document(text):
    """
    Validates extracted OCR text using OpenAI.
    Returns structured validation response.
    """

    prompt = f"""
    You are a document verification assistant.

    Analyze the following text and determine if it looks like a valid government ID
    such as a passport or driving license.

    Extract:
    - Full Name
    - ID Number
    - Expiry Date (if available)

    Also say clearly: VALID or INVALID.

    Text:
    {text}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You validate identity documents."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Validation failed: {str(e)}"