# CRUD_with_fastapi

Reposítório para estudo do Framework Fast API.

Para usar criar um db no postgress ajustar a URL de conexão no arquivo database/connection.py e executar o arquivo init_db.py no terminal.
Feito isso o script criará os a tabela corretamente.

para executar a api
```
uvicorn main:app --reload
```

a tag --reload, garantirá que a api continue executando mesmo com alterações no codigo

o FastAPI gerá automaticante a documentação, para visualizar acessar 127.0.0.1:8000/docs