import requests
from bs4 import BeautifulSoup

# verifica se o usuario quer fazer uma nova pesquisa, e trata o erro de digitos.
def reiniciar():
  voltar = str(input("\nDeseja verificar novamente? S/N: ")).lower()
  if voltar == "s":
    menu_entrada_dados()
    return
  if voltar == "n":
    print("Programa fechado com sucesso!!")
    return
  else:
    try:
      print("Erro, Digitou algo errado, digite S para sim e N para não.")
      reiniciar()
    except:
      reiniciar()


# faz a busca dos dados, e organiza em uma lista, e é reponsavel por mostar o menu de numero + nome do pais
def menu_lista():
  # puxa as informações do site para a variavel
  url = "https://www.iban.com/currency-codes"
  r_iban = requests.get(url)
  # pega apenas o html
  html_iban = r_iban.text
  # organiza o html
  html_organizado = BeautifulSoup(html_iban,"html.parser")
  #pega um card da tag tbody
  tabela = html_organizado.find("tbody")
  linhas = tabela.find_all("tr")
  # joga todos os nomes das moedas da tag td dentro de uma lista
  lista_dict = []
  count = 0
  for linha in linhas:
    count += 1
    itens = linha.find_all("td")
    nome = itens[0].text
    currency_nome = itens[1].text
    moeda = itens[2].text
    
    lista = {
      "count" : count,
      "name_moeda" : nome,
      "currency" : currency_nome,
      "codigo_moeda" : moeda
    } 
    lista_dict.append(lista)
  
  
  return lista_dict


# recebe os dados do usuário, e faz a pesquisa na lista 
def menu_entrada_dados():
  lista = menu_lista()
  try:
    entrada_de_dados = int(input("#: "))
    if entrada_de_dados > len(lista):
      print("\nValor errado, digite apenas um números válido.")
      reiniciar()
    elif entrada_de_dados == 0:
      print("Programa fechado com sucesso!!")
      return
    else:
      lista = menu_lista()
      for i in lista:
        if i["count"] == entrada_de_dados:
          if i["currency"] == "No universal currency":
            print(f"\n{i['name_moeda']} não tem uma moeda para o país.")
            reiniciar()
          else:
            print(f"\nVocê escolheu o(a) {i['name_moeda']}")
            print(f"O código da moeda é {i['codigo_moeda']}")
            reiniciar()
        


  except:
    print("\nValor errado, digite apenas um números válido.")
    reiniciar()


# puxa os dados para printar tudo que é necessário na tela
def main():
  for i in menu_lista(): 
    print(f"# {i['count']} = {i['name_moeda']}")
    
  print("\nCaso queira sair do programa, digite um 0.")
  print("Informe qual pais você quer saber o código da moeda, informando o número: ")
  menu_entrada_dados()
  


main()
  
    


