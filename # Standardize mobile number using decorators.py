# ============================
# PLATFORM:
# HackerRank
# PROBLEM:
# Standardize Mobile Number Using Decorators
# ============================

def wrapper(f):
    def fun(l):
        temp = []

        for i in range(len(l)):

            # Last 10 digits of the number
            a = int(l[i][-10:-5])
            b = int(l[i][-5:])

            temp.append("+91 " + str(a) + " " + str(b))

        # Call original function
        f(temp)

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)