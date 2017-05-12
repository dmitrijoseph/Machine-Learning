# MatplotLib
import matplotlib.pyplot as plt
import numpy as np

objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10, 8, 6, 4, 2, 1]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
plt.show()

# Bokeh
from bokeh.charts import Bar, show
import pandas as pd

dictionary = {'languages':objects, 'values':performance}
df = pd.DataFrame(dictionary)
p = Bar(df, 'languages', values='values', title='Programming language usage')
show(p)
