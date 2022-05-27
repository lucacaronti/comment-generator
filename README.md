# Really easy comment generator in python.

## Dependencies

```
pip install pyperclip
```

## Examples:
Input:
```bash
./comment-generator.py "This is a comment"
```
Output:
```
/*=======================*/
/*== This is a comment ==*/
/*=======================*/

Comment copyed to the clipboard
```

---
Input:
```bash
./comment-generator.py "This is a wide comment" -w
```
Output:
```
/*==========================================================================*/
/*========================= This is a wide comment =========================*/
/*==========================================================================*/

Comment copyed to the clipboard
```
---
Input:
```bash
./comment-generator.py -l python "This is a wide comment in python" -w
```
Output:
```
#==========================================================================#
#==================== This is a wide comment in python ====================#
#==========================================================================#

Comment copyed to the clipboard
```
---
Input:
```bash
./comment-generator.py --sep
```
Output
```
/*==========================================================================*/

Comment copyed to the clipboard
```
---
Run `--help` to more informations

## How to install it (linux)
```bash
$ git clone https://github.com/lucacaronti/comment-generator.git
$ chmod +x comment-generator.py
```

And if you want you can also create an alias to run the program whenever you want. Put:
```
alias gen-comment "path/to/comment-generator.py $argv"
```

in your shell configuration file.