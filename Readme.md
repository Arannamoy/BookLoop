### Table Of Contents
- [223](#223-1)
- [8](#8)
- [12](#12-1)
- [14](#14-1)
- [24](#24-1)

## Commands

- cancel commit & remove code
```bash
git reset --hard HEAD~1
```


## Contribution status


### 223

|Code Part|Status|
|----------|----|
|books.forms|X|
|books.views|X|
|books.urls|X|
|books.templates.books.html|X|
|books.templates.book.html|X|


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
|borrow_records.urls|X|
|borrow_records.models|X|
|borrow_records.admin|X|
|disscussions.model|X|
|disscussions.admin|X|
|disscussions.urls|X|
|reviews.models|X|
|reviews.templates|X|
|reviews.forms|X|


### 14

|Code Part|Status|
|----------|----|
|borrow_records.templates|X|
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


### root@1234