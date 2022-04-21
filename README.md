```
python3 -m venv .venv
.venv/bin/activate
python server.py
```

```
npm exec node index.js
```

```
while sleep 1; do curl localhost:3001/reload; done  # Test the server, itself
```

```
while sleep 1; do curl localhost:3000/reload; done  # Test the proxy.
```

While curl is running, edit server.py and add a comment and save it to trigger a reload. Alternative, kill the server and run it again.
