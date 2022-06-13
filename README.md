## Dev.:

1. Create virtual env:

```
$ python -m venv enafood_env
```

2. Activate virtual env:

```
$ . enafood_env/bin/activate
```

If you want to deactivate:

```
$ deactivate
```

4. Install requirements:

```
$ pip install -r requirements.txt
```

And then...

```
$ pip install -e .
```


or update (if you want to add some package):

```
pip install --upgrade --force-reinstall -r requirements.txt
```

3. Test coverage:

```
pytest --cov-report html:cov_html --cov=enafood tests/
```
