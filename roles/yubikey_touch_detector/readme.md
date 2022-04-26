# `dannixon.user.yubikey_touch_detector`

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
