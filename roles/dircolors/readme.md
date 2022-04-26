# `dannixon.user.dircolors`

Creates the `dircolors` configuration file.

## Role Variables

The path to the file to write is set via `dircolors_dest`.

The terminal specific configurations are specified via the `dircolors_configs` variable.
The expected format is show in the example below.
See `man 5 dir_colors` for expected values.

## Example Playbook

```yaml
- hosts: all
  become: true

  vars:
    dircolors_configs:
      - terminal:
          - "*"
        config:
          RESET: 00
          DIR: 00;34
          LINK: 00;36
          MULTIHARDLINK: 00
          FIFO: 40;33
          SOCK: 00;35
          DOOR: 00;35
          BLK: 40;33;01
          CHR: 40;33;01
          ORPHAN: 40;31;01
          MISSING: 00
          SETUID: 37;41
          SETGID: 30;43
          CAPABILITY: 30;41
          STICKY_OTHER_WRITABLE: 30;42
          OTHER_WRITABLE: 34;42
          STICKY: 37;44
          EXEC: 00;32
        files:
          - name: Image formats
            color: 00;35
            match:
              - .jpg
              - .bmp
              - .png
          - name: Audio formats
            color: 00;36
            match:
              - .mp3
              - .ogg
              - .wav

  roles:
    - dannixon.user.dircolors
```

## License

MIT
