import os
import fcntl
import random

def get_next_index(used_indices_file="used_indices.txt", random_int=None):
    if not os.path.exists(used_indices_file):
        with open(used_indices_file, "a") as f:
            pass

    with open(used_indices_file, "r+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)

        used_indices = set()
        for line in f.readlines():
            try:
                used_indices.add(int(line.strip()))
            except:
                continue

        if random_int_max is not None:
            available_indices = set(range(random_int)) - used_indices
            if not available_indices:
                raise ValueError(f"All integers less than {random_int} have been used.")
            next_index = random.choice(list(available_indices))
        else:
            next_index = 0
            while next_index in used_indices:
                next_index += 1

        f.write(str(next_index) + "\n")

    return next_index
