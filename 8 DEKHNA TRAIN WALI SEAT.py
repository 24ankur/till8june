seat_map = {1: (11, "WS"), 2: (9, "MS"), 3: (7, "AS"), 4: (5, "AS"), 5: (3, "MS"), 6: (1, "WS"), 7: (-1, "WS"),
            8: (-3, "MS"), 9: (-5, "AS"), 10: (-7, "AS"), 11: (-9, "MS"), 0: (-11, "WS")}

for _ in range(int(input())):
    seat = int(input());
    op_seat = seat_map[seat % 12]
    print(op_seat[0] + seat, op_seat[1])