from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# Create a custom config
# config = DEFAULT_CONFIG.copy()
# config["llm_provider"] = "openai"  # Use OpenAI
# config["backend_url"] = "https://api.openai.com/v1"  # OpenAI backend
# config["deep_think_llm"] = "gpt-4o"  # Use a different model
# config["quick_think_llm"] = "gpt-4o-mini"  # Use a different model
# config["max_debate_rounds"] = 1  # Increase debate rounds
# config["online_tools"] = True  # Enable online tools

# Initialize with custom config
ta = TradingAgentsGraph(debug=True)

# forward propagate with cryptocurrency
_, decision = ta.propagate("BTC", "2024-05-10")
print(decision)

# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns
