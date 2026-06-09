# Old Sessions
## Description
Proper session timeout controls are critical for securing user accounts. If a user logs in on a public or shared computer but doesn’t explicitly log out (instead simply closing the browser tab), and session expiration dates are misconfigured, the session may remain active indefinitely.

This then allows an attacker using the same browser later to access the user’s account without needing credentials, exploiting the fact that sessions never expire and remain authenticated.

Your friend tells you to check out a new social media platform he built a few years ago. Although its still under development, he said the site is almost complete. He also mentioned that he hates constantly logging into sites, and so has made his page that 'once you login, you never have to log-out again'!

Browse [here]() and find the flag!
## Hints
1. Do you know how to use the web inspector?
2. Where are cookies stored?
## Solution
First, register a new user. Choose whatever username and password you like. When you login, you’ll see a series of messages, specifically one that says:

```
Hey I found a strange page at /sessions
```

Visit that part of the site and it will reveal two sessions, the one you created and one for `admin`. You can use the web inspector of your browser to edit the session cookie. Do that and copy in the `admin` session. Reload the previous page and you should get the flag.

The flag is revealed: `picoCTF{s3t_s3ss10n_3xp1rat10n5_77b6684a}`