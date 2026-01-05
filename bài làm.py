import random
while True:
    a = input("Bạn muốn chọn kéo, búa hay bao? ").lower()

    if a not in ['kéo', 'búa', 'bao']:
        print("Lựa chọn không hợp lệ. Vui lòng chọn kéo, búa hoặc bao.")
        continue
    may = random.choice(['kéo', 'búa', 'bao'])
    print("Máy chọn:", may)
    if a == may:
        print("Hòa!")
    elif (a == 'kéo' and may == 'bao') or (a == 'búa' and may == 'kéo') or (a == 'bao' and may == 'búa'):
        print("Bạn đã thắng ")
    else:
        print("Bạn thua rồi ")
    while True:
        b = input("Bạn muốn chơi lại không? (có/không): ").lower()
        if b not in ['có', 'không']:
            print("Vui lòng trả lời 'có' hoặc 'không'.")
            continue
        if b == 'có':
            break
        else:
            print("Cảm ơn bạn đã chơi")
            break
    if(b == 'không'):
        break
