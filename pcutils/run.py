from .core.config import Config
from .core.workspace import Workspace
from .phase_1 import phase_1
from .phase_2 import phase_2
from .phase_3 import phase_3
from .phase_4_kalman import phase_4_kalman
from time import time

def run_pcutils(config: Config):

    ws = Workspace(config.workspace)
    pad_map = ws.get_pad_map()
    nuclear_map = ws.get_nuclear_map()
    start = time()
    for idx in range(config.run.run_min, config.run.run_max + 1, 1):

        if config.run.do_phase1:
            phase_1(idx, ws, pad_map, config.trace, config.cross, config.detector)

        if config.run.do_phase2:
            phase_2(idx, ws, config.cluster)

        if config.run.do_phase3:
            phase_3(idx, ws, config.estimate, config.detector)

        if config.run.do_phase4:
            #phase_4(idx, ws, config.detector, config.solver)
            phase_4_kalman(idx, ws, config.detector, config.solver, nuclear_map)
        
    stop = time()
    print(f'Total ellapsed runtime: {stop - start}s')