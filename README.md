# climbing-scorecard

A simple Python script, that will generate a climbing scorecard image,
with a range of route numbers and different colors.

## Example

![Sample output](sample.png)

* `1-100`: Stands for the route number, given by the route setters
* `OE`, `GB`, `GN` etc.: These are the color codes used by the route setters. E.g. `OE` stands for "Orange".
* `1-6`: These are the points given to the climber, if he succeeded with the route.

This scorecard was generated with the following options:

	$ python scorecard.py -r OE 1 -r GB 1 -r GN 2 -r RT 3 -r BU 4 -r GU 5 -r SZ 6 -r PK 3

The sample route color codes are taken from the [Bonner Boulderliga](http://bonnerboulderliga.de/regeln.html):

* OE = Orange
* GB = Yellow
* GN = Green
* RT = Red
* BU = Blue
* GU = Grey
* SZ = Black
* PK = Pink

## Installation

Install the requirements:

	$ pip install -r requirements.txt


## Usage

	Usage: scorecard.py [OPTIONS]

	Options:
	  -r, --route <TEXT INTEGER>...  One or many route definitions, defined as
	                                 tuples, e.g. -r RT 3 -r BU 4
	  --start-number INTEGER         Starting range for route numbers.
	  --end-number INTEGER           End range for route numbers.
	  -o, --outfile TEXT             Name of the output file
	  --help                         Show this message and exit.

### Route codes

You will have to specify the list of route names and points. They can be added with the
`-r/--route` argument. Each route consists of a tuple: route name and points. E.g.:

	$ python scorecard.py -r RT 3 -r BU 4

This will generate a scorecard for the route number 1 to 100 and with the route colors
"RT" (3 points) and "BU" (4 points.).

**Note:** currently only 1-9 route colors are supported.

### Route numbers

To adjust the route numbers, simply change the parameters `--start-number` and `--end-number`, e.g.:

	$ python scorecard.py -r ... --start-number=100 --end-number=200

**Note:** currently only up to 100 numbers per page are supported.
