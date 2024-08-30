from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
INSTAGRAM_USER_ID = 'YOUR_INSTAGRAM_USER_ID'

def send_message(to_user_id, message_text):
    url = f"https://graph.facebook.com/v17.0/{INSTAGRAM_USER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    data = {
        "recipient": {"id": to_user_id},
        "message": {"text": message_text}
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()

def process_user_message(message_text):
    # Normalizar texto do usuário: remover espaços e converter para minúsculas
    message_text = message_text.strip().lower()

    # Respostas baseadas em palavras-chave
    if message_text in ["1", "realizar pedido", "pedido", "pedidos"]:
        return "Para realizar pedidos, por favor visite nosso site: https://xbom.net.br/. Você pode escolher entre retirada no balcão ou delivery."
    elif message_text in ["2", "horário", "horários", "funcionamento"]:
        return "Nosso horário de funcionamento é de segunda a domingo, das 18:30 às 22:30."
    elif message_text in ["3", "pagamento", "pagamentos", "formas de pagamento"]:
        return "Aceitamos as seguintes formas de pagamento: Pix, débito ou crédito."
    elif message_text in ["oi", "olá", "bom dia", "boa tarde", "boa noite"]:
        return "Olá! Como posso ajudar você hoje? Por favor, escolha uma das opções abaixo:\n1 - Realizar pedidos\n2 - Horários de funcionamento\n3 - Formas de pagamento"
    else:
        # Resposta padrão para entradas não reconhecidas
        return ("Desculpe, não entendi sua mensagem. Por favor, escolha uma das opções abaixo digitando o número ou a palavra correspondente:\n"
                "1 - Realizar pedidos\n"
                "2 - Horários de funcionamento\n"
                "3 - Formas de pagamento")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    for entry in data['entry']:
        for message in entry['messaging']:
            if 'message' in message:
                sender_id = message['sender']['id']
                text = message['message'].get('text')

                if text:
                    response_text = process_user_message(text)
                    response = send_message(sender_id, response_text)
                    print(response)

    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))