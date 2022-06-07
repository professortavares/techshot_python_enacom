# techshot_python_enacom
Repositório de código e modelos para o techshot python da enacom

# Operações úteis com o Poetry:

1. Criar o projeto:

```
poetry new enafood
```

2. Instalar dependências:

```
poetry add numpy
```

2.1. Instalar dependências para dev:

```
poetry add faker
```

2.2. Atualizar dependências:

```
poetry update numpy
```

2.3. Usando o arquivo requeriments:

```
poetry add `cat requirements.txt`
```

2.4. Exportar as dependências 

```
poetry export --output requirements.txt
```

3. Executar teste de unidade

```
poetry run pytest
```

4. Listar os envs:

```
poetry env list
```

5. Maiores informações:

https://realpython.com/dependency-management-python-poetry/
