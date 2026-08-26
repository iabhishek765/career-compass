from pathlib import Path


def load_prompt(prompt_filename: str) -> str:
    """
    Load a prompt template from the prompts folder.

    Parameters
    ----------
    prompt_filename : str
        Example: career_report_prompt.txt

    Returns
    -------
    str
        Prompt text
    """

    project_root = Path(__file__).resolve().parent.parent

    prompt_path = project_root / "prompts" / prompt_filename

    if not prompt_path.exists():
        raise FileNotFoundError(
            f"Prompt file not found:\n{prompt_path}"
        )

    with open(prompt_path, "r", encoding="utf-8") as file:
        prompt = file.read()

    return prompt