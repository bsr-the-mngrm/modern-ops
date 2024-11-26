import json
from src.arithmetic_app.arithmetic import add, save_to_file

def test_integration(tmp_path):
    a, b = 10, 5
    result = add(a, b)
    
    filename = tmp_path / "integration_test.json"
    save_to_file(filename, {"operation": "add", "result": result})

    with open(filename, 'r') as file:
        loaded_data = json.load(file)
    assert loaded_data == {"operation": "add", "result": 15}
