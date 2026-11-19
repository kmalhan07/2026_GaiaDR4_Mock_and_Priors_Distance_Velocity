These two files are based on the paper **Malhan & Bailer-Jones (2026)**.

arXiv: 

<br>

The details about these files are provided below.

1. `zFile04b_priors_edsd_ggd.fits`: This file provides distance priors based on two models, namely **EDSD** and **GGD**. The file contains the following columns.
   
`healpix_id`                         : healpixel id

`glon`, `glat`                       : Galactic longitude and latitude corresponding to the healpixel

`Gmag_GDR4_q0.998`                   : Stars brighter than G<`Gmag_GDR4_q0.998` are used to fit the models

`edsd_L`                             : fitted $L$ parameter of the EDSD model 

`r_edsd_50`, `r_edsd_16`, `r_edsd_84`: 50, 16, and 84 quantiles of the fitted EDSD model

`ggd_alpha`, `ggd_beta`, `ggd_L`     : fitted ($\alpha, \beta, L$) parameters of the GGD model

`r_ggd_50`, `r_ggd_16`, `r_ggd_84`   : 50, 16, and 84 quantiles of the fitted GGD model

