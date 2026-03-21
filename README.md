# apgman

APGsearch MANager
I got tired of compiling and recompiling apgsearch, and managing all of the builds, so I wrote this

> **\*Note:** apgman is a toolkit of Bash shell scripts.\*
> _On Windows, you have to install Cygwin or similar_

## Functions

Manages and simplifies the:

- Installation
- Building
- And Running
  of apgsearch.

## Install

To install APGMan itself, make sure you have `git`, then run:

```bash
git clone https://github.com/NNlk05/apgman.git
cd apgman
```

> **\*Note:** All following commands will assume you ran `cd apgman` and your working dir is wherever you cloned apgman.\*
> _If not `cd` there again_

## Usage

### Install Apgserach

To install apgsearch, run:

```bash
./apgman-init
```

It defaults the install location to $HOME/.apgman
You can change it by running:

```bash
./apgman-init /path/to/your/install/dir/
```

### Building Apgsearch

```bash
./apgman-build rule symm
```

Rule defaults to b3s23, and symm defaults to C1 as a failsafe in case apgsearch changes its behaviour.

### Running a Build

```bash
./apgman-run rule symm options -k 0000000000000000000000000000000000000000000000000000000000000000 -n 1000000 ...
```

Again, rule defaults to b3s23, and symm defaults to C1 as a failsafe in case apgsearch changes its behaviour.
