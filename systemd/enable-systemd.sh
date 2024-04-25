#!/bin/sh

loginctl enable-linger
mkdir -p ~/.config/systemd/user/
cp *.timer *.service ~/.config/systemd/user/

systemctl --user enable pontoon
systemctl --user enable pontoon-sync
systemctl --user enable pontoon-insights
systemctl --user enable pontoon-clearsessions
systemctl --user enable pontoon-sync.timer
systemctl --user enable pontoon-insights.timer
systemctl --user enable pontoon-clearsessions.timer