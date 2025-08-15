# Importando o Flask
from flask import Flask, render_template
# Importando o PyMySQL
import pymysql
# Importando as rotas que estão nos controllers
from controllers import routes
# Importando os models

# Carregando o Flask na variável app
app = Flask(__name__, template_folder='views')

# Chamando as rotas
routes.init_app(app)

app.run(host='localhost', port=5000, debug=True)