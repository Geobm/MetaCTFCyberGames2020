# Target 10.0.50.160
### Problem description
Our TCP connect Nmap scan found some open ports it seems. We may only have a pcap of the traffic, but I'm sure that won't be a problem! Can you tell us which ones they are?

The flag will be the sum of the open ports. For example, if ports 25 and 110 were open, the answer would be MetaCTF{135}.

## Steps I followed to find relevant information and the flag

The problem states that the sum of the opened ports is the flag, with prefix MetaCTF{}. 

Firstly, I opened the .pcap provided by the problem itself. I ordered the packets by protocol realizing that there were only 2 ARP and 4 DNS packages, the rest of them were TCP. Since I didn't know how to filter the packages by opened ports, I found this youtube [video](https://www.youtube.com/watch?v=Zi1aaEJg5YI) that explains quite well how to do it.   

I just selected the first SYN TCP packet from the src `10.0.2.15` to destination src `10.0.2.6`, then I opened `Conversations` from `Statistics` wireshark tool and selected TCP protocol. 

![Demo](https://res.cloudinary.com/dxbnpu2rx/image/upload/v1603833143/Screenshot_from_2020-10-24_16-26-55_v0nent.png)

I ordered it by packets Realizing that there were only 7 ports (`80, 23, 21, 53, 22, 443, 3128`)  with more than 4 packages exchanged (opened ports).

The sum all of the opened ports is 3770.

I typed the flag **MetaCTF{3770}** in MetaCTF dashboard's problem and we got **275** points. 


