
# Welcome to the [NEON Tutorial 2023](https://github.com/NCAR/CTSM-Tutorial/blob/NEON_Tutorial_2023/README.md)

[![Jupyter Build](https://img.shields.io/github/actions/workflow/status/NCAR/CTSM-Tutorial/gh-page_builder.yml?label=JupyterBook&logo=GitHub&style=flat-square)](https://ncar.github.io/CTSM-Tutorial/README.html)

[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg?style=flat-square)](https://github.com/NCAR/CTSM-Tutorial/blob/main/LICENSE)
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-green?style=flat-square&logo=Jupyter&color=green)](https://jupyter.org/try)
[![Commits](https://img.shields.io/github/last-commit/NCAR/CTSM-Tutorial?label=Last%20commit&style=flat-square&color=green)](https://github.com/NCAR/CTSM-Tutorial/commits/NEON_Tutorial_2023) 
[![Contributors](https://img.shields.io/github/contributors/NCAR/CTSM-Tutorial?label=Contributors&logo=github&style=flat-square&color=green)](https://img.shields.io/github/contributors/NCAR/CTSM-Tutorial?logo=github) 


This tutorial will be used as a resource during the 2023 NEON Tutorial, Flux Course 2023 & ESA 2023 workshop. 

<!---
[![Visits Badge](https://badges.pufler.dev/visits/NCAR/CTSM-Tutorial?style=flat-square&logo=GitHub&color=green)](https://badges.pufler.dev)
 ![example workflow](https://github.com/NCAR/CTSM-Tutorial/actions/workflows/gh-page_builder.yml/badge.svg)

[![Github All Releases](https://img.shields.io/github/downloads/NCAR/CTSM-Tutorial/total.svg)]()
![GitHub All Releases](https://img.shields.io/github/downloads/NCAR/CTSM-Tutorial/total)

![ViewCount](https://views.whatilearened.today/views/github/NCAR/CTSM-Tutorial/views.svg)
![Hits](https://hitcounter.pythonanywhere.com/count/tag.svg?url=https://github.com/Tanu-N-Prabhu/Python)

-->


The materials and notebooks in this tutorial is published as a Jupyter book <a href="https://ncar.github.io/CTSM-Tutorial/README.html" target="_blank"> here</a>. 

These tutorials are designed as an introduction to running the Community Terrestrial Systems Model (CTSM).  Users can begin with the notebooks in the `Getting Started` directory, which contains:

1. An introduction to CTSM, CESM-Lab, and Git
2. Running CTSM simulations at NEON tower sites
3. Evaluating CTSM at NEON tower sites

We'll also have opportunities to explore more `advanced notebooks` which describe how to: 
- Make simple code modifications
- Change plant type
- etc

<!-- TODO: fill in additional advanced notebook topics -->

<!-- TODO: Do we want to include a video here like Adrianna's from 2022 Mini Tutorial? And an updated webpage for posted lectures after the tutorial? -->

The <a href="https://www.youtube.com/playlist?list=PLsqhY3nFckOF6VRh5gqpNAlHPgP3gLnXn" target="_blank">full set of lectures from the tutorial can be found here</a>, and will be posted after the tutorial.


# Quick Start
## Step 1: Open up CESM-Lab
- In your web browser go to <a href="https://ctsmworkshop2023.cesm.cloud/" target="_blank"> https://ctsmworkshop2023.cesm.cloud/</a>

  It will automatically open up a portal to connect to the cloud: 

  ![Screen Shot 2022-05-17 at 1 58 17 AM](https://user-images.githubusercontent.com/17344536/168760701-e436721a-3b84-4d82-b28c-026890a22266.png)


- Enter your username and password provided with your tutorial registration
- This should launch a JupyterLab window in your browser.

## Step 2: Clone CTSM Tutorial Repository
- Click on the `Terminal` icon to open a terminal window.

![Screen Shot 2022-05-17 at 2 05 32 AM](https://user-images.githubusercontent.com/17344536/168761721-b87d21a0-f92a-4040-9296-926f9b234113.png)


- Run the following command to clone this repository. (Just copy and paste the text below into the terminal window that opens in JupyterLab) 

```
git clone -b NEON_Tutorial_2023 https://github.com/NCAR/CTSM-Tutorial
```

This gives you a local copy of the material you'll need for the tutorial

<!-- TODO: if we pre-stage everything, we may not actually have to do this? -->

*Can you see a new directory on your navigation sidebar called `CTSM-Tutorial`?* (See the left sidebar of your JupyterLab window)
![Screen Shot 2022-05-17 at 4 46 13 PM](https://user-images.githubusercontent.com/17344536/168924550-f7a3f821-7e5a-48e3-9155-9ffdff954ca1.png)


## Step 3: Navigate to `notebooks` directory
- Click on the `CTSM-Tutorial` directory
- Click on the `notebooks` directory
- Click on the `GettingStarted` directory
- Click on the `1_GitStarted.ipynb` notebook in the sidebar of your JupyterLab window.

Now you're ready to get started with the pre-tutorial homework.  Let's get started by following along in the first notebook.
 
## 📚 Resources

[CTSM Repository](https://github.com/ESCOMP/ctsm) which includes the [CTSM Wiki page](https://github.com/ESCOMP/CTSM/wiki) that has lots of resources, including much of the following:
- [CTSM Technical Documentation](https://escomp.github.io/ctsm-docs/versions/master/html/index.html)
- [CTSM User's Guide](https://escomp.github.io/ctsm-docs/versions/master/html/users_guide/index.html)
- [Quickstart Guide for Various Model Configuraions](https://escomp.github.io/CESM/release-cesm2/quickstart.html#create-a-case)
- [Running single-point cases other than NEON](https://escomp.github.io/ctsm-docs/versions/master/html/users_guide/running-single-points/single-point-and-regional-grid-configurations.html)
- [Running NEON cases with a container](https://ncar.github.io/ncar-neon-books/intro.html) -- Running CTSM for NEON cases on a laptop

[CLM5 Overview Paper](https://doi.org/10.1029/2018MS001583) Lawrence et al. 2019 JAMES

[CLM5 Diagnostic plots](https://www.cesm.ucar.edu/experiments/cesm2.0/land/diagnostics/clm_diag_PCKG.html), from the overview paper.

[CLM5 ILAMB page](https://www.cesm.ucar.edu/experiments/cesm2.0/land/diagnostics/clm_diag_ILAMB.html), also from the overview paper.


## ❓ Questions

For questions about running simulations, please use DiscussCESM Forums:

[Containers & Cloud Platforms Forum](https://bb.cgd.ucar.edu/cesm/forums/containers-cloud-platforms.162/)

[CTSM Forum](https://bb.cgd.ucar.edu/cesm/forums/ctsm-clm-mosart-rtm.134/)

## 👍 Acknowledgements

A number of people have been critical to this effort, including: 
- Adrianna Foster, Negin Sobhani, Danica Lombardozzi, Will Wieder, Gordon Bonan, & Teagan King who put together tutorial materials. 
- Brian Dobbins, who put together the AWS configuration of CESM-Lab;
- Jackie Shuman, Polly Buotte, & Keith Oleson, who tested tutorial materials;
- Erik Kluzek & Bill Sacks, who made CTSM tags needed for running simulations.
- Elizabeth Faircloth and Ryan Johnson who helped with tutorial registration, logistics and webpages; and finally the rest of the
- TSS staff who provided lecture materials and helped answer questions during the tutorial.

This material is based upon work supported by the National Center for Atmospheric Research (NCAR), which is a major facility sponsored by the National Science Foundation (NSF) under Cooperative Agreement No. 1852977. Staff time on this project was also supported by NSF award numbers 2039932, 2031238, 1926413, and 2120804.
