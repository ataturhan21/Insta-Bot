import importlib.util
import unittest
from pathlib import Path
from unittest.mock import Mock

spec = importlib.util.spec_from_file_location(
    "operations", Path(__file__).parents[1] / "insta_bot/modules/operations.py"
)
operations = importlib.util.module_from_spec(spec)
spec.loader.exec_module(operations)


class OperationTests(unittest.TestCase):
    def test_partial_batch_is_not_retried(self):
        action = Mock(return_value=3)
        self.assertEqual(operations.perform_batch(action, 10), 3)
        action.assert_called_once_with(count=10)

    def test_zero_progress_stops(self):
        action = Mock(return_value=0)
        self.assertEqual(operations.perform_batch(action, 10), 0)
        action.assert_called_once_with(count=10)

    def test_invalid_request_never_invokes_action(self):
        action = Mock()
        for count in [0, -1, True, 1.5]:
            with self.subTest(count=count), self.assertRaises(ValueError):
                operations.perform_batch(action, count)
        action.assert_not_called()

    def test_invalid_report_is_rejected(self):
        for result in [None, True, -1, 11]:
            with self.subTest(result=result), self.assertRaises(RuntimeError):
                operations.perform_batch(Mock(return_value=result), 10)

    def test_action_error_propagates_without_retry(self):
        action = Mock(side_effect=RuntimeError("dialog closed"))
        with self.assertRaisesRegex(RuntimeError, "dialog closed"):
            operations.perform_batch(action, 10)
        action.assert_called_once()


if __name__ == "__main__":
    unittest.main()
