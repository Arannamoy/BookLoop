### Table Of Contents
- [223](#223-1)
- [8](#8)
- [12](#12-1)
- [14](#14-1)
- [24](#24-1)

### URL- https://bookloop-s6np.onrender.com
## Commands

- 1 project clone 

```bash
git clone https://github.com/Arannamoy-Mondal/BookLoop.git
```

- 2 

```bash 
git branch osman
```

- 3

```bash
git checkout osman
```

- 4
```bash
git add . && git commit -m ""
```
- 5
```bash
git push origin osman
```

- cancel commit & remove code

```bash
git reset --hard HEAD~1
```







#### Requirements.txt without version

```bash
pip freeze | python -c "for p in __import__('sys').stdin: print(p.split('=')[0])" > requirements.txt
```

#### 
```bash
tree -a -I 'node_modules|.git|__pycache__|.vscode|migrations|.venv | ss' > structure.txt
```
### root@1234