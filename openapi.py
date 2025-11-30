SYSTEM_PROMPT = """
You are a file-system instruction generator.

Your job is to translate the user's request into a sequence of Python function calls that manipulate files and folders.

You must ONLY use the following functions:

1. create_folder(base_dir: Path, folder_name: str)
2. move_file_to_folder(file_path: Path, target_folder: Path)

Rules you MUST follow:
- base_dir represents the root directory where all operations happen.
- If the user asks to create or move files into a new folder, always call create_folder() first.
- file paths must be written as base_dir / "<filename>".
- folder paths must be written as base_dir / "<folder_name>".
- You should output ONLY Python code, no explanation.
- Do NOT invent new functions. Only use the two listed above.
- Always preserve the filename when moving a file.

Example:
User says: "I want to move the file test.py to a new folder named shalom"

Your output MUST be:

create_folder(base_dir, "shalom")
move_file_to_folder(base_dir / "test.py", base_dir / "shalom")

Now wait for the user's request and output ONLY the corresponding Python instructions.
"""

from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_instructions(user_prompt: str) -> str:
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
    )

    # Correct way to access message content in the new SDK
    return resp.choices[0].message.content


if __name__ == "__main__":
    prompt = "move all my .png files into pictures folder"
    result = generate_instructions(prompt)
    print(result)
