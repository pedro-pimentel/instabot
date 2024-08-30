## 📱 My Instagram Bot

Este projeto é um bot para Instagram desenvolvido em Python usando o framework Flask. O bot responde automaticamente às mensagens diretas dos usuários no Instagram, fornecendo informações sobre como realizar pedidos, horários de funcionamento e formas de pagamento.

### 🚀 Funcionalidades

- **Respostas Automáticas**: O bot responde automaticamente a mensagens diretas com base em palavras-chave ou opções numeradas fornecidas pelo usuário.
- **Inteligência de Entrada**: Reconhece diferentes variações de entrada do usuário, como números, palavras-chave e saudações comuns.
- **Fácil Integração**: Utiliza a API do Instagram Graph para enviar e receber mensagens diretas.
- **Implementação Serverless**: Ideal para deploy rápido no Heroku ou outras plataformas de hospedagem em nuvem.

### 📋 Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

- [Python 3.9+](https://www.python.org/)
- [Git](https://git-scm.com)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

### 🔧 Configuração do Projeto

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/my-instagram-bot.git
   cd my-instagram-bot
   ```

2. **Crie um ambiente virtual e ative-o**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Windows use: venv\Scripts\activate
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente**:

   Certifique-se de definir suas variáveis de ambiente `ACCESS_TOKEN` e `INSTAGRAM_USER_ID` no arquivo `app.py` ou configure-as no Heroku diretamente.

### 🚀 Como Executar o Projeto Localmente

Após configurar o ambiente, execute o comando abaixo para iniciar o servidor:

```bash
python app.py
```

O servidor estará em execução em `http://127.0.0.1:5000/`.

### ☁️ Deploy no Heroku

1. **Faça login no Heroku**:

   ```bash
   heroku login
   ```

2. **Crie um novo aplicativo no Heroku**:

   ```bash
   heroku create my-instagram-bot
   ```

3. **Faça o deploy para o Heroku**:

   ```bash
   git push heroku main
   ```

4. **Configure o Webhook no Facebook Developers**:

   Vá para o painel do Facebook Developers, configure um endpoint de webhook apontando para a URL do seu aplicativo Heroku (`https://my-instagram-bot.herokuapp.com/webhook`) e selecione o campo de mensagens para sua página.

### 📘 Estrutura do Projeto

```plaintext
my-instagram-bot/
│
├── app.py                # Código principal do bot em Flask
├── requirements.txt      # Lista de dependências do Python
├── Procfile              # Arquivo de configuração do Heroku para iniciar o app
├── runtime.txt           # (Opcional) Define a versão do Python usada no Heroku
├── .gitignore            # Arquivos e diretórios a serem ignorados pelo Git
└── README.md             # Documentação do projeto
```

### 🛠 Tecnologias Utilizadas

- **Python**: Linguagem de programação principal usada no projeto.
- **Flask**: Framework web utilizado para criar o servidor e as rotas da API.
- **Requests**: Biblioteca Python usada para fazer requisições HTTP para a API do Instagram Graph.
- **Heroku**: Plataforma de hospedagem em nuvem para deploy do bot.

### 🤝 Contribuindo

Contribuições são o que fazem a comunidade de código aberto ser um lugar incrível para aprender, inspirar e criar. Sinta-se à vontade para contribuir!

1. Faça um fork do projeto
2. Crie uma branch com a sua feature (`git checkout -b feature/sua-feature`)
3. Faça commit das suas alterações (`git commit -m 'Add some feature'`)
4. Dê push na sua branch (`git push origin feature/sua-feature`)
5. Abra um Pull Request

### 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.