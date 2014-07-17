---
layout: documentation
title: dirperm
category: documentation
subcategory: components
menu: 'components.md'
---
### NAME

dirperm: permissions and file/directory creation NCM component
 

### DESCRIPTION

Object to set permissions and ownership of files and directories.
Will create directories if they do not exist (with the proper
permissions).  Useful, e.g., to give every pool-user a ".globus"
directory in its $HOME, or to create a bunch of home directories for
poolaccounts on a non-CE machine.
 

If the list initdir is set, then files in those directories will be
copied to the created directory.  They will be given the same
ownership as the directory. 

When creating a file, all of the parent directories must already
exist.  
 

### RESOURCES

#### `/software/components/dirperm/paths`

A list of files/directories to manage with this component.  Each entry
must be of the structure\_dirperm\_entry type which has the following
fields: path, owner, perm, type, initdir.  

### EXAMPLES
 
