# A Color Analyzer By Using Python
In this simple script we extract the image colors by using python and `KMeans` clustring method


## Requierments
```bash
pip install -r requirements.txt
```

## Features
- [x] Pie Chart
- [x] CLI
- [x] Telegram Bot
- [x] Rest API
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

## How To Serve API Server
You Only Need To Install `Uvicorn` Library For Python By:
```bash
pip install uvicorn
```

or

```bash
pip install -r requirements.txt
```

and run

```bash
python server.py
```

## How To Serve Telegram Bot
Firstly, You Need To Get `API_TOKEN` from `Bot_Fother` and put it in `.env` File Then You Just Need To Run: 
```bash
python bot.py
```