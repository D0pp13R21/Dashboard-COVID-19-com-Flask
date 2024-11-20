
# Dashboard COVID-19 com Flask

Este projeto é uma aplicação web criada com Flask que exibe uma tabela com os casos e mortes diários de COVID-19 no Brasil. Ele utiliza dados do [Our World in Data](https://ourworldindata.org/) e apresenta informações atualizadas diretamente de um arquivo CSV.

---

## 🚀 **Tecnologias Utilizadas**
- Python
- Flask
- Pandas
- Bootstrap (para estilização)

---

## 📦 **Como Executar o Projeto**

### 1. Clone o repositório
```bash
git clone https://github.com/D0pp13R21/Dashboard-COVID-19-com-Flask
cd nome-do-repositorio
```

### 2. Instale as dependências
Certifique-se de ter o Python 3.8+ instalado. Em seguida, rode:
```bash
pip install -r requirements.txt
```

### 3. Execute a aplicação
```bash
python app.py
```

### 4. Acesse no navegador
Abra o navegador e acesse: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📊 **Funcionalidades**
- Exibe uma tabela com:
  - Data
  - Casos diários de COVID-19 no Brasil
  - Mortes diárias de COVID-19 no Brasil

---

## 🗂️ **Estrutura do Projeto**
```
/project-folder
  |-- app.py           # Backend Flask
  |-- templates/
      |-- index.html   # Template HTML
  |-- requirements.txt # Dependências do projeto
```

---

## 🌐 **Fontes dos Dados**
- [Our World in Data](https://ourworldindata.org/)

## 💡 **Estilização**
- A tabela foi estilizada com [Bootstrap 4](https://getbootstrap.com/).
