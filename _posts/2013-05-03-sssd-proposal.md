---
layout: article
title: Configuring the System Security Services Daemon
category: review
image: img/quattor-logo.png
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

SSSD access control is structured in domains, each domain having a
provider.  We'll index our domains by provider and then by name:

```bash
prefix "/software/components/authconfig/sssd/domains";

"simple/my_domain" =...
"ldap/your_domain" =...
```

The _simple_ provider is described in the
[Fedora guide section 8.2.3.2.3](https://docs.fedoraproject.org/en-US/Fedora/16/html/System_Administrators_Guide/chap-SSSD_User_Guide-Setting_Up_SSSD.html).
The Pan data sctructure mimics the file, except that the `simple`
prefixes are removed.  For instance,

```bash
prefix "/software/components/authconfig/sssd/domains/simple/foo";

"allow_users" = list("u1", "u2");
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
entry in ou

```bash
prefix "/software/components/authconfig/sssd/domains/ldap/foo";

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
"...domains/ldap/foo/krb5_keytab" = "/etc/keytab";
```

## Services

WIP.
