def f2c(temp_f):
    return (temp_f - 32) * 5/9

def c2f(temp_c):
    return ( temp_c * 1.8 ) + 32
def main():
    temp_f = float(input('온도를 입력하세요(화씨) '))
    temp_c = float(input('온도를 입력하세요(섭씨) '))

    print(f"{temp_f}F => \033[36m{f2c(temp_f):.1f}℃\033[0m")
    print(f"{temp_c}℃ => \033[36m{c2f(temp_c):.1f}F")


if __name__ == "__main__":
    main()
