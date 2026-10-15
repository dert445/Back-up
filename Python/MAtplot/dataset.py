

import pandas as pd
import numpy as np

# Set seed for reproducible results
np.random.seed(42)

# Generate synthetic company data (12 months)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
data = {
    'Month': months,
    'Online_Sales': np.random.randint(20000, 50000, size=12),
    'InStore_Sales': np.random.randint(15000, 40000, size=12),
    'Marketing_Spend': np.random.randint(5000, 15000, size=12),
    'New_Customers': np.random.randint(100, 1000, size=12),
    'Region_Best': np.random.choice(['North', 'East', 'South', 'West'], size=12)
}

df = pd.DataFrame(data)
print(df.head())
df.to_csv("data.csv")