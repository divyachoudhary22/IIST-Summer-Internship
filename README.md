# Abstract
This project explores the buckling behavior of dished shallow shells subjected to uniform external pressure, with particular emphasis on the influence of geometric imperfections. Such shells—commonly used in aerospace, marine, and structural applications are prone to sudden snap-through buckling, making reliable design essential.

A finite element framework was established in Abaqus, employing S4R shell elements to model the dished geometry and material properties representative of thin metallic shells. Both linear eigenvalue analysis and nonlinear Riks analysis were used to investigate ideal (perfect) shell responses, capturing critical buckling modes and postbuckling paths.

To account for manufacturing irregularities, two imperfection strategies were implemented: localized dimples introduced via static displacement fields, and spatially correlated random thickness variations generated through a spectral representation of a prescribed power spectral density function. These imperfections were superimposed on the nominal shell geometry to create a suite of imperfect models.

A probabilistic workflow was developed to integrate imperfection statistics into buckling analysis, enabling the extraction of knock-down factors from load-deflection curves. The methodology lays the groundwork for a reliability-based design approach, linking imperfection characteristics to buckling performance in dished shallow shells.
