import pandas as pd

# We'll also import seaborn, a Python graphing library
import warnings # current version of seaborn generates a bunch of warnings that we'll ignore
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

# Next, we'll load the Iris flower dataset, which is in the "../input/" directory
iris = pd.read_csv("tfidf1.csv") # the iris dataset is now a Pandas DataFrame


# Press shift+enter to execute this cell

iris.plot(kind="scatter", x="tf", y="idf")
plt.show()