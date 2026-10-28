from flask import Flask
app = Flask(__name__)

@app.route('/')
def inicio();
    print('Acesso a pagina inicial', flush=True)
    mensagem = os.getenv('MENSAGEM', 'Ola, FASF!')
    return f' <h1>{mensagem}</h1><p>Aula de PaaS</p>'

@app.rout('/sobre')
def sobre();
    return 'Computacao em Nuvem - FASF'
