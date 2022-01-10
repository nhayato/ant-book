__version__ = "0.1.0"


def fact(n: int) -> int:
    if n == 0:
        return 1
    return n * fact(n - 1)


def fib(n: int) -> int:
    memo: dict[int, int] = {}
    return fib_with_memo(n, memo)


def fib_with_memo(n: int, memo: dict[int, int]) -> int:
    if n <= 1:
        return n
    memodata = memo.get(n)
    if memodata is not None:
        return memodata
    ans = fib_with_memo(n - 1, memo) + fib_with_memo(n - 2, memo)
    memo[n] = ans
    return ans


def use_stack():
    stack: list[int] = []
    stack.append(1)
    stack.append(2)
    stack.append(3)
    print(stack[-1])
    stack.pop()
    print(stack[-1])
    stack.pop()
    print(stack[-1])
    stack.pop()


def use_queue():
    # https://docs.python.org/ja/3/tutorial/datastructures.html#using-lists-as-queues
    from collections import deque

    queue: deque[int] = deque([])
    queue.append(1)
    queue.append(2)
    queue.append(3)
    print(queue[0])
    queue.popleft()
    print(queue.popleft())
    print(queue.popleft())


def main():
    print(fact(4))
    print(fib(40))
    use_stack()
    use_queue()


if __name__ == "__main__":
    main()
