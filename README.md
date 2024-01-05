# azumanga_clock
a retro azumanga daioh clock widget for i3 gtk

install the prereq modules:

```
pip install gi.repository
```

then simply run:

```
python3 azumanga_clock.py
```

you can configure your system to run it on startup as needed. i have no clue if this works on systems that aren't running gtk. i use it with i3, so the widget is opened a little above where the task bar would be !

to run with i3 config (use at your own risk!)

the python script needs access to the gif in this repo, so change line 30 to path to wherever your repo is (i might change this later to be more user friendly)

add the python script to your bin:

```
sudo cp -i azumanga_clock.py /bin
sudo chmod +x /bin/azumanga_clock.py
```

then edit your i3 config (.config/i3/config) to exec on startup

```
exec --no-startup-id i3-msg 'workspace 1; exec /usr/bin/azumanga_clock.py'
```



![azumanaga](https://github.com/shawnschulz/azumanga_clock/assets/94928969/c643ffaf-57a6-41eb-8041-cfd60efc0979)

