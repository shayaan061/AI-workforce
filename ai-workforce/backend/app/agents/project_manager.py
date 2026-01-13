def run(state: dict) -> dict:
    """
    Project Manager AI
    - Reads user intent
    - Makes assumptions
    - Decomposes project
    - NEVER asks questions
    """

    prompt = f"""
You are a senior technical project manager.

User intent:
{state["user_prompt"]}

RULES:
- The user will NOT answer questions
- You must proceed with reasonable defaults
- Choose simple, widely compatible tech
- Decompose the project internally
- Do NOT include explanations
- Do NOT ask questions

Return JSON ONLY with:
- assumptions (list)
- modules (list)
- phases (list)
- tasks:
    - developer (list)
    - writer (list)
"""

    # Placeholder (real LLM call in next stage)
    state["assumptions"] = [
        "Use simple HTML/CSS for maximum compatibility",
        "Static website, no backend required"
    ]

    state["modules"] = [
        "Home page",
        "About page",
        "Projects page",
        "Contact page",
        "Shared styles"
    ]

    state["phases"] = [
        "Planning",
        "Page structure",
        "Styling",
        "Integration",
        "Documentation"
    ]

    state["tasks"] = {
        "developer": [
            "Create HTML pages for each module",
            "Create shared CSS file",
            "Ensure consistent navigation"
        ],
        "writer": [
            "Write README",
            "Write deployment instructions"
        ]
    }

    state["status"] = "planned"
    state["logs"].append("Project planned by PM AI")

    return state
