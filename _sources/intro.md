# Welcome to the 2022 CTSM mini-tutorial

These tutorials are designed as an introduction to running the Community Terrestrial Systems Model (CTSM).  We we will run through three configurations that include running a:
1. Supported NEON tower site,
2. Global FATES simution, and
3. Generic single point simulation.  

Using models can enhance the impact of ecological, hydrological, and atmospheric science research. Regardless of whether you are a seasoned modeler or a novice, this tutorial introduces different ways to set up and run CTSM in different configurations using the latest scientific and software developments in the Community Earth System Model (CESM). ngle point NCAR-NEON collaboration makes the process simple. 

We have developed new capabilities to easily run Community Land Model (CLM) simulations at NEON tower sites by setting up the appropriate model configurations, datasets, and initial conditions. With this new tool, CLM uses gap-filled meteorology from NEON tower sites, the dominant plant species is mapped to the appropriate model plant functional type (PFT), and soil characteristics used in the simulations are updated to match observations from NEON’s soil megapits. Gap-filled NEON tower flux data are also available for model evaluation. Additionally, all the commands to run the model are combined into a script that you can easily call from a single line of code. This part of the tutorial was supported by an NSF investment to foster NCAR-NEON collaborations to generate cyberinfrastructure tools for the university research and teaching community.

These new capabilities are packaged into a Docker container, CESM-Lab, so that you can run simulations on any computing system, including your laptop or the cloud. Within the CESM-Lab container, you will find tutorials that guide you through how to run a CLM simulation and help you to access, process, visualize and evaluate model simulations. 

This tutorial will guide you through setting up a container on your local system and it will guide you through running a simulation and provides example of basic visualization and analysis of the simulation results.



## Resources

[CTSM Technical Documentation](https://escomp.github.io/ctsm-docs/versions/master/html/index.html)

[CTSM User's Guide](https://escomp.github.io/ctsm-docs/versions/master/html/users_guide/index.html)

[Quickstart Guide for Various Model Configuraions](https://escomp.github.io/CESM/release-cesm2/quickstart.html#create-a-case)

[Running single-point cases other than NEON](https://escomp.github.io/ctsm-docs/versions/master/html/users_guide/running-single-points/single-point-and-regional-grid-configurations.html)


## Questions

For questions about running simulations, please use DiscussCESM Forums:

[Containers & Cloud Platforms Forum](https://bb.cgd.ucar.edu/cesm/forums/containers-cloud-platforms.162/)

[CTSM Forum](https://bb.cgd.ucar.edu/cesm/forums/ctsm-clm-mosart-rtm.134/)

