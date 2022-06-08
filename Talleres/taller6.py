#%%
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
plt.style.use('default')
plt.style.use('dark_background')

#PUNTO B
def punto_B(num_points=30000, lambda_poisson=10, k=0):
    #Distribución de Poisson
    #p(x)=((e^(-lambda))*(lambda^x))/(x!))=((e^(-10))*(lambda^0))/(0!)
    x = np.arange(0, num_points, 1)
    y = stats.poisson.pmf(x, mu=lambda_poisson)
    min_x = -10
    max_x = 10
    min_y = 0.0
    max_y = np.amax(y)
    random_y = np.random.rand(num_points) * (max_y - min_y) + min_y
    index = np.where(y - random_y > 0.0)
    interval_integral = (max_y-min_y) * (max_x - min_x)
    integral  = interval_integral * (np.size(index)/(1.0*np.size(random_y)))
    print(f"a) P = {integral*100}")
punto_B()
# %%