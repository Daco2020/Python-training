import pandas as pd

from datetime import datetime


now = datetime.now()

df = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

print(df.to_dict(orient="records"))


market = "upbit-krw"
a = market.split("-")[1].upper()
print(a)
