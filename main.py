from check_balance import check_brackets_balance

def main():
    brackets = '[(check) {bracket}] balance ()'
    print(check_brackets_balance(brackets))

if __name__ == "__main__":
    main()
