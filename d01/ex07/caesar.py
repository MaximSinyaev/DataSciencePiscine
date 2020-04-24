import sys

states = ['encode', 'decode']


def check_args():
    if len(sys.argv) != 4:
        raise Exception('Wrong number of arguments, must be 3')
    if sys.argv[1].strip() not in states:
        raise Exception('Wrong parameter')
    if not sys.argv[2].strip().isascii():
        raise Exception('The script does not support your language yet.')


def encode(word, n):
    result = ''
    for i in word:
        result += chr((ord(i) - ord('a') + n) % 26 + ord('a'))
    return result


def decode(word, n):
    result = ''
    for i in word:
        result += chr((ord(i) - ord('a') - n) % 26 + ord('a'))
    return result


def main():
    check_args()
    if sys.argv[1] == states[0]:
        print(encode(sys.argv[2], int(sys.argv[3])))
    elif sys.argv[1] == states[1]:
        print(decode(sys.argv[2], int(sys.argv[3])))


if __name__ == "__main__":
    main()
