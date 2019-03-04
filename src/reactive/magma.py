from charms.reactive import when, when_not, set_flag
from charmhelpers.core.hookenv import open_port, status_set


@when_not('magma.installed')
@when('snap.installed.magma-mud')
def magma_installed_ops():
    """Post install ops
    """

    # Open port 4001 for magma-mud
    open_port(4001)

    status_set('active', "Magma-Mud Ready")
    set_flag('magma.installed')
