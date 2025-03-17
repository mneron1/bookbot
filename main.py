def get_book_text(file_path):
    print(f'{file_path=}')
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_contents = get_book_text("./books/frankenstein.txt")
    print(file_contents)

main()
