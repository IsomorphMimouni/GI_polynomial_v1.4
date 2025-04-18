# GI_polynomial v1.4

> 🔬 Efficient Graph Isomorphism Algorithm  
> 🧠 Developed by **Mohamed Mimouni**  
> 📅 Version 1.4 — April 2025  
> 🪪 License: GNU GPL v3.0

---

## 🚀 Overview

**GI_polynomial** is an efficient graph isomorphism algorithm designed to handle large graphs using a novel labeling and tree-based approach.  
This version (v1.4) significantly improves performance on rigid graphs with thousands of vertices.

The algorithm is implemented in **Python 3** and uses a **SQLite** database for structured data management.

---

## 🧠 Key Features

- Polynomial-time labeling heuristic
- Label propagation using pseudo-trees
- Multi-stage verification (vertices and edges)
- Supports large graphs (tested on 4,000+ vertices)
- Automatically detects isomorphic mappings
- Command-based modular execution (`01_install.py` to `12_fin.py`)

---

## 🗂️ File Structure


---

## 📝 How to Use

1. Install Python 3.x and ensure `sqlite3` is available (built-in).
2. Clone this repository.
3. Prepare your graph input files in `.txt` format using the format:
    ```
    e 1 2
    e 2 3
    ...
    ```
4. Set the input paths in `head.py`:
    ```python
    myfichier1 = "instances/graphA.txt"
    myfichier2 = "instances/graphB.txt"
    ```

5. Run the pipeline from step 01 to 12:
    ```bash
    python 01_install.py
    # ... all the way to
    python 12_fin.py
    ```

---

## 📊 Performance

Tested on rigid graphs up to **4000 vertices and 10,000+ edges**.  
Execution time ≈ **3 hours** on a standard CPU (Python + SQLite).

---

## 📁 Output

- `solutions.txt` → all possible images for each node in Graph A.
- `solutions_uniques.txt` → filtered list with only one-to-one matches.

---

## 👨‍💻 Author

**Mohamed Mimouni**  
Email: `mimouni.mohamed@gmail.com`  
Specialist in algorithms, graph theory, and educational software development.

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**  
See the [LICENSE](./LICENSE) file for more details.

---
