Title: Test of Markdown Extensions 
Date: 23.01.2022  
Author: Kamil Urbanek 
Category: DEV
Summary: Syntax check

## Table of Contents

[TOC]

## Admonitions

Code: 
```markdown
!!! note
    This is note

!!! danger
    Danger note

!!! important ""
    Important block with no title
```

!!! note
    This is note

!!! danger
    Danger note

!!! important ""
    Important block with no title

## Progress Bar

```markdown
[=0% "0%"]{: .candystripe}
[=5% "5%"]
[=25% "25%"]
[=45% "45%"]
[=65% "65%"]
[=85% "85%"] {: .candystripe}
[=100% "100%"]
```
[=0% "0%"] {: .candystripe}
[=5% "5%"]
[=25% "25%"]
[=45% "45%"]
[=65% "65%"]
[=85% "85%"] {: .candystripe}
[=100% "100%"]
