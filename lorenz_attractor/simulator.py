import matplotlib.pyplot as plt
import numpy as np
from lorenz_attractor.lorenz_dynamics import LorenzDynamics

class Simulator:
  def __init__(self, obj:LorenzDynamics) -> None:
    self.obj = obj
  
  def get_state_T0(self, state):
    dt = self.obj.step
    T0 = self.obj.T0
    num_steps = int(T0 / dt)
    derivative = []
    if T0 == 0:
      return state
    xi,yi,zi = state
    for i in range(num_steps):
      derivative = self.obj.__call__([xi,yi,zi])
      xi = xi + derivative[0] * dt
      yi = yi + derivative[1] * dt
      zi = zi + derivative[2] * dt
    return [xi,yi,zi]
  
  def run(self,state):
    dt = self.obj.step
    T0 = self.obj.T0
    T1 = self.obj.T1
    num_steps = int((T1 - T0) / dt)
    dots = np.empty((num_steps + 1, 3))
    derivative = []
    if T0 != 0:
      xi,yi,zi = self.get_state_T0(state)
    else:
      xi,yi,zi = state
    dots[0] = [xi,yi,zi]
    for i in range(num_steps):
      derivative = self.obj.__call__(dots[i])
      dots[i + 1][0] = dots[i][0] + derivative[0] * dt
      dots[i + 1][1] = dots[i][1] + derivative[1] * dt
      dots[i + 1][2] = dots[i][2] + derivative[2] * dt
    return dots

  def draw_attractor(self,state):
    dots = self.run(state)
    ax = plt.figure().add_subplot(projection='3d')

    ax.plot(*dots.T, lw=0.5)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")

    plt.show()
