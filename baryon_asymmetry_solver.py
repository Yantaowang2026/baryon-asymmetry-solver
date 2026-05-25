"""
Baryon Asymmetry Exact Solver
==============================
Author: Wang Yantao
Zenodo DOI: 10.5281/zenodo.20299118
Date: 2026-05-20

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IMPORTANT: This script is a NUMERICAL VERIFICATION TOOL only.
It is NOT the derivation itself.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The complete derivation is in the paper (9 pages):
    https://zenodo.org/records/20299118
    DOI: 10.5281/zenodo.20299118

Where each constant comes from (see paper for full proofs):

    kappa = 16/3  (exact analytic value: 5.3333...)
        → Unique eigenvalue of a boundary value problem.
        → Derived from variational minimization dE/dR = 0
          applied to the master equation potential V(Phi).
        → Full proof in Sections 8-12, including exhaustion
          of all alternative solution families via
          Picard-Lindelof theorem.
        → NOT a free parameter. NOT a numerical fit.

    x = tau_cross / R* = 0.5166
        → tau_cross = 6*sigma (wall crossing dynamics)
        → R* = kappa * xi (nucleation scale)
        → sigma cancels algebraically in the full eta_B
          expression (structural identity, not approximation).
          See Section 3.5 and Section 10.

    delta_B = (9/2) * sqrt(x) * arctan(sqrt(x)) = 2.016
        → Derived by integrating the potential asymmetry
          current dB/dtau over the transition-layer crossing.
        → Full derivation in Section 3.4.
        → NOT an arbitrary function. NOT constructed to fit.

    Denominator = 256 * pi  (exact)
        → Follows from kappa = 16/3:
          denom = 6 * (16/3) * 8 * pi = 256 * pi
        → Decimal approximation: 804.247...

    T_CMB = 2.725 K, T_surface = 5500 K
        → Two independent observational boundary conditions.
        → T_CMB: measured by Planck satellite.
        → T_surface: consistent with structural necessity
          Phi_surface = 1 of the master equation potential
          V(Phi) = -Phi^2/2 + Phi^4/4 (stable minimum at
          Phi = 1). See Section 13.
        → Their ratio f_m = T_CMB/T_surface fixes the global
          potential value at the current epoch.

    The observed eta_B value (6.12e-10) is NOT used
    as an input at any stage of the derivation.
    The 0.49% agreement is a genuine prediction, not a fit.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

import math

T_CMB     = 2.725
T_surface = 5500.0

kappa            = 16.0 / 3.0
tau_cross_over_R = 0.5166

f_m     = T_CMB / T_surface
x       = tau_cross_over_R
sqrt_x  = math.sqrt(x)
delta_B = (9.0/2.0) * sqrt_x * math.atan(sqrt_x)
denom   = 256.0 * math.pi
eta_B   = (delta_B / denom) * (f_m ** 2)

eta_B_planck = 6.12e-10
deviation    = abs(eta_B - eta_B_planck) / eta_B_planck * 100

print("=" * 60)
print("  Baryon Asymmetry Exact Solver")
print("  Numerical verification only — see paper for derivation")
print("=" * 60)
print()
print("── Inputs ──────────────────────────────────────────────")
print(f"  T_CMB              = {T_CMB} K")
print(f"  T_surface          = {T_surface} K")
print()
print("── Derivation chain ────────────────────────────────────")
print(f"  f_m = T_CMB/T_surface  = {f_m:.10e}")
print(f"  f_m^2                  = {f_m**2:.10e}")
print()
print(f"  kappa = 16/3           = {kappa:.6f}  [Sections 8-12]")
print(f"  x = tau_cross/R*       = {x}      [Section 3.4]")
print(f"  delta_B                = {delta_B:.6f}  [Section 3.4]")
print(f"  Denominator = 256*pi   = {denom:.6f}  [Section 3.5]")
print()
print("── Result ──────────────────────────────────────────────")
print(f"  eta_B = {eta_B:.6e}")
print()
print("── Comparison with Planck 2018 ─────────────────────────")
print(f"  This derivation : eta_B = {eta_B:.4e}")
print(f"  Planck 2018     : eta_B = {eta_B_planck:.4e}")
print(f"  Deviation       : {deviation:.2f}%")
print()
print("── Quick verification (any calculator, 5 minutes) ──────")
print("  eta_B = (2.016 / (256*pi)) * (T_CMB / T_surface)^2")
print(f"        = {(2.016/(256*math.pi))*(T_CMB/T_surface)**2:.6e}")
print()
print("── Reference ───────────────────────────────────────────")
print("  Full derivation (9 pages):")
print("  https://zenodo.org/records/20299118")
print("  DOI: 10.5281/zenodo.20299118")
print("=" * 60)
