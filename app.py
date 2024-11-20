from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Carregar os dados (substitua o caminho para o arquivo CSV correto)
def load_data():
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    df = pd.read_csv(url)
    
    # Filtrar os dados para o Brasil e apenas as colunas necessárias
    brazil_data = df[df['location'] == 'Brazil'][['date', 'new_cases', 'new_deaths']]
    
    # Remover as linhas com valores nulos
    brazil_data = brazil_data.dropna()
    
    # Converter a coluna 'date' para o formato correto
    brazil_data['date'] = pd.to_datetime(brazil_data['date']).dt.strftime('%Y-%m-%d')
    
    # Converter os dados para uma lista de dicionários
    return brazil_data.to_dict(orient='records')

@app.route('/')
def index():
    # Carregar os dados para o template
    table_data = load_data()
    print(table_data)  # Verifique os dados no console
    return render_template("index.html", table_data=table_data)

if __name__ == '__main__':
    app.run(debug=True)
