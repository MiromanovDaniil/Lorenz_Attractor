from lorenz_attractor.lorenz_dynamics import LorenzDynamics
from lorenz_attractor.simulator import Simulator
from lorenz_attractor.data import Data

args_1 = {"rho": 28, "sigma": 10, "beta": 8/3, "sigma_x": 0,
          "sigma_y": 0, "sigma_z": 0, "T0": 50, "T1": 100, "step": 0.01}
args_2 = {"rho": 14, "sigma": 10, "beta": 8/3, "sigma_x": 0,
          "sigma_y": 0, "sigma_z": 0, "T0": 0, "T1": 100, "step": 0.01}
args_3 = {"rho": 15, "sigma": 10, "beta": 8/3, "sigma_x": 0,
          "sigma_y": 0, "sigma_z": 0, "T0": 0, "T1": 100, "step": 0.01}

state = {"x": 0., "y": 1., "z": 1.05}

data_1 = Data(**args_1)
data_2 = Data(**args_2)
data_3 = Data(**args_3)

attractor = LorenzDynamics(data_2)
simulation = Simulator(attractor)
dots = simulation.run(list(state.values()))
print(dots)
simulation.draw_attractor(list(state.values()))
