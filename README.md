# Collaborative Software Development with Python

This package demonstrates collaborative software development concepts using a simple model of `Student` objects organized in a `Team`. Students can have relationships as either neighbors or acquaintances, which can be visualized as a graph using `networkx`.

## Features

- Define student relationships as neighbors and acquaintances.
- Visualize relationships using a graph representation.
- Easily extendable to include additional attributes and methods for further scenarios.

## Installation

Follow these steps to set up the package in a new conda environment:

1. **Clone the repository** (if applicable):
    ```bash
    git clone git@github.com:flo-schu/collaborative-software-development.git  # (with ssh)
    cd collaborative-software-development
    ```

2. **Create and activate a conda environment**:
    ```bash
    conda create -n csd python=3.11
    conda activate csd
    ```

3. **Install the package** in editable mode along with required libraries:
    ```bash
    pip install -e .
    ```

## Usage

To run the program, execute the following command:

```bash
python main.py