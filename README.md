# HoneyAttack
Implementation of DLA and CUA attacks against the HoneyIndex honeyword scheme.

This repository contains the official source code, evaluation scripts, and data for the paper:

**When Updates Become a Vulnerability: Novel Attacks on the HoneyIndex Scheme**
*[Link to the paper]*

---

### About The Project

This project provides a detailed security analysis of Erguler's "HoneyIndex" scheme, a honeyword generation approach that creates decoy passwords by selecting from other existing users' passwords. The scheme, which relies on periodic updates, was declared to be ideally secure.

Our work demonstrates that this scheme has critical security flaws. We propose and implement two effective attack methodologies that can compromise the system with high success rates and a low probability of being detected.

### Key Contributions & Implemented Attacks

1.  **Double Leakage Attack (DLA):** An offline attack that leverages two password file leaks from different time periods. By intersecting sweetword sets and analyzing statistical information, DLA can fully break **over 93%** of user accounts.

2.  **Cross Update Attack (CUA):** A novel and stealthy online attack that requires only a *single* password file leak. The attacker waits for the system's periodic honeyword update and then launches strategically chosen login attempts. This method can identify real passwords while keeping the honeyword hitting probability (i.e., the chance of detection) **below 1%**.

### In This Repository

*   Python/C++ source code for the DLA and CUA attack simulators.
*   Scripts to run the evaluations on the real-world password datasets mentioned in the paper.
