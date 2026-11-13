"""Network-free regression tests for FirstPR AI."""

import unittest
from unittest.mock import Mock, patch

import requests

import app
from skill_registry import SKILL_FOLDERS, load_skill


class FirstPRAITests(unittest.TestCase):
    def test_blank_issue_is_rejected_before_model_call(self):
        with patch("app.requests.post") as post:
            result = app.analyze_issue("   ", "Issue Analyzer")

        self.assertIn("paste a github issue", result.lower())
        post.assert_not_called()

    def test_non_string_issue_is_rejected(self):
        self.assertIn("paste a github issue", app.analyze_issue(None, "Issue Analyzer").lower())

    def test_unknown_skill_returns_helpful_error(self):
        content, error = load_skill("Not a real skill")

        self.assertIsNone(content)
        self.assertIn("Unknown skill", error)

    def test_every_registered_skill_loads_real_instructions(self):
        self.assertEqual(len(SKILL_FOLDERS), 5)

        for skill_name in SKILL_FOLDERS:
            with self.subTest(skill=skill_name):
                content, error = load_skill(skill_name)
                self.assertIsNone(error)
                self.assertTrue(content)
                self.assertNotIn("---", content[:10])

    def test_ollama_connection_error_is_actionable(self):
        with patch(
            "app.requests.post",
            side_effect=requests.exceptions.ConnectionError(),
        ):
            result = app.analyze_issue(
                "The application crashes when I open settings.",
                "Issue Analyzer",
            )

        self.assertIn("Cannot connect to Ollama", result)

    def test_ollama_response_is_returned(self):
        response = Mock()
        response.json.return_value = {"response": "A useful investigation plan."}
        response.raise_for_status.return_value = None

        with patch("app.requests.post", return_value=response) as post:
            result = app.analyze_issue("A sample issue", "Issue Analyzer")

        self.assertEqual(result, "A useful investigation plan.")
        self.assertEqual(post.call_args.kwargs["json"]["model"], app.MODEL)
        self.assertIn("Issue summary", post.call_args.kwargs["json"]["prompt"])


if __name__ == "__main__":
    unittest.main()
