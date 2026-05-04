def format_name(f_name: str, l_name: str) -> str:
    return f"{f_name.title()} {l_name.title()}"

full_name = format_name("TIRSO", "GomEz")
print(full_name)