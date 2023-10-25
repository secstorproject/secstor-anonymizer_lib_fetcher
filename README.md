# Anonymizer Lib Fetcher 🕵️‍♂️

Este projeto captura tempos de execução de diferentes técnicas de anonimização de dados aplicadas a um conjunto de dados escolhido, baseado no parâmetro de carga especificado, usando uma biblioteca secstor-anonymizer_lib.

## Introdução

 O projeto suporta três diferentes configurações de carga: 1, 2 e 3. Cada configuração de carga corresponde a um conjunto específico de técnicas de anonimização de dados. Estas configurações podem ser personalizadas.

## Exemplo de Resultado

Neste exemplo, utilizamos o conjunto de dados "1kB_100objects_dataset.json" e executamos o processo de anonimização de dados com diferentes parâmetros de execução.

Resultados dos Parâmetros de Execução 1:

| Propriedade              | Antes        | Depois      |
|--------------------------|--------------|-------------|
| k-anonymity              | 1.0          | 100.0       |
| l-diversity              | 1.0          | 8.0         |
| t-closeness (latitude)   | 4.907627     | 4.907627    |
| t-closeness (longitude)  | 13.131974    | 13.131974   |
| t-closeness (renda)      | 24024.258748 | 24024.258748|

Resultados dos Parâmetros de Execução 3:

| Propriedade              | Antes        | Depois      |
|--------------------------|--------------|-------------|
| k-anonymity              | 1.0          | 100.0       |
| l-diversity              | 1.0          | 8.0         |
| t-closeness (latitude)   | 4.907627     | 5.732671    |
| t-closeness (longitude)  | 13.131974    | 13.286883   |
| t-closeness (renda)      | 24024.258748 | 20725.841869|


Execution Parameters 3 Results:

| Propriedade              | Antes        | Depois      |
|--------------------------|--------------|-------------|
| k-anonymity              | 1.0          | 1.0         |
| l-diversity              | 1.0          | 1.0         |
| t-closeness (latitude)   | 4.907627     | 4.897002    |
| t-closeness (longitude)  | 13.131974    | 13.137886   |
| t-closeness (renda)      | 24024.258748 | 24024.247941|


## Uso

Para utilizar este projeto, siga estes passos:

1. Configure ./src/settings.py:

```bash
  [...]
  RESULTS_PATH = "./tests/results/"
  [...]
```

2. Na raiz do repositório, execute:

```bash
  [...]
    python -m venv venv
    venv/scripts/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt

    python .\fecth_results.py -h
  [...]
```

3.1 Execução via .bat:

```bash
  [...]
    .\fetch_results.bat
  [...]
```

3.2 Execução Manual:

```bash
  [...]
    python .\fecth_results.py -a ".\tests\datasets\1kB_100objects_dataset.json" -t 5 -p 1 
  [...]
```
---

👤 Contribuidor Principal: [losthunter52](https://github.com/losthunter52/anonymizer_lib_fetcher)