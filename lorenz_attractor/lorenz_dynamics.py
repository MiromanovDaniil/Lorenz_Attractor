import random
from lorenz_attractor.data import Data

class LorenzDynamics:
  # Начальные условия
  #self, rho, sigma, beta, sigma_x, sigma_y, sigma_z, T0, T1, step
  def __init__(self, data: Data) -> None:
    self.sigma = data.sigma 
    self.rho = data.rho 
    self.beta = data.beta 
    self.sigma_x = data.sigma_x
    self.sigma_y = data.sigma_y
    self.sigma_z = data.sigma_z
    self.step = data.step
    self.T0 = data.T0
    self.T1 = data.T1
    
  # Уравнения Лоренца
  def __call__(self, state) -> [float, float, float]:
    x, y, z = state
    
    noise_x = random.gauss(0, self.sigma_x)
    noise_y = random.gauss(0, self.sigma_y)
    noise_z = random.gauss(0, self.sigma_z)
    
    dxdt = self.sigma * (y - x) + noise_x
    dydt = x * (self.rho - z) - y + noise_y
    dzdt = x * y - self.beta * z + noise_z
    return [dxdt, dydt, dzdt]