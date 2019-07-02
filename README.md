# APTMe API

This repository is the public source code of https://aptme.io

# Running The Dev Sever

```
export FLASK_DEBUG=1
flask run
```

This service allows you to view and download debian packages from certain repostories. Most simple repo setups that include a Packages.bz2 or Packages file will work. Feel free to make a PR for .xz or .gz, I had it before but it wasn't working so I scrapped them. Also if you can fix anything with Dynastic or Packix please feel free :)

This runs on flask with uwsgi and uses a JSON db for the search count. 

Please make PRs and don't rehost this service somewhere else using this code. This code should be used for learning purposes only.

This source code is under copyright to myself so you are not allowed to redistribute or host on your own. If you are caught I will not hesitate to strike a DCMA on your website.
