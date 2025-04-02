from enum import Enum, auto


Problem = Enum('Problem', '''
    leading_space
    trailing_space
    no_tab 
    multiple_tab
    no_space_after_comma
''')


def check_known_problems(file_name: str) -> dict[tuple[int, str], list[Problem]]:
    from collections import defaultdict
    from functools import partial
    
    problems = defaultdict(list)
    with open(file_name) as file:
        for n, line in enumerate(map(lambda line: line.rstrip('\n'), file)):
            if line.startswith(' '): 
                problems[(n, line)].append(Problem.leading_space.name)
            if line.endswith(' '):
                problems[(n, line)].append(Problem.trailing_space.name)
            if '\t' not in line and line.strip():
                problems[(n, line)].append(Problem.no_tab.name)
            if len(line.split('\t')) > 2:
                problems[(n, line)].append(Problem.multiple_tab.name)
            if any(not p.startswith(' ') for p in line.split(',')[1:]):
                problems[(n, line)].append(Problem.no_space_after_comma.name)
    return problems


if __name__ == '__main__':
    from sys import argv
    import os.path
    from pprint import pprint
    
    for fname in argv[1:]:
        print('File:', fname)
        if not fname.endswith('.tsv'):
            print('NOT A TSV FILE')
        elif os.path.exists(fname):
            problems = check_known_problems(fname)
            if problems:
                pprint(dict(problems))
            else:
                print('OK')
        else:
            print('DO NOT EXISTS')
