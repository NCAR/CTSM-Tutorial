from glob import glob
from os.path import join, expanduser
import time
import xarray as xr
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import requests
import pandas as pd
import os
import matplotlib.colors as colors
import calendar
import tqdm
import cftime

def preprocess (ds):
    variables = [
        'TSOI',
        'H2OSOI'
    ]
    ds_new= ds[variables]
    return ds_new


#--this just drops an unused coordinate variable (lndgrid) from the dataset
def preprocess_all (ds):
    ds_new= ds.isel(lndgrid=0) 
    return ds_new


# -- fix timestamp on monthly CTSM files
def fix_time_h0 (ds):
    nsteps = len(ds.time)
    yr0 = ds['time.year'][0].values
    month0 = ds['time.month'][0].values - 1 
    day0 = ds['time.day'][0].values 

    date = cftime.datetime(yr0,month0,day0).isoformat() 
    ds['time'] = xr.cftime_range(date, periods=nsteps, freq='M')
    ds['time']= ds['time'].dt.strftime("%Y-%m").astype("datetime64[ns]")
    return ds

# -- fix timestamp on CTSM 30 minute h1 files so they can be matched with eval files
def fix_time_h1 (ds):
    '''
    fix time formatting with reading multiple cesm files.
    '''
    nsteps = len(ds.time)
    yr0 = ds['time.year'][0].values
    month0 = ds['time.month'][0].values
    day0 = ds['time.day'][0].values

    date = cftime.datetime(yr0,month0,day0).isoformat() 
    ds['time'] = xr.cftime_range(date, periods=nsteps, freq='30min')
    ds['time']= ds['time'].dt.strftime("%Y-%m-%d %H:%M:%S").astype("datetime64[ns]")
    return ds

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap


def quick_soil_profile(sim_path, case_name, var, year):
    """              
    Function for quick visualization of soil profile vs. time
    Args:            
        sim_path (str):   
            path where the simulation files exist
        case_name (str) : 
            CTSM case name
        var (str):
            variable to create the plot for
        year (int):
            simulation year for plot
    """
    plt.rcParams["font.weight"] = "bold"    
    plt.rcParams["axes.labelweight"] = "bold"
    font = {'weight' : 'bold',
                'size'   : 15} 
    matplotlib.rc('font', **font)
    
    sim_files = sorted(glob(join(sim_path,case_name+".h1."+year.__str__()+"*.nc")))
    print("All Simulation files: [", len(sim_files), "files]")
    
    start = time.time()
    ds_ctsm = xr.open_mfdataset(sim_files, decode_times=True, preprocess=preprocess, combine='by_coords',parallel=True)
    end = time.time()
    
    print("Reading all simulation files [", len(sim_files), "files] took:", end-start, "s.")
        
    if var=='TSOI':
        ds_ctsm[var].isel(levgrnd=(slice(0,9))).plot(x="time",yincrease=False, robust=True,cmap='YlOrRd',figsize=(15, 5))
    elif var=='H2OSOI':
        ds_ctsm[var].isel(levsoi=(slice(0,15))).plot(x="time",yincrease=False, robust=True,cmap='viridis',figsize=(15, 5))
    else:
        print ('Please choose either TSOI or H2OSOI for plotting.')
        
        
def plot_soil_profile_timeseries(sim_path, neon_site, case_name, var, year):
    """              
    Function for quick visualization of soil profile vs. time
    Args:            
        sim_path (str):   
            path where the simulation files exist
        case_name (str) : 
            CTSM case name
        var (str):
            variable to create the plot for
        year (int):
            simulation year for plot
    """
    
    time_0 = time.time()
    plt.rcParams["font.weight"] = "bold"    
    plt.rcParams["axes.labelweight"] = "bold"
    font = {'weight' : 'bold',
                'size'   : 15} 
    matplotlib.rc('font', **font)
    
    sim_files = sorted(glob(join(sim_path,case_name+".h1."+year.__str__()+"*.nc")))
    print("All Simulation files: [", len(sim_files), "files]")
    
    start = time.time()
    #ds_ctsm = xr.open_mfdataset(sim_files, decode_times=True, preprocess=preprocess, combine='by_coords',parallel=True)
    
    ds_all = []
    for f in tqdm.tqdm(sim_files):
        ds_tmp = xr.open_dataset(f,drop_variables=['ZSOI','DZSOI','WATSAT','SUCSAT','BSW','HKSAT','ZLAKE','DZLAKE','PCT_SAND','PCT_CLAY'])
        ds_all.append(ds_tmp.isel(time = 24))
    
    ds_ctsm = xr.concat (ds_all,dim='time')
    
    end = time.time()
    
    print("Reading all simulation files [", len(sim_files), "files] took:", end-start, "s.")
        
    if var=='TSOI':
        #ds_ctsm[var].isel(levgrnd=(slice(0,9))).plot(x="time",yincrease=False, robust=True,cmap='YlOrRd',figsize=(15, 5))
        
        tsoi = ds_ctsm[var].isel(levgrnd=(slice(0,9)))
        x= tsoi.time.values
        y= -tsoi.levgrnd.values
        plot_var =  tsoi[:,:,0].values.transpose()
        plot_var = plot_var-273.15
        
        cmap = 'YlOrRd'
        var_name = 'Soil Temperature'
        var_unit = '[\u00B0C]'
        
    elif var=='H2OSOI':
        
        h2o_soi = ds_ctsm[var].isel(levsoi=(slice(0,15)))
        x= h2o_soi.time.values
        y= -h2o_soi.levsoi.values
        plot_var =  h2o_soi[:,:,0].values.transpose()
        
        #cmap = 'viridis'
        var_name = 'Soil Moisture'
        var_unit = '[mm3/mm3]'
        #ds_ctsm[var].isel(levsoi=(slice(0,15))).plot(x="time",yincrease=False, robust=True,cmap='viridis',figsize=(15, 5))
        cmap = plt.get_cmap('gist_earth_r')
        cmap = truncate_colormap(cmap, 0.15, 0.9)
        
    else:
        print ('Please choose either TSOI or H2OSOI for plotting.')
    
    
    X, Y = np.meshgrid(x, y)
    fig= plt.figure(num=None, figsize=(15,5),  facecolor='w', edgecolor='k')

    ax = plt.gca()
    cs = ax.contourf(X, Y, plot_var,cmap=cmap,extend="both")
    plt.xticks(rotation=30)
    plt.ylabel('Soil Depth [m]')
    plt.xlabel('Time')
    plt.title ('Time-Series of '+ var_name +' Profile at '+neon_site,fontweight="bold")
    cbar = fig.colorbar(cs, ax=ax, shrink=0.9)
    y_label = var_name +' '+var_unit
    cbar.ax.set_ylabel(y_label)

    #plt.show()
    time_1 = time.time()
    print("Making this plot took ", time_1-time_0, "s.")
                     
                     
def download_file(url, fname):
    """              
    Function to download a file.
    Args:            
        url (str):   
            url of the file for downloading
        fname (str) : 
            file name to save the downloaded file.
    """              
    response = requests.get(url)
                     
    with open(fname, 'wb') as f:
        f.write(response.content)
                     
    #-- Check if download status_code
    if response.status_code == 200:
        print('Download finished successfully for', fname,'.')
    elif response.status_code == 404:
        print('File '+fname+'was not available on the neon server:'+ url) 
        
def list_neon_eval_files(neon_site):                               
    """              
    A function to download neon listing.csv file
    and parse it to find all eval files for the specified
    neon tower site .
    
    Args:
        neon_site (str):
            4 character name of your neon site
    """
    # -- download listing.csv
    listing_file = 'listing.csv'
    url = "https://storage.neonscience.org/neon-ncar/listing.csv"
    download_file(url, listing_file)
    
    # -- find eval files
    df = pd.read_csv(listing_file)
    df = df[df['object'].str.contains(neon_site+"_eval")]
    
    dict_out = dict(zip(df['object'],df['last_modified']))
    return dict_out  
        
def download_eval_files (neon_site, eval_dir, year="all"):
    """              
    A function to download all eval files for the specified
    neon tower site .
    
    Args:
        neon_site (str):
            4 character name of your neon site
        eval_dir (str):
            directory where you want your evaluation files
    """

    if (year=="all"):
        print ("Downloading all available evaluation files for "+neon_site+".")
    else:
        print ("Downloading evaluation files for "+neon_site+" for year "+year+".")

    #-- create directory if it does not exist
    if not os.path.isdir(eval_dir):
        os.mkdir(eval_dir)
    
    site_eval_dir = os.path.join(eval_dir,neon_site)

    #-- create directory for the site if it does not exist
    if not os.path.isdir(site_eval_dir):
        os.mkdir(site_eval_dir)

    #-- get all available eval file names
    file_time = list_neon_eval_files(neon_site)

    for key, value in file_time.items():
        fname = key.rsplit('/',1)[1]
        if year=="all" or year in fname:
                fname_out = os.path.join(site_eval_dir, fname)
                download_file(key, fname_out)     
