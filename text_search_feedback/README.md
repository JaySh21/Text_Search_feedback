# Text Search with Feedback

This project provides a simple text search system that learns from feedback. It uses TF-IDF vectorization and cosine similarity to find the most relevant documents for a given query.

## Directory Structure

- `data/`: Contains the text documents.
- `src/`: Source code for preprocessing and search functionality.
- `notebooks/`: Jupyter Notebook for experimentation.
- `tests/`: Unit tests.
- `.gitignore`: Specifies files and directories to ignore in Git.
- `README.md`: Provides an overview of the project.
- `requirements.txt`: Lists the dependencies.

## Installation

1. Clone the repository.
2. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

You can run the Jupyter Notebook in the `notebooks/` directory to experiment with the text search system. To run the unit tests, use:
```sh
python -m unittest discover -s tests
