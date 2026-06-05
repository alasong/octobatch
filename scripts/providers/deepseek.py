"""
deepseek.py - DeepSeek LLM provider (OpenAI-compatible API).

DeepSeek API is OpenAI-compatible, so this provider reuses the OpenAI SDK
with a custom base_url. Supports both batch and realtime APIs.

Environment variables required:
    DEEPSEEK_API_KEY: API key for DeepSeek API access
"""

import os

from .openai import OpenAIProvider
from .base import AuthenticationError


class DeepSeekProvider(OpenAIProvider):
    """
    DeepSeek LLM provider for both batch and realtime APIs.

    Uses OpenAI's Python SDK with DeepSeek's base URL.
    Supports:
    - Realtime: Synchronous Chat Completions API at api.deepseek.com
    - Batch: Asynchronous Batch API

    Config options (under api:):
        model: Model to use (default: "deepseek-chat")
    """

    DEEPSEEK_BASE_URL = "https://api.deepseek.com"

    def __init__(self, config: dict):
        """
        Initialize the DeepSeek provider.

        Args:
            config: Configuration dict with api settings

        Raises:
            AuthenticationError: If API key not set
            ImportError: If openai package not installed
        """
        # Call OpenAIProvider.__init__ which calls _validate_sdk, _validate_credentials, _init_client
        # We override _validate_credentials and _init_client below
        super().__init__(config)

    def _validate_credentials(self):
        """Check that DEEPSEEK_API_KEY is set."""
        api_key = os.environ.get("DEEPSEEK_API_KEY")
        if not api_key:
            raise AuthenticationError(
                "DEEPSEEK_API_KEY environment variable not set. "
                "Required for DeepSeek API access."
            )
        self._api_key = api_key

    def _init_client(self):
        """Initialize the OpenAI client with DeepSeek base URL."""
        from openai import OpenAI
        self._client = OpenAI(
            api_key=self._api_key,
            base_url=self.DEEPSEEK_BASE_URL,
            timeout=120.0
        )

    def get_api_key_env_var(self) -> str:
        """Get the environment variable name for DeepSeek API key."""
        return "DEEPSEEK_API_KEY"
