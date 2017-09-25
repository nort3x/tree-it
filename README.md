## tree-it:

_fast tiny tool as always_
Generate a Map of all files and directorys

* list size 
* count all
* search file 
* search dir
* pretty color mode
* depth of listing 

`root@bing:~# ./tree.py -f md  -s ../eternal_scanner/
`

```
---⚈/root/Desktop/../eternal_scanner/
   │
   │---⚈/root/Desktop/../eternal_scanner/.git
   │   │
   │   │---⚈/root/Desktop/../eternal_scanner/.git/branches
   │   │   ╰
   │   │
   │   │
   │   │---⚈/root/Desktop/../eternal_scanner/.git/hooks
   │   │   │applypatch-msg.sample                                     478 byte
   │   │   │commit-msg.sample                                         896 byte
   │   │   │post-update.sample                                        189 byte
   │   │   │pre-applypatch.sample                                     424 byte
   │   │   │pre-commit.sample                                         2 Kb
   │   │   │pre-push.sample                                           1 Kb
   │   │   │pre-rebase.sample                                         5 Kb
   │   │   │pre-receive.sample                                        544 byte
   │   │   │prepare-commit-msg.sample                                 1 Kb
   │   │   │update.sample                                             4 Kb
   │   │   ╰
   │   │
   │   │
   │   │---⚈/root/Desktop/../eternal_scanner/.git/info
   │   │   │exclude                                                   240 byte
   │   │   ╰
   │   │
   │   │
   │   │---⚈/root/Desktop/../eternal_scanner/.git/logs
   │   │   │
   │   │   │---⚈/root/Desktop/../eternal_scanner/.git/logs/refs
   │   │   │   │
   │   │   │   │---⚈/root/Desktop/../eternal_scanner/.git/logs/refs/heads
   │   │   │   │   │master                                            192 byte
   │   │   │   │   ╰
   │   │   │   │
   │   │   │   │
   │   │   │   │---⚈/root/Desktop/../eternal_scanner/.git/logs/refs/remotes
   │   │   │   │   │
   │   │   │   │   │---⚈/root/Desktop/../eternal_scanner/.git/logs/refs/remotes/origin
   │   │   │   │   │   │HEAD                                          192 byte
   │   │   │   │   │   ╰
   │   │   │   │   │
   │   │   │   │   ╰
   │   │   │   │
   │   │   │   ╰
   │   │   │
   │   │   │HEAD                                                      192 byte
   │   │   ╰
   │   │
   │   │
   │   │---⚈/root/Desktop/../eternal_scanner/.git/objects
   │   │   │
   │   │   │---⚈/root/Desktop/../eternal_scanner/.git/objects/info
   │   │   │   ╰
   │   │   │
   │   │   │
   │   │   │---⚈/root/Desktop/../eternal_scanner/.git/objects/pack
   │   │   │   │pack-c8b836696e648760920d7b7e3dd29567024ed523.idx     5 Kb
   │   │   │   │pack-c8b836696e648760920d7b7e3dd29567024ed523.pack    29 Kb
   │   │   │   ╰
   │   │   │
   │   │   ╰
   │   │
   │   │
   │   │---⚈/root/Desktop/../eternal_scanner/.git/refs
   │   │   │
   │   │   │---⚈/root/Desktop/../eternal_scanner/.git/refs/heads
   │   │   │   │master                                                41 byte
   │   │   │   ╰
   │   │   │
   │   │   │
   │   │   │---⚈/root/Desktop/../eternal_scanner/.git/refs/remotes
   │   │   │   │
   │   │   │   │---⚈/root/Desktop/../eternal_scanner/.git/refs/remotes/origin
   │   │   │   │   │HEAD                                              32 byte
   │   │   │   │   ╰
   │   │   │   │
   │   │   │   ╰
   │   │   │
   │   │   │
   │   │   │---⚈/root/Desktop/../eternal_scanner/.git/refs/tags
   │   │   │   ╰
   │   │   │
   │   │   ╰
   │   │
   │   │config                                                        271 byte
   │   │description                                                   73 byte
   │   │HEAD                                                          23 byte
   │   │index                                                         505 byte
   │   │packed-refs                                                   361 byte
   │   ╰
   │
   │┌──────────────┐
   ││ changelog.md │      938 byte
   │└──────────────┘
   │elog                                                              1 Kb
   │escan                                                             17 Kb
   │LICENSE                                                           1 Kb
   │┌───────────┐
   ││ readme.md │      1 Kb
   │└───────────┘
   │┌────────┐
   ││ use.md │      4 Kb
   │└────────┘
   │vuln.txt                                                          175 byte
   ╰
```
```
# found 3 search result Do you want to list them all here? <y/N>: y
```
```
File:        /root/Desktop/../eternal_scanner/changelog.md
File:        /root/Desktop/../eternal_scanner/readme.md
File:        /root/Desktop/../eternal_scanner/use.md


Total number of dirs and files:
┌────────────────────────────────┐
│ Directoris: 18 , Files:     30 │
└────────────────────────────────┘

```

```
usage: tree.py [-h] [-f] [-fd] [-d] [-s] [-v] [-jd] [Directory]

Dir{file Tree listing tool

positional arguments:
  Directory         Point to start listing (default current directory)

optional arguments:
  -h, --help        show this help message and exit
  -f , --findfile   search and find specific file (provide part of file name)
  -fd , --finddir   find specific directory (provide part of directory name)
  -d , --depth      Depth of listing directories
  -s, --size        also list files size
  -v, --verbose     Don't round size

```


