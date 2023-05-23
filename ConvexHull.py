# **** ****
import matplotlib.pyplot as plt                     # Plotting

# **** ****
from skimage.morphology import convex_hull_image    # Convex Hull
from skimage import data, img_as_float              # Image
from skimage.util import invert                     # Invert Image


# **** read horse_image ****
horse_image = data.horse()

# **** invert horse_image ****
horse_inverted = invert(data.horse())

# **** ****
fig, axes = plt.subplots(   1, 
                            2, 
                            figsize=(12, 8),        # width, height in inches
                            sharex=True,            # x-axis will be shared among all subplots
                            sharey=True)            # y-axis will be shared among all subplots

# **** flatten axes ****
ax = axes.ravel()

# **** plot horse_image ****
ax[0].set_title('horse_image')
ax[0].imshow(   horse_image,
                cmap='gray')

# **** plot horse_inverted ****
ax[1].set_title('horse_inverted')
ax[1].imshow(   horse_inverted,
                cmap='gray')

# **** fit plots within your figure cleanly (an alternative to tight_layout is constrained_layout) ****
fig.tight_layout()

# **** display the plots****
plt.show()


# **** convex hull of horse_inverted ****
covexhull_horse = convex_hull_image(horse_inverted)

fig, axes = plt.subplots(   1,
                            2,
                            figsize=(12, 12),
                            sharex=True,
                            sharey=True)

# **** flatten axes ****
ax = axes.ravel()

# **** plot horse_inverted ****
ax[0].set_title('horse_inverted')
ax[0].imshow(   horse_inverted,
                cmap='gray',
                interpolation='nearest')

# **** plot convex hull of horse_inverted ****
ax[1].set_title('convex hull of horse_inverted')
ax[1].imshow(   covexhull_horse,
                cmap='gray',
                interpolation='nearest')

# **** fit plots within your figure cleanly (an alternative to tight_layout is constrained_layout) ****
fig.tight_layout()

# **** display the plots ****
plt.show()


# **** ****
convexhull_diff = img_as_float(covexhull_horse.copy())
convexhull_diff[horse_inverted] = 2                     # 2: white

# **** ****
fig, ax = plt.subplots(1, 1, figsize=(12, 8))           # width, height in inches

# **** ****
ax.imshow(  convexhull_diff,
            cmap='gray',
            interpolation='nearest')
ax.set_title('Difference between inverted and convex hull image')
plt.show()