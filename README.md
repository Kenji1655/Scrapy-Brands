# Scrapy RankingTheBrands Scraper

Este projeto utiliza o Scrapy para acessar o site RankingTheBrands, navegando por todas as marcas de A a Z e armazenando os dados em um arquivo JSON.

## Requisitos

- Python 3.8+
- Scrapy instalado

Para instalar o Scrapy, execute:
```sh
pip install scrapy
```

## Como usar

1. Execute o scraper:
```sh
scrapy crawl brands -o marcas.json
```

## Saída

O scraper gera um arquivo `marcas.json` contendo todas as marcas extraídas do site.

## Estrutura do JSON

```json
[
  {
    "brand:" "Nome da empresa",
  },
  ...
]
```

