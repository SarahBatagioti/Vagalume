from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel, load_tool
from tools.final_answer import final_answer
from tools.linkedin_scraper import extrair_perfil_linkedin
import yaml
from Gradio_UI import GradioUI

image_generation_tool = load_tool("agents-course/text-to-image", trust_remote_code=True)

tools = [
    DuckDuckGoSearchTool(),
    extrair_perfil_linkedin,
    image_generation_tool,
    final_answer
]

