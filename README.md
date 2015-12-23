
Multigraph Munin Plugin for MongoDB
===================================

Graphs
------
* ops: operations/second
* mem: mapped, virtual and resident memory usage
* conn: current connections
* lock: read/write lock info
* document_activity: number of documents (inserted, updated...)
* page_faults: number of page faults/second
* collections: number of documents per collection and size of each collection

Requirements
------------
* MongoDB 2.4+
* python/pymongo

Installation (ubuntu)
---------------------

**Install pymongo:**

    sudo apt-get install pip
    sudo apt-get install build-essential python-dev
    sudo pip install pymongo

**Install plugins**

    git clone https://github.com/cureatr/mongo-munin.git /tmp/mongo-munin
    sudo cp /tmp/mongo-munin/mongo_munin /usr/share/munin/plugins
    sudo ln -sf /usr/share/munin/plugins/mongo_munin /etc/munin/plugins/mongo_munin
    sudo chmod +x /usr/share/munin/plugins/mongo_munin
    sudo service munin-node restart

Check if plugins are running:

    munin-node-configure | grep "mongo_munin"

Test plugin output:

    munin-run mongo_munin

Configuration
-------------

munin-node environment can be customized by adding a configuration file:

`/etc/munin/plugin-conf.d/munin-mongo`

You can specify a custom mongodb connection URI,
or a custom path if you want to run mongo_munin in a python virtualenv:

```
[mongo_munin]
env.MONGO_DB_URI mongodb://user:password@host:port/dbname
env.PATH /path/to/virtualenv/bin:/usr/sbin:/usr/bin:/sbin:/bin
```
