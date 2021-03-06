## at_coder_contests

miwpayou0808の練習用

## prerequisites

* yarn
    * npmも
    * [atcoder-cli](https://github.com/Tatamo/atcoder-cli)を使用するため
* python
    * pyenvとpoetryも
    * [online-judge-tools/oj](https://github.com/online-judge-tools/oj)のためと、解くよう
* お好きな言語環境(上記以外)

## usage

### init

```sh
yarn install --pure-lockfile
pyenv install $(cat .python-version)
poetry env use "${HOME}/.pyenv/versions/$(cat .python-version)/bin/python"
poetry install
```

### new contests

`$contest_name`は`abc190`とか`atcoder-cli`が認識できるやつ

```sh
yarn run acc new $contest_name
```

### test & submit

`$task_dir`は`$contest_name/a`とか

python以外での実行は[oj/getting-started.ja.md at master · online-judge-tools/oj](https://github.com/online-judge-tools/oj/blob/master/docs/getting-started.ja.md)参照

```sh
cd $task_dir
touch main.py # write some code
mv tests test
# test with oj
poetry run oj t -c "python main.py"
# submit with atcoder-cli
yarn run acc submit -c abc194 -t abc194_c $(readlink -f main.py)
```

