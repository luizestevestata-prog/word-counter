def count_words(text):
    """Count the number of words in a string."""
    return len(text.split())


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print(count_words(" ".join(sys.argv[1:])))
    else:
        print(0)
