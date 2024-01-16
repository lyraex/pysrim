![srim heatmap](https://github.com/costrouc/pysrim/raw/master/examples/images/length-heatmap-log-cropped.png)

# pysrim: Automation, Analysis, and Plotting of SRIM Calculations

`pysrim` is a [Python] package that aims to wrap and extend [SRIM], a
popular tool for simulating ions travelling through a material. There
are many pain points to [SRIM] and this package aims to address
them. These include compatibility with *all* popular operating systems, automation and crash
recovery of [SRIM] calculations, parsing of all output files, and
publication quality plots.

There is now a [Docker] image
[costrouc/pysrim](https://hub.docker.com/r/costrouc/pysrim/tags/) for
running `pysrim` and [SRIM]! **No setup necessary and does not require a
display so it is server ready**. If you would like to try it run the
short command below (obviously requires [Docker]). All output files will
be stored in `/tmp/output` for this example. [Benchmarks
show](https://pysrim.readthedocs.io/en/latest/benchmarks.html) the
docker container is around 50-60% faster. I believe this is due to
using [xvfb].

``` bash
docker run -v $PWD/examples/docker:/opt/pysrim/ \
           -v /tmp/output:/tmp/output \
           -it costrouc/pysrim sh -c "xvfb-run -a python3.6 /opt/pysrim/ni.py"
ls /tmp/output
```

<table>
<tr>
  <td>Latest Release</td>
  <td><img src="https://img.shields.io/pypi/v/pysrim.svg" alt="latest release"/></td>
</tr>
<tr>
  <td></td>
  <td><img src="https://anaconda.org/costrouc/pysrim/badges/version.svg" alt="latest release" /></td>
</tr>
<tr>
  <td>Package Status</td>
  <td><img src="https://img.shields.io/pypi/status/pysrim.svg" alt="status" /></td>
</tr>
<tr>
  <td>License</td>
  <td><img src="https://img.shields.io/pypi/l/pysrim.svg" alt="license" /></td>
</tr>
<tr>
  <td>Build Status</td>
  <td> <a href="https://gitlab.com/costrouc/pysrim/pipelines"> <img
src="https://gitlab.com/costrouc/pysrim/badges/master/pipeline.svg"
alt="gitlab pipeline status" /> </a> </td>
</tr>
<tr>
  <td>Coverage</td> <td><img src="https://gitlab.com/costrouc/pysrim/badges/master/coverage.svg" alt="coverage" /></td> </tr> <tr> <td>Conda</td>
  <td> <a href="https://gitlab.com/costrouc/pysrim"> <img src="https://anaconda.org/costrouc/pysrim/badges/downloads.svg" alt="conda downloads" /> </a> </td>
</tr>
<tr>
  <td>Documentation</td>
  <td> <a href="https://pysrim.readthedocs.io/en/latest/"> <img src="https://readthedocs.org/projects/pysrim/badge/?version=latest" alt="readthedocs documentation" /> </a> </td>
</tr>
<tr>
    <td>Publication</td>
    <td><a href="http://joss.theoj.org/papers/d5ff2e218ff209390eb4882822e7b382"><img src="http://joss.theoj.org/papers/d5ff2e218ff209390eb4882822e7b382/status.svg"></a></td>
</tr>
<tr>
    <td>DOI Repository Archive</td>
    <td><a href="https://zenodo.org/badge/latestdoi/135215837"><img src="https://zenodo.org/badge/135215837.svg" alt="DOI"></a></td>
</tr>
</table>

# Documentation

Link to [documentation on readthedocs](https://pysrim.readthedocs.io/en/latest/)

# Features

## Automate running SRIM and TRIM on all operating systems

While `TRIM` is a great code, it has many downsides regarding
automation. The `TRIM.IN` input file is tedious to write yourself and
the [GUI] that constructs the `TRIM.IN` will crash at unexpected moments.
One of these crashes everyone has encountered is the fact that a float
text field can never be empty. `TRIM` also has a tendency to crash
because it stores all cascades in memory. Meaning that for large runs
with full cascades greater than ~1000 ions it will run out of
memory. `pysrim` addresses all of these issues by providing a simple
[API] wrapper for the input file (supporting all of `TRIM`'s features),
that can be run on *all* operating systems
(e.g., [Windows], [macOS], [Linux], etc.)
using [wine]
(see the [SRIM WineHQ page]),
allowing for batch calculations
(see
[this notebook example](https://gitlab.com/costrouc/pysrim/blob/master/examples/notebooks/SiC.ipynb)).

Below is a ["Hello, World!"] example of using `pysrim` for running a `TRIM`
calculation. Note that `/tmp/srim` is the path to the [SRIM] executable
directory (`SRIM.exe` should reside in this directory). `pysrim` will
add all the necessary input files. If this ran successfully for you a
[SRIM] window will popup and start the calculation.

``` python
from srim import Ion, Layer, Target, TRIM

# Construct a 3MeV Nickel ion
ion = Ion('Ni', energy=3.0e6)

# Construct a layer of nick 20um thick with a displacement energy of 30 eV
layer = Layer({
        'Ni': {
            'stoich': 1.0,
            'E_d': 30.0,
            'lattice': 0.0,
            'surface': 3.0
        }}, density=8.9, width=20000.0)

# Construct a target of a single layer of Nickel
target = Target([layer])

# Initialize a TRIM calculation with given target and ion for 25 ions, quick calculation
trim = TRIM(target, ion, number_ions=25, calculation=1)

# Specify the directory of SRIM.exe
# For windows users the path will include C://...
srim_executable_directory = '/tmp/srim'

# takes about 10 seconds on my laptop
results = trim.run(srim_executable_directory)
# If all went successfull you should have seen a TRIM window popup and run 25 ions!
# results is `srim.output.Results` and contains all output files parsed
```

See the [documentation](https://pysrim.readthedocs.io/en/latest/)
for all available options.

## Copy SRIM output files to directory

After a SRIM calculation has completed run `copy_output_files` to take
all of the output files and move them to a directory of your liking.

``` python
from srim import TRIM

TRIM.copy_output_files('/tmp/srim', '/home/costrouc/scratch/srim')
```

## Post processes SRIM output as numpy arrays

By far the hardest part about running `TRIM` calculations is analyzing
the output files. `pysrim` comes with parsers for
[`IONIZ.txt`](https://pysrim.readthedocs.io/en/latest/source/srim.html#srim.output.Ioniz),
[`VACANCY.txt`](https://pysrim.readthedocs.io/en/latest/source/srim.html#srim.output.Vacancy),
[`NOVAC.txt`](https://pysrim.readthedocs.io/en/latest/source/srim.html#srim.output.NoVacancy),
[`E2RECOIL.txt`](https://pysrim.readthedocs.io/en/latest/source/srim.html#srim.output.EnergyToRecoils),
[`PHONON.txt`](https://pysrim.readthedocs.io/en/latest/source/srim.html#srim.output.Phonons),
[`RANGE.txt`](https://pysrim.readthedocs.io/en/latest/source/srim.html#srim.output.Range),
and
[`COLLISON.txt`](https://pysrim.readthedocs.io/en/latest/source/srim.html#srim.output.Collision). The
`COLLISON.txt` file can get quite large so the `Collision` parser uses a
buffered reader that can handle any file size. Additionally, a class
[`srim.output.Results`](https://pysrim.readthedocs.io/en/latest/source/srim.html#srim.output.Results)
will processes all output files in a directory and provide a
dictionary of each parsed output file. `pysrim` comes with some
helpful plotting utilities such a plotting the atomic displacements per atom (DPAs) vs. depth. However,
`pysrim's` most powerful feature is that all of the text files are
exposed as [NumPy] arrays. The example below shows how to plot DPAs using
a simple math and [NumPy]. This enables the user to seamlessly use `TRIM`
and do analysis.

``` python
from srim.output import Phonons, Ioniz

def plot_damage_energy(folder, ax):
    phon = Phonons(folder)
    dx = max(phon.depth) / 100.0
    energy_damage = (phon.ions + phon.recoils) * dx
    ax.plot(phon.depth, energy_damage / phon.num_ions, label='{}'.format(folder))
    return sum(energy_damage)

def plot_ionization(folder, ax):
    ioniz = Ioniz(folder)
    dx = max(ioniz.depth) / 100.0
    ax.plot(ioniz.depth, ioniz.ions, label='Ionization from Ions')
    ax.plot(ioniz.depth, ioniz.recoils, label='Ionization from Recoils')
```

Set `folders` to list of directories to [SRIM] outputs. See
[Analysis](https://gitlab.com/costrouc/pysrim/blob/master/examples/notebooks/Analysis.ipynb)
for detailed example. Notice how there is a [Python] class for each [SRIM]
output file and gives simple access to each column. This did require
some complex regex to get working just right.

``` python
folders = ['test_files/2', 'test_files/4']
image_directory = 'examples/images'

fig, axes = plt.subplots(1, len(folders), sharey=True, sharex=True)

for ax, folder in zip(np.ravel(axes), folders):
    plot_damage_energy(folder, ax)
    plot_ionization(folder, ax)
    ax.legend()
    ax.set_ylabel('eV')
    ax.set_xlabel('Depth [Angstroms]')
fig.suptitle('Ionization Energy vs Depth', fontsize=15)
fig.set_size_inches((20, 6))
fig.savefig(os.path.join(image_directory, 'ionizationvsdepth.png'), transparent=True)
```

![srim heatmap](https://gitlab.com/costrouc/pysrim/raw/master/examples/images/ionizationvsdepth.png)

See [jupyter
notebook](https://gitlab.com/costrouc/pysrim/blob/master/examples/notebooks/Analysis.ipynb)
for full demonstration of features.

An example of creating some publication graphics with `pysrim` can also
be found in that
[directory](https://gitlab.com/costrouc/pysrim/blob/master/examples/notebooks/SiC.ipynb). I
have used this in a
[publication](https://doi.org/10.1016/j.cossms.2017.09.003).


# Installation

Installation of `pysrim` is easy via [pip] or [Conda].

Available on [PyPI]

 -  `pip install pysrim`

Available on [Conda]

 - `conda install -c costrouc pysrim`

Available on [Docker]

 - `docker pull costrouc/pysrim`

Unless you are using the [Docker] image, you will need to install [SRIM]
on your machine using the instructions bellow for [Linux], [macOS], and
[Windows].

## Docker

There is a [Docker] container with `pysrim` and SRIM already
installed. Some interesting tricks had to be done with using [wine] and
faking an [X11] session. `xvfb-run -a ` creates a fake [X11] session
within the docker container therefore allowing [SRIM] to run on servers
without displays. This is the method that I always use to run [SRIM].

Image: [costrouc/pysrim](https://hub.docker.com/r/costrouc/pysrim/tags/)

## Linux and OSX

For [Linux] an [macOS] you will need to first have wine installed. See [this
post](https://www.davidbaumgold.com/tutorials/wine-mac/) on
installation of [wine] on [macOS]. For [Linux] you will typically be able to
install [wine] via something like:
```bash
apt get install wine # Ubuntu
dnf install wine
```
Further details specific to running [SRIM] via [wine] can be found on the
[SRIM WineHQ page].

Once you have [wine] installed run the [installer
script](https://gitlab.com/costrouc/pysrim/raw/master/install.sh)
`install.sh`.

Click extract and then done.

## Windows

A collegue of mine has gotten it to work easily on [Windows], but I
myself have no experience. Just download the executable at
[srim.org](http://srim.org/). Next you will extract the [SRIM] files
into a directory on your [Windows] machine. Note the directory of
installation as it will be needed from `trim.run()`.

# Contributing

All contributions, bug reports, bug fixes, documentation improvements,
enhancements and ideas are welcome! These should be submitted at the
[Github repository](https://github.com/costrouc/pysrim). GitHub is
only used for visibility.

Contributors:
 - [Chris Ostrouchov](https://gitlab.com/costrouc) (maintainer)
 - [Alex Hanson](https://gitlab.com/wahanson)
 - [dschwen](https://github.com/dschwen)


# License

MIT

[API]: https://en.wikipedia.org/wiki/API
[Conda]: https://en.wikipedia.org/wiki/Conda_(package_manager)
[Docker]: https://en.wikipedia.org/wiki/Docker_(software)
[GUI]: https://en.wikipedia.org/wiki/Graphical_user_interface
["Hello, World!"]: https://en.wikipedia.org/wiki/%22Hello,_World!%22_program
[Linux]: https://en.wikipedia.org/wiki/Linux
[macOS]: https://en.wikipedia.org/wiki/MacOS
[NumPy]: https://en.wikipedia.org/wiki/NumPy
[pip]: https://en.wikipedia.org/wiki/Pip_(package_manager)
[PyPI]: https://en.wikipedia.org/wiki/Python_Package_Index
[Python]: https://en.wikipedia.org/wiki/Python_(programming_language)
[SRIM]: https://en.wikipedia.org/wiki/Stopping_and_Range_of_Ions_in_Matter
[SRIM WineHQ page]: https://appdb.winehq.org/objectManager.php?sClass=application&iId=5992
[X11]: https://en.wikipedia.org/wiki/X_Window_System
[xvfb]: https://en.wikipedia.org/wiki/Xvfb
[Windows]: https://en.wikipedia.org/wiki/Microsoft_Windows
[wine]: https://en.wikipedia.org/wiki/Wine_(software)
