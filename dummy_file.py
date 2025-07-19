from json import dumps

def hello_world() -> str:
  return 'hello world'

def dummy_function() -> list[str]:
  return [ 
    {"source_id": "dummy_source_hash","slots": [{"name": "dummy_slot_name","value": "dummy_slot_value"}]}
    for _ in range(3)
  ]
if __name__ == "__main__":
  results = dummy_function()
  for result in results:
      print(dumps(result))
