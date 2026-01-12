# yahoo-crawler

O projeto realiza a coleta de dados do site Yahoo Finances de uma região específica informada e salva os dados em CSV.

## Requisitos

Para o projeto ser executado é necessário ter:

- Python 3.11+
- Google Chrome

## Como executar

Primeiro acesse o repositório e crie um ambiente virtual:

```
$ python -m venv venv
```

Ative o ambiente virtual.

No Windows:

```
$ .\venv\Scripts\activate
```

No linux:

```
$ source venv/bin/activate
```

Instale as dependências:

```
$ pip install -r requirements.txt
```

Para executar o projeto rode o seguinte comando, informando a região desejada como parâmetro:

```
$ python main.py {region}
```

Exemplo:

```
$ python main.py China
```

Após isso será criado um arquivo equities.py contendo os dados coletados.

## Executar testes

Para executar os testes é necessário executar o seguinte comando:

```
$ python -m pytest
```