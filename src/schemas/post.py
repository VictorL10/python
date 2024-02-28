POST_SCHEMA = {
    "properties": {
        "age": {"type": "number"},
        "daily_food": {"type": "number"},
        "daily_sleep": {"type": "number"},
        "name": {"type": "string", "enum": ["Victor"]}
    },
    "required": ["age"]
}

# {'age': 32, 'daily_food': 0.96, 'daily_sleep': 200.0, 'name': 'Victor'}