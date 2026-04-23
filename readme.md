# setup
```shell
# Create python env
python -m venv .venv
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Run in development mode
fastapi dev
```

# Api Endpoints
### `POST /api/v1/todos`
create new todo item
body:
```json
{
    "_id": "sdfasfdf",
    "task_title": "Complete Public todo api to learn fastapi",
    // Note is optional
    "note": " > Use pydantic for requests auto validation",
    "completed": false
}
```
Response(200):
```json
{
    "_id": "69e9fe3b319e51a10356d2aa",
    "task_title": "Complete Public todo api to learn fastapi",
    "note": " > Use pydantic for requests auto validation",
    "completed": false,
    "created_at": "2026-04-23T11:10:51.566149Z"
}
```

---
### `GET /api/v1/todos`
Get all todos, response:
```json
[
        {
        "_id": "69e9fe3b319e51a10356d2aa",
        "task_title": "Complete Public todo api to learn fastapi",
        "note": " > Use pydantic for requests auto validation",
        "completed": false,
        "created_at": "2026-04-23T11:10:51.566000"
    }
]
```

---
### `PUT /api/v1/todos/{id}`
Edit or update todo item, body:
```json
{
    "note": "Pydantic for model validation",
    "completed": true
}
```

Response:
```json
{
    "_id": "69e9fe3b319e51a10356d2aa",
    "task_title": "Complete Public todo api to learn fastapi",
    "note": "Pydantic for model validation",
    "completed": true,
    "created_at": "2026-04-23T11:10:51.566000"
}
```
# File Structure
```shell
├── app 
│   ├── core # types, configs, auth, etc. common logics
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── functions.py
│   │   └── types.py
│   ├── db # mongodb or other related db stuff
│   │   ├── __init__.py
│   │   └── mongodb.py
│   └── routes # api routes (v1, v2, v3, ...)
│       └── v1
│           ├── todos # an endpoint in v1
│           │   ├── __init__.py
│           │   ├── methods
│           │   │   ├── create_todo.py # post
│           │   │   ├── list_todos.py # get
│           │   │   └── update_todo.py # put
│           │   ├── router.py
│           │   └── schema.py
│           └── v1_router.py # all endpoints included in one v1_router value
│           # other endpoints with the same todos structure
├── env.development # debug only env values
├── main.py
├── readme.md
└── requirements.txt
```