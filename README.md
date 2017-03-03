climbing-scorecard
===

A simple Python script, that will generate a climbing scorecard used for
Boulder sessions at [Bouldershabitat](http://www.bouldershabitat.de/) and
the [Bonner Boulderliga](http://bonnerboulderliga.de/) in Bonn, Germany.

![Sample output](sample.png)

* `1-100`: Stands for the route number, given by the route setters
* `OE`, `GB`, `GN` etc.: These are the color codes used by the route setters. E.g. `OE` stands for "Orange".
* `1-6`: These are the points given to the climber, if he succeeded with the route.

Installation
---

Install the requirements:

	$ pip install -r requirements.txt


Usage
---

	Usage: scorecard.py [OPTIONS]

	Options:
	--start-number INTEGER  First route number
	--end-number INTEGER    last route number
	-o, --outfile TEXT      Name of the output file
	--help                  Show this message and exit.

To adjust the route numbers, simply change the parameters `--start-number` and `--end-number`, e.g.:

	$ python scorecard.py --start-number=100 --end-number=200

**Note:** currently only 100 numbers per page are supported.
