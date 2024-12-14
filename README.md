- Run Docker
```bash
docker compose up
```

- Create Python environment
```bash
python -m venv venv
```

- Init database
```bash
python ./src/models/schema.py
```


- Run the application
```bash
python ./main.py
```