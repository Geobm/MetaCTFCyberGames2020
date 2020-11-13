# Redacted
### Problem description
The CEO of Cyber Corp has strangely disappeared over the weekend. After looking more into his disappearance Local Police Department thinks he might have gotten caught up into some illicit activities.

The IT Department just conducted a search through his company-provided laptop and found an old memo containing a One Time Password to log into his e-mail. However it seems as if someone has redacted the code, can you recover it for us? 

## Steps I followed to find relevant information and the flag

The problem provided a [PDF](https://metaproblems.com/64caa79bcb6c606269db91db9d57f46e/cybercorp_memo.pdf) file. First, I tried to convert the file to a `.doc` extention in order to remove the black box that hides the flag without success.

Then, I examinated the file with binwalk and realize that within the file are data compressed such as another PDF file, JPEG and Zlib compressed data.

```bash
$ binwalk -z cybercorp_memo.pdf
```   
![output](https://res.cloudinary.com/dxbnpu2rx/image/upload/v1605319693/rsz_screenshot_from_2020-11-13_14-05-25_kvso7z.png)

I extracted the files using the same binwalk utility, but with the following flag that extract type signatures, give the files an extension of ext, and execute cmd:

```bash
$ binwalk --dd='.*' cybercorp_memo.pdf
```
According to the binwalk documentation: 

```bash
-D, --dd=<type:ext:cmd>
    Extract <type> signatures, give the files an extension of <ext>, and execute <cmd> 
```

Afterwards, a directory is created with the name `_cybercorp_memo.pdf.extracted`. Inside the directory we found the original memo without the black box covering the flag in the 30E file.

The flag for this problem is **MetaCTF{politics_are_for_puppets}**
