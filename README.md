About Mock Converter
===================
This is a free and open source software distributed in two languages, [**pt_BR**](https://github.com/ViniciusFM/MockConverter/blob/master/README-pt_BR.md) and [**en_US**](https://github.com/ViniciusFM/MockConverter/blob/master/README.md). You can download its executable version (for win64 only) by clicking [here](https://github.com/ViniciusFM/MockConverter/releases/tag/v2.0a), or you can follow the steps described in **Default Script Execution** section.

It's intention is to convert **JSON datasets** into your desired **pattern** easily. You can, for example, use a dataset that contains JSON objects like this:

```json
[...,
{
    "id": 1,
    "product_name": "Chocolate Pizza",
    "price": 13.89
},
...]
```

To, for example, a java language code like this:
```java
...
p = new Product(1, "Chocolate Pizza", 13.89f);
...
```

So, for an output like above you need to provide a pattern. And this pattern would be like:

~~~
p = new Product(#id#, "#product_name#", #price#f);
~~~

Convert something in three steps!
---------------------------------

1) Click "Choose a File" and select a JSON formatted file.
2) Type a pattern you want to convert and, in real-time, you'll see its conversion applied to the first JSON object as a model.
3) Convert! Choose a path and file + extension name and save your conversion! 

* Easy Peasy Lemon Squeezy!

Default Script Execution
------------------------
------------------------

Follow this steps if you want to execute this software as a python script.

1) You will need to download a python 3 version for your desired platform first and update your pip3.
2) Then you'll need to download **virtualenv**, if you already haven't do this.
~~~
pip3 install virtualenv
~~~
3) Create a virtual environment inside this code repository directory:
~~~
python3 -m virtualenv .env
~~~
4) Then enter your new environment:
~~~
windows powershell:
> .env\Scripts\activate

linux terminal:
$ source .env/bin/activate
~~~
5) And download the required libs to execute Mock Converter:
~~~
pip3 install -r requirements.txt
~~~
6) Then you're ready to execute:
~~~
python3 main.py
~~~
