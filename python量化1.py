import pandas as pd

mydataser = {
    'sites':["Google","Runoob","wiki"],
    'number':[1,2,3]
}

myvar = pd.DataFrame(mydataser)
print(myvar)