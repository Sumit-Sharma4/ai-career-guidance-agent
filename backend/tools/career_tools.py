from typing import Dict, List
from langchain.tools import Tool

from tools.knowledge_base import COURSE_INFO, ROLE_SKILL_MAP, PROJECTS_BY_GOAL


def course_info_tool_func(course_name: str) -> str:
    course = course_name.strip().lower()
    data = COURSE_INFO.get(course)

    if not data:
        return (
            f"No exact course info found for '{course_name}'. "
            "Available examples include BTech, BCA, and BSc Computer Science."
        )

    return str(data)


def suitability_tool_func(user_profile: str) -> str:
    return (
        "Suitability analysis based on profile: "
        f"{user_profile}\n"
        "Recommended process: evaluate education background, interest area, comfort with math/coding, "
        "career goals, and course duration preference. For tech-oriented students, common suitable options "
        "include B.Tech CSE, B.Tech AI/DS, BCA, and B.Sc Computer Science."
    )


def skill_analysis_tool_func(user_profile: str) -> str:
    return (
        "Analyze this user profile for current level, strengths, gaps, and readiness for the target role:\n"
        f"{user_profile}"
    )


def role_recommendation_tool_func(user_profile: str) -> str:
    return (
        "Recommend suitable immediate and future career roles for this user profile:\n"
        f"{user_profile}"
    )


def future_skills_tool_func(target_role: str) -> str:
    role = target_role.strip().lower()
    skills = ROLE_SKILL_MAP.get(role)

    if not skills:
        return (
            f"No exact role skill map found for '{target_role}'. "
            "Available examples include AI Engineer, ML Engineer, and Software Engineer."
        )

    return str(skills)


def project_suggestion_tool_func(target_role: str) -> str:
    role = target_role.strip().lower()
    projects = PROJECTS_BY_GOAL.get(role)

    if not projects:
        return (
            f"No exact project list found for '{target_role}'. "
            "Available examples include AI Engineer, ML Engineer, and Software Engineer."
        )

    return str(projects)


def roadmap_tool_func(user_profile: str) -> str:
    return (
        "Generate a practical roadmap from the user's current level to the target career goal.\n"
        f"User profile: {user_profile}\n"
        "The roadmap should be staged, practical, student-friendly, and project-oriented."
    )


def resume_tool_func(resume_text: str) -> str:
    return (
        "Review this resume text and suggest improvements for skills, projects, formatting, and career alignment:\n"
        f"{resume_text}"
    )


course_info_tool = Tool(
    name="Course Info Tool",
    func=course_info_tool_func,
    description="Use when the user asks for information about a course like BTech, BCA, or BSc Computer Science.",
)

suitability_tool = Tool(
    name="Suitability Checker",
    func=suitability_tool_func,
    description="Use when the user asks which course or path suits them according to education, interests, or goals.",
)

skill_analysis_tool = Tool(
    name="Skill Analyzer",
    func=skill_analysis_tool_func,
    description="Use to analyze the user's current skill level, strengths, gaps, and readiness.",
)

role_recommendation_tool = Tool(
    name="Role Recommendation Tool",
    func=role_recommendation_tool_func,
    description="Use to suggest suitable immediate and future career roles for the user.",
)

future_skills_tool = Tool(
    name="Future Skills Tool",
    func=future_skills_tool_func,
    description="Use to get important future skills for a specific target role like AI Engineer or ML Engineer.",
)

project_suggestion_tool = Tool(
    name="Project Suggestion Tool",
    func=project_suggestion_tool_func,
    description="Use to get project suggestions for a specific target role like AI Engineer or Software Engineer.",
)

roadmap_tool = Tool(
    name="Roadmap Tool",
    func=roadmap_tool_func,
    description="Use to build a personalized learning roadmap from the user's current profile to their target career.",
)

resume_tool = Tool(
    name="Resume Tool",
    func=resume_tool_func,
    description="Use when the user shares resume content or asks for resume improvements.",
)