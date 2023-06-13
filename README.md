# tacosdbfilter
Database merger for a certain game about tacos

## Usage

```
./merge.py --help

usage: merge.py [-h] [--overrides OVERRIDES] [-p {all,songs,modes,folders,default} [{all,songs,modes,folders,default} ...]] [source] [mix_with] [target]

positional arguments:
  source
  mix_with
  target

options:
  -h, --help            show this help message and exit
  --overrides OVERRIDES
  -p {all,songs,modes,folders,default} [{all,songs,modes,folders,default} ...], --patch {all,songs,modes,folders,default} [{all,songs,modes,folders,default} ...]
```

- Generate wordlist.merged.json using wordlist.json as a base and including values from wordlist.en.json if they share the same "key".
  ```
  ./merge.py wordlist.json wordlist.en.json wordlist.merged.json -p all
  ```
  Note: Those are the default values, so this is the equivalent of typing `./merge.py -p all`.
  
- Only include the keys that starts with "song_"
  ```
  ./merge.py -p songs
  ```
  Available "patch sets":
  ```
  "songs": ["song_"]
  "folders": ["genre_", "folder_"]
  "modes": ["mode_select_"]
  "default": "songs" + "folders"
  ```
  You can combine them, like so `./merge.py -p songs -p modes`
  
- If you want to override some items, you can have a overrides.json file containing items that will be used instead of the file you are merging with.

  Example overrides.json:
  ```json
  [
      {
        "key": "folder_intro_howto",
        "japaneseText": "Let's learn how to play this game!",
        "japaneseFontType": 0
    }
  ]
  ```
  
- If you want to use another path, you can do so like this `./merge.py --overrides custom_overrides.json`
  
## Helper scripts

- wordlist.bin and wordlist.en.bin -> wordlist.json and wordlist.en.json
  ```
  ./unzip.sh
  ```
  
- wordlist.merged.json -> wordlist.bin
  ```
  ./zip.sh
  ```
