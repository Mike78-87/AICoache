def solve(input_str: str) -> str:
    """
    Возвращает количество воды в увлажнителе сразу после последнего долива.
    Временная сложность: O(N), где N – количество доливов.
    """
    lines = input_str.strip().splitlines()
    n = int(lines[0].strip())
    water = 0
    prev_time = 0
    for i in range(1, n + 1):
        t_str, v_str = lines[i].split()
        t = int(t_str)
        v = int(v_str)

        leak = t - prev_time
        water = max(0, water - leak)
        water += v
        prev_time = t

    return str(water)
