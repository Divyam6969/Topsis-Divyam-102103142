__author__ = "Divyam Malik"
__email__ = "divyammalik2003@gmail.com"

import sys
import pandas as pd
import numpy as np

class Topsis:
    def __init__(self, evaluation_matrix, weights, impacts):
        self.evaluation_matrix = np.array(evaluation_matrix, dtype="float")
        self.row_size, self.column_size = self.evaluation_matrix.shape
        self.weights = np.array(weights, dtype="float")
        self.weights = self.weights / sum(self.weights)
        self.impacts = np.array([1 if impact == '+' else -1 for impact in impacts], dtype="float")

        # Check if the number of weights, impacts, and columns match
        if len(self.weights) != self.column_size or len(self.impacts) != self.column_size:
            raise ValueError("Number of weights, impacts, and columns must be the same.")

    def normalize_matrix(self):
        self.normalized_decision = self.evaluation_matrix / np.linalg.norm(self.evaluation_matrix, axis=0)

    def calculate_weighted_normalized(self):
        self.weighted_normalized = self.normalized_decision * self.weights

    def determine_worst_best_alternatives(self):
        self.worst_alternatives = np.min(self.weighted_normalized, axis=0)
        self.best_alternatives = np.max(self.weighted_normalized, axis=0)

    def calculate_distances(self):
        self.worst_distance = np.linalg.norm(self.weighted_normalized - self.worst_alternatives, axis=1)
        self.best_distance = np.linalg.norm(self.weighted_normalized - self.best_alternatives, axis=1)

    def calculate_topsis_score(self):
        self.topsis_score = self.worst_distance / (self.worst_distance + self.best_distance)

    def rank_to_similarity(self, similarity_array):
        return [rank + 1 for rank in similarity_array.argsort()]

    def rank_to_worst_similarity(self):
        return self.rank_to_similarity(self.worst_distance)

    def rank_to_best_similarity(self):
        return self.rank_to_similarity(self.best_distance)

    def rank_to_topsis_score(self):
        return self.rank_to_similarity(-self.topsis_score)

    def calculate_topsis(self):
        self.normalize_matrix()
        self.calculate_weighted_normalized()
        self.determine_worst_best_alternatives()
        self.calculate_distances()
        self.calculate_topsis_score()
    

def run_topsis(input_file, weights, impacts, output_file):
    try:
        # Read the CSV file
        data = pd.read_csv(input_file)
        # Print the number of weights, impacts, and columns
        print("Topsis Code Written By: Divyam 102103142")
        # print("Number of Weights:", len(weights))
        # print("Number of Impacts:", len(impacts))
        # print("Number of Columns:", data.shape[1] - 1)  # Excluding the non-numeric first column

        # Check if the input file contains three or more columns
        if data.shape[1] < 3:
            raise ValueError("Input file must contain three or more columns.")

        # Extracting data columns, skipping non-numeric values in the first column
        numeric_data = data.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').values
        if np.isnan(numeric_data).any():
            raise ValueError("Columns from 2nd to last must contain numeric values only.")

        # Create an instance of the Topsis class
        topsis_instance = Topsis(numeric_data, weights, impacts)

        # Call the TOPSIS calculation
        topsis_instance.calculate_topsis()

        # Get ranks based on worst, best, and TOPSIS score
        # worst_ranks = topsis_instance.rank_to_worst_similarity()
        # best_ranks = topsis_instance.rank_to_best_similarity()
        topsis_score_ranks = topsis_instance.rank_to_topsis_score()

        # Create a new DataFrame with original data, TOPSIS scores, and ranks
        result_data = pd.concat([data.iloc[:, 0], pd.DataFrame(numeric_data)], axis=1)
        result_data['Topsis Score'] = topsis_instance.topsis_score
        # result_data['Worst Similarity Rank'] = worst_ranks
        # result_data['Best Similarity Rank'] = best_ranks
        result_data['Topsis Score Rank'] = topsis_score_ranks

        # Save the result to a new CSV file
        result_data.to_csv(output_file, index=False)

        print("TOPSIS analysis completed. Results saved to", output_file)

    except FileNotFoundError:
        print("File not found. Please provide a valid input file.")
    except ValueError as ve:
        print("An error occurred:", str(ve))

def main():

    if len(sys.argv) != 5:
        print("Usage: python tospis_program.py <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file = sys.argv[1]
    weights = list(map(float, sys.argv[2].split(',')))
    impacts = sys.argv[3].split(',')
    output_file = sys.argv[4]

    run_topsis(input_file, weights, impacts, output_file)



if __name__ == "__main__":
    main()