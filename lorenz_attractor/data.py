from dataclasses import dataclass

@dataclass
class Data:
  rho: float = 28
  sigma: float = 10
  beta: float = 8/3
  sigma_x: float = 0
  sigma_y: float = 0
  sigma_z: float = 0
  T0: float = 0
  T1: float = 100
  step: float = 0.01
  

    