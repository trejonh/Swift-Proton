echo "in side script about to run"
raspivid -o - -t 0 -w 1920 -h 1080 -fps 30|cvlc stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:9000}' :demux=h264