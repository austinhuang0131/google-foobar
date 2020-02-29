def solution(n, b):
    numbers = list()
    switch = True
    while switch:
        numbers.append(n)
        digits = list(str(n))
        while len(digits) < len(str(numbers[0])):
           digits.append("0")
        z_dec = int("".join(sorted(digits, reverse=True)), b)-int("".join(sorted(digits)), b)
        z_list_mod = list()
        for q in range(len(digits)):
            if (q == len(digits)):
                break
            z_working = z_dec // (b ** q)
            z_list_mod.append(str(z_working % b))
        n = int("".join(z_list_mod[::-1]))
        if len(filter(lambda x:x==n, numbers)) != 0:
            switch = False
    return len(numbers) - numbers.index(n)
    
# Last line must be RETURN not PRINT
# Otherwise all cases will fail
