import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', 15)

aq = pd.read_csv('LaqnData.csv')
aq = pd.DataFrame(aq)

#Metadata
aq.head()
aq.shape
aq.dtypes
aq = aq.rename(index=str, columns={'Provisional or Ratified': 'PR'})

#Most of them are at the same site, HR2. The other 9 are most likely mistakes.
aq.Site.describe()
aq.Site.value_counts()

#3 different species found, meaning 3 different types of molecules measured.
aq.Species.unique()
aq.Species.value_counts()

#3 different measurements per site per date confirmed by having 3 counts per ReadingDateTime.
aq.ReadingDateTime.value_counts()

#i assume the units are all the same, but just to check...
aq.Units.value_counts()
#So NO2 has it's own category, but it's in ug m-3 so the same unit.

aq.PR.unique()
aq.PR.value_counts()