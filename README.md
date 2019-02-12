# filetransfer

## Description

This script ise for securely (checks using multiple anti-viruses before) transfer files from locally connected external media to a remote file server. It can reduces the possibility of transmitting malware to your internal (secure) network with files imported from external media.

## Basic Capabilities

* Ability to scan the files with multiple antivirus/anitmalware before transfer
* Use multiple antivirus software to scan the files
* Block file transfer in case of virus detection
* Checks if virus scanning signatures up to date
* If no malware found, the scanned files/folders will be transferred to Linux/Windows file servers (running CIFS)
* User crendentials are asked to mount the remote CIFS folder
* Mounting external media in read-only mode (to make sure that no data will be transferred out from this channel)
* All the actions are logged properly (including the username and file names) and can be sent to a central rsyslog servers using RELP.
* The script can be installed in a LTSP image to run on diskless (thin) clients.

## Usage Scenario

1. User has a Linux terminal (may be an LTSP client) at hand in which he has no root access and he can't mount external media manually
1. User selects "Secure File Transfer" from the (LTSP) menu.
1. The active directory user name and password are taken to access the file server.
1. If the external media is not physically connected, the status is displayed on the screen and the user is expected to operate for <TIMEOUT> (Default:180) seconds. If the user does not perform the operation, the program will exit (and main LTSP menu will be is returned).
1. The external media connected to the system are automatically connected in read-only mode. This ensures that no data is transferred from the file server. (Because root can override it, it is important to keep the root password of client securely)
1. Files in external media will be scanned using multiple viruses 
1. If no virus is found in the scanned files:
   1. A new folder opens in the standard folder specified on the file server (Template: "<UserID> \ _ Transfer_ \ YYYYAAGG-SSDDss")
   1. External media information is copied to the destination folder in TXT / XML format. (?)
   1. The files are copied to the destination folder along with the hash value file.
1. If a virus is found or the scan fails, no transfer is performed.
1. The user is informed of the transaction result.
1. Each step of the operation will be logged including detailed (time, username, filenames, hashes, scanresults, etc.) which can also be sent to a central rsyslog (RELP) server.
