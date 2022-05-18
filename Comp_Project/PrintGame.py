import pandas as pd

# For Printing Matrix in a Proper Tabular Form
def print2DMatrix(Mat2D):
    df = pd.DataFrame(Mat2D)
    # Replacing 0 with _
    df = df.replace(0,"_")
    print(df.to_string(header=None, index=False))


