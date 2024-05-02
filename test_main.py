import unittest
from unittest.mock import patch, call
from io import StringIO
import sys

from main import rps, menu, user_choice


class TestMain(unittest.TestCase):

  @patch('main.input', side_effect=['1'])
  @patch('sys.stdout', new_callable=StringIO)
  def test_display_menu_and_get_user_choice(self, mock_stdout, mock_input):
    expected_output = "====== Main menu ======\n\n1. Rock paper scissors\n\n2.\
        Hangman\n\n3. Tic tac toe\n\n4. Exit\n\n"

    expected_calls = [call("Select a game (1-3): ")]

    menu()
    self.assertEqual(mock_stdout.getvalue(), expected_output)
    self.assertEqual(mock_input.mock_calls, expected_calls)

  @patch('sys.stdout', new_callable=StringIO)
  def test_rps_equal(self, mock_stdout):
    expected_output = "Player: r\tComputer: r.\nIt's a tie!\n"

    rps('r')

    actual_output = mock_stdout.getvalue()

    self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
  unittest.main()
