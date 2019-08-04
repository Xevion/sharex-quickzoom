# sharex-quickzoom

## The Repository

![trtx: you can radially blur any image and it'll be funny](./resources/screenshot.png)

The purpose of this project is to simply provide an easy way to apply a blur effect to an image using the ShareX application.
The reasoning for zoom is mostly for personal humor.
The effect may reach into being just zoom for radially, depending on how far I can get this project going.

## Modules in use

In case you wish to use this repo, these are the utilties you will require.

### [./main.py](./process.py)

**os** - Path managemennt

**sys** - Path Management

**argparse** - Parsing arguments from command line

**subprocess** - Issuing commands to ImageMagick

### [./clean.py](./clean.py)

**os** - Path Management

**sys** - Path Management

**send2trash** - sending files to recycle bin instead of permanently deleting

## Resources

Thanks to ImageMagick for giving very useful utilities involving image manipulation.

I used commands described [here](https://www.imagemagick.org/Usage/mapping/#blur) to figure out how it works and apply it, I didn't do all that much to learn it, but it was useful none-the-less.

[Blurring mechanics](https://www.imagemagick.org/Usage/mapping/#blur) | [Convert Command](https://imagemagick.org/script/convert.php) | [ImageMagick Commandline Utility](https://imagemagick.org)

And thanks to ShareX for providing such excellent screenshot utilities.

[ShareX GitHub](https://github.com/ShareX/ShareX/) | [ShareX Website](https://getsharex.com/)

And of course, my friend, **trtx**, for inspiring me to make my dumb humor even more accessible.
