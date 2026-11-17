# O que é:
É um pequeno projeto que fiz para ter um primeiro contato com APIs e para praticar minha POO. Ele usa a API Open-Meteo e consegue dar uma previsão do clima médio de um certo dia em Recife/Pernambuco.

## Como rodar:
Para rodar basta rodar clonar o código na sua máquina, instalar a biblioteca 'requests' e rodar o arquivo main.py:

```
pip install requests
git clone https://github.com/Davi-Rafael/projeto-agenda.git
python main.py
```

## Métodos da agenda:
Existem os seguintes métodos na agenda: adicionar_evento, remover_evento, relatorio_dia, detalhe_evento, mostrar_calendario.

## O que cada método faz:
### 1. adicionar_evento: segue o padrão a seguir, no qual 'evento' e 'dia' são strings:

``` python
self.adicionar_evento(evento, dia)
```
#### Ele adiciona um evento no seu calendário, a não ser que já exista um evento com mesmo nome no mesmo dia.

### 2. remover_evento: segue o padrão a seguir, no qual 'evento' e 'dia' são strings:

``` python
self.remover_evento(evento, dia)
```
#### Ele remove um evento que ocorreria naquele dia, a não ser que não exista o evento, ou ele não exista naquele dia específico.

### 3. relatorio_dia: segue o padrão a seguir, no qual 'dia' é uma string:

``` python
self.relatorio_dia(dia)
```
#### Printa uma lista com os eventos que ocorrem naquele dia. Se não houver eventos no dia, há um print explicitando isso. E também se conecta a API para dar o clima estimado em Recife naquele dia.

### 4.  dia_evento: segue o padrão a seguir, no qual 'evento' é uma string:

``` python
self.dia_evento(evento)
```
#### Printa uma lista com os dias que aquele evento ocorre. Se não houver dias com o evento, há um print explicitando isso. E também se conecta a API para dar o clima estimado em Recife nos dias dos eventos.

### 5.  mostrar_calendario: printa um relatório com todos os dias e eventos:

``` python
self.mostrar_calendario()
```
