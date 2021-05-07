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

class Student:
  def __init__(self, name, description, courses):
    self.name = name
    self.description = description
    self.courses = courses

@app.route('/ciclofor')
def ciclofor():
  c1 = ['C#','Python','Javascript','R']
  c2 = ['Ruby','Python','Javascript','R']
  # data = {
  #   "name" : "Victor",
  #   "description" : "Esta loquito",
  #   "is_premium": False,
  #   "courses" : courses
  # }

  s1 = Student("Victor","Esta loquito", c1)
  s2 = Student("Susana","Esta loquita", c2)
  s3 = Student("Dudmit","Este si esta locote",c2)
  students = [s1,s2,s3]
  return render_template('ciclofor.html', students = students)






if __name__ == "__main__":
    app.run('localhost',port=8000,debug=True)
else:
    print("main.py:Este no es mi entrypoint")
