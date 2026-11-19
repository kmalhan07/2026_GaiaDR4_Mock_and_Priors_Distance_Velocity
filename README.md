This repository provides certain data products based on the paper **Malhan & Bailer-Jones (2026)**, arXiv: __________________

<br>
<br>

The details about these files are provided below.

<br>
1. `Gaia DR4 mock stellar catalogue`:  This data, along with its accompanying readme file, is publicly available at _____________


<br>
2. `zFile04b_priors_edsd_ggd.fits`: This file provides two types of distance priors, based on **EDSD** and **GGD** models, both constrained using the `Gaia DR4 mock stellar catalogue`. This file contains the following columns.
   
`healpix_id`                         : healpixel id

`glon`, `glat`                       : Galactic longitude and latitude corresponding to the healpixel

`Gmag_GDR4_q0.998`                   : Stars brighter than G<`Gmag_GDR4_q0.998` are used to fit the models

`edsd_L`                             : fitted $L$ parameter of the EDSD model 

`r_edsd_50`, `r_edsd_16`, `r_edsd_84`: 50, 16, and 84 quantiles of the fitted EDSD model

`ggd_alpha`, `ggd_beta`, `ggd_L`     : fitted ($\alpha, \beta, L$) parameters of the GGD model

`r_ggd_50`, `r_ggd_16`, `r_ggd_84`   : 50, 16, and 84 quantiles of the fitted GGD model


<br>
3. `____Coryn's velocity file_____`

