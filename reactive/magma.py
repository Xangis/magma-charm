from charms.reactive import when, when_not, set_flag, status_set
from charmhelpers.core.hookenv import open_port

@when_not('magma.installed')
def install_magma():
    # Do your setup here.
    #
    # If your charm has other dependencies before it can install,
    # add those as @when() clauses above., or as additional @when()
    # decorated handlers below
    #
    # See the following for information about reactive charms:
    #
    #  * https://jujucharms.com/docs/devel/developer-getting-started
    #  * https://github.com/juju-solutions/layer-basic#overview
    #
    open_port(4001)
    set_flag('magma.installed')
    status_set('active')
