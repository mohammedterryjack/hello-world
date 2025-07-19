from json import dumps

def hello_world() -> str:
  return 'hello world'

def dummy_function() -> None:
  for _ in range(3):
    payload = dumps({"source_id": "dummy_source_hash","slots": [{"name": "dummy_slot_name","value": "dummy_slot_value"}]})
    print(payload)

if __name__ == "__main__":
  dummy_function()
