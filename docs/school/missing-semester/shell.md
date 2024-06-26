---
layout: post
title:  "The Shell"
parent: 'Missing Semester'
grand_parent: 'School (2013-2022)'
date:   2022-08-12 18:00:00 +0900
last_modified_date: 2024-06-21
---
# 셸
{: .no_toc }

<details markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

```bash
missing:~$
```

bash Shell 배시 셸
1. `missing` $\rightarrow$ missing이라는 기계에 있다.
2. `~` $\rightarrow$ 현재 작업 디렉토리는 ~ (홈) 디렉토리이다.
3. `$` $\rightarrow$ root 사용자가 아니다.

```bash
missing:~$ date
Fri 10 Jan 2020 11:49:31 AM EST
missing:~$ echo hello
```

`date` 프로그램만 호출하거나, `echo` 프로그램을 `hello` 인자와 함께 호출하도록 셸에 명령함
- 명령을 space 단위로 분할하여 첫 번째 단어 (`echo`) 로 표시된 프로그램을 실행하고, 후속 단어를 프로그램이 액세스 가능한 인수로 제공
- space나 특수문자를 인자에 포함시키려면 ' 또는 "로 감싸거나 (`"My Drive"`), space 앞에 `\`를 넣어 표기할 수 있음 (`My\ Drive`)

```bash
missing:~$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
missing:~$ which echo
/bin/echo
missing:~$ /bin/echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

셸이 명령을 실행하도록 요청되면 `echo`라는 프로그램을 찾아서 실행해야하므로, `$PATH`라는 환경변수에 접근하여 `:` 단위로 분리된 디렉토리 목록을 검색함.
- `$PATH`: 명령을 받을 때 프로그램을 검색해야하는 디렉토리를 나열
- `which`: 주어진 프로그램 (`echo`) 이름에 대해 실행되는 파일을 찾는 프로그램

## Linux 파일 시스템 기준 셸 이동 

```bash
missing:~$ pwd
/home/missing
missing:~$ cd /home
missing:/home$ pwd
/home
missing:/home$ cd ..
missing:/$ pwd
/
missing:/$ cd ./home
missing:/home$ pwd
/home
missing:/home$ cd missing
missing:~$ pwd
/home/missing
missing:~$ ../../bin/echo hello
hello
```
- 절대 경로: `\`로 시작하는 경로
- 상대 경로: `\`로 시작하지 않는 경로이며, 최근 작업 디렉토리에 상대적
- 현재 디렉토리: `.`, 상위 디렉토리: `..`

```bash
missing:~$ ls
missing:~$ cd ..
missing:/home$ ls
missing
missing:/home$ cd ..
missing:/$ ls
bin
boot
dev
etc
home
...
missing:~$ ls -l /home
drwxr-xr-x 1 missing  users  4096 Jun 15  2019 missing
```

`ls`는 (인수가 없을 때는) 현재 디렉토리의 내용을 출력하는 프로그램이다.

`drwxr-xr-x`
- `d`: missing이 디렉토리임을 의미
- `rwx`, `r-x`, `r-x`: 세 개의 문자가 세 그룹
    - 파일 소유자 (missing), 소유 그룹 (users), 나머지 사람들이 관련 항목에 대해 각각 권한을 갖고 있는지를 나타냄
- `r`: 디렉토리 읽기 권한으로, 콘텐츠 나열을 위해 필요함
- `w`: 디렉토리 수정 권한으로, 위의 경우 소유자만 디렉토리를 수정(`w`, 파일 추가/제거)할 수 있음
- `x`: 디렉토리 검색 권한으로, 디렉토리를 입력하기 위해 필요함
- `-`: 그 자리의 권한이 없음을 의미

그 외에도 `mv` (이름 변경 및 파일 이동), `cp` (파일 복사), `mkdir` (새 디렉토리 만들기), `man` (어떤 프로그램의 인자, 입출력 또는 작동 방식에 대한 정보)가 있다.

## 프로그램 연결
```bash
missing:~$ echo hello > hello.txt
missing:~$ cat hello.txt
hello
missing:~$ cat < hello.txt
hello
missing:~$ cat < hello.txt > hello2.txt
missing:~$ cat hello2.txt
hello

missing:~$ ls -l / | tail -n1
drwxr-xr-x 1 root  root  4096 Jun 20  2019 var
missing:~$ curl --head --silent google.com | grep --ignore-case content-length | cut --delimiter=' ' -f2
219
```

셸에서의 프로그램은 입출력 스트림을 보유하며, 프로그램이 입력을 읽을 때는 입력 스트림에서 읽고 출력할 때는 출력 스트림으로 출력함.
- 경로를 재설정하는 간단한 방법은 `< file_name` 또는 `> file_name`
- 파일에 추가할 수 있는 기능을 제공하는 `>>`과 프로그램 간 체인을 만들 때 쓰는 `|`연산자는 `파이프`를 구성할 때 유용하게 사용됨

## sudo (super-user-do)
root 사용자는 액세스 제한 없이 거의 모든 시스템 파일을 생성/읽기/수정/삭제할 수 있지만, 실수로 무언가를 망치기 쉽다. 

root 사용자로 시스템에 로그인하는 대신, `sudo` (super-user-do) 명령을 사용하면 root 권한을 이용하여 이전에 거부된 권한 문제를 해결할 수 있다.

```bash
$ sudo find -L /sys/class/backlight -maxdepth 2 -name '*brightness*'
/sys/class/backlight/thinkpad_screen/brightness
$ cd /sys/class/backlight/thinkpad_screen
$ sudo echo 3 > brightness
An error occurred while redirecting file 'brightness'
open: Permission denied

$ echo 3 | sudo tee brightness
```

예 - `/sys/class/backlight` 파일에 값을 기록하여 화면 밝기를 변경한다고 하자.
- `|, >, <` 같은 명령어는 `echo` 같은 개별 프로그램이 아니라, 셸이 직접 실행하는 기능이다.
- user 권한으로 `>`을 실행하여 파일을 작성하려했기 때문에 문제가 발생했던 것.
- `tee` 프로그램은 `/sys` 파일을 읽고 실행하며 root에서 실행되므로 모든 권한을 해결함

## 연습문제
```zsh
# 1. /tmp에 missing이라는 새로운 경로를 만들어 보세요
kisookim@Krooner-MBP / % cd tmp/ 
kisookim@Krooner-MBP /tmp % mkdir missing

# 2. touch라는 프로그램을 관찰해보세요. man 프로그램이 도움이 될겁니다
kisookim@Krooner-MBP /tmp % man touch

# 3. touch를 이용해서 semester라는 파일을 missing 안에 만들어 보세요
kisookim@Krooner-MBP /tmp % cd missing
kisookim@Krooner-MBP missing % touch semester

# 4. semester 파일에 다음 내용 작성하기

#!/bin/sh
curl --head --silent https://missing.csail.mit.edu

# 5. 파일을 실행하고 왜 작동하지 않는지 ls로 파악하기
kisookim@Krooner-MBP missing % ./semester
zsh: permission denied: ./semester
kisookim@Krooner-MBP missing % ls -l semester 
-rw-r--r--  1 kisookim  wheel  61 Feb 13 16:41 semester
 
# 파일 소유자 kisookim (rw-), 소유 그룹 wheel (r--), 나머지 (r--)
# x 권한이 없기 때문에 파일을 실행할 수 없음

# 6. sh 인터프리터로 시작해 명령을 실행하고 , semester 파일에 첫 인자로 주세요. /semester는 안되는데, 앞에 거는 왜 실행이 될까요?
kisookim@Krooner-MBP missing % sh semester
HTTP/2 200 
... # DONE

# 7. chmod 프로그램 사용
kisookim@Krooner-MBP missing % man chmod

# 8. chmod를 활용해 sh semester 대신에 ./semester을 사용 가능하게 해보세요. sh을 이용해 이 파일을 해석해야 한다는 것을 셸이 어떻게 알까요?
kisookim@Krooner-MBP missing % chmod 700 semester
kisookim@Krooner-MBP missing % ./semester
HTTP/2 200 
... # DONE
kisookim@Krooner-MBP missing % cat semester      
#!/bin/sh
curl --head --silent https://missing.csail.mit.edu

# 9. | 와 > 를 사용해 semester별 “last modified” 날짜 출력을 홈 디렉토리에 last-modified.txt라는 파일에 작성하세요.
kisookim@Krooner-MBP missing % ./semester | grep last-modified > last-modified.txt 
kisookim@Krooner-MBP missing % cat last-modified.txt 
last-modified: Tue, 11 Jan 2022 16:37:26 GMT

# 10. 노트북 배터리의 전원 레벨 또는 데스크탑 컴퓨터의 CPU 온도를 /sys에서 읽는 명령을 작성하십시오. 참고: 만약 macOS 사용자라면, 당신의 OS는 sysfs가 없기 때문에, 이 예제를 건너뛸 수 있습니다.
MacOS라서 PASS
```