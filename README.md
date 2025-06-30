# Metropolis-Hastings Simulation Study 🧪

This project explores the **Metropolis-Hastings (MH)** algorithm for sampling from probability distributions using Python. It was developed as part of a graduate course in *Statistical Inference* at Virginia Tech.

---

## 📌 Project Overview

The Metropolis-Hastings algorithm is a powerful **Markov Chain Monte Carlo (MCMC)** method used to draw samples from complex distributions. In this project, we simulate:

- Sampling from **t-distribution** using:
  - A standard **normal proposal** (unconditional)
  - A **conditional normal proposal** (centered at the previous sample)
- Sampling from a **normal distribution** using a **t-distribution** proposal

For each case, we test various sample sizes and degrees of freedom to evaluate how well the algorithm captures the target distribution.

---

## 🎯 Relevance to ML & AI

Metropolis-Hastings is foundational in:
- **Bayesian inference**
- **Generative models**
- **Probabilistic programming**
- **Machine learning research**

Understanding its behavior improves insight into convergence, posterior approximation, and sampling efficiency — all highly relevant in AI/ML roles.

---

## 🗂️ Repository Structure

```
.
├── mh_sampler.py         # Core M-H logic
├── experiments.py        # Run different sampling experiments
├── plot_utils.py         # Plotting: histograms, QQ plots
├── results/              # Generated figures
├── report.pdf            # Final written report (with discussion and figures)
└── README.md             # This file
```

---

## ▶️ How to Run

1. Install dependencies:
```bash
pip install numpy scipy matplotlib
```

2. Run a simulation (example):
```bash
python experiments.py
```

3. Output figures will be saved to the `results/` folder.

---

## 📈 Sample Output

Histogram of samples from a t-distribution (ν = 5) using a normal proposal:

![Histogram](results/hist_t_from_normal.png)

QQ plot comparing target and sampled distributions:

![QQ Plot](results/qq_t_from_normal.png)

---

## 📄 Full Report

The full project report (written in LaTeX) explains the setup, methodology, analysis, and conclusions. It includes dozens of figures demonstrating convergence behavior.

📎 [Download the report (PDF)](./report.pdf)

---

## ✍️ Author

**Saeed Mohseni**  
Graduate Student, Electrical & Computer Engineering, Virginia Tech  
🧠 Passionate about Machine Learning, Statistical Methods, and Simulation-Based Inference

---

## ⭐️ If you find this project insightful, consider starring it on GitHub!
