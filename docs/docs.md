# Documentação

## Pascoa
Classe para obter a data do domingo de páscoa para determinado ano, de acordo com o calendário gregoriano, utilizado pelo Brasil.

Algoritmo de Gauss é o utilizado, conforme a referência:

https://www.whydomath.org/Reading_Room_Material/ian_stewart/2000_03.html

## FeriadosBr

Classe que pode ser utilizada para retornar conjunto de feriados entre *ano_inicial* e *ano_final*, números inteiros 
passados em seu construtor ou através dos *setters* dos atributos.

Também pode-se verificar se determinado dia é útil ou não chamando o método *eh_dia_util*.

Não depende de API - considera as datas fixas de feriados e, para feriados derivados da páscoa de determinado ano, consulta a classe *Pascoa* acima.


