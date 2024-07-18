# Minions  

It is good to always carefully read instructions provided by author.

### Step-1: Download the .png

https://mega.nz/file/1UBViYgD#kjKISs9pUB4E-1d79166FeX3TiY5VQcHJ_GrcMbaLhg

![png](Hey_You.png)

### Step-2: Strings

Just paste in your terminal `strings Hey_You.png`

![Strings](minionsstrings.png)

We can see the link: 

https://mega.nz/file/wZw2nAhS#i3Q0r-R8psiB8zwUrqHTr661d8FiAS1Ott8badDnZkoH

Let's download another photo.

![jpg](Only_Few_Steps.jpg)

Paste in terminal `strings Only_Few_Steps.jpg`

We can see:

![Strings](minionsstrings2.png)

There is definitely some data hidden in this file.

### Step-3: Binwalk

![Binwalk](minionsbinwalk.png)

We have to recover these files.

![Binwalk](minionsbinwalk2.png)

Now go to `_Only_Few_Steps.jpg.extracted`

There is a `YouWon(Almost).jpg`

![jpg](YouWonAlmost.jpg)

### Step-4: Strings again

![Strings](minionsstrings3.png)

`CTF{VmtaU1IxUXhUbFZSYXpsV1RWUnNRMVpYZEZkYWJFWTJVVmhrVlZGVU1Eaz0=)`

Phrase in brackets is encoded with `base64`.

### Step-5: Base64

Using the author hints:

![Strings](minionsbase64.png)

Here it is.

### Step-6: Paste The Flag

```
CTFlearn{M1NI0NS_ARE_C00L}
```