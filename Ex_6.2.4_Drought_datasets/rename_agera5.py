#%%
from pathlib import Path
import glob
import os
from shutil import copy

#%%
indir = Path('./data/agera5')
infiles = glob.glob(str(indir / '*.nc'))
print(infiles)

# %%
outdir = indir / 'renamed'
outdir.mkdir(exist_ok=True, parents=True)
for infile in infiles:
    fname = Path(infile).name
    new_fname = '-'.join(fname.split('-')[5:-1])
    print(new_fname)
    outfile = str(outdir / new_fname) + '.nc'
    copy(infile, outfile)
# %%
