# `dannixon.user.yubikey_touch_detector`

[![dannixon.user.yubikey_touch_detector](https://github.com/DanNixon/ansible-user/actions/workflows/yubikey_touch_detector.yml/badge.svg?branch=main)](https://github.com/DanNixon/ansible-user/actions/workflows/yubikey_touch_detector.yml)

Installs and configures [yubikey-touch-detector](https://github.com/maximbaz/yubikey-touch-detector).

## Role Variables

`yubikey_touch_detector_verbose` and `yubikey_touch_detector_libnotify` set the environment variables described [here](https://github.com/maximbaz/yubikey-touch-detector#configuring-the-app).

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    yubikey_touch_detector_libnotify: true

  roles:
    - dannixon.user.yubikey_touch_detector
```

## License

MIT
