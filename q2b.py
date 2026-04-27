import subprocess
import os

penalties = [4, 8, 12, 14]
predictors = ['one_bit', 'pentium_m']

for pred in predictors:
    for penalty in penalties:
        # Fresh copy each time
        os.system('cp ~/sniper-assignment/Sniper_Assignment/small.cfg .')
        
        # Set branch predictor type
        os.system(f"sed -i 's/type = pentium_m/type = {pred}/' small.cfg")
        
        # Set penalty
        os.system(f"sed -i 's/mispredict_penalty=8/mispredict_penalty={penalty}/' small.cfg")
        
        print(f"\n=== Running: predictor={pred}, penalty={penalty} ===")
        os.system('./run-sniper -p splash2-fft -i small -n 4 -c small')
