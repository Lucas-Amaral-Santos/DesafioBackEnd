<h1>Executar Localmente</h1>

1)Executar ambiente: "source bin/activate"
IMPORTANTE: Meu ambiente está configurado em Linux. Talvez necessite adaptações
para outros sistemas operacionais.

2)Entrar no diretório "desafiobackend" onde está localizado o arquivo manage.py e
executar ./manage.py runserver

<h1>Executar em heroku</h1>
Criado um heroku app (link):
https://salty-brushlands-45215.herokuapp.com/

(AINDA DEBUGANDO ERRO:
Is the server running on host "127.0.0.1" and accepting TCP/IP connections on 
port 5432?
)


<h1>Sobre o APP</h1>
<h2>USUÁRIO ADMINISTRADOR:</h2>
Login: admin
Senha: admin123

<h2>USUÁRIO</h2>
Usuário não-logado terá, a direita do navbar, as opções REGISTRO e LOGIN que o 
permitirá fazer o seu registro e depois logar-se.

O usuário logado terá apenas a opção LOGIN.

<h2>OS PRODUTOS</h2>
Apenas o admin pode cadastrar produtos pela página do administrado do django.
Após cadastrar o produto pode-se adicionar uma foto pela classe ProductImage.

<h2>OS PEDIDOS</h2>
Após os produtos cadastrados os usuários da sessão poderá adicionar ao carrinho
e em seguida poderá completar o pedido clicando "Realizar Pedidos".

IMPORTANTE: O Pedido apenas será realizado se o administrador aceitar.
Para tal deve ser mudado o status da classe Orders para "Finished" 
