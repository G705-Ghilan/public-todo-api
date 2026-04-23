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