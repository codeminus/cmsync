# cmsync

## Installation
Install using pip:
```
pip install cmsync
```

Usage:

Create a sync.json file with the following minimal structure:

```
{ 
  "manifest": [
    {
      "src": "",
      "dest": ""
    }
  ]
}
```
`src` and `dest` can be an absolute or relative file or a directory path.


The following example copies the contents of `/dir/to/copy` to `/tmp/abc`
and tranfers `/dir/file.txt` to `/tmp/xyz/newfile.txt`:

```
{ 
  "manifest": [
    {
      "src": "/dir/to/copy",
      "dest": "/tmp/"
    },
    {
      "src": "/dir/file.txt",
      "dest": "/tmp/xyz/newfile.txt"
    }
  ]
}
```

## Run command after copying files

To run a command line after copying files, set `run_after`. Example:

```
{ 
  "manifest": [
    {
      "src": "/dir/to/copy",
      "dest": "/tmp/",
      "run_after": "echo 'Done!'"
    }
  ]
}
```

## Running CMSync

