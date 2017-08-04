__author__ = 'stef'

# -*- coding: utf-8 -*-


class C(object):
    """
    Gather the various constants used by deescalate.
    """
    #: List of usual capabilities on Linux
    HARD_CODED_CAPS = [
        'chown', 'dac_override', 'dac_read_search', 'fowner', 'fsetid', 'kill', 'setgid',
        'setuid', 'setpcap', 'linux_immutable', 'net_bind_service', 'net_broadcast', 'net_admin',
        'net_raw', 'ipc_lock', 'ipc_owner', 'sys_module', 'sys_rawio', 'sys_chroot', 'sys_ptrace',
        'sys_pacct', 'sys_admin', 'sys_boot', 'sys_nice', 'sys_resource', 'sys_time', 'sys_tty_config',
        'mknod', 'lease', 'audit_write', 'audit_control', 'setfcap', 'mac_override', 'mac_admin',
        'syslog', 'wake_alarm', 'block_suspend'
    ]

    #: number of caps in HARD_CODED_CAPS
    NB_HARD_CODED = len(HARD_CODED_CAPS)

    #: NOROOT securebit
    SECBIT_NOROOT = 1 << 0
    #: NOROOT_LOCKED securebit
    SECBIT_NOROOT_LOCKED = 1 << 1
    #: NO_SETUID_FIXUP securebit
    SECBIT_NO_SETUID_FIXUP = 1 << 2
    #: NO_SETUID_FIXUP_LOCKED securebit
    SECBIT_NO_SETUID_FIXUP_LOCKED = 1 << 3
    #: SECBIT_KEEP_CAPS securebit
    SECBIT_KEEP_CAPS = 1 << 4
    #: SECBIT_KEEP_CAPS_LOCKED securebit
    SECBIT_KEEP_CAPS_LOCKED = 1 << 5

    #: capabilities supported by the running platform
    SUPPORTED_CAPS = {}
    INVERSE_SUPPORTED_CAPS = {}
    SUPPORTED_CAPS_NAMES = set()
    #: capabilities not supported by the running platform
    UNSUPPORTED_CAPS = [] + HARD_CODED_CAPS
    SUPPORTED_CAPS_VALUES = set()

    # type of capability sets
    FLAGS = {'permitted': 1, 'inheritable': 2, 'effective': 0}
    # possible values for each capability
    FLAG_VALUES = {'clear': 0, 'set': 1}
    PRCTL = {}
