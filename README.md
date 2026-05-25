# Baryon Asymmetry Exact Solver

**Author:** Yantao Wang (Independent Researcher)
**Paper:** https://zenodo.org/records/20299118
**DOI:** 10.5281/zenodo.20299118

---

## What this is

A numerical verification tool for the parameter-free derivation
of the baryon-to-photon ratio eta_B.

This script is NOT the derivation itself.
The complete derivation (9 pages) is in the paper above.

---

## Five-minute verification

eta_B = (2.016 / (256*pi)) * (2.725 / 5500)^2 = 6.15e-10
Planck 2018: 6.12e-10, deviation 0.49%, zero free parameters.

---

## FAQ

**Q1: Where does 5500 K come from?**
V(Phi)=-Phi^2/2+Phi^4/4 has stable minimum at Phi=1.
With T=Lambda|Phi| and Phi_surface=1, T_surface=Lambda.
Anchored by T_CMB: Lambda=2.725/4.9545e-4=5499.7 K (0.018% from 5500 K).
5500 K is not the Sun's special property — it is the temperature
mapping of the stable state Phi=1.

**Q2: Is this circular reasoning?**
No. Chain is one-directional:
master equation → kappa=16/3 → delta_B=2.016 → denom=256*pi → eta_B.
The observed value 6.12e-10 never appears in the derivation.
Reverse check: kappa_reverse=5.34, differs from 16/3=5.3333...
by 0.2%. If circular, this difference would be zero.

**Q3: Two inputs or one?**
Two observational boundary conditions: T_CMB and T_surface.
Both are fixed public values, not adjustable parameters.
T_surface is consistent with structural necessity Phi_surface=1
(see paper Section 13).

**Q4: Why is V(Phi) this specific form?**
Four constraints uniquely determine it:
1. Two stable minima (Axiom B)
2. Unstable maximum between them (Axiom C)
3. Lowest-order polynomial (Axiom A, simplicity)
4. Z2 symmetry (Phi -> -Phi)
Not chosen — constrained.

**Q5: Where does kappa=16/3 come from?**
Exact analytical solution of dE/dR=0:
xi=sqrt(2C), sigma_wall=2*sqrt(2C)/3, Delta_V=1/4
R*=2*sigma_wall/Delta_V, kappa=R*/xi=16/3.
Factor sqrt(2C) cancels exactly. Pure structural constant.
Reverse check: kappa_reverse=5.34, confirming no circular fit.

**Q6: Why the Sun? Other stars have different surface temperatures.**
5500 K is not the Sun's special property.
Phi=1 is the stable minimum of V(Phi) — a mathematical necessity.
Any stellar photosphere in the stable state Phi=1 maps to
the same energy scale Lambda. Different observed temperatures
reflect different local conditions, not a contradiction.

**Q7: Where does the master equation itself come from?**
Three axioms: (A) potential exists, (B) competing tendencies,
(C) any extremum triggers reversal.
The master equation is the minimal mathematical expression
of these three axioms. It was not constructed to explain
any specific phenomenon — the results emerged after the fact.

**Q8: Is the 0.49% deviation a coincidence or fine-tuned?**
Neither. kappa=16/3 is an exact analytical result.
If the result were fine-tuned, back-calculating from
eta_B_obs=6.12e-10 would give kappa_reverse=16/3 exactly.
Instead, kappa_reverse=5.34, differing by 0.2%.
The residual 0.49% deviation is genuine, not fitted to zero.
