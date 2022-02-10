__version__ = "0.1.0"


def main():
    heap = [0 for x in range(100)]
    sz = 0

    # イケてないな
    sz = push(1, heap, sz)
    print(heap, sz)
    sz = push(2, heap, sz)
    ans, sz = pop(heap, sz)
    print(ans)
    sz = push(10, heap, sz)
    sz = push(3, heap, sz)
    ans, sz = pop(heap, sz)
    print(ans)
    ans, sz = pop(heap, sz)
    print(ans)
    ans, sz = pop(heap, sz)
    print(ans)


def push(x: int, heap: list[int], sz: int) -> int:
    # 自分のノード番号
    i = sz
    sz += 1

    while i > 0:
        # 親のノード番号
        p = int((i - 1) / 2)

        # 逆転してないなら抜ける
        if heap[p] <= x:
            break

        # 親のノードの数字をおろして、自分は上へ
        heap[i] = heap[p]
        i = p

    heap[i] = x
    return sz


def pop(heap: list[int], sz: int) -> tuple[int, int]:
    if sz <= 0:
        raise IndexError

    # 最小値
    ret = heap[0]

    # 根に持ってくる値
    sz -= 1
    x = heap[sz]

    # 根からおろしていく
    i = 0
    while i * 2 + 1 < sz:
        # 子同士を比較
        a = i * 2 + 1
        b = i * 2 + 2
        if b < sz and heap[b] < heap[a]:
            a = b

        # もう逆転してないなら終わり
        if heap[a] >= x:
            break

        # 子の数字を持ち上げる
        heap[i] = heap[a]
        i = a

    heap[i] = x

    return ret, sz


if __name__ == "__main__":
    main()
