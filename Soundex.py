def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters


def process_characters(name):
    soundex_code = [name[0].upper()]
    previous_code = get_soundex_code(soundex_code[0])

    for char in name[1:]:
        current_code = get_soundex_code(char)
        if current_code != '0' and current_code != previous_code:
            soundex_code.append(current_code)
            previous_code = current_code
        if len(soundex_code) == 4:
            break

    return soundex_code

def generate_soundex(name):
    if not name:
        return ""

    soundex_code = process_characters(name)
    return ''.join(soundex_code).ljust(4, '0')
