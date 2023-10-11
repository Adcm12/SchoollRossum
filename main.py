from flask import Flask, render_template, request, redirect
from pessoa import Pessoa

pessoa1 = Pessoa('Rodrigo', 32, 1.87)
pessoa2 = Pessoa('Marina', 29, 1.69)
pessoa3 = Pessoa('André', 26, 1.80)
pessoa4 = Pessoa('Carlos', 55, 1.75)
pessoa5 = Pessoa('Elaine', 48, 1.82)
pessoa5 = Pessoa('Adrian Castillo', 19, 1.75)

lista = [pessoa1, pessoa2, pessoa3, pessoa4, pessoa5 ]

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('lista.html', titulo = 'Lista de Alunos', pessoas = lista)

@app.route('/novo')
def cadastro():
    return render_template('novo.html', titulo = 'Cadastro de Alunos')

@app.route('/editar')
def editar():
    return render_template('editar.html', titulo = 'Editar Aluno')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form ['nome']
    idade = request.form['idade']
    altura = request.form['altura']

    pessoas = Pessoa(nome, idade, altura)
    
    lista.append(pessoas)
    return redirect('/')

app.run(debug=True)