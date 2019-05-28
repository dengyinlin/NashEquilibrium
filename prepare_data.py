import os
import argparse
import time

parser=argparse.ArgumentParser()
args=parser.parse_args()

game_list=['CovariantGame','DispersionGame']

for game in game_list:
    players=2
    actions=300
    if game =='CovariantGame':
        for r in range(0,1,4):
            for i in range(0,100,1):
                os.system(f'java -jar gamut.jar -g {game} -f "ConvariantGame_{i}" -players {players} -actions {actions} -r {r} -output TwoPlayerOutput &')
            time.sleep(5)
    if game=='DispersionGame':
        os.system(f'java -jar gamut.jar -g {game} -players {players} -actions {actions} -output TwoPlayerOutput  &')
        time.sleep(5)