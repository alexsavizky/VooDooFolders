from pathlib import Path

from executor import execute_instructions
from ai_prompt import generate_instructions


if __name__ == "__main__":
    base_dir = Path(r"C:\Users\alexs\codeProj\VooDooFolders\playground")

    user_prompt = "Move all photos into a folder called Pictures and all the music into folder named music"

    print("USER:", user_prompt)

    # Step 1 — get Python code from LLM
    instructions = generate_instructions(user_prompt)
    print("\nAI GENERATED PYTHON:")
    print(instructions)

    # Step 2 — execute it
    execute_instructions(instructions, base_dir)

    print("\nDONE.")
