from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
import numpy as np

%matplotlib widget
# # Create a new plot
figure = pyplot.figure()
axes = figure.add_subplot(projection='3d')

# # Load the STL files and add the vectors to the plot
your_mesh = mesh.Mesh.from_file('tests/stl_binary/duto_teste.stl')
# your_mesh = mesh.Mesh.from_file('tests/stl_ascii/canal_saida1.2_0009.stl')
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

# Auto scale to the mesh size
scale = your_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

# # Show the plot to the screen
pyplot.show()


# ax = pyplot.figure().add_subplot(projection='3d')
# ax.scatter(np.mean(your_mesh.x,1),
#            np.mean(your_mesh.y,1),
#            np.mean(your_mesh.z,1))


# ax = pyplot.figure().add_subplot(projection='3d')
# ax.quiver(np.mean(your_mesh.x,1),
#           np.mean(your_mesh.y,1),
#           np.mean(your_mesh.z,1),
#           your_mesh.normals[:,0],
#           your_mesh.normals[:,1],
#           your_mesh.normals[:,2],
#           color='red',
#           length=2)


def hhm_t(nx, ny, nz):
    if(nx >= 0):
        tx = -ny
        ty = 1 - ny**2/(nx + 1)
        tz = - ny*nz/(nx + 1)
    else:
        tx = ny
        ty = 1 + ny**2/(nx - 1)
        tz = ny*nz/(nx - 1)

    return np.array([tx, ty, tz])

def hhm_b(nx, ny, nz):
    if(nx >= 0):
        bx = -nz
        by = - ny*nz/(nx + 1)
        bz = 1 - nz**2/(nx + 1)
    else:
        bx = nz
        by = ny*nz/(nx - 1)
        bz = 1 + nz**2/(nx - 1)

    return np.array([bx, by, bz])

# function definition to compute magnitude o f the vector
def magnitude(vector): 
    return np.sqrt(sum(pow(element, 2) for element in vector))

normals = your_mesh.normals
normals_mag = np.linalg.norm(normals,axis=1)
for count in range(len(normals_mag)):
    normals[count] = normals[count]/normals_mag[count]

tangents = np.empty(your_mesh.normals.shape)
binormals = np.empty(your_mesh.normals.shape)
for count, normal in enumerate(normals):
    # print(normal)
    # normal = normal/magnitude(normal)
    # print(normal)
    tangents[count] = hhm_t(normal[0],normal[1],normal[2])
    # print(tangents[count])
    binormals[count] = hhm_b(normal[0],normal[1],normal[2])
    # print(binormals[count])
    # print("")


ax = pyplot.figure().add_subplot(projection='3d')
ax.quiver(np.mean(your_mesh.x,1),
          np.mean(your_mesh.y,1),
          np.mean(your_mesh.z,1),
          normals[:,0],
          normals[:,1],
          normals[:,2],
          color='red',
          length=0.025)
ax.quiver(np.mean(your_mesh.x,1),
          np.mean(your_mesh.y,1),
          np.mean(your_mesh.z,1),
          tangents[:,0],
          tangents[:,1],
          tangents[:,2],
          color='blue',
          length=0.025)
ax.quiver(np.mean(your_mesh.x,1),
          np.mean(your_mesh.y,1),
          np.mean(your_mesh.z,1),
          binormals[:,0],
          binormals[:,1],
          binormals[:,2],
          color='black',
          length=0.025)
ax.auto_scale_xyz(scale, scale, scale)


ax = pyplot.figure().add_subplot(projection='3d')
ax.quiver(np.mean(your_mesh.x,1)[0],
          np.mean(your_mesh.y,1)[0],
          np.mean(your_mesh.z,1)[0],
          normals[0,0],
          normals[0,1],
          normals[0,2],
          color='red',
          length=0.01)
ax.quiver(np.mean(your_mesh.x,1)[0],
          np.mean(your_mesh.y,1)[0],
          np.mean(your_mesh.z,1)[0],
          tangents[0,0],
          tangents[0,1],
          tangents[0,2],
          color='blue',
          length=0.01)
ax.quiver(np.mean(your_mesh.x,1)[0],
          np.mean(your_mesh.y,1)[0],
          np.mean(your_mesh.z,1)[0],
          binormals[0,0],
          binormals[0,1],
          binormals[0,2],
          color='black',
          length=0.01)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# ax.view_init(0, 45, 0)


ax = pyplot.figure().add_subplot(projection='3d')
ax.quiver([0.025],
          [0.42],
          [0.5485],
          [-0.38],
          [0.34],
          [0.85],
          color='red',
          length=0.01)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim((0.025-0.03,0.025+0.03))
ax.set_ylim((0.42-0.03,0.42+0.03))
ax.set_zlim((0.5485-0.03,0.5485+0.03))


# import matplotlib.pyplot as plt

# from mpl_toolkits.mplot3d import axes3d

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')

# # Grab some example data and plot a basic wireframe.
# X, Y, Z = axes3d.get_test_data(0.05)
# ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

# # Set the axis labels
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')

# # Rotate the axes and update
# for angle in range(0, 360*4 + 1):
#     # Normalize the angle to the range [-180, 180] for display
#     angle_norm = (angle + 180) % 360 - 180

#     # Cycle through a full rotation of elevation, then azimuth, roll, and all
#     elev = azim = roll = 0
#     if angle <= 360:
#         elev = angle_norm
#     elif angle <= 360*2:
#         azim = angle_norm
#     elif angle <= 360*3:
#         roll = angle_norm
#     else:
#         elev = azim = roll = angle_norm

#     # Update the axis view and title
#     ax.view_init(elev, azim, roll)
#     plt.title('Elevation: %d°, Azimuth: %d°, Roll: %d°' % (elev, azim, roll))

#     plt.draw()
#     plt.pause(.001)
