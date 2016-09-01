# cmsync
A simple python package that syncs files and directories.

### Pending features:
- SFTP sync

## Installation
Install using pip:
```
pip install cmsync
```

Usage:

Create a **sync.json** file with the following minimal structure:

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
and `/dir/file.txt` to `/tmp/xyz/newfile.txt`:

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

## Running a command after copying files

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

run `cmsync` on the folder containing the *sync.json* file:
```
$ ls
sync.json
$ cmsync

Source:      'c:/dir/to/copy'
Destination: 'C:/Windows/Temp'
Copying file... Done.
Running `echo 'Done! :D'`
'Done! :D'
```
