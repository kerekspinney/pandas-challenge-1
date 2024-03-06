For the first time you create the branch use: 

``` shell
git checkout -b inclassnotes
```

After the first time, use: 

``` shell
git checkout inclassnotes
```


This command gets the changes in the main branch and pulls then down to the local branch.

``` shell
git fetch origin main
```



``` shell
git merge -Xours feature
```