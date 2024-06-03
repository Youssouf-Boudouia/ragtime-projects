PROJECT_NAME: str = "Albert"

import ragtime
from ragtime.pipeline.pipeline import Pipeline
from ragtime.llms import reference_LLM
from ragtime.prompters import reference_Prompter
from classes import Albert_LLM, Prompter_from_human_evaluated_Expe
import yaml

# always start with init_project before importing ragtime.config values since they are updated
# with init_project and import works by value and not by reference, so values imported before
# calling init_project are not updated after the function call
ragtime.config.init_project(name=PROJECT_NAME, init_type="globals_only")


# Here we set an internal ragtime state to register our custom LLM classe
reference_LLM(Albert_LLM, "Albert_LLM")
reference_Prompter(
    Prompter_from_human_evaluated_Expe, "Prompter_from_human_evaluated_Expe"
)
with open("configuration.yaml") as file:
    configuration: dict = yaml.safe_load(stream=file.read())
    pipline = Pipeline(**configuration)
pipline.run()
