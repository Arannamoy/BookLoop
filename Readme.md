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


## Contribution status


### 223

|Code Part|Status|
|----------|----|
|disscussions.model|X|
|disscussions.admin|X|
|disscussions.urls|X|
|reviews.models|X|
|reviews.templates|X|
|reviews.forms|X|

### 8


|Code Part|Status|
|----------|----|
|borrow_records.forms|X|
|borrow_records.templates|X|
|borrow_records.urls|X|
|borrow_records.views|X|
|disscussions.templates|X|
|disscussions.views|X|
|disscussions.forms|X|


### 12

|Code Part|Status|
|----------|----|
|borrow_records.urls|done|
|borrow_records.models|done|
|borrow_records.admin|done|
|books.forms|NA|
|books.views|done|
|books.urls|done|
|books.templates.books.html|done|


### 14

|Code Part|Status|
|----------|----|
|borrow_records.templates|Done|
|categorys.views|X|


### 24

|Code Part|Status|
|----------|----|
|book.models|Done|
|categorys.model|Done|
|users.models|Done|
|users.forms|Done|
|users.views|Done|
|users.urls|Done|
|transactions.forms|Done|
|transactions.views|Done|
|transactions.urls|Done|
|email verification|X|
|transaction.model|Done|




#### Requirements.txt without version

```bash
pip freeze | python -c "for p in __import__('sys').stdin: print(p.split('=')[0])" > requirements.txt
```

#### 
```bash
tree -a -I 'node_modules|.git|__pycache__|.vscode|migrations|.venv' > structure.txt
```
### root@1234