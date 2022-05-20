
# Welcome to the [2022 CTSM mini-tutorial](https://ncar.github.io/CTSM-Tutorial-2022/README.html)

![example workflow](https://github.com/NCAR/CTSM-Tutorial-2022/actions/workflows/gh-page_builder.yml/badge.svg)

The materials and notebooks in this tutorial is published as a Jupyter book <a href="https://ncar.github.io/CTSM-Tutorial-2022/README.html" target="_blank"> here</a>.

This repository includes materials for the <a href="https://github.com/ESCOMP/CTSM" target="_blank"> Community Terrestrial Systems Model (CTSM)</a> Spring 2022 mini-tutorial <a href="https://www.cesm.ucar.edu/events/2022/ctsm-tutorial/" target="_blank"> (link to agenda and resources)</a>. 

These tutorials are designed as an introduction to running the Community Terrestrial Systems Model (CTSM).  We will go through three configurations that include running a:

0. Supported NEON tower site,
1. Global FATES simution, and
2. Generic single point simulation.  

We'll also learn how to: 
- Visualize results, 
- Analize model output, and 
- Make simple code modifications.

This video will walk you through the initial steps of the tutorial, but the steps for quick start are also summarized below.

[![Watch the video](https://img.youtube.com/vi/xl73eC0VnMU/0.jpg)](https://www.youtube.com/embed/xl73eC0VnMU)


The <a href="https://www.youtube.com/playlist?list=PLsqhY3nFckOF6VRh5gqpNAlHPgP3gLnXn" target="_blank">full set of lectures from the tutorial can be found here</a>, and will be posted after the tutorial.


# Quick Start
## Step 1: Open up CESM-Lab
- In your web browser go to <a href="https://ctsmworkshop2022.cesm.cloud/" target="_blank"> https://ctsmworkshop2022.cesm.cloud/</a>

  It will automatically open up a portal to connect to the cloud: 

  ![Screen Shot 2022-05-17 at 1 58 17 AM](https://user-images.githubusercontent.com/17344536/168760701-e436721a-3b84-4d82-b28c-026890a22266.png)


- Enter your username and passsword provided with your tutorial registration
- This should launch a JupyterLab window in your browser.

## Step 2: Clone CTSM Tutorial Repository
- Click on the `Terminal` icon to open a terminal window.

![Screen Shot 2022-05-17 at 2 05 32 AM](https://user-images.githubusercontent.com/17344536/168761721-b87d21a0-f92a-4040-9296-926f9b234113.png)


- Run the following command to clone this repository. (Just copy and paste the text below into the terminal window that opens in JupyterLab) 

```
git clone https://github.com/NCAR/CTSM-Tutorial-2022
```

This gives you a local copy of the material you'll need for the tutorial

*Can you see a new directory on your navigation sidebar called `CTSM-Tutorial-2022`?* (See the left sidebar of your JupyterLab window)
![Screen Shot 2022-05-17 at 4 46 13 PM](https://user-images.githubusercontent.com/17344536/168924550-f7a3f821-7e5a-48e3-9155-9ffdff954ca1.png)


## Step 3: Navigate to `notebooks` directory
- Click on the `CTSM-Tutorial-2022` directory
- Click on the `notebooks` directory
- Click on the `Day0a_GitStarted.ipynb` notebook in the sidebar of your JupyterLab window.

Now you're ready to get started with the pre-tutorial homework.  Let's git started by following along in the Day0a notebook
 
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
- Adrianna Foster, Negin Sobhani, Brian Dobbins, Danica Lombardozzi and Will Wieder who built tutorial materials and the AWS configuration of CESM-Lab; 
- Keith Oleson, Jackie Shuman, and Polly Buotte who tested tutorial materials; 
- Erik Kluzek, who made CTSM tags needed for running simulations. 
- Elizabeth Faircloth and Ryan Johnson who helped with tutorial registration, logistics and webpages; and finally the rest of the 
- TSS staff who provided lecture materials and helped answer questions during the tutorial.

This material is based upon work supported by the National Center for Atmospheric Research (NCAR), which is a major facility sponsored by the National Science Foundation (NSF) under Cooperative Agreement No. 1852977. Staff time on this project was also supported by NSF award numbers 2039932, 2031238, 1926413, and 2120804.