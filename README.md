
<h1>TOPSIS Implementation</h1>

<p><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></p>

<p>TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) is a decision-making technique used for ranking a set of alternatives by evaluating them against multiple criteria. This project provides a Python implementation of the TOPSIS algorithm.</p>



<h2 id="introduction">Introduction</h2>

<p>
    TOPSIS is a decision analysis technique that helps in selecting the best alternative from a set of options based on their performance against multiple criteria.
    This implementation provides a command-line tool for performing TOPSIS analysis on a given dataset.
</p>

<h2 id="features">Features</h2>

<ul>
    <li>Perform TOPSIS analysis on a dataset</li>
    <li>Support for both maximizing and minimizing criteria</li>
    <li>Easy-to-use command-line interface</li>
</ul>

<h2 id="installation">Installation</h2>

<h3>Prerequisites</h3>

<ul>
    <li>Python 3.x</li>
    <li>pip (Python package installer)</li>
</ul>

<h3>Installation Steps</h3>

<ol>
    <li>Clone the repository:</li>
    <code>git clone https://github.com/your_username/topsis-implementation.git</code>

    <li>Navigate to the project directory:</li>
    <code>cd topsis-implementation</code>

    <li>Install dependencies:</li>
    <code>pip install -r requirements.txt</code>
</ol>

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

<h2 id="contributing">Contributing</h2>

<p>
    Contributions are welcome! Follow these steps to contribute:
</p>

<ol>
    <li>Fork the repository.</li>
    <li>Create a new branch for your feature: <code>git checkout -b feature-name</code></li>
    <li>Commit your changes: <code>git commit -m 'Add new feature'</code></li>
    <li>Push to the branch: <code>git push origin feature-name</code></li>
    <li>Open a pull request.</li>
</ol>

<h2 id="license">License</h2>

<p>
    This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.
</p>

</body>
</html>
