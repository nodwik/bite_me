def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    try:
        with open(file_) as f:
            lines = 0
            words = 0
            chars = 0
            for line in f:
                lines += 1
                words += len(line.split())
                chars += len(line)
                #chars += len([char for char in line])
            return f'{lines} {words} {chars} {file_}'
    except FileNotFoundError:
        return f"File '{file_path}' not found."

if __name__ == '__main__':
    # make it work from cli like original unix wc
    # python3 wc.py <file_path>
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 wc.py <file_path>")
    else:
        print(wc(sys.argv[1]))