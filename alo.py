import numpy as np
import pandas as pandas
import matplotlib.pyplot as plt
import matplotlib as mpl
plt.style.use('ggplot')
#mpl.style.use('classic')
import pandas as pd

quick = pd.read_csv("quick.txt", sep = '\t')
heap = pd.read_csv("heap.txt", sep = '\t')
plt.plot(quick.length, quick.reversed, label = 'quicksort')
plt.plot(heap.length, heap.reversed, label = 'heapsort')
plt.ylim(0, 15)
plt.legend()
plt.plot()
plt.xlabel('Array size')
plt.ylabel('Seconds')
plt.show()