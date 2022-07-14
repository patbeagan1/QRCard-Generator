# QRCode Generator

Given a list of urls and image urls, it creates a webpage that has infocards. You can print this web page out and use it as a physical backup for your bookmarks.

## Prerequisites

You should have `qrencode` installed on your device.

If you are on macOs, you can run `brew install qrencode`.

## Usage

You can run the script as `main.py <csv file>`. If you just want to quickly try out the script, you can do `main.py test.csv`

### Formatting

The CSV file should have 2 columns. They do not need to be titled.

- The first row is for the url. 
- The second row is for the image. 

Each row should look like this. Make sure that there are no empty rows
```csv
example.com, example.com/example.png
```

### Results

You should end up with a responsive web page in `build/index.html`, which looks like this

<img width="1087" alt="Screen Shot 2022-07-13 at 10 22 23 PM" src="https://user-images.githubusercontent.com/10187351/178892193-c8d4f467-56e2-4555-a4f0-7058bb615c4b.png">

If you'd like, you can print this page, to have a physical copy of your bookmarks.
