import unittest
from unittest.mock import patch, MagicMock
from source.response_manager import init_mistral, get_response
import streamlit as st

class TestMistralInteraction(unittest.TestCase):

    @patch("source.response_manager.Mistral")
    @patch("streamlit.session_state", {})
    def test_init_mistral_and_get_response(self, mock_mistral):
        st.session_state["mistral_model"] = "pixtral-12b"

        api_key = "test_api_key"

        mock_client = MagicMock()
        mock_mistral.return_value = mock_client
        mock_client.chat.complete.return_value.choices = [
            MagicMock(message=MagicMock(content="Test response"))
        ]

        client = init_mistral(api_key)
        mock_mistral.assert_called_once_with(api_key=api_key)

        messages = [{"role": "user", "content": "Hello from ercudu"}]
        response = get_response(client, messages)

        mock_client.chat.complete.assert_called_once_with(
            model="pixtral-12b",
            messages=messages
        )

        self.assertEqual(response, "Test response")

if __name__ == '__main__':
    unittest.main()
