from flask import Flask, render_template

# 1. Cria o aplicativo 
app = Flask(__name__)

# 2. Cria a Rota Principal (O endereço do site)
# A barra '/' significa a página inicial (Home)
@app.route('/')
def home():
    # Manda o garçom pegar o HTML que você criou e entregar na tela!
    return render_template('index.html')

# 3. Liga o servidor
if __name__ == '__main__':
    app.run(debug=True) # O debug=True atualiza o site sozinho se você mudar o código