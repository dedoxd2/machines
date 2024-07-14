# Lab: CSRF vulnerability with no defenses

This lab's email change functionality is vulnerable to CSRF.

To solve the lab, craft some HTML that uses a CSRF attack to change the viewer's email address and upload it to your exploit server.

You can log in to your own account using the following credentials: ```wiener:peter```

---

Analysis:
Inorder for a CSRF attack to be possible:

- Relevant action -> Email change functionality
- Cookie based session handling -> session cokkie
- No unpredictable parameters -> satisfied
