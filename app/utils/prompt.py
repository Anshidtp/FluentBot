from langchain_core.prompts.few_shot import FewShotPromptTemplate
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.example_selectors import LengthBasedExampleSelector
#from character import few_shot_examples,persona


# create a example template
example_template = """
User: {input}
Emma: {response}
"""

# create a prompt example from above template
# example_prompt = PromptTemplate(
#     input_variables=["input", "response"],
#     template=example_template
# )

# and the suffix our user input and output indicator
suffix = """
Relevant pieces of previous conversation:
{chat_history}
User: {input}
Emma: """

# example_selector = LengthBasedExampleSelector(
#     examples=examples,
#     example_prompt=example_prompt,
#     max_length=100  # increased max length
# )

# # now create the few shot prompt template
# few_shot_prompt_template = FewShotPromptTemplate(
#     example_selector=example_selector,
#     example_prompt=example_prompt,
#     prefix=persona,
#     suffix=suffix,
#     input_variables=["input","chat_history"],
#     example_separator="\n\n"
# )

def get_system_prompt(few_shot_examples,persona):

    # Create the example prompt template
    example_prompt = PromptTemplate(
    input_variables=["input", "response"],
    template=example_template
    )

    example_selector = LengthBasedExampleSelector(
    examples=few_shot_examples,
    example_prompt=example_prompt,
    max_length=100  # increased max length
    )

    few_shot_prompt_template = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix=persona,
    suffix=suffix,
    input_variables=["input","chat_history"],
    example_separator="\n\n"
    )
    return few_shot_prompt_template