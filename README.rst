===================
Maximum Acyclic Subgraph Solver
===================
.. image:: https://travis-ci.org/afrancis13/MAS-Solver.svg?branch=master
    :target: https://travis-ci.org/afrancis13/MAS-Solver

This project was posed in December 2015 as a final exercise in applying approximation algorithms learned in the course CS170 at UC Berkeley.

Problem Description
------------
:math:`\textsc{Maximum Acyclic Subgraph (MAS)}`: Given a directed graph :math:`G = (V = {1, ..., n}, E)`, find an ordering of the nodes :math:`r_1, ..., r_n` (we call :math:`r_i` the rank of the player :math:`i`) that maximizes the number of forward edges:

.. math::
\Bigg{\text{objective value achieved by ranking \{r_1, ..., r_n\}}} = \sum_{(i, j) \in E} \mathbbm{1}{r_i < r_j}


