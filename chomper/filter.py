# Copyright: (c) 2018, Aniket Panjwani <aniket@addictedto.tech>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Filter URLs according to rules."""

from mitmproxy import http, ctx

HTML_MESSAGE = "<h1>Website blocked by Chomper! "\
               "The {} rule is in effect until {}.</h1>"


def load(l):
    ctx.log.info("Registering arguments.")
    l.add_option("addresses_str", str, '', 'Concatenated addresses.')
    l.add_option("block_type", str, '', 'Whitelist or blacklist.')
    l.add_option("rule_name", str, '', 'Name of block rule.')
    l.add_option("block_end_time", str, '', 'Time at which block will end.')

def request(flow):
    addresses = ctx.options.addresses_str.split('$[]')

    has_match = any(address in flow.request.pretty_url for address in addresses)
    if ctx.options.block_type == 'whitelist' and not has_match \
       or ctx.options.block_type == 'blacklist' and has_match:

        flow.response = http.HTTPResponse.make(
            200,
            HTML_MESSAGE.format(ctx.options.rule_name,
                                ctx.options.block_end_time).encode(),
            {"Content-Type": "text/html"}
        )
