# OpenFOAM Cases Generated by Veen



- Basic OpenFOAM usage with script
- simpleFoam pisoFoam pimpleFoam usage
- RANS LES model study
- Euler-Euler multiphase case
- Euler-Lagrangian multiphase case
- and so on ...

## Case description

```bash
.
├── 2D_Plane_EE_Multiphase
├── 2D_Plane_LES
├── 2D_Plane_pimpleFoam
├── 2D_Plane_pisoFoam
├── 2D_Plane_simpleFoam
├── Airway_EL_run
├── Flow_around_cylider
├── VIV_cylider
├── LICENSE
└── README.md
```



> #### 2D Plane EE Multiphase

This case is an Euler-Euler multiphase case around an plane using OpenFOAM-7, not fix to OpenFOAM-8.

The mesh generated by snappyHexMesh, solving by twoPhaseEulerFoam.

```bash
.
├── 0_org
│   ├── alpha.air
│   ├── alpha.particles
│   ├── alphat.air
│   ├── alphat.particles
│   ├── epsilon.air
│   ├── k.air
│   ├── nut.air
│   ├── nut.particles
│   ├── p
│   ├── p_rgh
│   ├── T.air
│   ├── Theta.particles
│   ├── T.particles
│   ├── U.air
│   └── U.particles
├── Allrun
├── constant
│   ├── extendedFeatureEdgeMesh
│   │   └── plane.extendedFeatureEdgeMesh
│   ├── g
│   ├── include
│   │   └── turbulenceModels
│   ├── phaseProperties
│   ├── thermophysicalProperties.air
│   ├── thermophysicalProperties.particles
│   ├── triSurface
│   │   ├── plane.eMesh
│   │   └── plane.stl
│   ├── turbulenceProperties.air
│   └── turbulenceProperties.particles
└── system
    ├── blockMeshDict
    ├── controlDict
    ├── decomposeParDict
    ├── fvSchemes
    ├── fvSolution
    ├── include
    │   ├── fieldAverage
    │   ├── forceCoeffs
    │   ├── forces
    │   └── probes
    ├── residuals
    ├── snappyHexMeshDict
    └── surfaceFeaturesDict
```



> #### 2D Plane LES



```bash
.
├── 0_org
│   ├── epsilon
│   ├── k
│   ├── nut
│   ├── nuTilda
│   ├── omega
│   ├── p
│   └── U
├── constant
│   ├── include
│   │   └── turbulenceModels
│   ├── transportProperties
│   └── turbulenceProperties
├── gnuplot
│   ├── gnuplot_script
│   └── residual.png
├── gunplot.plt
├── run_clean.sh
├── run_solver.sh
├── show_residuals.sh
└── system
    ├── blockMeshDict
    ├── controlDict
    ├── decomposeParDict
    ├── fvSchemes
    ├── fvSolution
    ├── include
    │   ├── fieldAverage
    │   ├── forceCoeffs
    │   ├── forces
    │   └── probes
    └── residuals

```



> #### 2D_Plane_pimpleFoam




> #### 2D_Plane_pisoFoam




> #### 2D_Plane_simpleFoam




> #### Airway_EL_run




> #### Flow_around_cylider




> #### VIV_cylider