#Adriano Siqueira - 8/21/21 - Cotação de moedas com GUI

import requests;
import datetime;
from tkinter import *;


def cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL");

    requisicaoDic = requisicao.json();

    dolar = requisicaoDic['USDBRL']['bid'];
    euro = requisicaoDic['EURBRL']['bid'];
    btc = requisicaoDic['BTCBRL']['bid'];

    
    texto = f'''
    Dólar: {dolar}
    Euro: {euro}
    BTC: {btc}''';

    txtDolar ["text"] = "Dolar: " + dolar;
    txtEuro ["text"] = "Euro: " + euro;
    txtBtc ["text"] = "Bitcoin: " + btc;
    data["text"] = datetime.datetime.now();


app = Tk();

app.title("Cotaçoes");

txtTitulo = Label(app, text = "Cotação de moedas");
txtTitulo.grid(column=1, row=0);

txtInstrucao = Label(app, text = "Clique no botão para atualizar");
txtInstrucao.grid(column=1, row=1);

btn = Button(app, text = "Cotar", command = cotacoes);
btn.grid(column=1, row=2);

txtDolar = Label(app, text="");
txtDolar.grid(column=0, row=3);

txtEuro = Label(app, text="");
txtEuro.grid(column=1, row=3);

txtBtc = Label(app, text="");
txtBtc.grid(column=2, row=3);

data = Label(app, text="");
data.grid(column=1, row=5);

app.mainloop();