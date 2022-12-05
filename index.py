from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

class Despesas:
    def __init__(self, dic, cor, nome):
        self.cor = cor
        self.nome = nome
        self.dic = dic

class Grafico:  
  def __init__(self, despesas):
    self.despesas = despesas
    self.gerarGrafico()

  def gerarGrafico(self):   
    for despesa in self.despesas:
      x, y = zip(*despesa.dic.items())
      plt.plot(x, y, linewidth = 4, label = despesa.nome, marker = '.', markerfacecolor = 'black', markersize = 15, color = despesa.cor)
    plt.xlabel('Dia')
    plt.ylabel('Despesas em R$')
    plt.title('Gráficos de Despesas') 
    plt.legend()
    plt.show()

  def gerarRegressao(self):
    despesa = self.despesas[0]
    dias, valores = zip(*despesa.dic.items())
    dias = np.array(dias)
    dias = dias.reshape(-1, 1)
    valores = np.array(valores)
    valores = valores.reshape(-1, 1)
    plt.plot(dias, LinearRegression().fit(X = dias, y = valores).predict(dias), color = 'red', label = "Regressão Linear")
    x, y = zip(*despesa.dic.items())
    plt.plot(x, y, linewidth = 4, label = despesa.nome, marker='o', markerfacecolor='black', markersize = 15, color = despesa.cor )
    plt.legend()
    plt.show()

transporte = Despesas({1:10,2:34,3:45,4:87,5:150},'olive','transporte')
vestuário = Despesas({1:12,2:36,3:77,4:31,5:65},'red','vestuário')
alimentação = Despesas({1:66,2:56,3:250,4:320,5:132},'skyblue','alimentação')
despesas = [alimentação, vestuário, transporte]

grafico = Grafico(despesas)
grafico.gerarRegressao()