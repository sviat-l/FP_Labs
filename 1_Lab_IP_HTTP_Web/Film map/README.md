# Film Location Map
_Create a map with 10 closest locations that have been used for filming in the stated year_

## Implementation
All functions are completed in [main.py](main.py) module. Data about the film locations is stored in [data](data) directory. For each phase of the task were used different python packages.
* Get terminal agruments - argparse
* Data processing - pandas and regex
* Find place coordinates - geolocator
* Web map creating - Follium


## Usage

```bash
python3 main.py <latitude> <longitude> <year> <path to data>
```

Where parameters are:
1. latitude - your location latitude (float)
2. longitude - your longitude latitude (float)
3. year - take into account only that year films (int)
4. path to data - set file to get films data

## Example
```bash
python3 main.py 50.1536486 49.8063456 2014 data/short_locations.list
```
![image](https://user-images.githubusercontent.com/91615606/177374884-d5405570-7ae8-47f2-8016-4db5ce2568d0.png)

[HTML](/examples/Film_map.html) version of the map.
