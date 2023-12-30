
<!DOCTYPE html>
<html lang="en">

<body>

  <h1>Data Mining with Python</h1>

  <h2>Description</h2>
  <p>
    This project scrapes a Q&A website (Khmer language-based) to generate intents for a conversational AI system. It utilizes web scraping techniques, natural language processing, and data structuring to create a dataset of tagged intents for training language models.
  </p>

  <h2>Features</h2>
  <ul>
    <li><strong>Web Scraping:</strong> Utilizes requests and BeautifulSoup for data extraction from the website.</li>
    <li><strong>NLP Tagging:</strong> Implements the KhmerNLP library for part-of-speech tagging.</li>
    <li><strong>Intent Generation:</strong> Gathers unique nouns from questions to form intent patterns and extracts corresponding answers.</li>
  </ul>

  <h2>Installation</h2>
  <ol>
    <li>Clone the repository:
      <code>git clone https://github.com/your-username/repo-name.git</code>
    </li>
    <li>Install dependencies:
      <code>pip install -r requirements.txt</code>
    </li>
  </ol>

  <h2>Usage</h2>
  <ol>
    <li>Run the Python script <code>generate_intents.py</code>.</li>
    <li>The script will scrape the Q&A website and generate a JSON file (<code>data_intents.json</code>) containing intents for conversational AI systems.</li>
  </ol>

  <h2>Example</h2>
  <pre><code>python generate_intents.py</code></pre>

  <h2>Dependencies</h2>
  <ul>
    <li><code>requests</code></li>
    <li><code>beautifulsoup4</code></li>
    <li><code>khmernltk</code></li>
  </ul>

  <h2>Data Structure</h2>
  <p>The generated JSON file (<code>data_intents.json</code>) follows the structure:</p>
  <pre>
    <code>
{
  "intents": [
    {
      "tag": "id_1",
      "patterns": ["Question Pattern 1", "Noun Pattern 1"],
      "responses": ["Answer 1"]
    },
    // Other intents follow the same structure
  ]
}
    </code>
  </pre>

  <h2>Contribution</h2>
  <ol>
    <li>Fork the repository.</li>
    <li>Create a new branch (<code>git checkout -b feature/new-feature</code>).</li>
    <li>Make your changes and commit (<code>git commit -am 'Add new feature'</code>).</li>
    <li>Push to the branch (<code>git push origin feature/new-feature</code>).</li>
    <li>Create a new Pull Request.</li>
  </ol>

  <h2>License</h2>
  <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>

  <h2>Credits</h2>
  <ul>
    <li>Developed by <a href="https://github.com/soytet">SOY TET</a></li>
    <li>KhmerNLP Library: <a href="https://github.com/KhmerNLP/khmer-nltk">Link</a></li>
  </ul>

</body>
</html>
