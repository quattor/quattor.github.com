---
layout: article
title: Configuring the System Security Services Daemon
category: review
image: assets/img/quattor-logo.png
---

**WARNING: THIS IS WORK IN PROGRESS**  And you should read carefully
the SSSD documentation and man pages.

Another way to configure the authentication and authorisation in a
system is using
[SSSD](https://docs.fedoraproject.org/en-US/Fedora/16/html/System_Administrators_Guide/chap-SSSD_User_Guide-Introduction.html).

This daemon can control and centralise cache the communication with
LDAP and IPA servers for many services.  For consistency, we'll manage
it with `ncm-authconfig`.

The list of possible options is huge.  We propose here some data types
that model SSSD configuration files.

## Domains

Domains are databases containing user information.  We can use several
domains at the same time.  They have different providers for access
control, identity, password management...  In the first phase we'll
implement, only LDAP, simple and local providers.

Domains will be indexed by key, and the `ldap`, `simple` or `local`
portions will be substructures inside the domain.

```bash
prefix "/software/components/authconfig/sssd/domains";

"foo/id_provider" = "simple";
"foo/simple/allow_users" =...;
"bar/ldap/bind_dn" =...;
"bar/id_provider" = "simple";
```

The _simple_ provider is described in the
[Fedora guide section 8.2.3.2.3](https://docs.fedoraproject.org/en-US/Fedora/16/html/System_Administrators_Guide/chap-SSSD_User_Guide-Setting_Up_SSSD.html).
The Pan data structure mimics the file, except that the `simple`
prefixes are removed.  For instance,

```bash
prefix "/software/components/authconfig/sssd/domains/foo";

"access_provider" = "simple";
"simple/allow_users" = list("u1", "u2");
```

should generate:

```ini
[domain/foo]
access_provider = simple
simple_allow_users = u1, u2
```

### LDAP access provider

The LDAP provider has **lots** of options.  We have transcribed the
fields available in the `sssd-ldap` man page, together with their
types.  We have done some grouping as well, so that all the
`ldap_user_<field>` fields will enter in a matching `user/<field>`
entry e.g.

```bash
prefix "/software/components/authconfig/sssd/domains/foo/ldap";

"network_timeout" = 10;
"users/uid_number" = "uidNumber";
```

Should produce:

```ini
[domain/foo]
access_provider = ldap
ldap_users_uid_number = uidNumber
# And lots of other default values
```

Fields taking lists are mapped to Pan lists.  And most mandatory
fields have sensible default values to make things slightly easier.

#### LDAP substructures

We have grouped into several structures:

* `ldap_group_*` maps to `group/` inside your domain.
* `ldap_sudo_*` maps to `sudo/` inside your domain.
* `ldap_sudorules_*` maps to `sudo/rules/` inside your domain.
* `ldap_tls_*` maps to `tls/` in your domain.
* `ldap_sasl_*` maps to `sasl/` in your domain.
* `ldap_krb5_*` maps to `krb5/` in your domain.

The `krb5_*` entries, used for authenticating to the LDAP
server itself, are placed as-is inside the domain:

```bash
"...domains/foo/ldap/krb5_keytab" = "/etc/keytab";
```

## Services

NSS and PAM services are implemented in the `/.../sssd/pam` and
`/.../sssd/nss` subtrees.

Check the man page for `sssd.conf` for more details.


## Other considerations

The `[sssd]` section is mapped to the `/.../sssd/global` subtree.

The configuration tree of `ncm-authconfig` is already huge, and this
adds some more massive subtrees.  Splitting is difficult, since an
invocation of the `authconfig` command may affect the configurations
and files handled by many different components.

I think the best we can do is improve the component's code and
ability to be tested.  Ideas on how to split or make this component more
modular will be greatly appreciated.
