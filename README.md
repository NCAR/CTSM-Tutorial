# Welcome to the [NEON-NCAR Main Tutorial Repository](https://ncar.github.io/CTSM-Tutorial/README.html) 

[![Jupyter Build](https://img.shields.io/github/actions/workflow/status/NCAR/CTSM-Tutorial/gh-page_builder.yml?label=JupyterBook&logo=GitHub&style=flat-square)](https://ncar.github.io/CTSM-Tutorial-2022/README.html)

[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg?style=flat-square)](https://github.com/NCAR/CTSM-Tutorial/blob/main/LICENSE)
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-green?style=flat-square&logo=Jupyter&color=green)](https://jupyter.org/try)
[![Commits](https://img.shields.io/github/last-commit/NCAR/CTSM-Tutorial?label=Last%20commit&style=flat-square&color=green)](https://github.com/NCAR/CTSM-Tutorial/commits/main) 
[![Contributors](https://img.shields.io/github/contributors/NCAR/CTSM-Tutorial?label=Contributors&logo=github&style=flat-square&color=green)](https://img.shields.io/github/contributors/NCAR/CTSM-Tutorial?logo=github) 

Numerous versions of this tutorial can be found in this repository's branches.

<!---
[![Visits Badge](https://badges.pufler.dev/visits/NCAR/CTSM-Tutorial?style=flat-square&logo=GitHub&color=green)](https://badges.pufler.dev)
 ![example workflow](https://github.com/NCAR/CTSM-Tutorial/actions/workflows/gh-page_builder.yml/badge.svg)

[![Github All Releases](https://img.shields.io/github/downloads/NCAR/CTSM-Tutorial/total.svg)]()
![GitHub All Releases](https://img.shields.io/github/downloads/NCAR/CTSM-Tutorial/total)

![ViewCount](https://views.whatilearened.today/views/github/NCAR/CTSM-Tutorial/views.svg)
![Hits](https://hitcounter.pythonanywhere.com/count/tag.svg?url=https://github.com/Tanu-N-Prabhu/Python)

-->


The materials and notebooks in this tutorial is published as a Jupyter book <a href="https://ncar.github.io/CTSM-Tutorial/README.html" target="_blank"> here</a>.

This repository includes materials for tutorials such as the <a href="https://github.com/ESCOMP/CTSM" target="_blank"> Community Terrestrial Systems Model (CTSM)</a> 2022 mini-tutorial <a href="https://www.cesm.ucar.edu/events/2022/ctsm-tutorial/" target="_blank"> (link to agenda and resources)</a>. 

These tutorials are designed as an introduction to running the Community Terrestrial Systems Model (CTSM).  We will go through three configurations that include running a:

0. Supported NEON tower site,
1. Global FATES-SP simulation, and
2. Generic single point simulation.  

We'll also learn how to: 
- Visualize results, 
- Analyze model output, and 
- Make simple code modifications.

This video will walk you through the initial steps of the tutorial, but the steps for quick start are also summarized below.

[![Watch the video](https://img.youtube.com/vi/xl73eC0VnMU/0.jpg)](https://www.youtube.com/embed/xl73eC0VnMU)


The <a href="https://www.youtube.com/playlist?list=PLsqhY3nFckOF6VRh5gqpNAlHPgP3gLnXn" target="_blank">full set of lectures from the tutorial can be found here</a>, and will be posted after the tutorial.


# Quick Start
## Step 1: Open up CESM-Lab
- In your web browser go to the provided cloud link for the particular tutorial which you are attending.

  It will automatically open up a portal to connect to the cloud: 

  ![Screen Shot 2022-05-17 at 1 58 17 AM](https://user-images.githubusercontent.com/17344536/168760701-e436721a-3b84-4d82-b28c-026890a22266.png)


- Enter your username and password provided with your tutorial registration
- This should launch a JupyterLab window in your browser.

## Step 2: Clone CTSM Tutorial Repository
- Click on the `Terminal` icon to open a terminal window.

![Screen Shot 2022-05-17 at 2 05 32 AM](https://user-images.githubusercontent.com/17344536/168761721-b87d21a0-f92a-4040-9296-926f9b234113.png)


- Run the following command to clone this repository. (Just copy and paste the text below into the terminal window that opens in JupyterLab). You can also specify a particular branch which you'd like to clone, if you are interested in a particular tutorial. 

```
git clone https://github.com/NCAR/CTSM-Tutorial
```

This gives you a local copy of the material you'll need for the tutorial

*Can you see a new directory on your navigation sidebar called `CTSM-Tutorial`?* (See the left sidebar of your JupyterLab window)
![Screen Shot 2022-05-17 at 4 46 13 PM](https://user-images.githubusercontent.com/17344536/168924550-f7a3f821-7e5a-48e3-9155-9ffdff954ca1.png)


## Step 3: Navigate to `notebooks` directory
- Click on the `CTSM-Tutorial` directory
- Click on the `notebooks` directory
- Click on the `Day0a_GitStarted.ipynb` notebook in the sidebar of your JupyterLab window.

## Notebook Table of Contents
 - GettingStarted: These notebooks are the building blocks for all additional notebooks.
     - 1_NEON_Simulation_Tutorial.ipynb : This notebook shows how to run a NEON simulation
     - 2_NEON_Simulation_Visualization.ipynb : This notebook shows how to visualize NEON simulation output
 - ProjectExamples: These notebooks are project-specific and build upon the GettingStarted notebooks
     - Basic_CTSM-NEON_Plots.ipynb : This notebook shows how to create plots from NEON data, as well as perform time averaging, etc
     - CTSMsp_NEON_fromScratch.ipynb : This notebook focuses on using CTSM with satellite phenology
     - Clone_Case.ipynb : This notebook shares how to clone a case
     - FATES_NEON_fromScratch.ipynb : This notebook works on creating a FATES case from scratch with NEON
     - Plot_flux_climatology.ipynb : This notebook provides climatology plotting examples
     - QuickPlot_CTSM-FATESsp.ipynb : This notebook provides plotting tools for use with FATES run with satellite phenology
     - QuickPlot_CTSM_h0.ipynb : This plots monthly CTSM data
     - QuickPlot_CTSM_spinup.ipynb : This plots CTSM cases that have been spun up
     - customizeCase_PRISM.ipynb : This customizes a case to use PRISM precipitation input data
     - customizeCase_modelFeatures.ipynb : This customizes various model features
     - customizeCase_parameterModifications.ipynb : This notebook provides tools for parameter modifications and takes input that is generated from modifyParameterFile.ipynb
     - modifyParameterFile.ipynb : This notebook modifies a parameter file that can then be used by customizeCase_parameterModifications.ipynb
     - modifySurfdataFile.ipynb : This notebook modifies a surface data file that can then be used by customizeCase_modelFeatures.ipynb
 - ContributedNotebooks: These notebooks are contributed by workshop participants who dove further into a particular project.

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
- Adrianna Foster, Negin Sobhani, Danica Lombardozzi, Will Wieder, Teagan King, and Gordon Bonan who put together tutorial materials. 
- Brian Dobbins, who put together the AWS configuration of CESM-Lab;
- Jackie Shuman, Polly Buotte, Keith Oleson, Linnia Hawkins, and Katya Jay who tested tutorial materials;
- Erik Kluzek & Bill Sacks, who made CTSM tags needed for running simulations.
- Elizabeth Faircloth and Ryan Johnson who helped with tutorial registration, logistics and webpages; and finally the rest of the
- TSS staff who provided lecture materials and helped answer questions during the tutorial.

This material is based upon work supported by the National Center for Atmospheric Research (NCAR), which is a major facility sponsored by the National Science Foundation (NSF) under Cooperative Agreement No. 1852977. Staff time on this project was also supported by NSF award numbers 2039932, 2031238, 1926413, and 2120804.
