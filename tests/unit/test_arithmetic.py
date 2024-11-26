import json
from src.arithmetic_app.arithmetic import add, subtract, save_to_file

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_save_to_file(tmp_path):
    filename = tmp_path / "test_file.json"
    data = {"result": 42}
    save_to_file(filename, data)

    # Verify file contents
    with open(filename, 'r') as file:
        loaded_data = json.load(file)
    assert loaded_data == data
