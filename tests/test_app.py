"""Small, network-free regression tests for FirstPR AI."""

import unittest
from unittest.mock import patch

import requests

import app


class FirstPRAITests(unittest.TestCase):
    def test_blank_issue_is_rejected_before_model_call(self):
        with patch("app.requests.post") as post:
            result = app.analyze_issue("   ", "Issue Analyzer")

        self.assertIn("paste a GitHub issue", result.lower())
        post.assert_not_called()

    def test_unknown_skill_returns_helpful_error(self):
        content, error = app.load_skill("Not a real skill")

        self.assertIsNone(content)
        self.assertIn("Unknown skill", error)

    def test_issue_analyzer_skill_loads(self):
        content, error = app.load_skill("Issue Analyzer")

        self.assertIsNone(error)
        self.assertTrue(content)
        self.assertIn("issue", content.lower())

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
        self.assertIn("Ollama", result)


if __name__ == "__main__":
    unittest.main()
