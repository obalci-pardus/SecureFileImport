# TODO

1. Files/folders in external media may be selected by the user to be included in the transfer operations.
1. Information to be displayed: 
   1. Brand model, serial number, information (if available) for the external media; 
   1. Malware scan summary (number of files, total capacity, all file list, etc.) 
   1. Some information displayed on the screen should be dynamically updated so the user will see the process is still in progress.
1. Include as many antiviruses as possible (which supports Linux and preferably which have free versions)
   1. ClamAV
   1. VirusTotal
   1. YARA (https://blog.clamav.net/2015/06/clamav-099b-meets-yara.html)
   1. McAfee https://www.mcafee.com/enterprise/en-ca/products/virusscan-enterprise-for-linux.html
   1. ESET https://www.eset.com/us/home/antivirus-linux/
   1. F-PROT http://www.f-prot.com/products/home_use/linux/
   1. Sophos https://www.sophos.com/en-us/products/free-tools/sophos-antivirus-for-linux.aspx
   1. BitDefender https://www.bitdefender.com/support/scanning-from-the-command-line-of-bitdefender-rescue-cd-616.html
   1. Comodo https://www.comodo.com/home/internet-security/antivirus-for-linux.php
   1. Avast https://support.avast.com/en-eu/article/131/
   1. Avira https://www.avira.com/en/support-download-avira-antivir-rescue-system%20/ (binaries in the rescue system may be used)
   1. Microsoft Defender https://itsfoss.com/microsoft-defender-atp-linux (in the future)

## References:

1. https://github.com/evgentus/Online-Multi-AntiVirus-Checker/blob/master/daemon/checker.cfg
1. https://github.com/joxeankoret/multiav
1. https://github.com/PlagueScanner/PlagueScanner
1. https://github.com/DogFive/AVScanner
1. https://github.com/kimjoseph95/multiav-malware
1. https://github.com/paulosgf/multiAVscanners
1. https://github.com/mitre/multiscanner
   1. Otomatik çeviri: "Making Home VirusTotal" https://translate.google.com/translate?hl=tr&tab=TT&sl=auto&tl=en&u=https%3A%2F%2Fhabr.com%2Fpost%2F141103%2F
   1. https://github.com/evgentus/Online-Multi-AntiVirus-Checker/blob/master/daemon/checker.cfg adresinde tarama yazılımlarına ilişkin kullanılabilecek bazı anahtar bilgiler var.
1. http://blog.quarkslab.com/writing-our-own-analyzer-for-the-open-source-multi-scanner-irma.html
1. İnternet Erişimi Olan Sistemler İçin (İlave yetenek)
   1. https://github.com/Gawen/virustotal
   1. https://github.com/botherder/virustotal
   1. https://github.com/VirusTotal/qt-virustotal-uploader
   1. https://github.com/sysforensics/VirusTotal
