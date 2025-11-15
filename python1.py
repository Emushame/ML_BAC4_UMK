import bac4
import pandas as pd

b = bac4.benefice(150, 100)
print("Le bénéfice est de :", b)

liste = pd.DataFrame(1, index=range(3), columns=range(4))
print(liste)
