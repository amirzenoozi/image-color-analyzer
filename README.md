# A Color Analyzer By Using Python
In this simple script we extract the image colors by using python and `KMeans` clustring method


## Features
- [x] Pie Chart
- [x] CLI
- [ ] Rest API
- [ ] Video Files

## CLI Options
```bash
--src       Your Target File Path       #default: sample.jpg
--clusters  Number of KMeans Cluster    #default: 5
--dest      Your Target File Path       #default: results
```


## How To Use
```bash
python main.py --src PATH_TO_YOUR_IMAGE --clusters 5 --dest FOLDER_NAME
```