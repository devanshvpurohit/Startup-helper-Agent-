def get_market_prompt(idea):
    return f"""
You are a market analyst. Give detailed market research for this startup idea:
"{idea}"

Include:
- Market size and trends
- Key competitors
- SWOT analysis
- Target demographics
"""

def get_strategy_prompt(idea):
    return f"""
Act like a startup CMO. Devise a market strategy for the startup:
"{idea}"

Include:
- Positioning
- Go-to-market plan
- Digital & offline channels
- Influencer/viral strategy
"""

def get_tech_stack_prompt(idea):
    return f"""
As a CTO, list the complete tech stack for building:
"{idea}"

Include:
- Frontend
- Backend
- Database
- Cloud/infrastructure
- ML tools (if needed)
- DevOps tools
"""
