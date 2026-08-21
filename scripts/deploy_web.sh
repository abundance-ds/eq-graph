#!/bin/sh
set -eu

repo_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
web_dir="$repo_dir/web"
database="$web_dir/server/data/serving.sqlite"
host=${EQ_GRAPH_DEPLOY_HOST:-chat-host}
remote_root=/home/ubuntu/eq-graph-web
revision=$(git -C "$repo_dir" rev-parse --short=7 HEAD)
release=$(date -u '+%Y%m%d%H%M%S')-$revision
remote_release=$remote_root/releases/$release

test -f "$web_dir/.output/server/index.mjs"
test -f "$database"

prior=$(ssh -o BatchMode=yes "$host" "readlink -f '$remote_root/current'")
ssh -o BatchMode=yes "$host" "mkdir -p '$remote_release/.output' '$remote_release/data'"
rsync -a --delete "$web_dir/.output/" "$host:$remote_release/.output/"
rsync -a "$database" "$host:$remote_release/data/serving.sqlite"
ssh -o BatchMode=yes "$host" "chmod 600 '$remote_release/data/serving.sqlite'; ln -sfn '$remote_release' '$remote_root/current.next'; mv -Tf '$remote_root/current.next' '$remote_root/current'; sudo -n systemctl restart eq-graph-web"

if ! curl --fail --silent --show-error --max-time 30 \
    https://eq-graph.shoulde.rs/api/graph/status \
    | python3 -c 'import json,sys; d=json.load(sys.stdin); assert d["counts"]["works"] == 209; assert d["counts"]["studies"] >= 207'; then
    ssh -o BatchMode=yes "$host" "ln -sfn '$prior' '$remote_root/current.next'; mv -Tf '$remote_root/current.next' '$remote_root/current'; sudo -n systemctl restart eq-graph-web"
    echo "Deployment failed. The prior release is active." >&2
    exit 1
fi
if ! curl --fail --silent --show-error --max-time 30 \
    https://eq-graph.shoulde.rs/api/story \
    | python3 -c 'import json,sys; d=json.load(sys.stdin); assert d["portfolio"]["works"] == 209; assert d["portfolio"]["studies"] >= 207'; then
    ssh -o BatchMode=yes "$host" "ln -sfn '$prior' '$remote_root/current.next'; mv -Tf '$remote_root/current.next' '$remote_root/current'; sudo -n systemctl restart eq-graph-web"
    echo "Deployment failed. The prior release is active." >&2
    exit 1
fi
if ! curl --fail --silent --show-error --max-time 30 \
    https://eq-graph.shoulde.rs/api/graph \
    | python3 -c 'import json,sys; d=json.load(sys.stdin); assert d["metadata"]["evidence"]["publications"] == 209'; then
    ssh -o BatchMode=yes "$host" "ln -sfn '$prior' '$remote_root/current.next'; mv -Tf '$remote_root/current.next' '$remote_root/current'; sudo -n systemctl restart eq-graph-web"
    echo "Deployment failed. The prior release is active." >&2
    exit 1
fi
if ! curl --fail --silent --show-error --max-time 30 \
    https://eq-graph.shoulde.rs/ >/dev/null; then
    ssh -o BatchMode=yes "$host" "ln -sfn '$prior' '$remote_root/current.next'; mv -Tf '$remote_root/current.next' '$remote_root/current'; sudo -n systemctl restart eq-graph-web"
    echo "Deployment failed. The prior release is active." >&2
    exit 1
fi

echo "release=$release"
echo "url=https://eq-graph.shoulde.rs"
