from typing import Dict, Any
import time

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType

from config.settings import GOOGLE_API_KEY, MODEL_NAME
from memory.vector_db import save_user_memory, get_user_memory

from tools.career_tools import (
    course_info_tool,
    suitability_tool,
    skill_analysis_tool,
    role_recommendation_tool,
    future_skills_tool,
    project_suggestion_tool,
    roadmap_tool,
    resume_tool,
)


def build_system_prompt(user_input: str, previous_memory: str | None) -> str:
    return f"""
You are an AI Career Guidance Agent.

Rules:
- Keep answers SHORT (max 150 words)
- Use bullet points
- Give only useful info

If user asks:
- course → short info
- career → role + skills + roadmap
- skills → 5-7 skills only
- projects → 3-5 projects only

Previous memory:
{previous_memory if previous_memory else "None"}

User:
{user_input}
"""


def run_career_agent(user_input: str, user_id: str = "default_user") -> Dict[str, Any]:
    previous_memory = get_user_memory(user_id)

    if not GOOGLE_API_KEY:
        return {"response": "⚠️ API key missing."}

    llm = ChatGoogleGenerativeAI(
        model=MODEL_NAME,
        google_api_key=GOOGLE_API_KEY,
        temperature=0.2,
        max_output_tokens=250
    )

    tools = [
        course_info_tool,
        suitability_tool,
        skill_analysis_tool,
        role_recommendation_tool,
        future_skills_tool,
        project_suggestion_tool,
        roadmap_tool,
        resume_tool,
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False,
        handle_parsing_errors=True
    )

    prompt = build_system_prompt(user_input, previous_memory)

    try:
        time.sleep(1)  # avoid rapid calls
        result = agent.run(prompt)

    except Exception as e:
        error_msg = str(e)

        if "quota" in error_msg.lower() or "429" in error_msg:
            return {
                "response": "⚠️ API limit reached. Please wait 30–60 seconds."
            }

        return {
            "response": "⚠️ Server error. Please try again."
        }

    # save small memory
    save_user_memory(user_id, f"user: {user_input[:80]}")

    return {
        "user_id": user_id,
        "response": result,
    }