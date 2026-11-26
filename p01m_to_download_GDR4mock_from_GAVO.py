"""
>> To bulk download Gaia DR4 mock catalogue from GAVO 
>> Malhan & Bailer-Jones (2027)

>> See GAVO: https://dc.g-vo.org/browse/dr4mock/q

>> Alternatively, you may try running from the terminal:
wget --user=ari --password=ari -r --no-parent http://dc.g-vo.org/dr4mock/q/dl/static/



To run:
-------
python3 p01m_download_GDR4mock_from_GAVO.py


Time taken:
-----------
It took 0.3 hours to download 4922/12289 files (with N_CPUS   = 16 -- i.e., using 16 parallel download streams)
Estimated total time for all 12288 files: 0.75 hours (=0.3 hours x 12289/4922)
"""

import os, time, requests, shutil, multiprocessing as mp
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import unquote

OUT_DIR  = "_GaiaDR4_mock_catalogue_downloaded_from_GAVO"
BASE_URL = "https://dc.g-vo.org/dr4mock/q/dl/static/"
USERNAME = "ari"
PASSWORD = "ari"
N_CPUS   = 16

t_start0 = time.time()
print(f"Download started at {datetime.now():%Y-%m-%d %H:%M:%S}")

#-------------------
# Create directory
#-------------------
print()
print("1. Create directory to store the data....")
if Path(OUT_DIR).exists():
    shutil.rmtree(OUT_DIR)
Path(OUT_DIR).mkdir(parents=True)

#-------------------
# Get file list
#-------------------
print()
print("2. Getting file list...")
response = requests.get(BASE_URL, auth=(USERNAME, PASSWORD))
soup     = BeautifulSoup(response.text, "html.parser")
files    = [a["href"] for a in soup.find_all("a", href=True) if not a["href"].startswith("?") and not a["href"].startswith("/")]
n_files  = len(files)
print(f"Found {n_files} files")

#-------------------
# Download files
#-------------------
print()
print("3. Downloading files...")

def download_file(args):
    i, fname = args
    out_name = unquote(fname)  
    out_path = os.path.join(OUT_DIR, out_name)

    if os.path.exists(out_path):
        return i, out_name, "skipped"

    try:
        url      = BASE_URL + fname  # keep encoded in URL
        response = requests.get(url, auth=(USERNAME, PASSWORD), stream=True)
        response.raise_for_status()

        with open(out_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        return i, out_name, "done"
    except Exception as e:
        return i, out_name, f"error: {e}"


args = [(i, fname) for i, fname in enumerate(files)]

with mp.Pool(processes=N_CPUS) as pool:
    for i, (i_file, fname, status) in enumerate(pool.imap_unordered(download_file, args), 1):
        elapsed = (time.time() - t_start0) / 3600.
        print(f"\r{i}/{n_files} | {fname} | {status} | elapsed: {elapsed:.4f} hr", end="", flush=True)

#-------------------
# Complete
#-------------------
print()
print()
print(f"elapsed: {(time.time() - t_start0)/3600.:.4f} hr")
print("Complete")