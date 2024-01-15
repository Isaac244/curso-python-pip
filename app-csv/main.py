#Agregar el modulo creado
import utils
import read_csv
import chars

#Data de nuestros archivos
def run():
  data = read_csv.read_csv('data.csv')
  #Codigo para filtrar datos de sudamerica
  data = list(filter(lambda x: x['Continent'] == 'South America', data))

  #Crear grafico de barras de una columna
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  chars.generate_pie_char(countries, percentages)
  
  
  country = input('Agrega el nombre del pais => ')
  print(country)
  
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    chars.generate_bar_char(country['Country/Territory'], labels, values)

  print(result)
  
if __name__ == '__main__':
  run()