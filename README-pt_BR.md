Sobre o Mock Coverter
=====================
Este é um software livre e open source distribuído em dois idiomas, **pt_BR**
e **en_US**. Você pode baixar a sua versão executável (apenas para win64) ao clicar [aqui](https://github.com/ViniciusFM/MockConverter/releases/tag/v2.0a), ou você pode seguir os passos descritos na seção **Script de Execução Padrão**.

A intenção deste software é converter uma base de dados no **formato JSON** em um **padrão qualquer** desejado facilmente. Você pode, por exemplo, usar um dataset que contenha objetos JSON assim:

```json
[...,
{
    "id": 1,
    "product_name": "Chocolate Pizza",
    "price": 13.89
},
...]
```

Para a linguagem java assim:
```java
...
p = new Product(1, "Chocolate Pizza", 13.89f);
...
```

Então, para que se tenha uma saída como acima você deve fornecer um padrão para o programa. Este padrão seria assim:

~~~
p = new Product(#id#, "#product_name#", #price#f);
~~~

Converta uma base em três passos
---------------------------------

1) Clique em "Abra um Arquivo" e selecione o arquivo no formato JSON.
2) Digite um padrão ao qual você deseja converter e, em tempo real, você verá sua conversão acontecer para o primeiro objeto JSON do dataset como um modelo de saída. 
3) Converta! Escolha um caminho e um arquivo + extensão e salve a sua conversão!

* Mole que nem pudim!

Script de Execução Padrão
--------------------------
--------------------------

Siga estes passos se você quer executar este software como um script python.

1) Primeiro você precisa baixar a versão 3 do python para a plataforma em que deseja executar e depois atualizar o pip3.
2) Depois você precisa baixar o **virtualenv**, se não estiver instalado ainda.
~~~
pip3 install virtualenv
~~~
3) Crie um ambiente virtual dentro do diretório do repositório de código:
~~~
python3 -m virtualenv .env
~~~
4) Entre em seu novo ambiente virtual:
~~~
windows powershell:
> .env\Scripts\activate

linux terminal:
$ source .env/bin/activate
~~~
5) Baixe as bibliotecas necessárias para executar o Mock Converter:
~~~
pip3 install -r requirements.txt
~~~
6) Depois é só executar o programa:
~~~
python3 main.py
~~~