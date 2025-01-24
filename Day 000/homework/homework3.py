def test(lst):
    if lst[0] < 0:
        if lst[1] < 0:
            if lst[2] < 0:
                if lst[3] < 0:
                    return "a"
                else:
                    return "b"
            else:
                if lst[3] < 0:
                    return "c"
                else:
                    return "d"
        else:
            if lst[2] < 0:
                if lst[3] < 0:
                    return "e"
                else:
                    return "f"
            else:
                if lst[3] < 0:
                    return "g"
                else:
                    return "h"
    else:
        if lst[1] < 0:
            if lst[2] < 0:
                if lst[3] < 0:
                    return "i"
                else:
                    return "j"
            else:
                if lst[3] < 0:
                    return "k"
                else:
                    return "l"
        else:
            if lst[2] < 0:
                if lst[3] < 0:
                    return "m"
                else:
                    return "n"
            else:
                if lst[3] < 0:
                    return "o"
                else:
                    return "p"

print(test([1, 2, -3, -4]))

def test2(lst):
    if lst[0] < 0:
        if lst[1] < 0:
            if lst[2] < 0:
                if lst[3] < 0:
                    if lst[4] < 0:
                        return "a"
                    else:
                        return "b"
                else:
                    if lst[4] < 0:
                        return "c"
                    else:
                        return "d"
            else:
                if lst[3] < 0:
                    if lst[4] < 0:
                        return "e"
                    else:
                        return "f"
                else:
                    if lst[4] < 0:
                        return "g"
                    else:
                        return "h"
        else:
            if lst[2] < 0:
                if lst[3] < 0:
                    if lst[4] < 0:
                        return "i"
                    else:
                        return "j"
                else:
                    if lst[4] < 0:
                        return "k"
                    else:
                        return "l"
            else:
                if lst[3] < 0:
                    if lst[4] < 0:
                        return "m"
                    else:
                        return "n"
                else:
                    if lst[4] < 0:
                        return "o"
                    else:
                        return "p"
    else:
        if lst[1] < 0:
            if lst[2] < 0:
                if lst[3] < 0:
                    if lst[4] < 0:
                        return "q"
                    else:
                        return "r"
                else:
                    if lst[4] < 0:
                        return "s"
                    else:
                        return "t"
            else:
                if lst[3] < 0:
                    if lst[4] < 0:
                        return "u"
                    else:
                        return "v"
                else:
                    if lst[4] < 0:
                        return "w"
                    else:
                        return "x"
        else:
            if lst[2] < 0:
                if lst[3] < 0:
                    if lst[4] < 0:
                        return "y"
                    else:
                        return "z"
                else:
                    if lst[4] < 0:
                        return "aa"
                    else:
                        return "bb"
            else:
                if lst[3] < 0:
                    if lst[4] < 0:
                        return "cc"
                    else:
                        return "dd"
                else:
                    if lst[4] < 0:
                        return "ee"
                    else:
                        return "ff"

print(test2([1, 2, -3, -4, 5]))
