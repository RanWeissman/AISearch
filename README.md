<h1 style="color: purple; font-size: 64px;">AISearch: Heuristic Search for 4-Peg Tower of Hanoi</h1>

## 🧠 Brief Explanation

This project tackles the **4-peg Tower of Hanoi** problem using advanced heuristic search techniques based on **Pattern Databases (PDBs)**. Unlike the classical 3-peg version, the 4-peg puzzle lacks a closed-form optimal solution and requires intelligent planning to solve efficiently.

We introduce and evaluate two novel heuristic strategies:
- **Pattern Databases Interaction (PDBI)**
- **Additive Pattern Databases Interaction (APDBI)**

These heuristics improve upon the standard **Additive PDB (APDB)** by accounting for interactions between subgroups of discs during the solution search. The core algorithm used is **A\***, supported by precomputed PDBs and a bucket-based strategy for enhanced performance and admissibility.

---
## 👨‍💻 Authors

The project was collaboratively developed by:

- Ran Weissman  
- Uriel Zaed
---

## 🙏 Acknowledgment

This project was conducted as part of the **Search in Artificial Intelligence** course under the mentorship of **Prof. Ariel Felner**.

---

## 📖 Citation

If you reference or build upon this work in your own research, please credit the original Tower of Hanoi and Pattern Database literature. We especially recommend citing:

- Korf, R.E., & Felner, A. (2002). *Disjoint Pattern Database Heuristics*. Artificial Intelligence, 134(1–2), 9–22.
- Felner, A., Korf, R.E., & Hanan, S. (2004). *Additive Pattern Database Heuristics*. Journal of Artificial Intelligence Research, 22, 279–318.

---

## 🌍 Area

- Artificial Intelligence  
- Heuristic Search  
- Pattern Databases  
- Puzzle Solving  
- Towers of Hanoi

---

## 🧑‍💻 Code Language

- **Python 3.8+**

---

## 🚀 How to Run




**Run A\* with Desired Heuristic**
   ```bash
   python main_5.py --heuristic PDBI --discs 8 --grouping 4-4
   ```

**Output**
   - Printed console output with expanded node count.
   - Optional CSV result summaries (if enabled in experiments).

---

## 📊 Analytics

The experiment compares the following heuristics:

- **APDB (Additive PDB)**
- **PDBI (Pattern Databases Interaction)**
- **APDBI (Additive Pattern Databases Interaction)**

### Evaluation Metrics

- **Number of Nodes Expanded**  
- **Search Time**  
- **Admissibility of Heuristics**  
- **Impact of Disc Groupings** (e.g., 4-4, 6-2, 5-3, etc.)

---

## 📈 Results Summary

### 8 Discs (Selected Groupings)

| Grouping | PDBI Expansions | Additive Expansions |
|----------|------------------|----------------------|
| 4-4      | 7,198            | 27,953               |
| 3-5      | 8,777            | 23,917               |
| 6-2      | 5,559            | 15,814               |
| 1-7      | 36,638           | 8,438                |

- **PDBI maintains admissibility** across all tested groupings.
- **APDBI is not always admissible**, though faster in simple scenarios.
- Larger disc groups benefit more from **PDBI** over Additive methods.

---

## 🔬 Future Improvements

- **Optimize the Bucket Pricing stage** (Stage 4 of PDBI), which currently dominates the runtime.
- **Limit A\*** to minimal initial states per bucket to reduce node expansions.
- **Detect common patterns** in initial configurations to prune redundant states.
- **Extend applicability** to larger disc counts (e.g., >31) by refining memory and time efficiency.

---