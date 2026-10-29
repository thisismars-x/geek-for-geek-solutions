
from time import sleep
from collections.abc import Generator

def average() -> Generator[None, int, None]:
    curr_avg = 0
    n_items = 1

    while True:
        print("Average = ", curr_avg)
        new_value: int = yield
        print(new_value)
        curr_avg = ( (curr_avg * n_items) + new_value ) / (n_items + 1)
        n_items += 1


v = 10
avg = average()
next(avg)

while True:
    avg.send(v)
    v += 10
    sleep(1)
