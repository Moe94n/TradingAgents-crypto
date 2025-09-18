from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

import os

# Create a custom config with better OpenRouter support
config = DEFAULT_CONFIG.copy()

# You can override these settings with environment variables or modify directly
config["llm_provider"] = os.environ.get("LLM_PROVIDER", "openrouter")  # Use OpenRouter by default
config["backend_url"] = os.environ.get("BACKEND_URL", "https://openrouter.ai/api/v1")  # OpenRouter backend
config["api_key"] = os.environ.get("API_KEY", "")  # API key from environment

# Model selection - you can change these to any models supported by your provider
config["deep_think_llm"] = os.environ.get("DEEP_THINK_LLM", "openai/gpt-4o")  # Deep thinking model
config["quick_think_llm"] = os.environ.get("QUICK_THINK_LLM", "openai/gpt-4o-mini")  # Quick thinking model

# Additional configuration options
config["max_debate_rounds"] = int(os.environ.get("MAX_DEBATE_ROUNDS", "1"))  # Debate rounds
config["online_tools"] = os.environ.get("ONLINE_TOOLS", "True").lower() == "true"  # Enable online tools

# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config)

# forward propagate with cryptocurrency
_, decision = ta.propagate("BTC", "2024-05-10")
print(decision)

# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns
