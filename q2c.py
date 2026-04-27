import os

core_counts = [4, 8, 16, 32, 64]

for n in core_counts:
    os.system('cp ~/sniper-assignment/Sniper_Assignment/small.cfg .')
    print(f"\n=== Running: cores={n} ===")
    os.system(f'./run-sniper -p splash2-fft -i small -n {n} -c small')
