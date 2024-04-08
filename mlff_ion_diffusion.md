CH3NH3PbI3; all tests on dardel

System size: 384 atoms (perfect cell), 381 atoms (one Pb+2 vacancy, 2 I- vacancies, even electrons) 

- Equilibration is achieved in ~800fs (looking at velocity autocorrelation function), T = 300. K
- Goal: match g(r) after equilibration for ![perfect cell](./perfect_cell.jpeg "Perfect cell").
- Limitation: AIMD for MAPbI3 seems to be memory intensive

Ref: AIMD for 1ps
   1. 128 cores
   Walltime: 14.12 hours
   2. 196 cores
   Walltime: 
   3. 256 cores
   Walltime:
   4. 512 cores
   Walltime: 

MLFF - AIMD - 1000 steps (1fs each):
   1. 128 cores
   Walltime: 2.3585 hours
   2. 196 cores
   Walltime: 
   3. 256 cores
   Walltime: 
   4. 512 cores
   Walltime: 

- Diffusion events, need ~10 ps at the least for halides, more for cation diffusion