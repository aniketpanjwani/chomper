# Copyright: (c) 2018, Aniket Panjwani <aniket@addictedto.tech>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Filter URLs according to rules."""

from mitmproxy import http, ctx


def load(l):
    ctx.log.info("Registering arguments.")
    # ctx.options.allow_remote = True
    l.add_option("addresses_str", str, '', 'Concatenated addresses.')
    l.add_option("rule_type", str, '', 'Whitelist or blacklist.')


def request(flow):
    addresses = ctx.options.addresses_str.split('$[]')

    if ctx.options.rule_type == 'whitelist':
        if not any(address in flow.request.pretty_url
                   for address in addresses):
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                b"Website has been blocked by Chomper!",  # (optional) content
                {"Content-Type": "text/html"}  # (optional) headers
            )
        else:
            pass
    elif ctx.options.rule_type == 'blacklist':
        if any(address in flow.request.pretty_url for address in addresses):
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                b"Website has been blocked by Chomper!",  # (optional) content
                {"Content-Type": "text/html"}  # (optional) headers
            )
        else:
            pass
