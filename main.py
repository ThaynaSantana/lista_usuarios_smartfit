from flask import Flask, url_for, render_template
from datetime import datetime, timedelta

# inicializacao
app = Flask(__name__)

#funcoes

def atrasado(data_pagamento):
    data_pagamento = datetime.strptime(data_pagamento, '%Y-%m-%d')
    data_atual = datetime.now()
    dias_atraso = (data_atual - data_pagamento).days
    return dias_atraso > 30

#rotas
@app.route('/')
def ola_mundo():
    usuarios = [
        {"nome": "Guilherme", "id": 1, "idade": 35, "data_pagamento_mensalidade": "2023-11-05"},
        {"nome": "Thayna", "id": 2, "idade": 28, "data_pagamento_mensalidade": "2023-12-20"},
        {"nome": "Caio", "id": 3, "idade": 24, "data_pagamento_mensalidade": "2023-12-15"},
        {"nome": "Ana", "id": 4, "idade": 30, "data_pagamento_mensalidade": "2023-11-30"},
        {"nome": "Lucas", "id": 5, "idade": 22, "data_pagamento_mensalidade": "2023-12-10"},
        {"nome": "Juliana", "id": 6, "idade": 27, "data_pagamento_mensalidade": "2023-11-25"},
        {"nome": "Renato", "id": 7, "idade": 29, "data_pagamento_mensalidade": "2023-12-05"},
        {"nome": "Mariana", "id": 8, "idade": 31, "data_pagamento_mensalidade": "2023-11-15"},
        {"nome": "Pedro", "id": 9, "idade": 26, "data_pagamento_mensalidade": "2023-12-30"},
        {"nome": "Fernanda", "id": 10, "idade": 33, "data_pagamento_mensalidade": "2023-11-20"},
        {"nome": "Rafael", "id": 11, "idade": 25, "data_pagamento_mensalidade": "2023-12-25"},
        {"nome": "Carla", "id": 12, "idade": 28, "data_pagamento_mensalidade": "2023-11-10"},
        {"nome": "José", "id": 13, "idade": 32, "data_pagamento_mensalidade": "2023-12-18"},
        {"nome": "Beatriz", "id": 14, "idade": 23, "data_pagamento_mensalidade": "2023-11-28"},
        {"nome": "Vinícius", "id": 15, "idade": 27, "data_pagamento_mensalidade": "2023-12-22"},
    ]
     
    return render_template("index.html", usuarios=usuarios, atrasado=atrasado)

@app.route('/ficha')
def ficha():
    return render_template("ficha.html")

# execucao
app.run(debug=True)