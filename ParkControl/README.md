# ParkControl

Sistema desktop de controle de estacionamento desenvolvido em Python, com interface gráfica moderna utilizando CustomTkinter e persistência de dados com SQLite.

O sistema permite gerenciar entradas e saídas de veículos, calcular automaticamente o tempo de permanência e controlar vagas disponíveis de forma estruturada.

--- 

## Funcionalidades 

- Registro de entrada de veículos (carro e moto)
- Registro de saída com cálculo automático do valor
- Controle de vagas disponíveis
- Painel administrativo para visualização dos dados
- Validação de placas (padrão antigo e Mercosul)
- Tratamento de erros e validações de entrada

--- 

## Banco de dados

O sistema utiliza SQLite, com tabelas separadas para carros e motos, contendo:

- ID da vaga
- Status de ocupação
- Tipo de vaga
- Modelo do veículo
- Placa (única)
- Horário de entrada

## Tecnologias utilizadas 

- **Python 3** 
- **CustomTkinter** (interface gráfica) 
- **Git/GitHub** (controle de versão) 
- **SQLite3** (Banco de Dados)
- **DB Browser for SQLite** (Recomendado para visualização dos dados)

--- 

## Como executar 

1. Clone este repositório: 
``` 
git clone https://github.com/LucSousa21/ParkControl.git 
cd ParkControl

``` 
2. Instale as dependências: 
``` 
pip install customtkinter 

``` 
3. Prepare o Banco de Dados (Importante!)
``` 
python banco/criar_banco.py

``` 
4. Execute a Aplicação 
``` 
python main.py 

``` 

--- 

## Autor

Lucas Carvalho 

🔗 [LinkedIn](https://www.linkedin.com/in/lucas-carvalho-9173a5204/) 
🔗 [GitHub](https://github.com/LucSousa21)