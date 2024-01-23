#Importar el paquete instalado
import matplotlib.pyplot as plt

#Funcion para generar los graficos de barra
def generate_bar_char(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png')
  plt.close()

#Funcion para generar grafico circular
def generate_pie_char(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('chart_pie_FINAL_espero.png')
  plt.close()
  
#Condicion para mostrar el codigo
if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 300]
  generate_pie_char(labels, values)
  #generate_bar_char(labels, values)
