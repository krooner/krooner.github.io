---
layout: post
title:  "Shell Tools and Scripting"
parent: 'Missing Semester'
grand_parent: 'School (2013-2022)'
date:   2022-08-13 17:11:00 +0900
last_modified_date: 2024-06-21
---
# 셸 도구와 스크립팅
{: .no_toc }

<details markdown="block">
  <summary>
    목차
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## Shell Scripting 셸 스크립팅

bash에서 변수에 값을 할당할 때는 `foo=bar`, 변수의 값에 접근할 때는 `$foo`로 액세스한다. `foo = bar`처럼 space를 사용하면 `=`와 `bar`라는 인자와 함께 `foo` 프로그램 호출로 해석하여 작동 안 함.

bash에서 문자열은 `'`나 `"`로 선언될 수 있지만 둘이 동일하진 않다. `'`로 둘러싸인 문자열은 문자열 자체이며 `"`로 둘러싸인 문자열은 변수값을 반환

```bash
foo=bar
echo "$foo"
# prints bar
echo '$foo'
# prints $foo
```

bash는 `if, case, while, for`를 포함하는 제어 흐름 기술과, 인자를 생성/사용/작동하는 기능을 지원한다. 
```bash
# 디렉토리를 만들고 cd를 수행하는 함수 mcd의 예시
mcd () {
    mkdir -p "$1"
    cd "$1"
}
```

`$1`는 스크립트/함수의 첫 번째 인자이며, bash는 인수, 오류 코드 및 기타 변수를 참조하기 위해 다양한 특수 변수를 사용함.
- `$0`: 스크립트 이름
- `$1 ~ $9` - 스크립트의 인자이며 $1부터 첫번째 인자.
- `$@` - 모든 인자들
- `$#` - 인자의 수
- `$?` - 이전 명령을 반환하는 코드
- `$$` - 현재 스크립트에 대한 프로세스 식별 번호 (PID)
- `!!` - 인수를 포함한 마지막 명령 전체이며, 일반적으로는 사용 권한이 누락되어 실패할 때 사용. sudo를 함께 써서 실패한 명령을 신속하게 다시 실행할 수 있음.
- `$_` - 마지막 명령에서 나온 마지막 인수이며, 대화형 셸에 있는 경우 Esc를 입력한 후 .을 입력하여 얻을 수 있음

`STDOUT`을 이용하여 명령어의 실행 결과를 출력하고, `STDERR`를 이용하여 오류를 보고함.
- 리턴 코드 및 종료 상태는 스크립트나 명령어가 어떻게 실행 방법을 전달하는지 보임: `0`은 정상을 의미하며 나머지 값은 오류를 의미.
- 종료 코드는 `&&`와 `||` (short-circuiting) 연산자를 사용하여 조건부로 명령을 실행할 수 있음
- `;`는 동일한 행 내 명령을 분리함
- `true`인 프로그램의 리턴 코드는 항상 0, `false`의 경우는 항상 1.

```bash
false || echo "Oops, fail"
# Oops, fail

true || echo "Will not be printed"
#

true && echo "Things went well"
# Things went well

false && echo "Will not be printed"
#

true ; echo "This will always run"
# This will always run

false ; echo "This will always run"
# This will always run
```

명령어 대체 (명령의 출력을 변수로 가져오기)
- `$(CMD)`를 기입하면 `CMD`가 실행되고 명령 출력을 가져와 제자리에 대체
- `for file in $ (ls)`: 셸이 `ls`를 호출한 다음 해당 값을 반복

절차 대체 (Process replacement)
- `<(CMD)`는 `CMD`를 실행한 출력을 임시 파일에 배치하고 `<()`를 해당 파일 이름으로 대체함
- `diff < (ls foo) < (ls bar)`는 디렉토리 `foo, bar`에 있는 파일 간 차이점을 표시함

예 - `foobar`라는 문자열에 대해 `grep`을 반복하고, 찾을 수 없는 경우 주석으로 파일에 추가하기
- bash에서 비교 수행 시 `[]` 대신 `[[]]`을 사용하기

```bash
#!/bin/bash

echo "Starting program at $(date)" # Date will be substituted
echo "Running program $0 with $# arguments with pid $$"

for file in $@; do
    grep foobar $file > /dev/null 2> /dev/null
    # When pattern is not found, grep has exit status 1
    # We redirect STDOUT and STDERR to a null register since we do not care about them
    if [[ $? -ne 0 ]]; then
        echo "File $file does not have any foobar, adding one"
        echo "# foobar" >> "$file"
    fi
done
```

Shell globbing
- 와일드카드 `?` (단일 문자), `*` (임의의 문자): 
- 중괄호 {}: 명령에 공통 부분 문자열이 있을 때 자동으로 확장하며, 파일 이동 및 변환에 편리함

```bash
convert image.{png,jpg}
# Will expand to
convert image.png image.jpg

cp /path/to/project/{foo,bar,baz}.sh /newpath
# Will expand to
cp /path/to/project/foo.sh /path/to/project/bar.sh /path/to/project/baz.sh /newpath

# Globbing techniques can also be combined
mv *{.py,.sh} folder
# Will move all *.py and *.sh files

mkdir foo bar
# This creates files foo/a, foo/b, ... foo/h, bar/a, bar/b, ... bar/h
touch {foo,bar}/{a..h}
touch foo/x bar/y
# Show differences between files in foo and bar
diff <(ls foo) <(ls bar)
# Outputs
# < x
# ---
# > y
```

Python 스크립트 (인수를 역순으로 출력)

```python
#!/usr/local/bin/python
import sys
for arg in reversed(sys.argv[1:]):
    print(arg)
```
- 스크립트 상단에 `shebang` 줄이 포함되어 있으므로, 커널은 스크립트를 셸 명령 대신 Python 인터프리터로 실행하는 것을 알고 있음

셸 함수와 스크립트 간 차이점
1. 함수는 셸과 동일 언어로 작성되어야 하는 반면, 스크립트는 모든 언어로 작성 가능: 스크립트에 `shebang`을 포함하는 이유
2. 함수는 처음 읽을 때 한번만 로드되므로 빠르지만, 변경할 때마다 정의를 다시 로드해야 함. 반면 스크립트는 실행될 때마다 로드됨
3. 함수는 셸 환경에서 실행되므로 환경 변수를 수정할 수 있음. 반면 스크립트는 자체 프로세스에서 실행되므로 현재 디렉토리 변경 같은 작업을 할 수 없음.

## Shell Tools 셸 도구
1. 명령 사용 방법 찾기: `-h, --help` 플래그, `man`, [`tldr`](https://tldr.sh/)
2. 파일 찾기

```bash
# Find all directories named src
find . -name src -type d
# Find all python files that have a folder named test in their path
find . -path '**/test/**/*.py' -type f
# Find all files modified in the last day
find . -mtime -1
# Find all zip files with size in range 500k to 10M
find . -size +500k -size -10M -name '*.tar.gz'

# Delete all files with .tmp extension
find . -name '*.tmp' -exec rm {} \;
# Find all PNG files and convert them to JPG
find . -name '*.png' -exec convert {} {.}.jpg \;
```