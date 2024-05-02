import pytest
from main import rps


@pytest.mark.parametrize("user", ["1"])  # Provide the desired input value
def test_rps(monkeypatch, capsys, user):
  # Use monkeypatch to replace the input function
  monkeypatch.setattr('builtins.input', lambda _: user)

  # Call the function you want to test
  rps()

  # Capture the printed output
  captured = capsys.readouterr()

  # Assert against the expected output
  assert "Select a game (1-3):" in captured.out
  # Add more assertions as needed
