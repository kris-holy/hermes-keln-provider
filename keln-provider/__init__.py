"""Keln model provider for Hermes Agent."""

from providers import register_provider
from providers.base import ProviderProfile

keln = ProviderProfile(
    name="keln",
    display_name="Keln",
    description="Keln (open models through an OpenAI-compatible API)",
    signup_url="https://app.keln.ai/signup",
    env_vars=("KELN_API_KEY",),
    base_url="https://api.keln.ai/v1",
    auth_type="api_key",
    supports_vision=True,
    default_aux_model="zai-org/glm-5.3-flash",
    fallback_models=(
        "moonshotai/kimi-k3",
        "qwen/qwen3.8-2.4t-a95b",
        "zai-org/glm-5.3",
        "zai-org/glm-5.3-flash",
        "deepseek-ai/deepseek-v4.1-flash",
    ),
)

register_provider(keln)
