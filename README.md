# Glusterd Plus - Python SDK

## Install

Install Glusterd Plus SDK by running the following command.

```
pip install glusterd_plus
```

## Start Glusterd Plus Service

Start the Glusterd Plus service(If not started) in at least one node of the Cluster.

```
systemctl start glusterp
```

## Usage

### Peers management

```python
import glusterd_plus

conn = glusterd_plus.Connection("http://localhost:3000")

conn.add_peer("server2.gluster")
print(conn.list_peers())

conn.peer("server2.gluster").remove()
```
