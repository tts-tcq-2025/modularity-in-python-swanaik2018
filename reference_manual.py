from color_utils import get_color_from_pair_number

def generate_reference_manual():
    reference_lines = []
    for pair_number in range(1, 26):  # 25 pairs
        major, minor = get_color_from_pair_number(pair_number)
        reference_lines.append(f"{pair_number:2} -> {major:<6} | {minor}")
    return "\n".join(reference_lines)

//YAGNI violation
def print_reference_manual():
    print("Color Code Reference Manual:")
    print("-" * 32)
    print(generate_reference_manual())
