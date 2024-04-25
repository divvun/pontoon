# Deployment using systemd

Login as the user that should run the service.

- `loginctl enable-linger`. This allows users who are not logged in
  [to run long-running services](https://www.freedesktop.org/software/systemd/man/loginctl.html)
- `mkdir -p ~/.config/systemd/user/`
- `cp *.timer *.service ~/.config/systemd/user/`
