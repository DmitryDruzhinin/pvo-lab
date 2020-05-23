with open('new_text_document.txt') as f:
    print(sum(1 for _ in f))