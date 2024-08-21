# Lab: Blind OS command injection with time delays

Target : Exploit blind OS command injection in the feedback function

Analysis :

- csrf=kRWGLk00CaEDnLV1qCty9x72sXjOOJov&`name=khjg;ls`&email=gg%40gmail&subject=hg&message=jhgh -> 200 ok
- csrf=kRWGLk00CaEDnLV1qCty9x72sXjOOJov&`name=khjg;ls'"`&email=gg%40gmail&subject=hg&message=jhgh -> 500 internal server error
  - false positive , nither name,subject,messge are VULNERABLE
