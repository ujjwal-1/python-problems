def what_to_do(instructions):
    if instructions.startswith("Simon says"):
        return f"I{instructions[10:]}"
    elif instructions.endswith("Simon says"):
        new_val = instructions.split("Simon")
        return f"I {new_val[0]}"
    else:
        return "I won't do it!"



