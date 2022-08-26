import re
import os

def main():
    print('enter search directory')
    directory = input().strip()
    print('enter regex pattern for files to search')
    pattern = input().strip()
    print('should I print all found files? (y/n)')
    response = input().strip().lower()[0]
    maybe_print = lambda s: print('parsing file', s) if response == 'y' else lambda _: None

    files = 0
    lines = 0
    for path, _, filenames in os.walk(directory):
        for filename in filenames:
            file = os.path.join(path, filename)
            if re.match(pattern, file) is None:
                continue
            maybe_print(file)
            try:
                with open(file, 'rb') as f:
                    files += 1
                    for _ in f.readlines():
                        lines += 1
            except Exception as e:
                print(e)

    print('total files count:', files)
    print('total lines count:', lines)

if __name__ == '__main__':
    main()
