import abacusai
import requests

# Abacus.ai API anahtarınızı buraya ekleyin
API_KEY = '8e6e9655c8ad450986ed0105d6c10ffa'

def get_response(user_input):
    # Abacus.ai API'sini kullanarak kullanıcı girdisine yanıt alın
    client = abacusai.PredictionClient()
    response = client.get_chat_response(
        deployment_token=API_KEY,
        deployment_id='15e3f4d62c',
        messages=[{"is_user": True, "text": user_input}],
        llm_name=None,
        num_completion_tokens=None,
        system_message=None,
        temperature=0.0,
        filter_key_values=None,
        search_score_cutoff=None,
        chat_config=None
    )
    return response

def main():
    print("Welcome to the Movement Chatbot!")
    while True:
        user_input = input("Question: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        response = get_response(user_input)
        print(f"Answer: {response}")

if __name__ == "__main__":
    main()
