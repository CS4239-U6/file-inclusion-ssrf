# File Inclusion

An attacker can use Local File Inclusion (LFI) to trick the web application into exposing or running files on the web server.


# Quick start guide (Local File Inclusion)
1. Clone the repo
2. Go into the `LocalFileInclusion` directory.
3. Build the docker image using `docker build -t lfi .`
4. Run the docker image using `docker run -dt -p 5000:5000 lfi`
5. The server is now on [`localhost:5000`](http://localhost:5000)

# Quick start guide (Remote File Inclusion)
1. Clone the repo
2. Go into the `RemoteFileInclusion` directory.
3. Build the docker image using `docker build -t rfi .`
4. Run the docker image using `docker run -dt -p 5000:5000 rfi`
5. The server is now on [`localhost:5000`](http://localhost:5000)

# Defenses

## Using a Proxy


## Offloading to a third party Service


## Proper input validation

Filter user inputs and make sure that filepath is correct. An example is given below.
However, do note that this defense is very hard to implement as there might be many ways to bypass it.
This is not an exceptionally good defense as errors in logic are hard to detect.

```python
# Normalise the filepath
path = os.path.normpath(path) 

# Checks if the path leads to the supposed folder
if (not path.startswith(folderPath)):
    flash("File not allowed")
    return redirect(url_for('index'))
```


## Create a whitelist

Whitelist what can be included within a whitelist to prevent other files from being read.

```python
WHITE_LIST = (
    'allowed_path/file1',
    'allowed_path/file2',
)

...

# Check if filepath is in whitelist
if(filepath not in WHITE_LIST):
    flash("File not allowed")
    return redirect(url_for('index'))

```