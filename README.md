# O que é:
É um pequeno projeto que fiz para ter um primeiro contato com APIs e para praticar minha POO. Ele usa a API Open-Meteo e consegue dar uma previsão do clima médio de um certo dia em Recife/Pernambuco.

## Como rodar:
Para rodar basta rodar clonar o código na sua máquina, instalar a biblioteca 'requests' e rodar o arquivo main.py:

```
pip install requests
git clone https://github.com/Davi-Rafael/projeto-agenda.git
python main.py
```

## O que cada método faz:
1. adicionarEvento: segue o padrão a seguir, no qual 'evento' e 'dia' são strings:

``` python
self.adicionarEvento(evento, dia)
```
##### Ele adiciona um evento no seu calendário, a não ser que já exista um evento com mesmo nome no mesmo dia.

2. removerEvento: segue o padrão a seguir, no qual 'evento' e 'dia' são strings:

``` python
self.removerEvento(evento, dia)
```
##### Ele remove um evento que ocorreria naquele dia, a não ser que não exista o evento, ou ele não exista naquele dia específico.

3. relatorioDia: segue o padrão a seguir, no qual 'dia' é uma string:

``` python
self.relatorioDia(dia)
```
##### Printa uma lista com os eventos que ocorrem naquele dia. Se não houver eventos no dia, printa uma lista vazia. E também se conecta a API para dar o clima estimado em Recife naquele dia.

4.  diaEvento: segue o padrão a seguir, no qual 'evento' é uma string:

``` python
self.diaEvento(evento)
```
##### Printa uma lista com os dias que aquele evento ocorre. Se não houver dias com o evento, printa uma lista vazia.

5.  mostrarCalendario: printa um relatório com todos os dias e eventos:

``` python
self.mostrarCalendario()
```