from flask import Flask
from flask import render_template

# Que es: Intancia de la clase Flask (objeto)
# __name__: Guarda la ejecución del script en el entorno local
app = Flask(__name__)

@app.route('/')
def index():
  return "<{h1Mi pamgina mprincipal</h1>"

@app.route('/user')
def user():
  name = "Profe de python"
  return f"<h1>Hola {name}</h1>"

@app.route('/template')
def template():

  data = {
    "name" : "Victor",
    "description" : "Esta loquito"
  }
  return render_template('index.html', data = data)



@app.route('/conditional')
def conditional():

  data = {
    "name" : "Victor",
    "description" : "Esta loquito",
    "is_premium": False
  }
  return render_template('conditional.html', data = data)


@app.route('/ciclofor')
def ciclofor():
  courses = ['C#','Python','Javascript','R']

  data = {
    "name" : "Victor",
    "description" : "Esta loquito",
    "is_premium": False,
    "courses" : courses
  }
  return render_template('ciclofor.html', data = data)







if __name__ == "__main__":
    app.run('localhost',port=8000,debug=True)
else:
    print("main.py:Este no es mi entrypoint")
