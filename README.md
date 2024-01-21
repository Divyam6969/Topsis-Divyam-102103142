# Topsis Python Package

Made By
Divyam Malik (Roll No. 102103142)

## Description

The Topsis Python Package is a Python library that provides an implementation of the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) method. TOPSIS is a multi-criteria decision-making method used to determine the best alternative among a set of alternatives based on their performance on multiple criteria.


<h2 id="usage">Usage</h2>

<p>
    Use the following command to perform TOPSIS analysis on a dataset:
</p>

<code>topsis data.csv "1,0,1,0,1" "+,-,+,-,+"</code>

<p>
    - <code>data.csv</code>: Path to the input CSV file containing the dataset.<br>
    - <code>"1,0,1,0,1"</code>: Weights for each criterion separated by commas.<br>
    - <code>"+,-,+,-,+"</code>: Impacts for each criterion (either <code>+</code> for maximizing or <code>-</code> for minimizing).
</p>

<p>
    The output will be saved in a file named <code>output.csv</code>.
</p>



