import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

###

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

def Rx(phi):
    return np.array([[1, 0, 0],
                     [0, np.cos(phi), -np.sin(phi)],
                     [0, np.sin(phi), np.cos(phi)]])

def Ry(theta):
    return np.array([[np.cos(theta), 0, np.sin(theta)],
                     [0, 1, 0],
                     [-np.sin(theta), 0, np.cos(theta)]])

def Rz(psi):
    return np.array([[np.cos(psi), -np.sin(psi), 0],
                     [np.sin(psi), np.cos(psi), 0],
                     [0, 0, 1]])

#########


mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
#fig.subplots_adjust(top=1, bottom=0, left=0, right=1, wspace=0)
ax = fig.gca(projection='3d')
theta = np.linspace(0, 4.5 * np.pi, 100)
z = np.linspace(0, 2, 100)
r = 1.8
x = r * np.cos(theta)
y = r * np.sin(theta)


#ax.legend()

plt.axis('off')



ax.plot(x, y, z,linewidth=2)  #ax.plot(x, y, z, label='parametric curve')
a = Arrow3D([0,2], [0,0],[0,0], mutation_scale=20, 
                lw=3, arrowstyle="-|>", color="black")
ax.add_artist(a)

a = Arrow3D([0,0], [0,2],[0,0], mutation_scale=20, 
                lw=3, arrowstyle="-|>", color="black")
ax.add_artist(a)

a = Arrow3D([0,0], [0,0],[0,2.5], mutation_scale=20, 
                lw=3, arrowstyle="-|>", color="black")
ax.add_artist(a)

ax.text(2.1,-0.0, 0.0 ,'x')
ax.text(0.0, 2.1, 0.0 ,'y')
ax.text(0.0, 0.0, 2.6 ,'z')

ax.view_init(elev=45, azim=45)
plt.tight_layout(pad=0.0,h_pad=0.0,w_pad=0.0)
#plt.show()
plt.savefig("helice.eps", bbox_inches='tight',pad_inches=0,dpi=720)
plt.savefig("helice.svg", bbox_inches='tight',pad_inches=0)

