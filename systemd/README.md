# Deployment using systemd

Login as the user that should run the service. Run the script
`enable-systemd.sh` found in this directory.

Start pontoon by running `systemctl --user start pontoon`

Checking the status

- systemctl --user status pontoon
- journalctl --user-unit pontoon
