Last login: Sun Mar 31 12:59:51 on ttys001
Jeffs-MBP:~ jeff$ ssh jeff@nems
jeff@nems's password: 

Last login: Fri Mar 22 11:23:00 2019 from 2600:1700:130:b3d0:2094:2bfe:1536:b380

          ███╗   ██╗███████╗███╗   ███╗███████╗
          ████╗  ██║██╔════╝████╗ ████║██╔════╝
          ██╔██╗ ██║█████╗  ██╔████╔██║███████╗
          ██║╚██╗██║██╔══╝  ██║╚██╔╝██║╚════██║
          ██║ ╚████║███████╗██║ ╚═╝ ██║███████║
          ╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝╚══════╝
                                         LINUX

                   BY: ROBBIE FERGUSON
                      NEMSLINUX.COM

  NEMS Platform....: RPi 3 Model B+
  NEMS Version.....: 1.5 (Current Version is 1.5)
  NEMS IP Address..: 192.168.1.225
  Uptime...........: 13 days 20 hours 43 minutes 50 seconds
  Load.............: 0.13 (1 minute) 0.17 (5 minutes) 0.17 (15 minutes)
                     0.12 (1 week)
  Memory...........: Total: 927 MB / Cached: 0 MB
                     Used: 216 MB / Free: 209 MB
  Disk Usage.......: You're using 13% of your root filesystem

jeff@nems:~ $ 
jeff@nems:~ $ 
jeff@nems:~ $ telnet put_ip_addr_here 12489
-bash: telnet: command not found
jeff@nems:~ $ sudo apt-get install telnet
[sudo] password for jeff: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  telnet
0 upgraded, 1 newly installed, 0 to remove and 80 not upgraded.
Need to get 60.7 kB of archives.
After this operation, 131 kB of additional disk space will be used.
Get:1 http://raspbian.mirror.constant.com/raspbian buster/main armhf telnet armhf 0.17-41.2 [60.7 kB]
Fetched 60.7 kB in 1s (67.8 kB/s) 
Selecting previously unselected package telnet.
(Reading database ... 92084 files and directories currently installed.)
Preparing to unpack .../telnet_0.17-41.2_armhf.deb ...
Unpacking telnet (0.17-41.2) ...
Setting up telnet (0.17-41.2) ...
update-alternatives: using /usr/bin/telnet.netkit to provide /usr/bin/telnet (telnet) in auto mode
jeff@nems:~ $ telnet put_ip_addr_here 12489
Trying 104.239.207.44...
Trying 198.105.244.130...
^C
jeff@nems:~ $ telnet 192.168.1.99 12489
Trying 192.168.1.99...
telnet: Unable to connect to remote host: Connection refused
jeff@nems:~ $ sudo apt-get remove telnet
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages will be REMOVED:
  telnet
0 upgraded, 0 newly installed, 1 to remove and 80 not upgraded.
After this operation, 131 kB disk space will be freed.
Do you want to continue? [Y/n] y
(Reading database ... 92092 files and directories currently installed.)
Removing telnet (0.17-41.2) ...
jeff@nems:~ $ sudo apt-get purge telnet
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages will be REMOVED:
  telnet*
0 upgraded, 0 newly installed, 1 to remove and 80 not upgraded.
After this operation, 0 B of additional disk space will be used.
Do you want to continue? [Y/n] y
(Reading database ... 92082 files and directories currently installed.)
Purging configuration files for telnet (0.17-41.2) ...
jeff@nems:~ $ cat /var/log/nems/stats.log
Sat, 16 Mar 2019 15:28:17 -0400
LA: 2.09
Sending anonymous stats to https://new.nemslinux.com/stats/
a:15:{s:4:"hwid";s:32:"59bdd12a7e20b1d315c2bb7263dad363";s:8:"platform";s:1:"4";s:11:"uptime_days";i:0;s:12:"uptime_hours";i:0;s:11:"uptime_mins";i:0;s:11:"uptime_secs";d:18;s:7:"nemsver";s:3:"1.5";s:5:"hosts";s:1:"2";s:8:"services";s:1:"8";s:8:"disksize";d:5634408448;s:8:"diskfree";d:1730445312;s:11:"loadaverage";s:1:"0";s:11:"temperature";s:1:"0";s:8:"timezone";s:3:"EDT";s:10:"benchmarks";s:46:"{"cpu":null,"ram":null,"io":null,"mutex":null}";}
Success.
Assigned new API Key by server: b8de435a-f62f-44d0-963f-bf0350af59c0
LA: 3.45
--------------------
Sat, 16 Mar 2019 15:28:54 -0400
LA: 6.36
Sending anonymous stats to https://new.nemslinux.com/stats/
a:15:{s:4:"hwid";s:32:"59bdd12a7e20b1d315c2bb7263dad363";s:8:"platform";s:1:"4";s:11:"uptime_days";i:0;s:12:"uptime_hours";i:0;s:11:"uptime_mins";i:0;s:11:"uptime_secs";d:38;s:7:"nemsver";s:3:"1.5";s:5:"hosts";s:1:"2";s:8:"services";s:1:"8";s:8:"disksize";d:27460169728;s:8:"diskfree";d:23567450112;s:11:"loadaverage";s:1:"0";s:11:"temperature";s:1:"0";s:8:"timezone";s:3:"EDT";s:10:"benchmarks";s:46:"{"cpu":null,"ram":null,"io":null,"mutex":null}";}
Success.
LA: 9.25
--------------------
Sun, 17 Mar 2019 21:40:12 -0500
LA: 2.34
Sending anonymous stats to https://new.nemslinux.com/stats/
a:15:{s:4:"hwid";s:32:"59bdd12a7e20b1d315c2bb7263dad363";s:8:"platform";s:1:"4";s:11:"uptime_days";i:0;s:12:"uptime_hours";i:0;s:11:"uptime_mins";i:0;s:11:"uptime_secs";d:15;s:7:"nemsver";s:3:"1.5";s:5:"hosts";s:1:"2";s:8:"services";s:1:"8";s:8:"disksize";d:31346462720;s:8:"diskfree";d:27405303808;s:11:"loadaverage";s:4:"0.28";s:11:"temperature";s:15:"43.918333333333";s:8:"timezone";s:3:"CDT";s:10:"benchmarks";s:46:"{"cpu":null,"ram":null,"io":null,"mutex":null}";}
Success.
Assigned new API Key by server: 367b6629-9c49-427e-a678-6f4078819ad3
LA: 2.65
--------------------
Mon, 18 Mar 2019 00:00:02 -0500
LA: 0.24
Sending anonymous stats to https://new.nemslinux.com/stats/
a:15:{s:4:"hwid";s:32:"59bdd12a7e20b1d315c2bb7263dad363";s:8:"platform";s:1:"4";s:11:"uptime_days";i:0;s:12:"uptime_hours";i:2;s:11:"uptime_mins";i:19;s:11:"uptime_secs";d:55;s:7:"nemsver";s:3:"1.5";s:5:"hosts";s:1:"2";s:8:"services";s:1:"8";s:8:"disksize";d:31346462720;s:8:"diskfree";d:27402653696;s:11:"loadaverage";s:8:"0.329375";s:11:"temperature";s:9:"44.512375";s:8:"timezone";s:3:"CDT";s:10:"benchmarks";s:106:"{"cpu":"105.94387517269\n","ram":"1938218.1146026\n","io":"939.89146272904\n","mutex":"76.701821668265\n"}";}
Success.
LA: 0.85
--------------------
Tue, 19 Mar 2019 00:00:02 -0500
LA: 1.02
Sending anonymous stats to https://new.nemslinux.com/stats/
a:15:{s:4:"hwid";s:32:"59bdd12a7e20b1d315c2bb7263dad363";s:8:"platform";s:1:"4";s:11:"uptime_days";i:1;s:12:"uptime_hours";i:2;s:11:"uptime_mins";i:19;s:11:"uptime_secs";d:55;s:7:"nemsver";s:3:"1.5";s:5:"hosts";s:1:"2";s:8:"services";s:1:"8";s:8:"disksize";d:31346462720;s:8:"diskfree";d:27399995392;s:11:"loadaverage";s:16:"0.12857142857143";s:11:"temperature";s:15:"43.551660714286";s:8:"timezone";s:3:"CDT";s:10:"benchmarks";s:106:"{"cpu":"105.94387517269\n","ram":"1938218.1146026\n","io":"939.89146272904\n","mutex":"76.701821668265\n"}";}
Success.
LA: 0.94
--------------------
Wed, 20 Mar 2019 00:00:02 -0500
LA: 0.1
Sending anonymous stats to https://new.nemslinux.com/stats/
a:15:{s:4:"hwid";s:32:"59bdd12a7e20b1d315c2bb7263dad363";s:8:"platform";s:1:"4";s:11:"uptime_days";i:2;s:12:"uptime_hours";i:2;s:11:"uptime_mins";i:19;s:11:"uptime_secs";d:55;s:7:"nemsver";s:3:"1.5";s:5:"hosts";s:1:"2";s:8:"services";s:1:"8";s:8:"disksize";d:31346462720;s:8:"diskfree";d:27397906432;s:11:"loadaverage";s:16:"0.11341346153846";s:11:"temperature";s:15:"43.682096153846";s:8:"timezone";s:3:"CDT";s:10:"benchmarks";s:106:"{"cpu":"105.94387517269\n","ram":"1938218.1146026\n","io":"939.89146272904\n","mutex":"76.701821668265\n"}";}
Success.
LA: 0.4
--------------------
Thu, 21 Mar 2019 00:00:01 -0500
LA: 0.21
Sending anonymous stats to https://new.nemslinux.com/stats/
a:15:{s:4:"hwid";s:32:"59bdd12a7e20b1d315c2bb7263dad363";s:8:"platform";s:1:"4";s:11:"uptime_days";i:3;s:12:"uptime_hours";i:2;s:11:"uptime_mins";i:19;s:11:"uptime_secs";d:54;s:7:"nemsver";s:3:"1.5";s:5:"hosts";s:2:"13";s:8:"services";s:1:"8";s:8:"disksize";d:31346462720;s:8:"diskfree";d:27392307200;s:11:"loadaverage";s:16:"0.11164473684211";s:11:"temperature";s:15:"43.864651315789";s:8:"timezone";s:3:"CDT";s:10:"benchmarks";s:106:"{"cpu":"105.94387517269\n","ram":"1938218.1146026\n","io":"939.89146272904\n","mutex":"76.701821668265\n"}";}
Success.
LA: 0.7
--------------------
Fri, 22 Mar 2019 00:00:02 -0500
LA: 0.04
Sending anonymous stats to https://new.nemslinux.com/stats/
a:15:{s:4:"hwid";s:32:"59bdd12a7e20b1d315c2bb7263dad363";s:8:"platform";s:1:"4";s:11:"uptime_days";i:4;s:12:"uptime_hours";i:2;s:11:"uptime_mins";i:19;s:11:"uptime_secs";d:55;s:7:"nemsver";s:3:"1.5";s:5:"hosts";s:2:"33";s:8:"services";s:1:"8";s:8:"disksize";d:31346462720;s:8:"diskfree";d:27382620160;s:11:"loadaverage";s:8:"0.111175";s:11:"temperature";s:9:"43.915195";s:8:"timezone";s:3:"CDT";s:10:"benchmarks";s:106:"{"cpu":"105.94387517269\n","ram":"1938218.1146026\n","io":"939.89146272904\n","mutex":"76.701821668265\n"}";}
Success.
LA: 0.36
--------------------
Sat, 23 Mar 2019 00:00:01 -0500
LA: 0.07
Sending anonymous stats to https://new.nemslinux.com/stats/
a:15:{s:4:"hwid";s:32:"59bdd12a7e20b1d315c2bb7263dad363";s:8:"platform";s:1:"4";s:11:"uptime_days";i:5;s:12:"uptime_hours";i:2;s:11:"uptime_mins";i:19;s:11:"uptime_secs";d:54;s:7:"nemsver";s:3:"1.5";s:5:"hosts";s:2:"37";s:8:"services";s:1:"8";s:8:"disksize";d:31346462720;s:8:"diskfree";d:27376078848;s:11:"loadaverage";s:16:"0.11207661290323";s:11:"temperature";s:15:"43.972205645161";s:8:"timezone";s:3:"CDT";s:10:"benchmarks";s:106:"{"cpu":"105.94387517269\n","ram":"1938218.1146026\n","io":"939.89146272904\n","mutex":"76.701821668265\n"}";}
Success.
LA: 0.65
--------------------
Sun, 24 Mar 2019 00:00:02 -0500
LA: 0.42
Sending anonymous stats to https://new.nemslinux.com/stats/
a:15:{s:4:"hwid";s:32:"59bdd12a7e20b1d315c2bb7263dad363";s:8:"platform";s:1:"4";s:11:"uptime_days";i:6;s:12:"uptime_hours";i:2;s:11:"uptime_mins";i:19;s:11:"uptime_secs";d:55;s:7:"nemsver";s:3:"1.5";s:5:"hosts";s:2:"43";s:8:"services";s:1:"8";s:8:"disksize";d:31346462720;s:8:"diskfree";d:27370110976;s:11:"loadaverage";s:16:"0.11386824324324";s:11:"temperature";s:15:"43.994368243243";s:8:"timezone";s:3:"CDT";s:10:"benchmarks";s:106:"{"cpu":"105.94387517269\n","ram":"1938218.1146026\n","io":"939.89146272904\n","mutex":"76.701821668265\n"}";}
Success.
LA: 0.75
--------------------
Mon, 25 Mar 2019 00:00:02 -0500
LA: 0.08
Sending anonymous stats to https://new.nemslinux.com/stats/
a:15:{s:4:"hwid";s:32:"59bdd12a7e20b1d315c2bb7263dad363";s:8:"platform";s:1:"4";s:11:"uptime_days";i:7;s:12:"uptime_hours";i:2;s:11:"uptime_mins";i:19;s:11:"uptime_secs";d:55;s:7:"nemsver";s:3:"1.5";s:5:"hosts";s:2:"47";s:8:"services";s:2:"14";s:8:"disksize";d:31346462720;s:8:"diskfree";d:27363287040;s:11:"loadaverage";s:16:"0.11297176820208";s:11:"temperature";s:15:"44.033059679767";s:8:"timezone";s:3:"CDT";s:10:"benchmarks";s:105:"{"cpu":"78.59460275144\n","ram":"1336531.7698043\n","io":"860.92924027619\n","mutex":"59.188014427079\n"}";}
Success.
LA: 0.47
--------------------
Tue, 26 Mar 2019 00:00:02 -0500
LA: 0.06
Sending anonymous stats to https://new.nemslinux.com/stats/
a:15:{s:4:"hwid";s:32:"59bdd12a7e20b1d315c2bb7263dad363";s:8:"platform";s:1:"4";s:11:"uptime_days";i:8;s:12:"uptime_hours";i:2;s:11:"uptime_mins";i:19;s:11:"uptime_secs";d:54;s:7:"nemsver";s:3:"1.5";s:5:"hosts";s:2:"47";s:8:"services";s:2:"14";s:8:"disksize";d:31346462720;s:8:"diskfree";d:27355697152;s:11:"loadaverage";s:16:"0.11515601783061";s:11:"temperature";s:15:"44.123432950192";s:8:"timezone";s:3:"CDT";s:10:"benchmarks";s:105:"{"cpu":"78.59460275144\n","ram":"1336531.7698043\n","io":"860.92924027619\n","mutex":"59.188014427079\n"}";}
Success.
LA: 0.29
--------------------
Wed, 27 Mar 2019 00:00:02 -0500
LA: 0.11
Sending anonymous stats to https://new.nemslinux.com/stats/
a:15:{s:4:"hwid";s:32:"59bdd12a7e20b1d315c2bb7263dad363";s:8:"platform";s:1:"4";s:11:"uptime_days";i:9;s:12:"uptime_hours";i:2;s:11:"uptime_mins";i:19;s:11:"uptime_secs";d:55;s:7:"nemsver";s:3:"1.5";s:5:"hosts";s:2:"47";s:8:"services";s:2:"14";s:8:"disksize";d:31346462720;s:8:"diskfree";d:27350888448;s:11:"loadaverage";s:16:"0.11756315007429";s:11:"temperature";s:15:"44.176316268487";s:8:"timezone";s:3:"CDT";s:10:"benchmarks";s:105:"{"cpu":"78.59460275144\n","ram":"1336531.7698043\n","io":"860.92924027619\n","mutex":"59.188014427079\n"}";}
Success.
LA: 0.48
--------------------
Thu, 28 Mar 2019 00:00:01 -0500
LA: 0.01
Sending anonymous stats to https://new.nemslinux.com/stats/
a:15:{s:4:"hwid";s:32:"59bdd12a7e20b1d315c2bb7263dad363";s:8:"platform";s:1:"4";s:11:"uptime_days";i:10;s:12:"uptime_hours";i:2;s:11:"uptime_mins";i:19;s:11:"uptime_secs";d:54;s:7:"nemsver";s:3:"1.5";s:5:"hosts";s:2:"47";s:8:"services";s:2:"14";s:8:"disksize";d:31346462720;s:8:"diskfree";d:27348381696;s:11:"loadaverage";s:16:"0.11802377414562";s:11:"temperature";s:15:"44.212715897436";s:8:"timezone";s:3:"CDT";s:10:"benchmarks";s:105:"{"cpu":"78.59460275144\n","ram":"1336531.7698043\n","io":"860.92924027619\n","mutex":"59.188014427079\n"}";}
Success.
LA: 0.01
--------------------
Fri, 29 Mar 2019 00:00:02 -0500
LA: 0.19
Sending anonymous stats to https://new.nemslinux.com/stats/
a:15:{s:4:"hwid";s:32:"59bdd12a7e20b1d315c2bb7263dad363";s:8:"platform";s:1:"4";s:11:"uptime_days";i:11;s:12:"uptime_hours";i:2;s:11:"uptime_mins";i:19;s:11:"uptime_secs";d:55;s:7:"nemsver";s:3:"1.5";s:5:"hosts";s:2:"47";s:8:"services";s:2:"14";s:8:"disksize";d:31346462720;s:8:"diskfree";d:27345317888;s:11:"loadaverage";s:16:"0.11789004457652";s:11:"temperature";s:15:"44.254646125117";s:8:"timezone";s:3:"CDT";s:10:"benchmarks";s:105:"{"cpu":"78.59460275144\n","ram":"1336531.7698043\n","io":"860.92924027619\n","mutex":"59.188014427079\n"}";}
Success.
LA: 0.71
--------------------
Sat, 30 Mar 2019 00:00:02 -0500
LA: 0.16
Sending anonymous stats to https://new.nemslinux.com/stats/
a:15:{s:4:"hwid";s:32:"59bdd12a7e20b1d315c2bb7263dad363";s:8:"platform";s:1:"4";s:11:"uptime_days";i:12;s:12:"uptime_hours";i:2;s:11:"uptime_mins";i:19;s:11:"uptime_secs";d:54;s:7:"nemsver";s:3:"1.5";s:5:"hosts";s:2:"47";s:8:"services";s:2:"14";s:8:"disksize";d:31346462720;s:8:"diskfree";d:27342135296;s:11:"loadaverage";s:16:"0.11736998514116";s:11:"temperature";s:15:"44.285528706085";s:8:"timezone";s:3:"CDT";s:10:"benchmarks";s:105:"{"cpu":"78.59460275144\n","ram":"1336531.7698043\n","io":"860.92924027619\n","mutex":"59.188014427079\n"}";}
Success.
LA: 0.38
--------------------
Sun, 31 Mar 2019 00:00:02 -0500
LA: 0.03
Sending anonymous stats to https://new.nemslinux.com/stats/
a:15:{s:4:"hwid";s:32:"59bdd12a7e20b1d315c2bb7263dad363";s:8:"platform";s:1:"4";s:11:"uptime_days";i:13;s:12:"uptime_hours";i:2;s:11:"uptime_mins";i:19;s:11:"uptime_secs";d:55;s:7:"nemsver";s:3:"1.5";s:5:"hosts";s:2:"46";s:8:"services";s:2:"13";s:8:"disksize";d:31346462720;s:8:"diskfree";d:27339100160;s:11:"loadaverage";s:16:"0.11603268945022";s:11:"temperature";s:5:"46.16";s:8:"timezone";s:3:"CDT";s:10:"benchmarks";s:105:"{"cpu":"78.59460275144\n","ram":"1336531.7698043\n","io":"860.92924027619\n","mutex":"59.188014427079\n"}";}
Success.
LA: 0.35
--------------------
jeff@nems:~ $ packet_write_wait: Connection to 2600:1700:130:b3d0::2e port 22: Broken pipe
Jeffs-MBP:~ jeff$ ssh jeff@nems
jeff@nems's password: 

Last login: Mon Apr  1 19:13:09 2019 from 2600:1700:130:b3d0:21f1:356f:3664:1601

          ███╗   ██╗███████╗███╗   ███╗███████╗
          ████╗  ██║██╔════╝████╗ ████║██╔════╝
          ██╔██╗ ██║█████╗  ██╔████╔██║███████╗
          ██║╚██╗██║██╔══╝  ██║╚██╔╝██║╚════██║
          ██║ ╚████║███████╗██║ ╚═╝ ██║███████║
          ╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝╚══════╝
                                         LINUX

                   BY: ROBBIE FERGUSON
                      NEMSLINUX.COM

  NEMS Platform....: RPi 3 Model B+
  NEMS Version.....: 1.5 (Current Version is 1.5)
  NEMS IP Address..: 192.168.1.225
  Uptime...........: 0 days 1 hours 28 minutes 42 seconds
  Load.............: 0.33 (1 minute) 0.19 (5 minutes) 0.11 (15 minutes)
                     0.12 (1 week)
  Memory...........: Total: 927 MB / Cached: 99 MB
                     Used: 232 MB / Free: 212 MB
  Disk Usage.......: You're using 13% of your root filesystem

jeff@nems:~ $ nano fan.py
jeff@nems:~ $ python fan.py
Traceback (most recent call last):
  File "fan.py", line 10, in <module>
    import RPi.GPIO as GPIO
ImportError: No module named RPi.GPIO
jeff@nems:~ $ sudo apt-get install python-rpi.gpio python3-rpi.gpio
[sudo] password for jeff: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
  rpi.gpio-common
The following NEW packages will be installed:
  python-rpi.gpio python3-rpi.gpio rpi.gpio-common
0 upgraded, 3 newly installed, 0 to remove and 93 not upgraded.
Need to get 46.0 kB of archives.
After this operation, 158 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://mirrors.syringanetworks.net/raspbian/raspbian buster/main armhf rpi.gpio-common armhf 0.6.5-1 [5,424 B]
Get:2 http://mirrors.syringanetworks.net/raspbian/raspbian buster/main armhf python-rpi.gpio armhf 0.6.5-1 [20.3 kB]
Get:3 http://mirror.os6.org/raspbian/raspbian buster/main armhf python3-rpi.gpio armhf 0.6.5-1 [20.3 kB]
Fetched 46.0 kB in 2s (29.9 kB/s)      
Selecting previously unselected package rpi.gpio-common:armhf.
(Reading database ... 92084 files and directories currently installed.)
Preparing to unpack .../rpi.gpio-common_0.6.5-1_armhf.deb ...
Unpacking rpi.gpio-common:armhf (0.6.5-1) ...
Selecting previously unselected package python-rpi.gpio.
Preparing to unpack .../python-rpi.gpio_0.6.5-1_armhf.deb ...
Unpacking python-rpi.gpio (0.6.5-1) ...
Selecting previously unselected package python3-rpi.gpio.
Preparing to unpack .../python3-rpi.gpio_0.6.5-1_armhf.deb ...
Unpacking python3-rpi.gpio (0.6.5-1) ...
Setting up rpi.gpio-common:armhf (0.6.5-1) ...
Setting up python3-rpi.gpio (0.6.5-1) ...
Setting up python-rpi.gpio (0.6.5-1) ...
jeff@nems:~ $ nano fan.py
jeff@nems:~ $ python fan.py
Traceback (most recent call last):
  File "fan.py", line 16, in <module>
    GPIO.setup(4, GPIO.OUT)
RuntimeError: No access to /dev/mem.  Try running as root!
jeff@nems:~ $ sudo python fan.py
Traceback (most recent call last):
  File "fan.py", line 22, in <module>
    temp = int(temp)
ValueError: invalid literal for int() with base 10: "temp=34.3'C\n"
jeff@nems:~ $ sudo python3 fan.py
fan.py:16: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(4, GPIO.OUT)
Traceback (most recent call last):
  File "fan.py", line 22, in <module>
    temp = int(temp)
ValueError: invalid literal for int() with base 10: "temp=34.3'C\n"
jeff@nems:~ $ nano fan.py
jeff@nems:~ $ sudo python fan.py
fan.py:16: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(4, GPIO.OUT)
Traceback (most recent call last):
  File "fan.py", line 22, in <module>
    temp = float((res.replace("temp=","").replace("'C\n","")))
NameError: name 'res' is not defined
jeff@nems:~ $ nano fan.py
jeff@nems:~ $ sudo python fan.py
fan.py:16: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(4, GPIO.OUT)
Traceback (most recent call last):
  File "fan.py", line 35, in <module>
    time.sleep(5)
NameError: name 'time' is not defined
jeff@nems:~ $ sudo python3 fan.py
fan.py:16: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(4, GPIO.OUT)
Traceback (most recent call last):
  File "fan.py", line 35, in <module>
    time.sleep(5)
NameError: name 'time' is not defined
jeff@nems:~ $ nano fan.py
jeff@nems:~ $ sudo python3 fan.py
fan.py:16: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(4, GPIO.OUT)
^CTraceback (most recent call last):
  File "fan.py", line 35, in <module>
    sleep(5)
KeyboardInterrupt
jeff@nems:~ $ nano fan.py
jeff@nems:~ $ sudo python3 fan.py
  File "fan.py", line 24
    print 'Temperature from vcgencmd: {}'.format(temp)
                                        ^
SyntaxError: invalid syntax
jeff@nems:~ $ sudo python fan.py
fan.py:16: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(4, GPIO.OUT)
Temperature from vcgencmd: 33.8
Turning off GPIO 4
Temperature from vcgencmd: 34.3
Turning off GPIO 4
Temperature from vcgencmd: 34.3
Turning off GPIO 4
^CTraceback (most recent call last):
  File "fan.py", line 35, in <module>
    sleep(5)
KeyboardInterrupt
jeff@nems:~ $ sudo python fan.py
fan.py:16: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(4, GPIO.OUT)
Temperature from vcgencmd: 35.4
Turning off GPIO 4
Temperature from vcgencmd: 35.9
Turning off GPIO 4
Temperature from vcgencmd: 35.4
Turning off GPIO 4
Temperature from vcgencmd: 35.4
Turning off GPIO 4
Temperature from vcgencmd: 34.9
Turning off GPIO 4
Temperature from vcgencmd: 35.4
Turning off GPIO 4
Temperature from vcgencmd: 35.4
Turning off GPIO 4
Temperature from vcgencmd: 34.3
Turning off GPIO 4
Temperature from vcgencmd: 34.9
Turning off GPIO 4
Temperature from vcgencmd: 35.4
Turning off GPIO 4
Temperature from vcgencmd: 34.9
Turning off GPIO 4
Temperature from vcgencmd: 34.9
Turning off GPIO 4
Temperature from vcgencmd: 35.9
Turning off GPIO 4
Temperature from vcgencmd: 35.4
Turning off GPIO 4
^CTraceback (most recent call last):
  File "fan.py", line 35, in <module>
    sleep(5)
KeyboardInterrupt
jeff@nems:~ $ sudo python fan.py
fan.py:16: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(4, GPIO.OUT)
Temperature from vcgencmd: 35.4
Turning off GPIO 4
^CTraceback (most recent call last):
  File "fan.py", line 35, in <module>
    sleep(5)
KeyboardInterrupt
jeff@nems:~ $ sudo python3 fan.py
  File "fan.py", line 24
    print 'Temperature from vcgencmd: {}'.format(temp)
                                        ^
SyntaxError: invalid syntax
jeff@nems:~ $ nano fan.py
jeff@nems:~ $ sudo python fan.py
fan.py:16: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(4, GPIO.OUT)
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 36.5
Turning off GPIO 4
Temperature from vcgencmd: 37.0
Turning off GPIO 4
Temperature from vcgencmd: 37.0
Turning off GPIO 4
Temperature from vcgencmd: 38.1
Turning off GPIO 4
Temperature from vcgencmd: 37.0
Turning off GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 38.1
Turning off GPIO 4
Temperature from vcgencmd: 37.0
Turning off GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 38.1
Turning off GPIO 4
Temperature from vcgencmd: 38.1
Turning off GPIO 4
Temperature from vcgencmd: 38.1
Turning off GPIO 4
Temperature from vcgencmd: 38.6
Turning off GPIO 4
Temperature from vcgencmd: 38.6
Turning off GPIO 4
Temperature from vcgencmd: 38.6
Turning off GPIO 4
Temperature from vcgencmd: 38.6
Turning off GPIO 4
Temperature from vcgencmd: 38.6
Turning off GPIO 4
^CTraceback (most recent call last):
  File "fan.py", line 35, in <module>
    sleep(5)
KeyboardInterrupt
jeff@nems:~ $ nano fan.py
jeff@nems:~ $ nano fan.py
jeff@nems:~ $ sudo python fan.py
fan.py:16: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(4, GPIO.OUT)
Temperature from vcgencmd: 39.7
Turning on GPIO 4
Temperature from vcgencmd: 39.7
Turning on GPIO 4
Temperature from vcgencmd: 39.7
Turning on GPIO 4
Temperature from vcgencmd: 39.2
Turning on GPIO 4
Temperature from vcgencmd: 38.6
Turning on GPIO 4
Temperature from vcgencmd: 38.6
Turning on GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 38.6
Turning on GPIO 4
Temperature from vcgencmd: 38.6
Turning on GPIO 4
Temperature from vcgencmd: 38.6
Turning on GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 38.6
Turning on GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 38.1
Turning on GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 38.6
Turning on GPIO 4
Temperature from vcgencmd: 38.6
Turning on GPIO 4
Temperature from vcgencmd: 38.1
Turning on GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 39.2
Turning on GPIO 4
Temperature from vcgencmd: 39.7
Turning on GPIO 4
Temperature from vcgencmd: 40.8
Turning on GPIO 4
Temperature from vcgencmd: 39.2
Turning on GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 38.1
Turning on GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 38.6
Turning on GPIO 4
Temperature from vcgencmd: 38.1
Turning on GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 38.1
Turning on GPIO 4
Temperature from vcgencmd: 38.1
Turning on GPIO 4
Temperature from vcgencmd: 38.1
Turning on GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 38.6
Turning on GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
Temperature from vcgencmd: 37.6
Turning off GPIO 4
^CTraceback (most recent call last):
  File "fan.py", line 35, in <module>
    sleep(5)
KeyboardInterrupt
jeff@nems:~ $ 
jeff@nems:~ $ 
jeff@nems:~ $ 
jeff@nems:~ $ 
jeff@nems:~ $ 
jeff@nems:~ $ nano fan.py
jeff@nems:~ $ nano fan.py
jeff@nems:~ $ pwd
/home/jeff
jeff@nems:~ $ nano fan.py
jeff@nems:~ $ cat fan.py
#!/susr/bin/python

# connect red lead to one pint to 3.3v pin (pin 1)
# connect black lead to GPIO 4 (pin 7)

# on NEMS run
# $ sudo apt-get install python-rpi.gpio python3-rpi.gpio -y

#########################
#
# simple-fan turns a fan on and off when temperature exceeds temperature
# thresholds.
#
# The fan comes with a MiuZei case, and can run on 3.3V (low speed) or
# 5V (high speed). The fan can be plugged into either 3.3V or 5.5v GPIO
# pin and to a ground GPIO pin, but that means the fan will always run
# and that isn't very much fun. Any fan can be used as long it can operate
# at 3.3V
#
# run-fan was tested on a raspberry pi 3b+ running nems linux
#
#########################

#########################
#
# simple-fan.py is based on:
#    https://stackoverflow.com/questions/41819683/how-can-i-control-a-fan-with-gpio-on-a-raspberry-pi-3-using-python
#
#########################


#########################
#
# simple-fan starts automatically using systemd
#
# Create a systemd service file using:
#   $ sudo nano /lib/systemd/system/simple-fan.service
#
# with the contents as shown below
# remove # and leading spaces:
#   [Unit]
#   Description=run fan when hot
#   After=meadiacenter.service
#
#   [Service]
#   # If User and Group are not specified as root, then it won't work
#   User=root
#   Group=root
#   Type=simple
#   ExecStart=/usr/bin/python /home/pi/run-fan.py
#   Restart=Always
#
#   [Install]
#   WantedBy=multi-user.target
#
# end of the simple-fan.service
# ctrl-o, ENTER, ctrl-x to save and exit the nano editor
#
# After any changes to /lib/systemd/system/simple-fan.service:
#    sudo systemctl daemon-reload
#    sudo systemctl enable simple-fan.service
#    sudo reboot
#
# Ensure the run-fan.service in systemd is enabled and running:
#    systemctl list-unit-files | grep enabled
#    systemctl | grep running | grep fan
#    systemctl status simple-fan.service -l
#
# If there are any issues with starting the script using systemd,
# then examine the journal using:
#    sudo journalctl -u simple-fan.service
#
#########################

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

while True:     # Loop forever

    # Read the current temperature
    res = os.popen('vcgencmd measure_temp').readline()
    temp = float((res.replace("temp=","").replace("'C\n","")))

    # print 'Temperature from vcgencmd: {}'.format(temp)

    # Control the fan
    if temp > 65.0:
        # print 'Turning on GPIO 4'
        GPIO.output(4, False)
    else:
        # print 'Turning off GPIO 4'
        GPIO.output(4, True)

    # Wait before the next iteration
    sleep(10)
jeff@nems:~ $ nano fan.py
jeff@nems:~ $ Connection to nems closed by remote host.
Connection to nems closed.
Jeffs-MBP:~ jeff$ ssh jeff@nems
Warning: Permanently added the ECDSA host key for IP address '192.168.1.225' to the list of known hosts.
jeff@nems's password: 

Last login: Mon Apr  1 21:40:41 2019 from 2600:1700:130:b3d0:21f1:356f:3664:1601

          ███╗   ██╗███████╗███╗   ███╗███████╗
          ████╗  ██║██╔════╝████╗ ████║██╔════╝
          ██╔██╗ ██║█████╗  ██╔████╔██║███████╗
          ██║╚██╗██║██╔══╝  ██║╚██╔╝██║╚════██║
          ██║ ╚████║███████╗██║ ╚═╝ ██║███████║
          ╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝╚══════╝
                                         LINUX

                   BY: ROBBIE FERGUSON
                      NEMSLINUX.COM

  NEMS Platform....: RPi 3 Model B+
  NEMS Version.....: 1.5 (Current Version is 1.5)
  NEMS IP Address..: 192.168.1.225
  Uptime...........: 0 days 0 hours 0 minutes 19 seconds
  Load.............: 2.40 (1 minute) 0.54 (5 minutes) 0.18 (15 minutes)
                     0.12 (1 week)
  Memory...........: Total: 927 MB / Cached: 99 MB
                     Used: 215 MB / Free: 482 MB
  Disk Usage.......: You're using 13% of your root filesystem

jeff@nems:~ $ nano fan.py
jeff@nems:~ $ Connection to nems closed by remote host.
Connection to nems closed.
Jeffs-MBP:~ jeff$ ssh jeff@nems
jeff@nems's password: 

Last login: Mon Apr  1 21:48:51 2019 from 2600:1700:130:b3d0:21f1:356f:3664:1601

          ███╗   ██╗███████╗███╗   ███╗███████╗
          ████╗  ██║██╔════╝████╗ ████║██╔════╝
          ██╔██╗ ██║█████╗  ██╔████╔██║███████╗
          ██║╚██╗██║██╔══╝  ██║╚██╔╝██║╚════██║
          ██║ ╚████║███████╗██║ ╚═╝ ██║███████║
          ╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝╚══════╝
                                         LINUX

                   BY: ROBBIE FERGUSON
                      NEMSLINUX.COM

  NEMS Platform....: RPi 3 Model B+
  NEMS Version.....: 1.5 (Current Version is 1.5)
  NEMS IP Address..: 192.168.1.225
  Uptime...........: 0 days 0 hours 0 minutes 31 seconds
  Load.............: 1.83 (1 minute) 0.49 (5 minutes) 0.16 (15 minutes)
                     0.12 (1 week)
  Memory...........: Total: 927 MB / Cached: 99 MB
                     Used: 229 MB / Free: 452 MB
  Disk Usage.......: You're using 13% of your root filesystem

jeff@nems:~ $ nano fan.py
jeff@nems:~ $ mv fan.py simple-fan.py
jeff@nems:~ $ Connection to nems closed by remote host.
Connection to nems closed.
Jeffs-MBP:~ jeff$ ssh jeff@nems
jeff@nems's password: 

Last login: Mon Apr  1 21:48:59 2019 from 2600:1700:130:b3d0:21f1:356f:3664:1601

          ███╗   ██╗███████╗███╗   ███╗███████╗
          ████╗  ██║██╔════╝████╗ ████║██╔════╝
          ██╔██╗ ██║█████╗  ██╔████╔██║███████╗
          ██║╚██╗██║██╔══╝  ██║╚██╔╝██║╚════██║
          ██║ ╚████║███████╗██║ ╚═╝ ██║███████║
          ╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝╚══════╝
                                         LINUX

                   BY: ROBBIE FERGUSON
                      NEMSLINUX.COM

  NEMS Platform....: RPi 3 Model B+
  NEMS Version.....: 1.5 (Current Version is 1.5)
  NEMS IP Address..: 192.168.1.225
  Uptime...........: 0 days 0 hours 0 minutes 18 seconds
  Load.............: 2.12 (1 minute) 0.47 (5 minutes) 0.16 (15 minutes)
                     0.12 (1 week)
  Memory...........: Total: 927 MB / Cached: 99 MB
                     Used: 216 MB / Free: 483 MB
  Disk Usage.......: You're using 13% of your root filesystem

jeff@nems:~ $ ls
changelog.txt  ip_to_mac.sh  license.txt  map.sed  simple-fan.py
jeff@nems:~ $ nano simple-fan.py

  GNU nano 3.2                                                                         simple-fan.py                                                                                    

#!/susr/bin/python

# connect red lead to one pint to 3.3v pin (pin 1)
# connect black lead to GPIO 4 (pin 7)

# on NEMS run
# $ sudo apt-get install python-rpi.gpio python3-rpi.gpio -y

#########################
#
# simple-fan turns a fan on and off when temperature exceeds temperature
# thresholds.
#
# The fan comes with a MiuZei case, and can run on 3.3V (low speed) or
# 5V (high speed). The fan can be plugged into either 3.3V or 5.5v GPIO
# pin and to a ground GPIO pin, but that means the fan will always run
# and that isn't very much fun. Any fan can be used as long it can operate
# at 3.3V
#
# run-fan was tested on a raspberry pi 3b+ running nems linux
#
#########################

#########################
#
# simple-fan.py is based on:
#    https://stackoverflow.com/questions/41819683/how-can-i-control-a-fan-with-gpio-on-a-raspberry-pi-3-using-python
#
#########################

#########################
#
# simple-fan starts automatically using systemd
#
# Create a systemd service file using:
#   $ sudo nano /lib/systemd/system/simple-fan.service
#
# with the contents as shown below
# remove # and leading spaces:
#   [Unit]
#   Description=run fan when hot
#   After=meadiacenter.service
#
#   [Service]
#   # If User and Group are not specified as root, then it won't work
#   User=root
#   Group=root
#   Type=simple
#   ExecStart=/usr/bin/python /home/pi/run-fan.py
#   Restart=Always
#
#   [Install]
#   WantedBy=multi-user.target
#
# end of the simple-fan.service
# ctrl-o, ENTER, ctrl-x to save and exit the nano editor
#
# After any changes to /lib/systemd/system/simple-fan.service:
#    sudo systemctl daemon-reload
#    sudo systemctl enable simple-fan.service
#    sudo reboot
#
# Ensure the run-fan.service in systemd is enabled and running:
#    systemctl list-unit-files | grep enabled
#    systemctl | grep running | grep fan
#    systemctl status simple-fan.service -l
#
# If there are any issues with starting the script using systemd,
# then examine the journal using:
#    sudo journalctl -u simple-fan.service
#
#########################

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

while True:     # Loop forever

    # Read the current temperature
    res = os.popen('vcgencmd measure_temp').readline()
    temp = float((res.replace("temp=","").replace("'C\n","")))

    # print 'Temperature from vcgencmd: {}'.format(temp)

    # Control the fan
    if temp > 65.0:
        # print 'Turning on GPIO 4'
        GPIO.output(4, False)
    else:
        # print 'Turning off GPIO 4'
        GPIO.output(4, True)

    # Wait before the next iteration
    sleep(10)

