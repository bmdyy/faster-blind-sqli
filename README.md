# Faster (Boolean) Blind SQLi

- [https://aircconline.com/csit/papers/vol10/csit101909.pdf](https://aircconline.com/csit/papers/vol10/csit101909.pdf)

\<link to YT video>

<!-- python3 dump.py 5 | grep -Eo '[0-9].[0-9]{6}' | tr '\n' '\t' | xc -->

```bash
kali@kali$ python3 dump.py 12
[+] Oracle verified

--- ITERATIVE ---
[+] $2a$12$HEXnjRPQxxSLVrdUSf7d6.uHn2LZt4vyZ2CN66L/qI177ovoHea66

[*] Total number of requests: 4827
[*] Average requests per char: 80.450
[*] Time elapsed: 4.129857 seconds

--- BISECTION ---
[+] $2a$12$HEXnjRPQxxSLVrdUSf7d6.uHn2LZt4vyZ2CN66L/qI177ovoHea66

[*] Total number of requests: 420
[*] Average requests per char: 7.000
[*] Time elapsed: 0.071599 seconds

--- SQL-ANDING ---
[+] $2a$12$HEXnjRPQxxSLVrdUSf7d6.uHn2LZt4vyZ2CN66L/qI177ovoHea66

[*] Total number of requests: 420
[*] Average requests per char: 7.000
[*] Time elapsed: 0.069890 seconds
```