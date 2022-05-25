# Frequently Asked Questions (FAQ)

* **How can I access CESM-Lab after the tutorial?**
  - You can always find all the tutorial materials [here](https://ncar.github.io/CTSM-Tutorial-2022/README.html). 
  - Your access to AWS will be depracted after this tutorial but you can access CESM-Lab using an AWS account (check with your lab or university).
  - You can also run CTSM using dockers on your own laptops. Details on running CTSM using containers through our CTSM-NEON tutorial tool are available [here](https://ncar.github.io/NEON-visualization/).

* **I messed up the notebooks. How can I find what it should be??**

    You can look at the notebooks on GitHub and correct small mistakes, or you can do the following:
     - Open up terminal window
     - Navigate to CTSM-Tutorial-2022 directory (`cd ~/CTSM-Tutorial-2022`)
     - Run `git status` to check the status of your notebooks and which branch you are on. 
     - If you are on the main branch, run `git stash` which stashes your progress and whatever you saved in your notebooks. 
     - Next, run `git pull` to get a clean version of the tutorial notebooks from the original repository. 

* **How do I see what jobs are running on AWS?**
  - You can either use `qstat` or `squeue` in terminal to list all your jobs and their status. 
  - Below is the list of acronyms in the `ST` column and their meanings:

    | Status | Code | Description |
    | --- | ----------- | ----------- |
    | Completed | C | Job just successfully completed. |
    | Running | R | The Job is currently running. |
    | Queued/Waiting | Q / PD | The job is waiting for allocation in the queue. |


* **How do I kill a job that’s running?**
  - You can either use `qdel JOBID` or `scancel JOBID`. You should replace `JOBID` with the job ids that you'd want to stop. Please note that you can get your `JOBID` by using `qstat` or `squeue`.


* **I get a message saying that there is an existing directory and cannot run my code. What do I do??**

    * Remove the existing directory, which was likely created for an earlier failed case. Alternatively, if this error occurs when using the `run_neon` script, you can use the `--overwrite` option.

* **Which parameters need to have a re-build after changing them?**

    * You only need to rebuild if you've changed something in `env_build.xml` or `env_mach_pes.xml`. You can change `env_run.xml` or `user_nl_*` files without rebuilding. The only exception to that is if you are restarting and trying to change the years you are running over for DATM. For more information on when a rebuild is necessary, please see section 4.2 on [this website.](https://esmci.github.io/cime/versions/ufs_release_v1.0/html/users_guide/building-a-case.html)

