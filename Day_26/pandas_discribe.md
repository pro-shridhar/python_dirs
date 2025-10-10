There is a convenient describe() function which computes a variety of summary statistics about a Series or the columns of a DataFrame (excluding NAs of course):

  => series = pd.Series(np.random.randn(1000))

You can select specific percentiles to include in the output:

  => series.describe(percentiles=[0.05, 0.25, 0.75, 0.95])

For a non-numerical Series object, describe() will give a simple summary of the number of unique values and most frequently occurring values:

Note that on a mixed-type DataFrame object, describe() will restrict the summary to include only numerical columns or, if none are, only categorical columns:

This behavior can be controlled by providing a list of types as include/exclude arguments. The special value all can also be used:
   
  ==> frame = pd.DataFrame({"a": ["Yes", "Yes", "No", "No"], "b": range(4)})

  ==> frame.describe(include=["object"])